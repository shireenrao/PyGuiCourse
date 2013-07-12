# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Jul 12 18:32:23 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(529, 334)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/osx.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainDialog.setWindowIcon(icon)
        self.xpButton = QtGui.QPushButton(mainDialog)
        self.xpButton.setGeometry(QtCore.QRect(30, 70, 151, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/windows_xp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xpButton.setIcon(icon1)
        self.xpButton.setIconSize(QtCore.QSize(32, 32))
        self.xpButton.setObjectName("xpButton")
        self.ubuntuButton = QtGui.QPushButton(mainDialog)
        self.ubuntuButton.setGeometry(QtCore.QRect(190, 70, 151, 81))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/ubuntu.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ubuntuButton.setIcon(icon2)
        self.ubuntuButton.setIconSize(QtCore.QSize(32, 32))
        self.ubuntuButton.setObjectName("ubuntuButton")
        self.debainButton = QtGui.QPushButton(mainDialog)
        self.debainButton.setGeometry(QtCore.QRect(350, 70, 151, 81))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/debian.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.debainButton.setIcon(icon3)
        self.debainButton.setIconSize(QtCore.QSize(32, 32))
        self.debainButton.setObjectName("debainButton")

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(QtGui.QApplication.translate("mainDialog", "Pick an OS", None, QtGui.QApplication.UnicodeUTF8))
        self.xpButton.setText(QtGui.QApplication.translate("mainDialog", "Load XP", None, QtGui.QApplication.UnicodeUTF8))
        self.ubuntuButton.setText(QtGui.QApplication.translate("mainDialog", "Load Ubuntu", None, QtGui.QApplication.UnicodeUTF8))
        self.debainButton.setText(QtGui.QApplication.translate("mainDialog", "Load Debian", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
