import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
