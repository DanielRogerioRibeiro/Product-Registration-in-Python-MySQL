#Cadastro de Produtos
#Importando PyQt5
from PyQt5 import  uic,QtWidgets




app=QtWidgets.QApplication([])
formulario=uic.loadUi("main.ui")


formulario.show()
app.exec()