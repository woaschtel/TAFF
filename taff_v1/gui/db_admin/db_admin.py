# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_admin.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(775, 485)
        self.gridLayout_7 = QtWidgets.QGridLayout(Form)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.btn_loadData = QtWidgets.QPushButton(self.widget_3)
        self.btn_loadData.setObjectName("btn_loadData")
        self.gridLayout_6.addWidget(self.btn_loadData, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout_7.addWidget(self.widget_3, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setMinimumSize(QtCore.QSize(350, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -83, 480, 631))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setMinimumSize(QtCore.QSize(320, 0))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.groupBox)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_cmCount = QtWidgets.QLabel(self.widget_2)
        self.label_cmCount.setObjectName("label_cmCount")
        self.gridLayout_4.addWidget(self.label_cmCount, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.widget_2, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.groupBox)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 12, 0, 1, 1)
        self.label_ambientCount = QtWidgets.QLabel(self.widget)
        self.label_ambientCount.setObjectName("label_ambientCount")
        self.gridLayout_3.addWidget(self.label_ambientCount, 2, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 8, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_chassisCount = QtWidgets.QLabel(self.widget)
        self.label_chassisCount.setObjectName("label_chassisCount")
        self.gridLayout_3.addWidget(self.label_chassisCount, 5, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 9, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 7, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 14, 0, 1, 1)
        self.label_EUTCount = QtWidgets.QLabel(self.widget)
        self.label_EUTCount.setObjectName("label_EUTCount")
        self.gridLayout_3.addWidget(self.label_EUTCount, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 13, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 4, 0, 1, 1)
        self.label_systemCount = QtWidgets.QLabel(self.widget)
        self.label_systemCount.setObjectName("label_systemCount")
        self.gridLayout_3.addWidget(self.label_systemCount, 1, 1, 1, 1)
        self.label_testloadCount = QtWidgets.QLabel(self.widget)
        self.label_testloadCount.setObjectName("label_testloadCount")
        self.gridLayout_3.addWidget(self.label_testloadCount, 3, 1, 1, 1)
        self.label_configurationCount = QtWidgets.QLabel(self.widget)
        self.label_configurationCount.setObjectName("label_configurationCount")
        self.gridLayout_3.addWidget(self.label_configurationCount, 4, 1, 1, 1)
        self.label_cpuCount = QtWidgets.QLabel(self.widget)
        self.label_cpuCount.setObjectName("label_cpuCount")
        self.gridLayout_3.addWidget(self.label_cpuCount, 6, 1, 1, 1)
        self.label_hddCount = QtWidgets.QLabel(self.widget)
        self.label_hddCount.setObjectName("label_hddCount")
        self.gridLayout_3.addWidget(self.label_hddCount, 7, 1, 1, 1)
        self.label_memCount = QtWidgets.QLabel(self.widget)
        self.label_memCount.setObjectName("label_memCount")
        self.gridLayout_3.addWidget(self.label_memCount, 8, 1, 1, 1)
        self.label_moboCount = QtWidgets.QLabel(self.widget)
        self.label_moboCount.setObjectName("label_moboCount")
        self.gridLayout_3.addWidget(self.label_moboCount, 9, 1, 1, 1)
        self.label_psuCount = QtWidgets.QLabel(self.widget)
        self.label_psuCount.setObjectName("label_psuCount")
        self.gridLayout_3.addWidget(self.label_psuCount, 12, 1, 1, 1)
        self.label_pcieCtrlTableCount = QtWidgets.QLabel(self.widget)
        self.label_pcieCtrlTableCount.setObjectName("label_pcieCtrlTableCount")
        self.gridLayout_3.addWidget(self.label_pcieCtrlTableCount, 13, 1, 1, 1)
        self.label_pcieCtrlCount = QtWidgets.QLabel(self.widget)
        self.label_pcieCtrlCount.setObjectName("label_pcieCtrlCount")
        self.gridLayout_3.addWidget(self.label_pcieCtrlCount, 14, 1, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 4, 0, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.groupBox)
        self.label_42.setObjectName("label_42")
        self.gridLayout_5.addWidget(self.label_42, 3, 0, 1, 1)
        self.widget_31 = QtWidgets.QWidget(self.groupBox)
        self.widget_31.setObjectName("widget_31")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_31)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_36 = QtWidgets.QLabel(self.widget_31)
        self.label_36.setObjectName("label_36")
        self.gridLayout_8.addWidget(self.label_36, 4, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.widget_31)
        self.label_33.setObjectName("label_33")
        self.gridLayout_8.addWidget(self.label_33, 1, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.widget_31)
        self.label_32.setObjectName("label_32")
        self.gridLayout_8.addWidget(self.label_32, 0, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.widget_31)
        self.label_34.setObjectName("label_34")
        self.gridLayout_8.addWidget(self.label_34, 2, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.widget_31)
        self.label_35.setObjectName("label_35")
        self.gridLayout_8.addWidget(self.label_35, 3, 0, 1, 1)
        self.label_sensorNameCount = QtWidgets.QLabel(self.widget_31)
        self.label_sensorNameCount.setObjectName("label_sensorNameCount")
        self.gridLayout_8.addWidget(self.label_sensorNameCount, 0, 1, 1, 1)
        self.label_sensorMaxCount = QtWidgets.QLabel(self.widget_31)
        self.label_sensorMaxCount.setObjectName("label_sensorMaxCount")
        self.gridLayout_8.addWidget(self.label_sensorMaxCount, 1, 1, 1, 1)
        self.label_sensorValueCount = QtWidgets.QLabel(self.widget_31)
        self.label_sensorValueCount.setObjectName("label_sensorValueCount")
        self.gridLayout_8.addWidget(self.label_sensorValueCount, 2, 1, 1, 1)
        self.label_sensorTypListCount = QtWidgets.QLabel(self.widget_31)
        self.label_sensorTypListCount.setObjectName("label_sensorTypListCount")
        self.gridLayout_8.addWidget(self.label_sensorTypListCount, 3, 1, 1, 1)
        self.label_sensorTypCount = QtWidgets.QLabel(self.widget_31)
        self.label_sensorTypCount.setObjectName("label_sensorTypCount")
        self.gridLayout_8.addWidget(self.label_sensorTypCount, 4, 1, 1, 1)
        self.gridLayout_5.addWidget(self.widget_31, 6, 0, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.gridLayout_5.addWidget(self.label_43, 5, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_7.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_delCM_id = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_delCM_id.setObjectName("lineEdit_delCM_id")
        self.gridLayout.addWidget(self.lineEdit_delCM_id, 1, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 2)
        self.btn_delCM = QtWidgets.QPushButton(self.frame_3)
        self.btn_delCM.setObjectName("btn_delCM")
        self.gridLayout.addWidget(self.btn_delCM, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_loadData.setText(_translate("Form", "load data"))
        self.label.setText(_translate("Form", "Database Administration Tool: "))
        self.groupBox.setTitle(_translate("Form", "Database Informations:"))
        self.label_4.setText(_translate("Form", "Climatic Measure:"))
        self.label_cmCount.setText(_translate("Form", "TextLabel"))
        self.label_11.setText(_translate("Form", "Climatic Measurement:"))
        self.label_10.setText(_translate("Form", "EUT Component:"))
        self.label_18.setText(_translate("Form", " - PSU:"))
        self.label_ambientCount.setText(_translate("Form", "TextLabel"))
        self.label_20.setText(_translate("Form", " - Testload:"))
        self.label_13.setText(_translate("Form", " - Memory:"))
        self.label_9.setText(_translate("Form", " - Chassis:"))
        self.label_19.setText(_translate("Form", " - System:"))
        self.label_chassisCount.setText(_translate("Form", "TextLabel"))
        self.label_12.setText(_translate("Form", " - Motherboard:"))
        self.label_5.setText(_translate("Form", " - HDD:"))
        self.label_7.setText(_translate("Form", " - CPU:"))
        self.label_6.setText(_translate("Form", "EUT:"))
        self.label_16.setText(_translate("Form", " - PCIe Ctrl:"))
        self.label_EUTCount.setText(_translate("Form", "TextLabel"))
        self.label_8.setText(_translate("Form", " - Ambient Temp:"))
        self.label_17.setText(_translate("Form", "PCIe Ctrl [Table]:"))
        self.label_21.setText(_translate("Form", "Configuration"))
        self.label_systemCount.setText(_translate("Form", "TextLabel"))
        self.label_testloadCount.setText(_translate("Form", "TextLabel"))
        self.label_configurationCount.setText(_translate("Form", "TextLabel"))
        self.label_cpuCount.setText(_translate("Form", "TextLabel"))
        self.label_hddCount.setText(_translate("Form", "TextLabel"))
        self.label_memCount.setText(_translate("Form", "TextLabel"))
        self.label_moboCount.setText(_translate("Form", "TextLabel"))
        self.label_psuCount.setText(_translate("Form", "TextLabel"))
        self.label_pcieCtrlTableCount.setText(_translate("Form", "TextLabel"))
        self.label_pcieCtrlCount.setText(_translate("Form", "TextLabel"))
        self.label_42.setText(_translate("Form", "([Count] and [id] should be the same)"))
        self.label_36.setText(_translate("Form", "- SensorTyp:"))
        self.label_33.setText(_translate("Form", "sensorMax:"))
        self.label_32.setText(_translate("Form", "sensor Name:"))
        self.label_34.setText(_translate("Form", "sensorValue:"))
        self.label_35.setText(_translate("Form", "sensorTyp_List:"))
        self.label_sensorNameCount.setText(_translate("Form", "TextLabel"))
        self.label_sensorMaxCount.setText(_translate("Form", "TextLabel"))
        self.label_sensorValueCount.setText(_translate("Form", "TextLabel"))
        self.label_sensorTypListCount.setText(_translate("Form", "TextLabel"))
        self.label_sensorTypCount.setText(_translate("Form", "TextLabel"))
        self.label_43.setText(_translate("Form", "Sensor Data:"))
        self.groupBox_2.setTitle(_translate("Form", "Tools"))
        self.label_2.setText(_translate("Form", "Delete Climatic Measurement:"))
        self.label_3.setText(_translate("Form", "id"))
        self.btn_delCM.setText(_translate("Form", "delete"))

