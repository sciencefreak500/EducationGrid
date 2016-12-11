# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EducationGridGUIInstaller.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EducationGridGUIInstaller(object):
    def setupUi(self, EducationGridGUIInstaller):
        EducationGridGUIInstaller.setObjectName(_fromUtf8("EducationGridGUIInstaller"))
        EducationGridGUIInstaller.resize(243, 270)
        self.verticalLayout_2 = QtGui.QVBoxLayout(EducationGridGUIInstaller)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(EducationGridGUIInstaller)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.checkBox = QtGui.QCheckBox(EducationGridGUIInstaller)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(EducationGridGUIInstaller)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout.addWidget(self.checkBox_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(EducationGridGUIInstaller)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(EducationGridGUIInstaller)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(EducationGridGUIInstaller)
        QtCore.QMetaObject.connectSlotsByName(EducationGridGUIInstaller)

    def retranslateUi(self, EducationGridGUIInstaller):
        EducationGridGUIInstaller.setWindowTitle(_translate("EducationGridGUIInstaller", "Form", None))
        self.label.setText(_translate("EducationGridGUIInstaller", "Download Boinc and/or GridCoin", None))
        self.checkBox.setText(_translate("EducationGridGUIInstaller", "Boinc", None))
        self.checkBox_2.setText(_translate("EducationGridGUIInstaller", "GridCoin", None))
        self.pushButton_2.setText(_translate("EducationGridGUIInstaller", "Ok", None))
        self.pushButton.setText(_translate("EducationGridGUIInstaller", "Cancel", None))

