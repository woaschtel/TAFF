import sys
from PyQt5 import QtWidgets

if __name__ == '__main__':
    print("INFO: create_eut_handler class import as '__main__'")
    import create_eut
else:
    print("INFO: create_eut_handler class import as '__module__'")
    from gui.createeut import create_eut
    from dbconnector import db_select, db_insert


class create_eut_handler(QtWidgets.QWidget):
    def __init__(self):
        super(create_eut_handler, self).__init__()
        self.ui = create_eut.Ui_Form()
        self.ui.setupUi(self)

        # dbconnector objects
        self.__dbSELECT = db_select.dbselect()
        self.__dbINSERT = db_insert.dbinsert()

        # define the btn clicked connection
        self.ui.btn_createConfig.clicked.connect(self.event_btn_createConfig)
        self.ui.btn_createEUT.clicked.connect(self.event_btn_createEUT)
        self.ui.btn_create_PCIeTable.clicked.connect(
            self.event_btn_createPCIeTable)
        self.ui.btn_loaddatas.clicked.connect(self.event_btn_loadDatas)

        print("INFO: start the create eut handler")

    def __clearAllDatas(self):
        """
        clear all datas -- from the GUI
        """

        # Viewing listen loeschen
        self.ui.listWidget_eut.clear()
        self.ui.listWidget_configs.clear()
        self.ui.listWidget_pcietable.clear()

        # felder in EUT Reiter loeschen
        self.ui.comboBox_eut_configid.clear()
        self.ui.comboBox_eut_systemid.clear()

        # felder in config loeschen
        self.ui.comboBox_config_chassisid.clear()
        self.ui.comboBox_config_cpuid.clear()
        self.ui.comboBox_config_hddid.clear()
        self.ui.comboBox_config_memid.clear()
        self.ui.comboBox_config_moboid.clear()
        self.ui.comboBox_config_psu.clear()
        self.ui.comboBox_config_pcietableid.clear()

        # alle felder der pcie tabel reiter loeschen
        self.ui.comboBox_ctrl01.clear()
        self.ui.comboBox_ctrl02.clear()
        self.ui.comboBox_ctrl03.clear()
        self.ui.comboBox_ctrl04.clear()
        self.ui.comboBox_ctrl05.clear()
        self.ui.comboBox_ctrl06.clear()
        self.ui.comboBox_ctrl07.clear()
        self.ui.comboBox_ctrl08.clear()
        self.ui.comboBox_ctrl09.clear()
        self.ui.comboBox_ctrl10.clear()
        self.ui.comboBox_ctrl11.clear()
        self.ui.comboBox_ctrl12.clear()
        self.ui.comboBox_ctrl13.clear()
        self.ui.comboBox_ctrl14.clear()
        self.ui.comboBox_ctrl15.clear()

        print("INFO: clear all contend --> DONE")

    def event_btn_createEUT(self):
        # erstellen des EUT s
        # erstmal checken ob auch alle felder ausgefuellt sind
        # nicht das leere oder falsche datensetze in der datenbank sind

        eut_name = self.ui.lineEdit_eut_name.text()
        eut_info = self.ui.lineEdit_eut_info.text()
        eut_systemID = int(self.ui.comboBox_eut_systemid.currentIndex() + 1)
        eut_configID = int(self.ui.comboBox_eut_configid.currentIndex() + 1)

        self.__dbINSERT.add_EUT(eut_name, eut_info, eut_systemID, eut_configID)

        print("INFO: create EUT --> DONE")

    def event_btn_createConfig(self):
        """
        Event button create config

        event function to create a config and store it in the database
        """

        # checken ob ein name eingetragen wurde
        if self.ui.lineEdit_config_name.text() == "":
            print("FEHLER es wurde kein name eingetragen")
        else:
            cfg_name = self.ui.lineEdit_config_name.text()
            cfg_info = self.ui.lineEdit_config_info.text()
            cfg_chassisID = int(
                self.ui.comboBox_config_cpuid.currentIndex() + 1)
            cfg_moboID = int(self.ui.comboBox_config_moboid.currentIndex() + 1)
            cfg_hddAnz = self.ui.lineEdit_config_hddcount.text()
            cfg_hddID = int(self.ui.comboBox_config_hddid.currentIndex() + 1)
            cfg_cpuAnz = self.ui.lineEdit_config_cpucount.text()
            cfg_cpuID = int(self.ui.comboBox_config_cpuid.currentIndex() + 1)
            cfg_memAnz = self.ui.lineEdit_config_memcount.text()
            cfg_memID = int(self.ui.comboBox_config_memid.currentIndex() + 1)
            cfg_psuAnz = int(self.ui.lineEdit_config_psucount.text())
            cfg_psuID = int(self.ui.comboBox_config_psu.currentIndex() + 1)
            cfg_pcietableID = int(
                self.ui.comboBox_config_pcietableid.currentIndex() + 1)
            self.__dbINSERT.add_configuration(cfg_name, cfg_info, cfg_chassisID,
                                              cfg_moboID, cfg_hddAnz, cfg_hddID,
                                              cfg_cpuAnz, cfg_cpuID, cfg_memAnz,
                                              cfg_memID, cfg_psuAnz, cfg_psuID,
                                              cfg_pcietableID)
            print("INFO: create Configuration --> DONE")

    def event_btn_createPCIeTable(self):

        if self.ui.lineEdit_pcie_t_name.text() == "":
            print("FEHLER es wurde kein name in PCIe Table name eingetragen")

        else:
            pci_name = self.ui.lineEdit_pcie_t_name.text()
            pci_info = self.ui.lineEdit_pcie_t_info.text()
            pci1 = int(self.ui.comboBox_ctrl01.currentIndex() + 1)
            pci2 = int(self.ui.comboBox_ctrl02.currentIndex() + 1)
            pci3 = int(self.ui.comboBox_ctrl03.currentIndex() + 1)
            pci4 = int(self.ui.comboBox_ctrl04.currentIndex() + 1)
            pci5 = int(self.ui.comboBox_ctrl05.currentIndex() + 1)
            pci6 = int(self.ui.comboBox_ctrl06.currentIndex() + 1)
            pci7 = int(self.ui.comboBox_ctrl07.currentIndex() + 1)
            pci8 = int(self.ui.comboBox_ctrl08.currentIndex() + 1)
            pci9 = int(self.ui.comboBox_ctrl09.currentIndex() + 1)
            pci10 = int(self.ui.comboBox_ctrl10.currentIndex() + 1)
            pci11 = int(self.ui.comboBox_ctrl11.currentIndex() + 1)
            pci12 = int(self.ui.comboBox_ctrl12.currentIndex() + 1)
            pci13 = int(self.ui.comboBox_ctrl13.currentIndex() + 1)
            pci14 = int(self.ui.comboBox_ctrl14.currentIndex() + 1)
            pci15 = int(self.ui.comboBox_ctrl15.currentIndex() + 1)

            self.__dbINSERT.add_PCIeTable(pci_name, pci_info, pci1, pci2, pci3,
                                          pci4, pci5, pci6, pci7, pci8, pci9,
                                          pci10, pci11, pci12, pci13, pci14,
                                          pci15)

            print("INFO: create PCIe Table --> DONE")

    def event_btn_loadDatas(self):
        """
        Event button load data

        event function to load all datas in the gui
        """

        # erstmal alle daten loeschen
        self.__clearAllDatas()

        # jetzt koennen die daten geladen werden
        for i in self.__dbSELECT.get_all_system():
            txt = "id: {:3}\t Name: {:35} all: {}".format(i[0], str(i[1]),
                                                          str(i))
            self.ui.comboBox_eut_systemid.addItem(str(txt))

        for i in self.__dbSELECT.get_all_configuration():
            txt = "|{:3}| {:10}".format(str(i[0]), str(i[1]))
            self.ui.comboBox_eut_configid.addItem(txt)

        for i in self.__dbSELECT.get_all_eut():
            txt = "id: {:3}\t Name: {:35} all: {}".format(i[0], str(i[1]),
                                                          str(i))
            self.ui.listWidget_eut.addItem(str(txt))

        # laden der configurattion
        for i in self.__dbSELECT.get_all_configuration():
            txt = "id: {:3}\t Name: {:35} all: {}".format(i[0], str(i[1]),
                                                          str(i))
            self.ui.listWidget_configs.addItem(str(txt))

        # laden der pcie tables
        for i in self.__dbSELECT.get_all_PCIeTable():
            txt = "id: {:3}\t Name: {:35} all: {}".format(i[0], str(i[1]),
                                                          str(i))
            self.ui.listWidget_pcietable.addItem(str(txt))

        # alle chassis
        for i in self.__dbSELECT.get_all_chassis():
            txt = "|{:3}| {:10}".format(str(i[0]), str(i[1]))
            self.ui.comboBox_config_chassisid.addItem(txt)

        for i in self.__dbSELECT.get_all_MoBo():
            txt = "|{:3}| {:10}".format(str(i[0]), str(i[1]))
            self.ui.comboBox_config_moboid.addItem(txt)

        for i in self.__dbSELECT.get_all_HDD():
            txt = "|{:3}| {:10}".format(str(i[0]), str(i[1]))
            self.ui.comboBox_config_hddid.addItem(txt)

        for i in self.__dbSELECT.get_all_CPU():
            txt = "|{:3}| {:10}".format(str(i[0]), str(i[1]))
            self.ui.comboBox_config_cpuid.addItem(txt)

        for i in self.__dbSELECT.get_all_mem():
            txt = "|{:3}| {:10}".format(str(i[0]), str(i[1]))
            self.ui.comboBox_config_memid.addItem(txt)

        for i in self.__dbSELECT.get_all_psu():
            txt = "|{:3}| {:10}".format(str(i[0]), str(i[1]))
            self.ui.comboBox_config_psu.addItem(txt)

        for i in self.__dbSELECT.get_all_PCIeTable():
            txt = "|{:3}| {:10}".format(str(i[0]), str(i[1]))
            self.ui.comboBox_config_pcietableid.addItem(txt)

        for i in self.__dbSELECT.get_all_PCIeCtrl():
            txt = "|{:3}| {:10}".format(str(i[0]), str(i[1]))
            self.ui.comboBox_ctrl01.addItem(txt)
            self.ui.comboBox_ctrl02.addItem(txt)
            self.ui.comboBox_ctrl03.addItem(txt)
            self.ui.comboBox_ctrl04.addItem(txt)
            self.ui.comboBox_ctrl05.addItem(txt)
            self.ui.comboBox_ctrl06.addItem(txt)
            self.ui.comboBox_ctrl07.addItem(txt)
            self.ui.comboBox_ctrl08.addItem(txt)
            self.ui.comboBox_ctrl09.addItem(txt)
            self.ui.comboBox_ctrl10.addItem(txt)
            self.ui.comboBox_ctrl11.addItem(txt)
            self.ui.comboBox_ctrl12.addItem(txt)
            self.ui.comboBox_ctrl13.addItem(txt)
            self.ui.comboBox_ctrl14.addItem(txt)
            self.ui.comboBox_ctrl15.addItem(txt)

        print("INFO: load Datas --> DONE")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    x = create_eut_handler()
    x.show()
    app.exec_()
