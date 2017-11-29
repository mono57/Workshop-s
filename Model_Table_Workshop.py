from PyQt5.QtCore import Qt, QVariant, QModelIndex, QAbstractTableModel
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from collections import namedtuple

import os

NOM_FICHIER_DB = 'atelier.sq3'

Client = namedtuple('Client',('Nom', 'Prenom','Sexe','Quartier','Telephone','Email', 'Modele'))

class ModelTableWorkshop(QAbstractTableModel):

	def __init__(self, parent=None):
		super(ModelTableWorkshop,self).__init__(parent)
		self.titresColonnes = ('NOM', 'PRENOM', 'TELEPHONE', 'PRIX')
		self.client = None
		dbExiste = os.path.exists(NOM_FICHIER_DB)
		db = QSqlDatabase.addDatabase('QSQLITE')
		db.setDatabaseName(NOM_FICHIER_DB)
		db.open()
		
		if not dbExiste:
			self.creeDB()
		self.litBD()
		
	def creeDB(self):
		QSqlQuery('''CREATE TABLE Modele(
						idModele Integer primary key,
						TypeModele TEXT,
						PrixModele Integer,
						DifficulteModele Integer);''')
						
		QSqlQuery('''CREATE TABLE Client(
						idClient Integer primary key,
						NomClient TEXT,
						PrenomClient TEXT,
						SexeClient TEXT,
						QuartierCLient TEXT,
						TelephoneClient TEXT,
						EmailClient TEXT,
						idModele Integer references Modele,
						idAdmin Integer references Administrateur;''')
							
		QSqlQuery('''CREATE TABLE Administrateur(
						idAdmin Integer primary,
						NomAdmin TEXT,
						PrenomAdmin TEXT,
						EmailAdmin TEXT,
						MotDePasseAdmin TEXT);''')
		QSqlQuery('''CREATE TABLE InfoSupp(
						idInfo Integer primary key,
						Poitrine Integer,
						Taille Integer,
						Hanche Integer,
						Bras Integer,
						Epaule Integer,
						idClient Integer references Client);''')
		
		QSqlQuery('''CREATE TABLE Choisir(
						idClient Integer references Client,
						idModele Integer references Modele,
						primary key(idClient, idModele));''')
		QSqlQuery('''INSERT INTO Modele values(NULL,'kaba', 1500,2)''')  
	def litBD(self):
		query = QSqlQuery('''SELECT NomClient, PrenomClient,SexeClient, QuartierClient, TelephoneClient, EmailClient, ModeleClient
								FROM Client
								JOIN Modele
								ON Modele.idModele = Client.idModele''')
		self.client = []
		while query.next():
			client = Client(*(query.value(i) for i in range(8)))
			self.client.append(client)
		
	def headerData(self, section, orientation, role):
		if role == Qt.DisplayRole and orientation == Qt.Horizontal:
			self.titresColonnes[section]
		return QVariant
		
	def columnCount(self, parent):
		return len(self.titresColonnes)
	
	def rowCount(self, parent):
		return len(self.client)
	
	def data(self, index, role):
		if role == Qt.DisplayRole and index.isValid():
			return self.client[index.row()][index.column()+1]
		return QVariant
	
	def AjouteClient(self, client):
		query = QSqlQuery()
		query.prepare('''INSERT INTO Client (idClient, NomClient, PrenomClient, QuartierClient, TelephoneClient, EmailClient, ModeleClient)
									VALUES(NULL, :nom, :prenom, :sexe, :quartier, :telephone, :email, :idmodele)''')
		query.bindValue(":nom", client.Nom)
		query.bindValue(":prenom",client.Prenom)
		query.bindValue(":sexe", client.Sexe)
		query.bindValue(":quartier", client.Quartier)
		query.bindValue(":telephone", client.Telephone)
		query.bindValue(":email", client.Email)
		query.bindValue(":idmodele", client.Modele)
		query.exec_()
		
		idClient = query.lastInsertId()
		client = Client(idClient, *client[1:])
		indiceClient = len(self.client)
		self.beginIsertRows(QModelIndex(), indiceClient, indiceClient)
		self.client.append(client)
		self.endInsertRows()
		
	def SupprimerClient(self,indiceClient):
		query = QSqlQuery()
		query.prepare('''DELETE FROM Client
							WHERE idClient = :idclient''')
		query.bindValue(":idclient", self.client[indiceClient].idClient)
		query.exec_()
		self.beginRemoveRows(QModelIndex(), indiceClient, indiceClient)
		del self.client[indiceClient]
		self.endRemoveRows()
