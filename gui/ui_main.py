# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("新澳门六合彩预测软件（中文版）")
        MainWindow.resize(600, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.btn_load = QtWidgets.QPushButton("📂 加载历史数据", self.centralwidget)
        self.btn_load.setGeometry(30, 20, 150, 40)

        self.btn_predict = QtWidgets.QPushButton("🔮 预测下一期", self.centralwidget)
        self.btn_predict.setGeometry(220, 20, 150, 40)
        
        self.btn_add = QtWidgets.QPushButton("➕ 手动添加新一期", self.centralwidget)
        self.btn_add.setGeometry(400, 20, 150, 40)  # 调整位置和大小
        self.btn_add.setObjectName("btn_add")

        self.txt_log = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_log.setGeometry(30, 80, 540, 480)

        MainWindow.setCentralWidget(self.centralwidget)

        # 为后续连接信号留用（可选）
        self.btn_load.setObjectName("btn_load")
        self.btn_predict.setObjectName("btn_predict")
        self.txt_log.setObjectName("txt_log")

