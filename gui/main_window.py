from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic
from core.loader import load_history
from core.analyzer import count_frequency
from core.predictor import simple_predict

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ui_main.ui", self)
        self.btnLoad.clicked.connect(self.load_data)
        self.btnAnalyze.clicked.connect(self.analyze)
        self.btnPredict.clicked.connect(self.predict)
        self.data = None

    def load_data(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select CSV", "", "CSV Files (*.csv)")
        if file:
            self.data = load_history(file)
            self.textLog.append(f"Loaded {len(self.data)} records")

    def analyze(self):
        if self.data is None:
            self.textLog.append("Please load data first")
            return
        freq = count_frequency(self.data)
        self.textLog.append("Frequency:")
        for n,c in freq.items():
            self.textLog.append(f"{n} : {c}")

    def predict(self):
        if self.data is None:
            self.textLog.append("Please load data first")
            return
        pred = simple_predict(self.data)
        self.textLog.append("Prediction: " + ", ".join(map(str,pred)))
