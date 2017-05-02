import sys
import csv
from PyQt5 import QtWidgets, QtCore
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QAction, QActionGroup, QApplication, QColorDialog,
        QComboBox, QDialog, QFontDialog, QGroupBox, QHBoxLayout, QLabel,
        QMainWindow, QMessageBox, QPushButton, QTableWidget,
        QTableWidgetItem, QToolBar)

from dbconnector import db_delete


if __name__ == '__main__':
    print("INFO: create_eut_handler class import as '__main__'")
    import db_admin
    # from ....dbconnector import db_select, db_insert
else:
    print("INFO: create_eut_handler class import as '__module__'")
    from gui.db_admin import db_admin
    from dbconnector import db_select, db_insert, db_selectAnalyser


class db_admin_handler(QtWidgets.QWidget):
    def __init__(self):
        super(db_admin_handler, self).__init__()
        self.ui = db_admin.Ui_Form()
        self.ui.setupUi(self)

        self.__dbSELECT = db_select.dbselect()
        self.__dbSELECTAnalyser = db_selectAnalyser.dbselect()
        self.__dbINSERT = db_insert.dbinsert()

        # Button connection --> clicked
        self.ui.btn_loadData.clicked.connect(self.event_btn_loadData)
        self.ui.btn_delCM.clicked.connect(self.event_btn_delCM)

    def event_btn_loadData(self):
        # hier muessen spater alle funktion aufgerufen werden die die labels
        # beschreiben ... damit das alles beim clicken des buttons load data
        # geladen wird

        self.__write_cm_label()
        self.__write_eut_label()
        self.__write_system_label()
        self.__write_ambientTemp_lable()
        self.__write_testLoad_lable()
        self.__write_configuration_lable()
        self.__write_chassis_lable()
        self.__write_cpu_lable()
        self.__write_hdd_lable()
        self.__write_mem_lable()
        self.__write_mobo_lable()
        self.__write_psu_lable()
        self.__write_pcieCtrlList_lable()
        self.__write_pcieCtrl_lable()
        self.__write_sensorName_lable()
        self.__write_sensorMax_lable()
        self.__write_sensorValue_lable()
        self.__write_sensorTypList_lable()
        self.__write_sensorTyp_lable()

    def __write_cm_label(self):
        # laden der anzahl von zeilen in der tabelle climaticmeasurment
        cm_count = self.__dbSELECT.count_climaticMeasurement()
        cm_max = self.__dbSELECT.MaxId_cmeasurement()
        # jetzt das lable beschrieften
        self.ui.label_cmCount.setText(
            "count: [{:05}] | max: [{:05}]".format(cm_count, cm_max))

    def __write_eut_label(self):
        # anzahl von zeilen in der tabelle eut
        eut_count = self.__dbSELECT.count_eut()
        eut_max = self.__dbSELECT.MaxId_eut()
        self.ui.label_EUTCount.setText(
            "count: [{:05}] | max: [{:05}]".format(eut_count, eut_max))

    def __write_system_label(self):
        # anzahl von zeilen in der tabelle system
        eut_count = self.__dbSELECT.count_system()
        eut_max = self.__dbSELECT.MaxId_system()
        self.ui.label_systemCount.setText(
            "count: [{:05}] | max: [{:05}]".format(eut_count, eut_max))

    def __write_ambientTemp_lable(self):
        ccount = self.__dbSELECT.count_ambientTemp()
        maxid = self.__dbSELECT.MaxId_ambientTemp()
        self.ui.label_ambientCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_testLoad_lable(self):
        ccount = self.__dbSELECT.count_testLoad()
        maxid = self.__dbSELECT.MaxId_testLoad()
        self.ui.label_testloadCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_configuration_lable(self):
        ccount = self.__dbSELECT.count_config()
        maxid = self.__dbSELECT.MaxId_config()
        self.ui.label_configurationCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_chassis_lable(self):
        ccount = self.__dbSELECT.count_chassis()
        maxid = self.__dbSELECT.MaxId_chassis()
        self.ui.label_chassisCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_cpu_lable(self):
        ccount = self.__dbSELECT.count_cpu()
        maxid = self.__dbSELECT.MaxId_cpu()
        self.ui.label_cpuCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_hdd_lable(self):
        ccount = self.__dbSELECT.count_hdd()
        maxid = self.__dbSELECT.MaxId_hdd()
        self.ui.label_hddCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_mem_lable(self):
        ccount = self.__dbSELECT.count_memory()
        maxid = self.__dbSELECT.MaxId_memory()
        self.ui.label_memCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_mobo_lable(self):
        ccount = self.__dbSELECT.count_mobo()
        maxid = self.__dbSELECT.MaxId_mobo()
        self.ui.label_moboCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_psu_lable(self):
        ccount = self.__dbSELECT.count_psu()
        maxid = self.__dbSELECT.MaxId_psu()
        self.ui.label_psuCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_pcieCtrlList_lable(self):
        ccount = self.__dbSELECT.count_pcieCtrlList()
        maxid = self.__dbSELECT.MaxId_pcieCtrlList()
        self.ui.label_pcieCtrlTableCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_pcieCtrl_lable(self):
        ccount = self.__dbSELECT.count_pcieCtrl()
        maxid = self.__dbSELECT.MaxId_pcieCtrl()
        self.ui.label_pcieCtrlCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_sensorName_lable(self):
        ccount = self.__dbSELECT.count_sensorName()
        maxid = self.__dbSELECT.MaxId_sensorName()
        self.ui.label_sensorNameCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_sensorMax_lable(self):
        ccount = self.__dbSELECT.count_sensorMax()
        maxid = self.__dbSELECT.MaxId_sensorMax()
        self.ui.label_sensorMaxCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_sensorValue_lable(self):
        ccount = self.__dbSELECT.count_sensorValue()
        maxid = self.__dbSELECT.MaxId_sensorValue()
        self.ui.label_sensorValueCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_sensorTypList_lable(self):
        ccount = self.__dbSELECT.count_sensorTypList()
        maxid = self.__dbSELECT.MaxId_sensorTypList()
        self.ui.label_sensorTypListCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def __write_sensorTyp_lable(self):
        ccount = self.__dbSELECT.count_sensorTyp()
        maxid = self.__dbSELECT.MaxId_sensorTyp()
        self.ui.label_sensorTypCount.setText(
            "count: [{:05}] | max: [{:05}]".format(ccount, maxid))

    def event_btn_delCM(self):
        cm_id = self.ui.lineEdit_delCM_id.text()
        deleter = db_delete.dbdelete()
        deleter.del_climaticMeasurement_byID(cm_id)
        print("DEBUG: event btn del CM funktion is connected and running")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    x = db_admin_handler()
    x.show()
    app.exec_()
