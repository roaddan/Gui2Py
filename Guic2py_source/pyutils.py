# -*- coding: utf-8 -*-
# ------------------------------------------------------
# Projet......: pyuic4Gui
# Fichier.....: pyutils.py
# Auteur......: daniel
# Création....: 20141023
# Version.....: 1.0 
# Révision....: 20141023
# ------------------------------------------------------
# Description.:
#
# ------------------------------------------------------
#from PySide.QtCore import *
#from PySide.QtGui import *
#import sys
import os
import fnmatch
import CodefenInfos
#import sys
import platform


def find(name, path='/'):
    for root, dirs, files in os.walk(path):
        if name in files:
            return True, os.path.join(root, name)
    return False, None


def find_in_path(name):
    ospath = os.getenv('PATH')
    pathsep = ";"
    found = False
    if not pathsep in ospath:
        pathsep = ':'
    paths = ospath.split(pathsep)
    for d in paths:
        found = find(name, d)
        if found[0]:
            return found
    return found


def vgui_find_in_path(name):
    found = False
    feninfo = CodefenInfos.FenInfo()
    feninfo.show()
    feninfo.setWindowTitle(u'Guic2py - Option "%s"' % platform.system())
    feninfo.lblTitre.setText(u"Recherche de <B><font color=blue>%s</font></b> dans les chemins d'accès ..." % name)
    ospath = os.getenv('PATH')
    pathsep = ';'
    if not pathsep in ospath:
        pathsep = ':'
    paths = ospath.split(pathsep)
    x = 0
    for d in paths:
        x += 1
        feninfo.txtTexte.append(u"%03d -> <B><font color=blue>%s</font></B>" % (x, d))
        feninfo.repaint()
        found = find(name, d)
        if found[0]:
            feninfo.close()
            return found
    feninfo.close()
    return found


def find_all(name, path='/'):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


def find_matching(pattern='*', path='/'):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def main():
    isfound, where = find_in_path('pyside-uic')
    if isfound:
        print "Voici les trouvailles! : " + where
    else:
        print "Pas trouvé !"


if __name__ == '__main__':
    main()

# END OF SCRIPT
