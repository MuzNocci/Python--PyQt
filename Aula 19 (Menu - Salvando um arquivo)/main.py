#importar modulos
from PyQt6 import uic, QtWidgets
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

    dados = 'Nome: '+nome+' | idade: '+idade+' | Telefone: '+telefone

    #pergunta o nome do arquivo a ser salvo
    #arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]

    if os.path.isfile('dados.txt'):
        with open('dados.txt','a') as a:
            a.write('\n'+dados)
    else:
        #with open(arquivo+'.txt','w') as a:
        with open('dados.txt','w') as a:
            a.write(dados)


#criar janela
App = QtWidgets.QApplication([])
window = uic.loadUi(resource_path('style.ui'))


#ações
window.actionSalvar.triggered.connect(salvar)


#exibir janela
window.show()
App.exec()