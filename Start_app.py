#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
#from PyQt5.QtCore import QLocale, QTranslator, QLibraryInfo
from main_workshop import Principale

def main():
    app = QApplication(sys.argv)
    
    fen = Principale()
    fen.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
