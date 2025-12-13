
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from data_loader import load_history
from predictor import predict_next

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 绑定按键事件
        self.btn_load.clicked.connect(self.load_data)
        self.btn_predict.clicked.connect(self.do_predict)

        self.history_data = None

    def load_data(self):
        try:
            self.history_data = load_history("./data/history.csv")
            self.txt_log.append("✅ 历史数据加载成功！")
            self.txt_log.append(f"总期数：{len(self.history_data)}")
        except Exception as e:
            self.txt_log.append(f"❌ 加载失败：{e}")

    def do_predict(self):
        if self.history_data is None:
            self.txt_log.append("⚠ 请先加载历史数据！")
            return

        prediction, prob = predict_next(self.history_data)

        self.txt_log.append("\n==== 【下一期预测】 ====")
        self.txt_log.append(f"推荐号码：{prediction}")
        self.txt_log.append(f"出现概率：{prob:.2f}%")
        self.txt_log.append("========================\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
