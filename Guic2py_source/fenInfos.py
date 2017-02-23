# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Mathlab/Documents/Mes Sources/Python/PycharmProjects/Guic2py/fenInfos.ui'
#
# Created: Tue Oct 28 07:42:13 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_StatusDialog(object):
    def setupUi(self, StatusDialog):
        StatusDialog.setObjectName("StatusDialog")
        StatusDialog.setWindowModality(QtCore.Qt.WindowModal)
        StatusDialog.resize(653, 267)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StatusDialog.sizePolicy().hasHeightForWidth())
        StatusDialog.setSizePolicy(sizePolicy)
        self.widget = QtGui.QWidget(StatusDialog)
        self.widget.setGeometry(QtCore.QRect(11, 11, 631, 249))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblTitre = QtGui.QLabel(self.widget)
        self.lblTitre.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitre.setObjectName("lblTitre")
        self.verticalLayout_2.addWidget(self.lblTitre)
        self.txtTexte = QtGui.QTextEdit(self.widget)
        self.txtTexte.setObjectName("txtTexte")
        self.verticalLayout_2.addWidget(self.txtTexte)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnClose = QtGui.QPushButton(self.widget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_2.addWidget(self.btnClose)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(StatusDialog)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL("clicked()"), StatusDialog.close)
        QtCore.QMetaObject.connectSlotsByName(StatusDialog)

    def retranslateUi(self, StatusDialog):
        StatusDialog.setWindowTitle(QtGui.QApplication.translate("StatusDialog", "Informations", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTitre.setText(QtGui.QApplication.translate("StatusDialog", "Titre du contenu", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose.setText(QtGui.QApplication.translate("StatusDialog", "Fermer", None, QtGui.QApplication.UnicodeUTF8))

