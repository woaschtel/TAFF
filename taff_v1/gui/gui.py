# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(816, 742)
        Form.setMinimumSize(QtCore.QSize(600, 600))
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 70))
        self.textBrowser.setMaximumSize(QtCore.QSize(200, 70))
        self.textBrowser.setStyleSheet("font: 63 11pt \"Tlwg Typo\";")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 4, 0, 1, 2)
        self.checkBox_openInfo = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_openInfo.setObjectName("checkBox_openInfo")
        self.gridLayout.addWidget(self.checkBox_openInfo, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.checkBox_openData = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_openData.setChecked(True)
        self.checkBox_openData.setObjectName("checkBox_openData")
        self.gridLayout.addWidget(self.checkBox_openData, 2, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.btn_openCM = QtWidgets.QPushButton(self.groupBox)
        self.btn_openCM.setObjectName("btn_openCM")
        self.gridLayout.addWidget(self.btn_openCM, 5, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_cmView = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_cmView.setObjectName("btn_cmView")
        self.gridLayout_2.addWidget(self.btn_cmView, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(65, 129, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 5, 1)
        self.btn_cmCreateMCPS = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_cmCreateMCPS.setObjectName("btn_cmCreateMCPS")
        self.gridLayout_2.addWidget(self.btn_cmCreateMCPS, 2, 0, 1, 1)
        self.btn_dbAdmin = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_dbAdmin.setObjectName("btn_dbAdmin")
        self.gridLayout_2.addWidget(self.btn_dbAdmin, 3, 0, 1, 1)
        self.btn_createEUT = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_createEUT.setObjectName("btn_createEUT")
        self.gridLayout_2.addWidget(self.btn_createEUT, 4, 0, 1, 1)
        self.btn_cmCreate = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_cmCreate.setObjectName("btn_cmCreate")
        self.gridLayout_2.addWidget(self.btn_cmCreate, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 3)
        self.mdiArea = QtWidgets.QMdiArea(Form)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout_3.addWidget(self.mdiArea, 0, 3, 3, 1)
        self.btn_test = QtWidgets.QPushButton(Form)
        self.btn_test.setObjectName("btn_test")
        self.gridLayout_3.addWidget(self.btn_test, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 0, 1, 3)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Info"))
        self.groupBox.setTitle(_translate("Form", "Open Climatic Measurement"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Tlwg Typo\'; font-size:11pt; font-weight:56; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-weight:600;\">INFO: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-weight:400;\">open &quot;cm_tabel&quot; and/or </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-weight:400;\">&quot;cm_info&quot; </span></p></body></html>"))
        self.checkBox_openInfo.setText(_translate("Form", "open [cm_info]"))
        self.label.setText(_translate("Form", "open cm by id"))
        self.checkBox_openData.setText(_translate("Form", "open [cm_tabel]"))
        self.btn_openCM.setText(_translate("Form", "openCM"))
        self.groupBox_2.setTitle(_translate("Form", "Tools:"))
        self.btn_cmView.setText(_translate("Form", "cm View"))
        self.btn_cmCreateMCPS.setText(_translate("Form", "cm CreateMCPS"))
        self.btn_dbAdmin.setText(_translate("Form", "db Admin"))
        self.btn_createEUT.setText(_translate("Form", "create EUT"))
        self.btn_cmCreate.setText(_translate("Form", "cm Create"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Viewer"))
        self.btn_test.setText(_translate("Form", "btn_test"))

