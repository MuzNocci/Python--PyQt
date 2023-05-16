# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'style.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(487, 365)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        MainWindow.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(130, 120, 231, 31))
        self.comboBox.setStyleSheet(u"QComboBox{background-color: rgb(255, 255, 255);border:0;font-weight:bold;font-size:12px;padding: 3px 10px;}")
        self.comboBox.setIconSize(QSize(30, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 60, 229, 31))
        self.label.setStyleSheet(u"font-size:20px;font-weight:bold;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 292, 371, 31))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet(u"font-size:18px;font-weight:bold; color:rgb(66, 199, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 190, 151, 41))
        self.pushButton.setStyleSheet(u"QPushButton{border:0; background-color:#FFF;border-radius:20px;font-weight:bold;font-size:12px;}QPushButton:hover{background-color:rgb(211, 211, 211);}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aula 18 - Combo Box", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Campos dos Goytacazes - RJ", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Ribeir\u00e3o Preto - SP", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"New York - NY", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Los Angeles - CA", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Escolha uma cidade:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cidade selecionada", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Selecionar", None))
    # retranslateUi

