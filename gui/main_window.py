import os  # ← 新增：用于检查文件路径
from PyQt5.QtWidgets import QMainWindow
from gui.ui_main import Ui_MainWindow
from core.loader import load_history
from core.predictor import simple_predict
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 保留按钮功能（以防用户想换文件）
        self.ui.btn_load.clicked.connect(self.load_data)
        self.ui.btn_predict.clicked.connect(self.predict)
        self.ui.btn_add.clicked.connect(self.add_new_period)

        self.data = None

        # === 自动加载默认数据文件 ===
        default_path = "data/datamarksix_history_2020_2025.csv"
        if os.path.exists(default_path):
            self._load_file(default_path)
        else:
            self.ui.txt_log.append("⚠️ 默认数据文件未找到，请手动加载 CSV")

    def _load_file(self, file_path):
        """统一的数据加载逻辑"""
        try:
            self.data = load_history(file_path)
            self.ui.txt_log.append(f"✅ 已加载 {len(self.data)} 期数据")
        except Exception as e:
            self.ui.txt_log.append(f"❌ 加载失败: {str(e)}")

    def load_data(self):
        from PyQt5.QtWidgets import QFileDialog
        file, _ = QFileDialog.getOpenFileName(self, "选择历史数据", "", "CSV 文件 (*.csv)")
        if file:
            self._load_file(file)

    def predict(self):
        if self.data is None:
            self.ui.txt_log.append("⚠️ 请先加载历史数据！")
            return
        try:
            # 提取最新一期的 年份 和 期号
            last_row = self.data[-1]  # 最后一行
            date_str = str(last_row['date'])  # 如 "2025,361"
            parts = date_str.split(',')
            if len(parts) >= 2:
                year = parts[0]
                period = int(parts[1])
                next_year = year
                next_period = period + 1
            else:
                next_year = "未知"
                next_period = "未知"

            pred = simple_predict(self.data)
            result_str = ', '.join(map(str, sorted(pred)))
            self.ui.txt_log.append(f"🔮 预测{next_year}年{next_period}期结果: {result_str}")
        except Exception as e:
            self.ui.txt_log.append(f"❌ 预测出错: {str(e)}")
            
    def add_new_period(self):
        """弹出对话框，手动添加新一期数据，并追加到 CSV"""
        dialog = QDialog(self)
        dialog.setWindowTitle("手动添加新一期")
        layout = QVBoxLayout()

        # 输入框
        labels = ["年份", "期号", "号1", "号2", "号3", "号4", "号5", "号6", "特别号"]
        inputs = {}
        for label in labels:
            hlayout = QHBoxLayout()
            hlayout.addWidget(QLabel(label))
            edit = QLineEdit()
            edit.setFixedWidth(80)
            inputs[label] = edit
            hlayout.addWidget(edit)
            layout.addLayout(hlayout)
            
        # === 自动填充下一期年份和期号 ===
        next_year = "2025"    # 默认值
        next_period = "1"     # 默认值
            
        if self.data:
            try:
                last_row = self.data[-1]
                date_str = str(last_row.get("date", ""))
                parts = date_str.split(",")
                if len(parts) >= 2:
                    last_year = parts[0]
                    last_period = int(parts[1])
                    next_year = last_year
                    next_period = str(last_period + 1)
            except:
                pass  # 出错则用默认值

        # 填入输入框
        inputs["年份"].setText(next_year)
        inputs["期号"].setText(next_period)

        # 按钮
        btn_layout = QHBoxLayout()
        ok_btn = QPushButton("确认添加")
        cancel_btn = QPushButton("取消")
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

        dialog.setLayout(layout)

        def on_ok():
            try:
                data = {}
                for label in labels:
                    text = inputs[label].text().strip()
                    if not text:
                        raise ValueError(f"{label} 不能为空")
                    num = int(text)
                    if label not in ["年份", "期号"]:
                        # 号码必须在 1~49 之间
                        if not (1 <= num <= 49):
                            raise ValueError(f"{label} 必须在 1~49 之间")
                    data[label] = num
                    
                # === 🛑 新增：重复期号检查 ===
                new_year = data["年份"]
                new_period = data["期号"]
                for record in self.data:
                    parts = str(record.get("date", "")).split(",")
                    if len(parts) >= 2:
                        exist_year = parts[0]
                        try:
                            exist_period = int(parts[1])
                        except ValueError:
                            continue
                        if str(exist_year) == str(new_year) and exist_period == new_period:
                            raise ValueError(f"第 {new_year} 年 {new_period} 期已存在，不能重复添加！")
            
                # 构造新记录
                new_record = {
                    "date": f"{data['年份']},{data['期号']}",
                    "号1": data["号1"],
                    "号2": data["号2"],
                    "号3": data["号3"],
                    "号4": data["号4"],
                    "号5": data["号5"],
                    "号6": data["号6"],
                    "special": data["特别号"]  # 可选，如果你后续要用
                }

                # 追加到 self.data
                self.data.append(new_record)
                
                # === 4. 追加写入 CSV 文件 ===
                csv_path = "data/datamarksix_history_2020_2025.csv"
                file_exists = os.path.exists(csv_path)
                
                with open(csv_path, "a", newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    # 如果是首次写入（文件不存在），先写标题（可选）
                    if not file_exists:
                        writer.writerow(["年份", "期号", "号1", "号2", "号3", "号4", "号5", "号6", "特别号"])
                    # 写数据行
                    row = [
                        data["年份"],
                        data["期号"],
                        f"{data['号1']:02d}",
                        f"{data['号2']:02d}",
                        f"{data['号3']:02d}",
                        f"{data['号4']:02d}",
                        f"{data['号5']:02d}",
                        f"{data['号6']:02d}",
                        f"{data['特别号']:02d}"
                    ]
                    writer.writerow(row)

                # 更新日志
                main_nums = ', '.join(f"{data[k]:02d}" for k in ['号1','号2','号3','号4','号5','号6'])
                special_num = f"{data['特别号']:02d}"
                self.ui.txt_log.append(f"✅ 已添加 {data['年份']} 年 {data['期号']} 期: {main_nums} + {special_num}")

                # 关闭对话框
                dialog.accept()

            except Exception as e:
                QMessageBox.critical(dialog, "错误", str(e))

        ok_btn.clicked.connect(on_ok)
        cancel_btn.clicked.connect(dialog.reject)

        dialog.exec_()
