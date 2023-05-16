#importar modulos
from PyQt6 import uic, QtWidgets
from PyQt5.QtWidgets import *
import sys
import os


#funções
#definir path (utilizado para corrigir caminho para exportar projeto em um único arquivo)
from os.path import join, abspath
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)

#função para salvar dados do formulário
def salvar():
    nome = window.lineEdit.text()
    idade = window.lineEdit_2.text()
    telefone = window.lineEdit_3.text()
    window.lineEdit.setText('')
    window.lineEdit_2.setText('')
    window.lineEdit_3.setText('')

    if nome == '' or idade == '' or telefone == '':

        print('Erro')

    else:

        dados = 'Nome: '+nome+' | idade: '+idade+' | Telefone: '+telefone

        #pergunta o nome do arquivo a ser salvo
        #arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]

        if os.path.isfile('dados.txt'):
            with open(resource_path('dados.txt'),'a') as a:
                a.write('\n'+dados)
        else:
            #with open(arquivo+'.txt','w') as a:
            with open(resource_path('dados.txt'),'w') as a:
                a.write(dados)

        ler()

def ler():

    #pergunta o nome do arquivo a ser lido
    #arquivo = QtWidgets.QFileDialog.getOpenFileName()[0]    

    with open(resource_path('dados.txt'),'r') as a:
        window.label_6.setText(a.read())


#criar janela
App = QtWidgets.QApplication(sys.argv)
window = uic.loadUi(resource_path('style.ui'))


#ações
window.actionSalvar.triggered.connect(salvar)
window.actionAbrir.triggered.connect(ler)
ler()

#exibir janela
window.show()
App.exec()