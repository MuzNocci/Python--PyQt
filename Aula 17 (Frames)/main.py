from PyQt6 import uic,QtWidgets

import sys
from os.path import join, abspath
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)

def fechar_frames():
    Tela.frame1.close()
    Tela.frame2.close()
    Tela.frame3.close()

def frame1():
    fechar_frames()
    Tela.frame1.show()

def frame2():
    fechar_frames()
    Tela.frame2.show()

def frame3():
    fechar_frames()
    Tela.frame3.show()


if __name__ == '__main__':

    App = QtWidgets.QApplication([])

    Tela = uic.loadUi(resource_path('styles.ui'))


    Tela.pushButton.clicked.connect(frame1)
    Tela.pushButton_2.clicked.connect(frame2)
    Tela.pushButton_3.clicked.connect(frame3)
    Tela.pushButton_4.clicked.connect(fechar_frames)

    fechar_frames()
    Tela.show()

    App.exec()