# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apropos.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Apropos(object):
    def setupUi(self, Apropos):
        Apropos.setObjectName("Apropos")
        Apropos.resize(306, 329)
        self.gridLayout = QtWidgets.QGridLayout(Apropos)
        self.gridLayout.setObjectName("gridLayout")
        self.label_logo = QtWidgets.QLabel(Apropos)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("images/machi.png"))
        self.label_logo.setObjectName("label_logo")
        self.gridLayout.addWidget(self.label_logo, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(284, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.label_developpeur = QtWidgets.QLabel(Apropos)
        self.label_developpeur.setAlignment(QtCore.Qt.AlignCenter)
        self.label_developpeur.setObjectName("label_developpeur")
        self.gridLayout.addWidget(self.label_developpeur, 2, 0, 1, 2)
        self.label_copyright = QtWidgets.QLabel(Apropos)
        self.label_copyright.setObjectName("label_copyright")
        self.gridLayout.addWidget(self.label_copyright, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Apropos)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)

        self.retranslateUi(Apropos)
        QtCore.QMetaObject.connectSlotsByName(Apropos)

    def retranslateUi(self, Apropos):
        _translate = QtCore.QCoreApplication.translate
        Apropos.setWindowTitle(_translate("Apropos", "A propos de Workshop"))
        self.label_developpeur.setText(_translate("Apropos", "Developpeur : AMONO Aymar\n"
"ATELIA\n"
"Version 1.1"))
        self.label_copyright.setText(_translate("Apropos", "Copyright (C) 2018"))
        self.pushButton.setText(_translate("Apropos", "Fermer"))

