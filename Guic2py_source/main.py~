#!/usr/bin/python
# -*- coding: utf-8 -*-
# ------------------------------------------------------
# Projet......: Guic2py
# Fichier.....: main.py
# Auteur......: daniel
# Création....: 20141021
# Version.....: 1.00.09
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
# inclure le fichier genere par pyside-uic
# 	ex. pyside-ui fenMain.ui -o QTGUI_Video_02_def_ui.py
import Guic2py_dialog1
import pyutils as pu
import fenInfos
# On se defini une classe de type "QDialog" pointant sur la
# definition de Interface


class Form(QDialog, Guic2py_dialog1.Ui_Dialog):
    # Le nom du programme
    ostype = u''
    scriptname = u"Guic2py"
    pyside_uic = u""
    pyuic4 = u""
    userconv = u""
    convertisseur = u""
    convpath = u""
    convparam = u"{SRC} -o {DST}"
    sourcepath = u""
    sourcefile = u""
    targetpath = u""
    targetfile = u""
    srcdstfmt = u''
    cmdfmt = u''
    cmdfilter = u'Tous (* *.*)'
    pyqt4cmd = u''
    pysidecmd = u''


# Comme il n'y a pas de constructeur genere par pyside-uic
# On en defini un que l'on doit lancer manuellement
    def __init__(self, parent=None):
        # On appelle le constructeur de la classe mère de notre classe Form
        super(Form, self).__init__(parent)
        # On cré les éléments graphiques de l'interface tel que par QTdesigner
        self.setupUi(self)
        #self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        # On connecte un un objet à un évenement et à une méthode à exécuter
        # les actions des boutons
        self.connect(self.btn_Go, SIGNAL("clicked()"), self.btn_Go_clicked)
        self.connect(self.btn_Quit, SIGNAL("clicked()"), self.btn_Quit_clicked)
        self.connect(self.btn_SelUtil, SIGNAL("clicked()"), self.select_util)
        self.connect(self.btn_SelSrcDirFile, SIGNAL("clicked()"), self.select_source)
        self.connect(self.btn_SelDstDir, SIGNAL("clicked()"), self.select_targetpath)
        self.connect(self.btn_APropos, SIGNAL("clicked()"), self.apropos)
        # les action des boutons de radio
        self.connect(self.rad_pyside, SIGNAL("clicked()"), self.refresh)
        self.connect(self.rad_pyqt4, SIGNAL("clicked()"), self.refresh)
        self.connect(self.rad_Perso, SIGNAL("clicked()"), self.refresh)
        # evenement écriture dans les champs texte
        self.connect(self.line_UtilParams, SIGNAL("editingFinished()"), self.newparam)
        # On initialise tous les paramêtres
        self.initialisation()
    # ici on défini la méthode exécuté par l"évenement

    def initialisation(self):
        self.ostype = platform.system()
        self.lbl_interpreteur.setText('Choisir un convertisseur sous "<font color=red>%s</font>" :' % self.ostype)
        self.setWindowTitle(u'Guic2py - Option "%s"' % platform.system())
        if "ndow" in platform.platform():
            self.srcdstfmt = u'"%s/%s"'
            self.cmdfmt = u'""%s" %s"'
            self.pyqt4cmd = 'pyuic4.exe'
            self.pysidecmd = 'pyside-uic.exe'
            self.cmdfilter = u'Exécutables MsWindows &tm;(*.com, *.exe);;Tous (* *.*)'
        else:
            self.srcdstfmt = u'%s/%s'
            self.cmdfmt = u'%s %s'
            self.pyqt4cmd = 'pyuic4'
            self.pysidecmd = 'pyside-uic'
        self.sourcepath = os.getcwd()
        self.targetpath = os.getcwd()
        self.is_pyuic4, self.pyuic4 = pu.vgui_find_in_path(self.pyqt4cmd)
        self.is_pyside, self.pyside_uic = pu.vgui_find_in_path(self.pysidecmd)

        self.rad_pyside.setChecked(True)
        if not self.is_pyuic4:
            self.rad_pyqt4.setVisible(False)
            self.rad_pyqt4.setChecked(False)
            self.rad_pyside.setChecked(True)
        if not self.is_pyside:
            self.rad_pyside.setVisible(False)
            self.rad_pyside.setChecked(False)
            self.rad_Perso.setChecked(True)
        self.sourcepath=os.getcwd()
        self.targetpath=os.getcwd()
        self.refresh()

    def newparam(self):
        self.convparam = self.line_UtilParams.text()
#        print self.line_UtilParams.text()

    def select_util(self):
        self.rad_Perso.setChecked(True)
        self.refresh()
        rep=self.convpath
        convobj = QFileDialog.getOpenFileName(self, self.scriptname + u' - Choisir convertisseur',
                                              dir=rep, filter=self.cmdfilter )
        self.userconv=convobj[0]
        self.set_convertisseur(self.userconv)
        self.refresh()

    def select_source(self):
        rep=self.sourcepath
        convobj = QFileDialog.getOpenFileName(self, self.scriptname + u' - Choisir la source!',
                                              dir=rep, filter=u"Fichiers ui (*.ui *.UI);;Tous (* *.*)")
        self.sourcepath = os.path.dirname(convobj[0])
        self.sourcefile = os.path.basename(convobj[0])
        self.targetpath = os.path.dirname(convobj[0])
        self.targetfile = os.path.basename(convobj[0]).replace('.ui','.py')
        self.refresh()

    def select_targetpath(self):
        rep=self.targetpath
        convobj = QFileDialog.getExistingDirectory(self, self.scriptname + u' - Choisir répertoire destination!', dir=rep, options=QFileDialog.ShowDirsOnly)
        self.targetpath = convobj
        self.targetfile = self.line_SrcFile.text().replace('.ui','.py')
        self.refresh()

    def btn_Go_clicked(self):
        for lineobj in [ self.line_SrcDir, self.line_DstDir,
                        self.line_SrcFile, self.line_DstFile,
                        self.line_UtilLocation ]:
            lineobj.setStyleSheet('color: black;')
        if self.check():
            util = str(self.line_UtilLocation.text())
            tmpsrc = self.srcdstfmt % (self.line_SrcDir.text(),self.line_SrcFile.text())
            tmpdst = self.srcdstfmt % (self.line_DstDir.text(),self.line_DstFile.text())
            source = tmpsrc
            target = tmpdst
            if not "indow" in platform.platform():
                util = util.replace(' ','\ ')
                source = tmpsrc.replace(' ','\ ')
                target = tmpdst.replace(' ','\ ')
            #params = self.convparam.replace("{SRC}", '"' + source + '"').replace("{DST}", '"' + target + '"')
            params = self.convparam.replace("{SRC}", source).replace("{DST}",target)
            commande = self.cmdfmt % (util, params)
            print commande
            error = os.system(commande)
#            error = 0
            print error
            if error == 0:
                QMessageBox.about(self, u"Commande", u"%s" % commande)
            else:
                QMessageBox.warning(self, u"Erreur", u"Une erreur système est survenue!\nVérifiez vos paramêtres.")


    def check(self):
        for lineobj in [ self.line_SrcDir, self.line_DstDir ]:
            if not os.path.isdir(lineobj.text()):
                self.set_color_focus(lineobj)
                QMessageBox.warning(self, u"Erreur", u"Le répertoire %s n'existe pas." % lineobj.text())
                return False
        if not os.path.isfile(self.line_SrcDir.text() + '/' + self.line_SrcFile.text()):
                self.set_color_focus(self.line_SrcFile)
                QMessageBox.warning(self, u"Erreur", u"Le fichier %s n'existe pas." %
                        (self.line_SrcDir.text() + '/' + self.line_SrcFile.text()))
                return False
        return True

    def set_color_focus(self,lineobject):
        lineobject.setStyleSheet('color: red;')
        #lineobject.setText('<font color=red>%s</font>' % lineobject.text())
        lineobject.setFocus()

    def btn_Quit_clicked(self):
        self.saveconfig()
        self.close()

    def saveconfig(self):
        apppath = os.path.expanduser('~') + '/.Guic2py'
        if not os.path.isdir(apppath):
            try:
                print apppath + u"/Guic2py.conf"
                os.mkdir(apppath)
            except:
                QMessageBox.warning(self, u"Erreur", u"Le répertoire %s n'existe pas." % apppath)
                print "Impossible de créer le répertoire de sauvegarde."
        else:
            try:
                f=open(apppath + u"/Guic2py.conf", "w+")
                f.write(u"line_UtilLocation:%s\n" % self.line_UtilLocation.text())
                f.write(u"line_UtilParams:%s\n" % self.line_UtilParams.text())
                f.write(u"line_SrcDir:%s\n" % self.line_SrcDir.text())
                f.write(u"line_SrcFile:%s\n" % self.line_SrcFile.text())
                f.write(u"line_DstDir:%s\n" % self.line_DstDir.text())
                f.write(u"line_DstFile:%s\n" % self.line_DstFile.text())
                f.close()
            except:
                QMessageBox.warning(self, u"Erreur", u"Impossible de créer le fichier de sauvegardes.")
                print "Impossible de créer le fichier de sauvegarde."

    def set_convertisseur(self, convertisseur):
        self.convertisseur = convertisseur
        if not convertisseur == None:
            self.convpath = os.path.dirname(convertisseur)

    def refresh(self):
        # On prend des décision en fonction des conditions
        if self.rad_pyside.isChecked():
            self.btn_SelUtil.setEnabled(False)
            self.btn_SelUtil.setVisible(False)
            self.set_convertisseur(self.pyside_uic)
            self.convparam = u"{SRC} -o {DST}"
        elif self.rad_pyqt4.isChecked():
            self.btn_SelUtil.setEnabled(False)
            self.btn_SelUtil.setVisible(False)
            self.set_convertisseur(self.pyuic4)
            self.convparam = u"{SRC} -o {DST}"
        elif self.rad_Perso.isChecked():
            self.btn_SelUtil.setEnabled(True)
            self.btn_SelUtil.setVisible(True)
            self.set_convertisseur(self.userconv)
            # self.convparam = ""
        else:
            self.convertisseur = u"Sélection nécessaire."
            self.line_UtilParams.setText(u"{SRC} -o {DST}")
        # On affiche le tout
        self.line_UtilLocation.setText(self.convertisseur)
        self.line_UtilParams.setText( self.convparam)
        self.line_SrcDir.setText(self.sourcepath)
        self.line_SrcFile.setText(self.sourcefile)
        self.line_DstDir.setText(self.targetpath)
        self.line_DstFile.setText(self.targetfile)
        self.setFocus()

    def apropos(self):
        #bells = QSound("mysounds/bells.wav")
        QMessageBox.about(self, u"Guic2py - Option \"%s\"" % platform.system(),
                          u"<H1> À propos ! </H1>"
                          u"<HR>" +
                          u"Utilitaire GUI pour la conversion des fichier QT &#153; (*.ui) en source python (*.py)." +
                          u"<HR>" +
                          u"<P>Ce programme recherche la présence des commandes<br>" +
                          u"'pyuic4' et 'pyside-uic' dans les chemins d'accès de votre<br>" +
                          u"système et ajuste les choix en conséquence." +
                          u"</P>" +
                          u"<HR>" +
                          u"<P>Ce programme s'ajuste automatiquement pour les plateformes ;<br>" +
                          u"Microsoft Windows &#153;, Apple Mac Os X &#153; et Linux/Unix.</P>" +
                          u"<HR>" +
                          u"<FONT>" +
                          u"<TABLE border=0 align=center cellpadding=4>" +
                          u"<TR><TH rowspan=5><img src=\"./moi.jpg\" width=120></TH>"
                          u"<TH align=right>Projet:</TH><TD>Guic2py</TD></TR>" +
                          u"<TR><TH align=right>Auteur:</TH><TD>Daniel Lafrance</TD></TR>" +
                          u"<TR><TH align=right>Création:</TH><TD>20141021</TD></TR>" +
                          u"<TR><TH align=right>Version:</TH><TD>1.00.09</TD></TR>" +
                          u"<TR><TH align=right>Révision:</TH><TD>20141031</TD></TR>" +
                          u"<TR><TH colspan=3>&copy; 2014 Daniel Lafrance</Th></TR>"
                          u"</TABLE>" +
                          u"</font>" +
                          "" )
        #print 'allo'
        #bells.play()



def main():
    # On cre l'instance de l'interface graphique ...
    app = QApplication(sys.argv)
    # ... et de l'objet
    form = Form()
    # On l'affiche
    form.show()
    form.setFocus()
    # et on l'execute
    app.exec_()


if __name__ == "__main__":
    main()

# END OF SCRIPT
