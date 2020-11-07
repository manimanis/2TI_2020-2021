# Créé par HP, le 01/11/2020 en Python 3.7
from PyQt5 import QtCore, QtGui, QtWidgets
from formPFC import Ui_MainWindow
import sys
from random import*

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
L = ["pierre.gif", "papier.gif", "ciseaux.gif"]


def affichep():
    global sh, so
    a = randint(0, 2)
    ui.rienO.setPixmap(QtGui.QPixmap(L[a]))
    ui.rienH.setPixmap(QtGui.QPixmap("pierre.gif"))
    if a == 1:
        so += 1
    elif a == 2:
        sh += 1
    ui.SH.setText(str(sh))
    ui.SO.setText(str(so))


def affichef():
    global sh, so
    a = randint(0, 2)
    ui.rienO.setPixmap(QtGui.QPixmap(L[a]))
    ui.rienH.setPixmap(QtGui.QPixmap("papier.gif"))
    if a == 0:
        sh += 1
    elif a == 2:
        so += 1
    ui.SH.setText(str(sh))
    ui.SO.setText(str(so))


def affichec():
    global sh, so
    a = randint(0, 2)
    ui.rienO.setPixmap(QtGui.QPixmap(L[a]))
    ui.rienH.setPixmap(QtGui.QPixmap("ciseaux.gif"))
    if a == 0:
        so += 1
    elif a == 1:
        sh += 1
    ui.SH.setText(str(sh))
    ui.SO.setText(str(so))


def close():
    MainWindow.close()


def recommencer():
    global sh, so
    ui.rienH.setPixmap(QtGui.QPixmap("rien.gif"))
    ui.rienO.setPixmap(QtGui.QPixmap("rien.gif"))
    sh = 0
    so = 0
    ui.SH.setText(str(sh))
    ui.SO.setText(str(so))


# Boutton
sh = 0
so = 0
ui.Bpierre.clicked.connect(affichep)
ui.Bfeuille.clicked.connect(affichef)
ui.Bciseaux.clicked.connect(affichec)
ui.Bquitter.clicked.connect(close)
ui.Brecommencer.clicked.connect(recommencer)
sys.exit(app.exec_())
