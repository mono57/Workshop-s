from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from UI_main_Window_WorkShop import Ui_WorkShop
from PyQt5.QtCore import pyqtSlot
from model_table_workshop import *

class MainWindowWorkShop(QMainWindow, Ui_WorkShop):
	def __init__(self, parent=None):
		super(MainWindowWorkShop, self).__init__(parent)
		self.setupUi(self)
		personnetest = [Personne('Amono','Aymar','M','Yatelim','698439057','aymaramono@gmail.com'), Personne('Aymar', 'Amono','F', 'Yatelim', '68945621', 'amonoaymar@yahoo.fr')]
		self.modelTablePersonne = ModelTableWorkShop(personnetest)
		self.treeViewLivres.setModel(self.modelTablePersonne)
		self.treeViewLivres.selectionModel().selectionChanged.connect(self.on_treeViewLivres_selectionChanged)
	
	def on_treeViewLivres_selectionChanged(self,selected,deselected):
		indexesSelection = selected.indexes()
		if len(indexesSelection)>0:
			self.indexSelection = indexesSelection[0]
			self.indexPersonneSelectionne = self.indexSelection.row()
			self.affichePersonne(self.modelTablePersonne.personne[self.indexPersonneSelectionne])

	def affichePersonne(self, personne):
		self.lineEditNom.setText(personne.nom)
		self.lineEditPrenom.setText(personne.prenom)
		if personne.sexe=='M':
			self.radioButtonMasculin.setChected(True)
		if personne.sexe=='F':
			self.radioButtonFeminin.setChected(True)
		self.lineEditQuartier.setText(personne.quartier)
		self.lineEditTelephone.setText(personne.telephone)
		self.lineEditEmail.setText(personne.email)
		
	@pyqtSlot()
	def on_actionOuvrir_triggered(self):
		(nomfichier, filtre) = QFileDialog.getOpenFileName(self, 'Ouvrir fichier', filter = "Bibliothèque (*.deb);; Tout (*.*)")
		if nomfichier:
			QMessageBox.information(self, 'Trace', 'Nom du fichier {}'.format(nomfichier))
	
	@pyqtSlot()
	def on_actionQuitter_triggered(self):
		self.close()
	def closeEvent(self, event):
		message_confirmation = "Êtes-vous sûr de vouloir Quitter"
		reponse = QMessageBox.question(self, 'Confirmation', message_confirmation, QMessageBox.Yes, QMessageBox.No)
		if reponse == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
