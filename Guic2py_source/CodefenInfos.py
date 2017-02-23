# -*- coding: utf-8 -*-
# ------------------------------------------------------
# Projet......: pyuic4Gui
# Fichier.....: CodefenInfos.py
# Auteur......: daniel
# Création....: 20141028
# Version.....: 1.0 
# Révision....: 20141028
# ------------------------------------------------------
# Description.:
#
# ------------------------------------------------------
# Inclure les bibliotheque
from PySide.QtCore import *
from PySide.QtGui import *
import sys
import os
import platform
import fenInfos

class FenInfo(QDialog,fenInfos.Ui_StatusDialog):
    ostype = u''
    def __init__(self, parent=None):
        # On appelle le constructeur de la classe mère de notre classe Form
        super(FenInfo, self).__init__(parent)
        # On cré les éléments graphiques de l'interface tel que par QTdesigner
        self.setupUi(self)


def main():
    # On cre l'instance de l'interface graphique ...
    app = QApplication(sys.argv)
    # ... et de l'objet
    # On l'affiche
    feninfo = FenInfo()
    feninfo.show()
    feninfo.setWindowTitle(u"Coucou !")
    feninfo.lblTitre.setText(u"Recherche dans les chemins d'accès.")
    feninfo.txtTexte.append('Allo')
    # et on l'execute
    app.exec_()


if __name__ == "__main__":
    main()

# END OF SCRIPT
