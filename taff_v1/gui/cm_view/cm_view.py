# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cm_view.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(446, 753)
        self.gridLayout_6 = QtWidgets.QGridLayout(Form)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_initGUI = QtWidgets.QPushButton(self.tab_5)
        self.btn_initGUI.setObjectName("btn_initGUI")
        self.gridLayout.addWidget(self.btn_initGUI, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 2, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_eut = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_eut.setObjectName("checkBox_eut")
        self.gridLayout_3.addWidget(self.checkBox_eut, 2, 0, 1, 1)
        self.comboBox_eut = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_eut.setStyleSheet("font: 11pt \"FreeMono\";")
        self.comboBox_eut.setObjectName("comboBox_eut")
        self.gridLayout_3.addWidget(self.comboBox_eut, 2, 1, 1, 1)
        self.comboBox_ctrl = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ctrl.setStyleSheet("font: 11pt \"FreeMono\";")
        self.comboBox_ctrl.setObjectName("comboBox_ctrl")
        self.gridLayout_3.addWidget(self.comboBox_ctrl, 8, 1, 1, 1)
        self.checkBox_cpu = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_cpu.setObjectName("checkBox_cpu")
        self.gridLayout_3.addWidget(self.checkBox_cpu, 6, 0, 1, 1)
        self.checkBox_ctrl = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_ctrl.setObjectName("checkBox_ctrl")
        self.gridLayout_3.addWidget(self.checkBox_ctrl, 8, 0, 1, 1)
        self.comboBox_cpu = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_cpu.setStyleSheet("font: 11pt \"FreeMono\";")
        self.comboBox_cpu.setObjectName("comboBox_cpu")
        self.gridLayout_3.addWidget(self.comboBox_cpu, 6, 1, 1, 1)
        self.checkBox_config = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_config.setObjectName("checkBox_config")
        self.gridLayout_3.addWidget(self.checkBox_config, 5, 0, 1, 1)
        self.checkBox_system = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_system.setObjectName("checkBox_system")
        self.gridLayout_3.addWidget(self.checkBox_system, 4, 0, 1, 1)
        self.comboBox_config = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_config.setStyleSheet("font: 11pt \"FreeMono\";")
        self.comboBox_config.setObjectName("comboBox_config")
        self.gridLayout_3.addWidget(self.comboBox_config, 5, 1, 1, 1)
        self.comboBox_system = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_system.setStyleSheet("font: 11pt \"FreeMono\";")
        self.comboBox_system.setObjectName("comboBox_system")
        self.gridLayout_3.addWidget(self.comboBox_system, 4, 1, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_3.addWidget(self.comboBox_6, 15, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_3.addWidget(self.checkBox_4, 13, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_3.addWidget(self.checkBox_6, 15, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 9, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_3.addWidget(self.comboBox_4, 13, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_3.addWidget(self.checkBox_2, 11, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_3.addWidget(self.comboBox_2, 11, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 9, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 12, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_3.addWidget(self.checkBox_5, 14, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_3.addWidget(self.comboBox_5, 14, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_3.addWidget(self.comboBox_3, 12, 1, 1, 1)
        self.btn_load_cm = QtWidgets.QPushButton(self.groupBox)
        self.btn_load_cm.setObjectName("btn_load_cm")
        self.gridLayout_3.addWidget(self.btn_load_cm, 17, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 16, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_36 = QtWidgets.QLabel(self.groupBox_2)
        self.label_36.setObjectName("label_36")
        self.gridLayout_5.addWidget(self.label_36, 0, 0, 1, 1)
        self.label_status01 = QtWidgets.QLabel(self.groupBox_2)
        self.label_status01.setObjectName("label_status01")
        self.gridLayout_5.addWidget(self.label_status01, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_37 = QtWidgets.QLabel(self.tab)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 0, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.tab)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 0, 1, 1, 1)
        self.list_climatcMeasur = QtWidgets.QListWidget(self.tab)
        self.list_climatcMeasur.setStyleSheet("font: 11pt \"FreeMono\";")
        self.list_climatcMeasur.setObjectName("list_climatcMeasur")
        self.gridLayout_2.addWidget(self.list_climatcMeasur, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setObjectName("widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_cmIDinput = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_cmIDinput.setObjectName("lineEdit_cmIDinput")
        self.gridLayout_7.addWidget(self.lineEdit_cmIDinput, 0, 1, 1, 1)
        self.btn_load_cmData = QtWidgets.QPushButton(self.widget)
        self.btn_load_cmData.setObjectName("btn_load_cmData")
        self.gridLayout_7.addWidget(self.btn_load_cmData, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 0, 2, 1, 1)
        self.gridLayout_12.addWidget(self.widget, 0, 0, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_cminfo01 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo01.setObjectName("lineEdit_cminfo01")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo01, 0, 1, 1, 1)
        self.label_cminfo_1 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_cminfo_1.setFont(font)
        self.label_cminfo_1.setObjectName("label_cminfo_1")
        self.gridLayout_9.addWidget(self.label_cminfo_1, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_cminfo02 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo02.setObjectName("lineEdit_cminfo02")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo02, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_9.addWidget(self.label_11, 2, 0, 1, 1)
        self.lineEdit_cminfo03 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo03.setObjectName("lineEdit_cminfo03")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo03, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 2, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_9.addWidget(self.label_12, 3, 0, 1, 1)
        self.lineEdit_cminfo04 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo04.setObjectName("lineEdit_cminfo04")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo04, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_9.addWidget(self.label_7, 3, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.label_13, 4, 0, 1, 1)
        self.lineEdit_cminfo05 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo05.setObjectName("lineEdit_cminfo05")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo05, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_9.addWidget(self.label_8, 4, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_9.addWidget(self.label_14, 5, 0, 1, 1)
        self.lineEdit_cminfo06 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo06.setObjectName("lineEdit_cminfo06")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo06, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_9.addWidget(self.label_9, 5, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_9.addWidget(self.label_15, 6, 0, 1, 1)
        self.lineEdit_cminfo07 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo07.setObjectName("lineEdit_cminfo07")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo07, 6, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_9.addWidget(self.label_10, 6, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_9.addWidget(self.label_16, 7, 0, 1, 1)
        self.lineEdit_cminfo08 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo08.setObjectName("lineEdit_cminfo08")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo08, 7, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_9.addWidget(self.label_27, 7, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_9.addWidget(self.label_18, 8, 0, 1, 1)
        self.lineEdit_cminfo09 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo09.setObjectName("lineEdit_cminfo09")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo09, 8, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_9.addWidget(self.label_23, 8, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_9.addWidget(self.label_19, 9, 0, 1, 1)
        self.lineEdit_cminfo10 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo10.setObjectName("lineEdit_cminfo10")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo10, 9, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_9.addWidget(self.label_28, 9, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_9.addWidget(self.label_29, 10, 0, 1, 1)
        self.lineEdit_cminfo11 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo11.setObjectName("lineEdit_cminfo11")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo11, 10, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_9.addWidget(self.label_22, 10, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout_9.addWidget(self.label_30, 11, 0, 1, 1)
        self.lineEdit_cminfo12 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo12.setObjectName("lineEdit_cminfo12")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo12, 11, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_9.addWidget(self.label_25, 11, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_9.addWidget(self.label_31, 12, 0, 1, 1)
        self.lineEdit_cminfo13 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo13.setObjectName("lineEdit_cminfo13")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo13, 12, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_9.addWidget(self.label_24, 12, 2, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout_9.addWidget(self.label_32, 13, 0, 1, 1)
        self.lineEdit_cminfo14 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo14.setObjectName("lineEdit_cminfo14")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo14, 13, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_9.addWidget(self.label_26, 13, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_9.addWidget(self.label_33, 14, 0, 1, 1)
        self.lineEdit_cminfo15 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo15.setObjectName("lineEdit_cminfo15")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo15, 14, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_9.addWidget(self.label_21, 14, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_9.addWidget(self.label_34, 15, 0, 1, 1)
        self.lineEdit_cminfo16 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo16.setObjectName("lineEdit_cminfo16")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo16, 15, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_9.addWidget(self.label_20, 15, 2, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.gridLayout_9.addWidget(self.label_35, 16, 0, 1, 1)
        self.lineEdit_cminfo17 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_cminfo17.setObjectName("lineEdit_cminfo17")
        self.gridLayout_9.addWidget(self.lineEdit_cminfo17, 16, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_9.addWidget(self.label_17, 16, 2, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.table_sensorvalues = QtWidgets.QTableWidget(self.tab_4)
        self.table_sensorvalues.setObjectName("table_sensorvalues")
        self.table_sensorvalues.setColumnCount(5)
        self.table_sensorvalues.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_sensorvalues.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_sensorvalues.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_sensorvalues.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_sensorvalues.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_sensorvalues.setHorizontalHeaderItem(4, item)
        self.gridLayout_11.addWidget(self.table_sensorvalues, 0, 0, 1, 2)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.gridLayout_12.addWidget(self.tabWidget_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_6.addWidget(self.tabWidget, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_initGUI.setText(_translate("Form", "update GUI"))
        self.groupBox.setTitle(_translate("Form", "Search for:"))
        self.checkBox_eut.setText(_translate("Form", "eut [id]"))
        self.checkBox_cpu.setText(_translate("Form", "cpu [name]"))
        self.checkBox_ctrl.setText(_translate("Form", "ctrl [name]"))
        self.checkBox_config.setText(_translate("Form", "configuration [id]"))
        self.checkBox_system.setText(_translate("Form", "system[name]"))
        self.checkBox_4.setText(_translate("Form", "CheckBox"))
        self.checkBox_6.setText(_translate("Form", "CheckBox"))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))
        self.checkBox.setText(_translate("Form", "CheckBox"))
        self.checkBox_3.setText(_translate("Form", "CheckBox"))
        self.checkBox_5.setText(_translate("Form", "CheckBox"))
        self.btn_load_cm.setText(_translate("Form", "Load Data"))
        self.groupBox_2.setTitle(_translate("Form", "Status:"))
        self.label_36.setText(_translate("Form", "Status: "))
        self.label_status01.setText(_translate("Form", "---"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Page"))
        self.label_37.setText(_translate("Form", "Search command:"))
        self.label_38.setText(_translate("Form", "hier soll der befehl angezeigt werden "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Climatic Measurements"))
        self.label_2.setText(_translate("Form", "Climatic measurement (ID):"))
        self.lineEdit_cmIDinput.setText(_translate("Form", "1"))
        self.btn_load_cmData.setText(_translate("Form", "load cm Data"))
        self.label_5.setText(_translate("Form", "ID:"))
        self.label_cminfo_1.setText(_translate("Form", "id_cm"))
        self.label_6.setText(_translate("Form", "Name:"))
        self.label_3.setText(_translate("Form", "name_cm"))
        self.label_11.setText(_translate("Form", "Info:"))
        self.label_4.setText(_translate("Form", "info_cm"))
        self.label_12.setText(_translate("Form", "Test load:"))
        self.label_7.setText(_translate("Form", "name_tl"))
        self.label_13.setText(_translate("Form", "EUT Name:"))
        self.label_8.setText(_translate("Form", "name_eut"))
        self.label_14.setText(_translate("Form", "EUT Info:"))
        self.label_9.setText(_translate("Form", "info_eut"))
        self.label_15.setText(_translate("Form", "System Name:"))
        self.label_10.setText(_translate("Form", "name_system"))
        self.label_16.setText(_translate("Form", "Config. Name:"))
        self.label_27.setText(_translate("Form", "name_cfg"))
        self.label_18.setText(_translate("Form", "Config. Info:"))
        self.label_23.setText(_translate("Form", "info_cfg"))
        self.label_19.setText(_translate("Form", "Chassis:"))
        self.label_28.setText(_translate("Form", "name_ch"))
        self.label_29.setText(_translate("Form", "Motherboard:"))
        self.label_22.setText(_translate("Form", "name_mobo"))
        self.label_30.setText(_translate("Form", "HDD count:"))
        self.label_25.setText(_translate("Form", "HDD Anzahl"))
        self.label_31.setText(_translate("Form", "HDD Name:"))
        self.label_24.setText(_translate("Form", "name_hdd"))
        self.label_32.setText(_translate("Form", "CPU count:"))
        self.label_26.setText(_translate("Form", "CPU Anzahl"))
        self.label_33.setText(_translate("Form", "CPU Name:"))
        self.label_21.setText(_translate("Form", "name_cpu"))
        self.label_34.setText(_translate("Form", "MEM Count:"))
        self.label_20.setText(_translate("Form", "MEM_ Anzahl"))
        self.label_35.setText(_translate("Form", "MEM Name:"))
        self.label_17.setText(_translate("Form", "name_mem"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Form", "EUT Info"))
        item = self.table_sensorvalues.horizontalHeaderItem(0)
        item.setText(_translate("Form", "sensorName"))
        item = self.table_sensorvalues.horizontalHeaderItem(1)
        item.setText(_translate("Form", "sensorType"))
        item = self.table_sensorvalues.horizontalHeaderItem(2)
        item.setText(_translate("Form", "SensorMax"))
        item = self.table_sensorvalues.horizontalHeaderItem(3)
        item.setText(_translate("Form", "sensorValue"))
        item = self.table_sensorvalues.horizontalHeaderItem(4)
        item.setText(_translate("Form", "sensorDiff"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "sensor Values"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "CM - Data"))
        self.label.setText(_translate("Form", "Climatic Measurement Viewer"))

