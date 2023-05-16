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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(721, 481)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.actionSalvar = QAction(MainWindow)
        self.actionSalvar.setObjectName(u"actionSalvar")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 60, 621, 141))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setStyleSheet(u"height:30px;background-color:#fff;border:0;border-radius:15px;padding: 3px 15px")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setStyleSheet(u"height:30px;background-color:#fff;border:0;border-radius:15px;padding: 3px 15px")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size:20px;font-weight:bold;color:rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setStyleSheet(u"height:30px;background-color:#fff;border:0;border-radius:15px;padding: 3px 15px")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:20px;font-weight:bold;color:rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:20px;font-weight:bold;color:rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 205, 241, 31))
        self.label_4.setStyleSheet(u"font-size:20px;font-weight:bold;color:rgb(255, 255, 0);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 20, 251, 31))
        self.label_5.setStyleSheet(u"font-size:20px;font-weight:bold;color:rgb(255, 255, 0);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 240, 621, 191))
        self.label_6.setStyleSheet(u"font-size:20px;color:rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 721, 21))
        self.menuArquivo = QMenu(self.menuBar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuArquivo.menuAction())
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addAction(self.actionAbrir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aula 20 - Cadastro e leitura de arquivos", None))
        self.actionSalvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Idade:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Conte\u00fado do arquivo:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Formul\u00e1rio de cadastro:", None))
        self.label_6.setText("")
        self.menuArquivo.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
    # retranslateUi

