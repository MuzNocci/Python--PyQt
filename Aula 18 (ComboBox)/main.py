from PyQt6 import uic, QtWidgets

import sys
from os.path import join, abspath
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)

def opcao_selecionada():
    cidade = window.comboBox.currentText()
    window.label_3.setText(cidade)
    window.label_3.setStyleSheet('color:rgb(255, 255, 0);font-size:18px;font-weight:bold;')

App = QtWidgets.QApplication([])
window = uic.loadUi(resource_path('style.ui'))

window.comboBox.addItems([
    'Rio de Janeiro - RJ',
    'Arraial do Cabo - RJ',
    'Penedo - RJ',
    'Miami - FL'
    ])

window.pushButton.clicked.connect(opcao_selecionada)

window.show()
App.exec()
