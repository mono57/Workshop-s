from collections import namedtuple
from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant, QModelIndex

Personne = namedtuple('Personne',('nom', 'prenom','sexe','quartier','telephone','email'))

class ModelTableWorkShop(QAbstractTableModel):
    def __init__(self, personne):
        super(ModelTableWorkShop, self).__init__()
        self.titresColonnes = ("Nom", "Prenom", "Telephone")
        self.personne = personne 

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            self.titresColonnes[section]
        return QVariant()

    def columnCount(self, parent):
        return len(titresColonnes)
    
    def rowCount(self, parent):
        return len(self.personne)

    def data(self, index, role):
        if role==Qt.DisplayRole and index.isValid():
            return (self.personne[index.row()][index.column()])
        return QVariant()
    
