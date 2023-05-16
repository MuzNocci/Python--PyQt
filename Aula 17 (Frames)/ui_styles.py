# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'styles.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, 129, 801, 471))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(41, 40, 201, 51))
        self.label.setStyleSheet(u"QLabel{font-size:20px;font-weight:bold;color:black;}")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 20, 75, 23))
        self.pushButton.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);color:black;font-weight:bold;border:0;border-radius:10px;}QPushButton:hover{background-color: rgb(175, 223, 255);}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 50, 75, 23))
        self.pushButton_2.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);color:black;font-weight:bold;border:0;border-radius:10px;}QPushButton:hover{background-color: rgb(175, 223, 255);}")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 80, 75, 23))
        self.pushButton_3.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);color:black;font-weight:bold;border:0;border-radius:10px;}QPushButton:hover{background-color: rgb(175, 223, 255);}")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 129, 801, 471))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 40, 201, 51))
        self.label_2.setStyleSheet(u"QLabel{font-size:20px;font-weight:bold;color:black;}")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 129, 801, 471))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 40, 201, 51))
        self.label_3.setStyleSheet(u"QLabel{font-size:20px;font-weight:bold;color:black;}")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(667, 20, 111, 23))
        self.pushButton_4.setStyleSheet(u"QPushButton{background-color: rgb(255, 255, 255);color:black;font-weight:bold;border:0;border-radius:10px;}QPushButton:hover{background-color:rgb(255, 151, 151);}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame.raise_()
        self.pushButton_4.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Janela com Frames", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Frame 1", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Frame 1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Frame 2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Frame 3", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Frame 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Frame 3", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Fechar Frames", None))
    # retranslateUi

