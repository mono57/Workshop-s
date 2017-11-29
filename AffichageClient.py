# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'affichage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Affichage(object):
    def setupUi(self, Affichage):
        Affichage.setObjectName("Affichage")
        Affichage.resize(562, 279)
        self.verticalLayout = QtWidgets.QVBoxLayout(Affichage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Affichage)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.treeView_clients = QtWidgets.QTreeView(Affichage)
        self.treeView_clients.setObjectName("treeView_clients")
        self.verticalLayout.addWidget(self.treeView_clients)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Afficher_details = QtWidgets.QPushButton(Affichage)
        self.pushButton_Afficher_details.setObjectName("pushButton_Afficher_details")
        self.horizontalLayout.addWidget(self.pushButton_Afficher_details)
        spacerItem = QtWidgets.QSpacerItem(298, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_fermer = QtWidgets.QPushButton(Affichage)
        self.pushButton_fermer.setObjectName("pushButton_fermer")
        self.horizontalLayout.addWidget(self.pushButton_fermer)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Affichage)
        QtCore.QMetaObject.connectSlotsByName(Affichage)

    def retranslateUi(self, Affichage):
        _translate = QtCore.QCoreApplication.translate
        Affichage.setWindowTitle(_translate("Affichage", "Liste des Clients"))
        self.label.setText(_translate("Affichage", "LISTE  DES  ENREGISTREMENTS"))
        self.pushButton_Afficher_details.setText(_translate("Affichage", "Afficher details"))
        self.pushButton_fermer.setText(_translate("Affichage", "Fermer"))

