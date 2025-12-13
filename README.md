# MarkSixPredictor
新澳门六合彩预测软件（测试中）
# 新澳门六合彩预测软件（PyQt 版 · 中文版）

本项目包含：

✔ PyQt 中文界面  
✔ 自动加载历史数据（2020–2025）  
✔ 自动预测下一期号码（基于频率模型）  
✔ 可打包成 EXE  

## 使用方法

1. 将历史数据放在：  
data/datamarksix_history_2020_2025.csv
2. 安装依赖：  
pip install -r requirements.txt
3. 运行：
python main_window.py
4. 生成 EXE：
pyinstaller -F -w main_window.py 
