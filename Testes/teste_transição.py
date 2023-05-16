import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Teste(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,700,500)
        self.vbox = QVBoxLayout()
        self.btn = QPushButton('start',self)
        self.btn.clicked.connect(self._efeito)
        self.vbox.addWidget(self.btn)
        self.label = QLabel()
        self.efeito = QGraphicsOpacityEffect(self.label)
        self.efeito.setOpacity(1)
        self.label.setGraphicsEffect(self.efeito)
        self.label.setStyleSheet("background:red")
        self.label.setMaximumWidth(100)
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)
        self.efeito = QPropertyAnimation(self.efeito,b'opacity')
    
    def _efeito(self):
    
        self.efeito.setDuration(1000)
        self.efeito.setStartValue(1)
        self.efeito.setEndValue(0.5)
        self.btn.setText('stop')
    
        self.efeito.start()


app = QApplication([])
w = Teste()
w.show()
sys.exit(app.exec_())