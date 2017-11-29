from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QWidget
from LogIn import Ui_Authentification
from Apropos import Ui_Apropos
from Workshop import Ui_WorkShop
from AffichageClient import Ui_Affichage
from PyQt5.QtCore import pyqtSlot
from Model_Table_Workshop import Client, ModelTableWorkshop

global client
		
class Principale(QMainWindow, Ui_WorkShop, Ui_Affichage):
	def __init__(self, parent=None):
		super(Principale, self).__init__(parent)
		self.setupUi(self)
		#self.setupUi(self)
	
	def EffacerClient(self):
		for lineEdit in (self.lineEdit_Nom, self.lineEdit_Prenom, self.lineEdit_Sexe, self.lineEdit_Quartier, self.lineEdit_Telephone, self.lineEdit_Email):
			lineEdit.setText('')
		
	def AfficheClient(self):
		self.lineEdit_Nom.setText(client.Nom)
		self.lineEdit_Prenom.setText(client.Prenom)
		self.lineEdit_Sexe.setText(client.Sexe)
		self.lineEdit_Quartier.setText(client.Quartier)
		self.lineEdit_Telephone.setText(client.Telephone)
		self.lineEdit_Email.setText(client.Email)
	
	@pyqtSlot()
	def on_actionAdministration_triggered(self):
		fenetre = Login()
		fenetre.exec_()
	
	@pyqtSlot()
	def on_action_Quitter_triggered(self):
		self.close()
		
	def closeEvent(self, event):
		messageConfirmation = "Êtes-vous sûr de vouloir quitter?"
		reponse = QMessageBox.question(self,'Confirmation',messageConfirmation, QMessageBox.Yes, QMessageBox.No)
		if reponse == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
			
	@pyqtSlot()		
	def on_actionA_propos_de_WorkShop_triggered(self):
		fenetre = Apropos()
		fenetre.exec_()
	@pyqtSlot()
	def on_pushButton_Sauvegarder_clicked(self):
		client = Client(#idclient=None,
						Nom = self.lineEdit_Nom.text(),
						Prenom = self.lineEdit_Prenom.text(),
						Sexe = self.radioButton_Masculin.text(),
						Quartier = self.lineEdit_Quartier.text(),
						Telephone = self.lineEdit_Telephone.text(),
						Email = self.lineEdit_Email.text(),
						Modele = '1')
		
	@pyqtSlot()
	def on_action_Afficher_liste_triggered(self):
		fenetre = Affichage()
		fenetre.exec_()
		
	
			#self.on_pushButton_clicked()
		#else:
		#	indicesClientSelectionnes = indexesSelectionnes[].Rows()
			
class Affichage(QDialog, Ui_Affichage):
	def __init__(self):
		super(Affichage,self).__init__()
		self.setupUi(self)
		self.label.setStyleSheet('''color:red''')
		self.pushButton_Afficher_details.setStyleSheet('''background-color:green''')
		
		self.modelTableWorkshop = ModelTableWorkshop()
		self.treeView_clients.setModel(self.modelTableWorkshop)
		selectionModel = self.treeView_clients.selectionModel()
		indexesSelectionnes = selectionModel.selectedRows()
		if len(indexesSelectionnes)==0:
			self.modelTableWorkshop.AjouteClient(client)
		#self.treeView_clients.selectionModel().selectionChanged.connect(self.on_treeView_clients_selectionChanged)
	
	
class Login(QDialog, Ui_Authentification):
	def __init__(self, parent=None):
		super(Login, self).__init__(parent)
		self.setupUi(self)
		self.setFixedSize(272, 300)


class Apropos(QDialog,Ui_Apropos):
	def __init__(self, parent=None):
		super(Apropos, self).__init__(parent)
		self.setupUi(self)
		self.setFixedSize(307,323)
		self.pushButton.clicked.connect(quit)
		
