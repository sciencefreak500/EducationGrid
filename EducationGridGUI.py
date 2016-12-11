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
        EducationGridGUIInstaller.resize(281, 191)
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
        self.label_2 = QtGui.QLabel(EducationGridGUIInstaller)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.BoincCheck = QtGui.QCheckBox(EducationGridGUIInstaller)
        self.BoincCheck.setObjectName(_fromUtf8("BoincCheck"))
        self.verticalLayout.addWidget(self.BoincCheck)
        self.GridCoinCheck = QtGui.QCheckBox(EducationGridGUIInstaller)
        self.GridCoinCheck.setObjectName(_fromUtf8("GridCoinCheck"))
        self.verticalLayout.addWidget(self.GridCoinCheck)
        self.SchoolCheck = QtGui.QCheckBox(EducationGridGUIInstaller)
        self.SchoolCheck.setObjectName(_fromUtf8("SchoolCheck"))
        self.verticalLayout.addWidget(self.SchoolCheck)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.OkButton = QtGui.QPushButton(EducationGridGUIInstaller)
        self.OkButton.setObjectName(_fromUtf8("OkButton"))
        self.horizontalLayout.addWidget(self.OkButton)
        self.CancelButton = QtGui.QPushButton(EducationGridGUIInstaller)
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(EducationGridGUIInstaller)
        QtCore.QMetaObject.connectSlotsByName(EducationGridGUIInstaller)

    def retranslateUi(self, EducationGridGUIInstaller):
        EducationGridGUIInstaller.setWindowTitle(_translate("EducationGridGUIInstaller", "Form", None))
        self.label.setText(_translate("EducationGridGUIInstaller", "Download EducationGrid ", None))
        self.label_2.setText(_translate("EducationGridGUIInstaller", "Software Components", None))
        self.BoincCheck.setText(_translate("EducationGridGUIInstaller", "Boinc", None))
        self.GridCoinCheck.setText(_translate("EducationGridGUIInstaller", "GridCoin", None))
        self.SchoolCheck.setText(_translate("EducationGridGUIInstaller", "School Platform", None))
        self.OkButton.setText(_translate("EducationGridGUIInstaller", "Ok", None))
        self.CancelButton.setText(_translate("EducationGridGUIInstaller", "Cancel", None))

