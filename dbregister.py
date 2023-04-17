#Cadastro de Produtos
#Importando PyQt5
from PyQt5 import  uic,QtWidgets
import mysql.connector

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    
    if formulario.radioButton.isChecked() :
        print("Categoria Eletronicos selecionada")
    elif formulario.radioButton_2.isChecked() :
        print("Categoria Informatica selecionada")
    else :
        print("Categoria Alimentos selecionada")

    print("Código:",linha1)
    print("Descricao:",linha2)
    print("Preco",linha3)
    

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()


 # criando a tabela
""" create table produtos (
    id INT NOT NULL AUTO_INCREMENT,
    codigo INT,
    descrição VARCHAR(50),
    preço DOUBLE,
    categoria VARCHAR (20),
    primary key (id)
); """
