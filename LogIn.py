# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogIn.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Authentification(object):
    def setupUi(self, Authentification):
        Authentification.setObjectName("Authentification")
        Authentification.setEnabled(True)
        Authentification.resize(272, 300)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        Authentification.setFont(font)
        Authentification.setMouseTracking(False)
        Authentification.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Chad))
        self.verticalLayout = QtWidgets.QVBoxLayout(Authentification)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Administrateur = QtWidgets.QLabel(Authentification)
        self.label_Administrateur.setText("")
        self.label_Administrateur.setPixmap(QtGui.QPixmap("../WorkShop\'s Plan/images/user.png"))
        self.label_Administrateur.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Administrateur.setObjectName("label_Administrateur")
        self.verticalLayout.addWidget(self.label_Administrateur)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Authentification)
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_Nom_Admin = QtWidgets.QLineEdit(Authentification)
        self.lineEdit_Nom_Admin.setObjectName("lineEdit_Nom_Admin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Nom_Admin)
        self.label_3 = QtWidgets.QLabel(Authentification)
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_Prenom_Admin = QtWidgets.QLineEdit(Authentification)
        self.lineEdit_Prenom_Admin.setObjectName("lineEdit_Prenom_Admin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Prenom_Admin)
        self.label_4 = QtWidgets.QLabel(Authentification)
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_Email_Admin = QtWidgets.QLineEdit(Authentification)
        self.lineEdit_Email_Admin.setObjectName("lineEdit_Email_Admin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Email_Admin)
        self.label_6 = QtWidgets.QLabel(Authentification)
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_MotDePasse_Admin = QtWidgets.QLineEdit(Authentification)
        self.lineEdit_MotDePasse_Admin.setMaxLength(15)
        self.lineEdit_MotDePasse_Admin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_MotDePasse_Admin.setObjectName("lineEdit_MotDePasse_Admin")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_MotDePasse_Admin)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 88, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_Valider = QtWidgets.QPushButton(Authentification)
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Valider.setFont(font)
        self.pushButton_Valider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../WorkShop\'s Plan/images/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Valider.setIcon(icon)
        self.pushButton_Valider.setObjectName("pushButton_Valider")
        self.horizontalLayout.addWidget(self.pushButton_Valider)
        spacerItem2 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Authentification)
        QtCore.QMetaObject.connectSlotsByName(Authentification)

    def retranslateUi(self, Authentification):
        _translate = QtCore.QCoreApplication.translate
        Authentification.setWindowTitle(_translate("Authentification", "Authentification"))
        self.label_2.setText(_translate("Authentification", "Nom : "))
        self.lineEdit_Nom_Admin.setPlaceholderText(_translate("Authentification", "Nom Admin"))
        self.label_3.setText(_translate("Authentification", "Prénom :"))
        self.lineEdit_Prenom_Admin.setPlaceholderText(_translate("Authentification", "Prénom Admin"))
        self.label_4.setText(_translate("Authentification", "Email : "))
        self.lineEdit_Email_Admin.setPlaceholderText(_translate("Authentification", "Email Admin"))
        self.label_6.setText(_translate("Authentification", "Mot de passe : "))
        self.lineEdit_MotDePasse_Admin.setPlaceholderText(_translate("Authentification", "Mot de passe"))
        self.pushButton_Valider.setText(_translate("Authentification", "Valider"))

