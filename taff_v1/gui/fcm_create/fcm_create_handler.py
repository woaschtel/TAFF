import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
import read_mcps

if __name__ == '__main__':
    print("INFO: create_eut_handler class import as '__main__'")
    import fcm_create
    from ....dbconnector import db_select, db_insert

    # from ....dbconnector import db_select, db_insert
else:
    print("INFO: create_eut_handler class import as '__module__'")
    import read_mcps
    from gui.fcm_create import fcm_create
    from dbconnector import db_select, db_insert


class fcm_create_handler(QtWidgets.QWidget):
    """
        class:          fcm_create_handler
        description:    handler klasse fuer
    """
    def __init__(self):
        super(fcm_create_handler, self).__init__()
        self.ui = fcm_create.Ui_Form()
        self.ui.setupUi(self)

        # dbconnector objects
        self.__dbSELECT = db_select.dbselect()
        self.__dbINSERT = db_insert.dbinsert()

        # Verbindung zwischen Buttons und Funktionen herstellen
        #
        self.ui.btn_loadData.clicked.connect(self.eventBtnLoadData)
        self.ui.btn_createSensorTypList2.clicked.connect(
            self.eventBtnCreateSensorTypList2)

        self.ui.btn_openfile.clicked.connect(
            self.eventBtnOpenFile)
        # self.ui.dialog_createSensorName = QtWidgets.QDialog()
        self.ui.btn_addMeasurment.clicked.connect(
            self.eventBtnAddMeasurement)

        print("INFO: start the create eut handler")

    def eventBtnAddMeasurement(self):
        # Hier kann man entweder die aktuelle Zeit
        dateTimeQT = QtCore.QDateTime.currentDateTime()
        # oder die Zeit laden die
        # in der qdatetimeedir gui widget liegt
        # dateTimeQT = self.dateTimeEdit.dateTime()
        # dieses datum und zeit kann aber auch schon awlter sein
        #   siehe auch self.loadData funktion
        aktuelleZeit = dateTimeQT.toString("yyyy.MM.dd-HH:mm:ss")
        # aktuelleZeit = QtCore.QDateTime.currentDateTime("yyyy.MM.dd-HH:mm:ss")
        print(aktuelleZeit)

        # CMeasurement -- name ausleseen und an die liste hinzufuegen
        name = str(self.ui.lineEdit_name.text())
        # CMeasurement -- info ausleseen und an die liste hinzufuegen
        info = str(self.ui.lineEdit_info.text())
        # CMeasurement -- eutid
        eutid = int(self.ui.comboBox_eutid.currentIndex() + 1)
        # CMeasurement -- abient temp id
        ambtempid = int(self.ui.comboBox_ambtempid.currentIndex() + 1)
        # CMeasurement -- eut test load id
        testloadid = int(self.ui.comboBox_testloadid.currentIndex() + 1)

        filename_mcps = self.ui.lineEdit_fileName.text()

        #
        # ueberpruefen ob alle daten vorhanden sind
        #  wenn nicht info label setzen
        #  wenn ja dann die daten aus dem file lesen und in der db abspeichern

        if (name == "" or info == "" or filename_mcps == ""):
            palette = QtGui.QPalette()
            palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
            self.ui.label_info1.setPalette(palette)
            self.ui.label_info1.setText("Bitte alles ausfuellen")

        else:
            print("Checkpoint 001 DEBUG")

            #try:
            data = read_mcps.read_mcpsStatisticFile(filename_mcps)
            data.print_sensorData()

            reply = QMessageBox.question(self, 'Ceckppoint Zero',
                                         "check the values",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)

            # Jetzt noch die QMessageBox Abfragen
            if reply == QMessageBox.Yes:
                # value liste aus dem mcps Statistik -object lesen
                value_list = data._newSensorValue_list
                # in die datenbank hinzufuegen
                self.__dbINSERT.add_sensorValue(value_list)
                # jetzt noch die id der aktuellen liste herrausfinden
                value_list_id = self.__dbSELECT.MaxId_sensorValue()
                # Status inforamtionen ausgeben
                self.ui.label_info2.setText("ValueID: {}".format(value_list_id))

                name_list = data._newSensorName_list
                # bei dieser liste kommt noch ein name hinzu
                # der name wird an position 0 eingefuegt
                # jetzt ist die liste 61 items lang
                name_list.insert(0, "genList: {}".format(name))
                self.__dbINSERT.add_sensorName(name_list)
                name_list_id = self.__dbSELECT.MaxId_sensorName()
                self.ui.label_info3.setText("NameID: {}".format(name_list_id))

                max_list = data._newSensorMax_list
                max_list.insert(0, "genList: {}".format(name))
                self.__dbINSERT.add_sensorMax(max_list)
                max_list_id = self.__dbSELECT.MaxId_sensorMax()
                self.ui.label_info4.setText("MaxID: {}".format(max_list_id))

                typ_list_id = int(
                    self.ui.comboBox_sensortyplistid.currentIndex() + 1)

                self.__dbINSERT.add_cimaticMeasurment(name, aktuelleZeit, info,
                                                      eutid, ambtempid,
                                                      testloadid, name_list_id,
                                                      value_list_id,
                                                      max_list_id, typ_list_id)

                cm_idid = self.__dbSELECT.MaxId_cmeasurement()

                self.ui.label_info5.setText(
                    "New Measurement ID: {}".format(cm_idid))

                palette = QtGui.QPalette()
                palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.green)
                self.ui.label_info1.setPalette(palette)
                self.ui.label_info1.setText("DONE ! All data added to DB")
                print("Added all data")
                print(aktuelleZeit)
            elif reply == QMessageBox.No:
                print("ende")

            #except:
            #    palette = QtGui.QPalette()
            #    palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
            #    self.ui.label_info1.setPalette(palette)
            #    self.ui.label_info1.setText("err: cannot read file")
            #    self.ui.label_info2.setText(" - fail - ")
            #    self.ui.label_info3.setText(" - fail - ")
            #    self.ui.label_info4.setText(" - fail - ")
            #    self.ui.label_info5.setText(" - fail - ")

    def eventBtnOpenFile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName()

        self.ui.lineEdit_fileName.setText(str(fname[0]))

        # if fname[0]:
        #     f = open(fname[0], 'r')
        #     with f:
        #         data = f.read()
        #         self.lineEdit_fileName2.setText(data)
        # print("CHECK")

    def eventBtnCreateSensorTypList2(self):
        """
        Funktion des Button Sensor Typ List erstellen
        ertellt einen neue Sensor typ list in der Daten Bank
        open a new gui
        """

        liste = []
        name = str(self.ui.lineEdit_createSensorTypList2_name.text())
        liste.append(name)

        # Erstmal die IDs der ComboBoxen einlesen
        #  und + 1 rechnen weil die ComboBox id bei 0 beginnt und die ids der
        #  datenbank beginnen bei 1
        #
        typId1 = self.ui.comboBox.currentIndex() + 1
        typId2 = self.ui.comboBox_2.currentIndex() + 1
        typId3 = self.ui.comboBox_3.currentIndex() + 1
        typId4 = self.ui.comboBox_4.currentIndex() + 1
        typId5 = self.ui.comboBox_5.currentIndex() + 1
        typId6 = self.ui.comboBox_6.currentIndex() + 1
        typId7 = self.ui.comboBox_7.currentIndex() + 1
        typId8 = self.ui.comboBox_8.currentIndex() + 1
        typId9 = self.ui.comboBox_9.currentIndex() + 1
        typId10 = self.ui.comboBox_10.currentIndex() + 1
        typId11 = self.ui.comboBox_11.currentIndex() + 1
        typId12 = self.ui.comboBox_12.currentIndex() + 1
        typId13 = self.ui.comboBox_13.currentIndex() + 1
        typId14 = self.ui.comboBox_14.currentIndex() + 1
        typId15 = self.ui.comboBox_15.currentIndex() + 1
        typId16 = self.ui.comboBox_16.currentIndex() + 1
        typId17 = self.ui.comboBox_17.currentIndex() + 1
        typId18 = self.ui.comboBox_18.currentIndex() + 1
        typId19 = self.ui.comboBox_19.currentIndex() + 1
        typId20 = self.ui.comboBox_20.currentIndex() + 1
        typId21 = self.ui.comboBox_21.currentIndex() + 1
        typId22 = self.ui.comboBox_22.currentIndex() + 1
        typId23 = self.ui.comboBox_23.currentIndex() + 1
        typId24 = self.ui.comboBox_24.currentIndex() + 1
        typId25 = self.ui.comboBox_25.currentIndex() + 1
        typId26 = self.ui.comboBox_26.currentIndex() + 1
        typId27 = self.ui.comboBox_27.currentIndex() + 1
        typId28 = self.ui.comboBox_28.currentIndex() + 1
        typId29 = self.ui.comboBox_29.currentIndex() + 1
        typId30 = self.ui.comboBox_30.currentIndex() + 1
        typId31 = self.ui.comboBox_31.currentIndex() + 1
        typId32 = self.ui.comboBox_32.currentIndex() + 1
        typId33 = self.ui.comboBox_33.currentIndex() + 1
        typId34 = self.ui.comboBox_34.currentIndex() + 1
        typId35 = self.ui.comboBox_35.currentIndex() + 1
        typId36 = self.ui.comboBox_36.currentIndex() + 1
        typId37 = self.ui.comboBox_37.currentIndex() + 1
        typId38 = self.ui.comboBox_38.currentIndex() + 1
        typId39 = self.ui.comboBox_39.currentIndex() + 1
        typId40 = self.ui.comboBox_40.currentIndex() + 1
        typId41 = self.ui.comboBox_41.currentIndex() + 1
        typId42 = self.ui.comboBox_42.currentIndex() + 1
        typId43 = self.ui.comboBox_43.currentIndex() + 1
        typId44 = self.ui.comboBox_44.currentIndex() + 1
        typId45 = self.ui.comboBox_45.currentIndex() + 1
        typId46 = self.ui.comboBox_46.currentIndex() + 1
        typId47 = self.ui.comboBox_47.currentIndex() + 1
        typId48 = self.ui.comboBox_48.currentIndex() + 1
        typId49 = self.ui.comboBox_49.currentIndex() + 1
        typId50 = self.ui.comboBox_50.currentIndex() + 1
        typId51 = self.ui.comboBox_51.currentIndex() + 1
        typId52 = self.ui.comboBox_52.currentIndex() + 1
        typId53 = self.ui.comboBox_53.currentIndex() + 1
        typId54 = self.ui.comboBox_54.currentIndex() + 1
        typId55 = self.ui.comboBox_55.currentIndex() + 1
        typId56 = self.ui.comboBox_56.currentIndex() + 1
        typId57 = self.ui.comboBox_57.currentIndex() + 1
        typId58 = self.ui.comboBox_58.currentIndex() + 1
        typId59 = self.ui.comboBox_59.currentIndex() + 1
        typId60 = self.ui.comboBox_60.currentIndex() + 1

        liste.append(typId1)
        liste.append(typId2)
        liste.append(typId3)
        liste.append(typId4)
        liste.append(typId5)
        liste.append(typId6)
        liste.append(typId7)
        liste.append(typId8)
        liste.append(typId9)
        liste.append(typId10)
        liste.append(typId11)
        liste.append(typId12)
        liste.append(typId13)
        liste.append(typId14)
        liste.append(typId15)
        liste.append(typId16)
        liste.append(typId17)
        liste.append(typId18)
        liste.append(typId19)
        liste.append(typId20)
        liste.append(typId21)
        liste.append(typId22)
        liste.append(typId23)
        liste.append(typId24)
        liste.append(typId25)
        liste.append(typId26)
        liste.append(typId27)
        liste.append(typId28)
        liste.append(typId29)
        liste.append(typId30)
        liste.append(typId31)
        liste.append(typId32)
        liste.append(typId33)
        liste.append(typId34)
        liste.append(typId35)
        liste.append(typId36)
        liste.append(typId37)
        liste.append(typId38)
        liste.append(typId39)
        liste.append(typId40)
        liste.append(typId41)
        liste.append(typId42)
        liste.append(typId43)
        liste.append(typId44)
        liste.append(typId45)
        liste.append(typId46)
        liste.append(typId47)
        liste.append(typId48)
        liste.append(typId49)
        liste.append(typId50)
        liste.append(typId51)
        liste.append(typId52)
        liste.append(typId53)
        liste.append(typId54)
        liste.append(typId55)
        liste.append(typId56)
        liste.append(typId57)
        liste.append(typId58)
        liste.append(typId59)
        liste.append(typId60)

        print("\n\nDEBUG\n\n")
        for i in liste:
            print("item {} | type {}".format(i, type(i)))

        self.__dbINSERT.add_sensorTypList(liste)

    def eventBtnLoadData(self):
        """ Funktion des 'Load Data' Buttons """

        # Die aktuelle Zeit in die QDateTimeEdit laden
        # mithilfe der QDateTime "currentDateTime()" funktion
        self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # CM liste loeschen
        self.ui.list_cm.clear()

        # Erstmal den Inhalt aller Listen Löschen
        # self.ui.list_sensorTypList.clear()
        self.ui.list_sensorTypListofLists.clear()
        self.ui.comboBox.clear()
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()
        self.ui.comboBox_4.clear()
        self.ui.comboBox_5.clear()
        self.ui.comboBox_6.clear()
        self.ui.comboBox_7.clear()
        self.ui.comboBox_8.clear()
        self.ui.comboBox_9.clear()
        self.ui.comboBox_10.clear()
        self.ui.comboBox_11.clear()
        self.ui.comboBox_12.clear()
        self.ui.comboBox_13.clear()
        self.ui.comboBox_14.clear()
        self.ui.comboBox_15.clear()
        self.ui.comboBox_16.clear()
        self.ui.comboBox_17.clear()
        self.ui.comboBox_18.clear()
        self.ui.comboBox_19.clear()
        self.ui.comboBox_20.clear()
        self.ui.comboBox_21.clear()
        self.ui.comboBox_22.clear()
        self.ui.comboBox_23.clear()
        self.ui.comboBox_24.clear()
        self.ui.comboBox_25.clear()
        self.ui.comboBox_26.clear()
        self.ui.comboBox_27.clear()
        self.ui.comboBox_28.clear()
        self.ui.comboBox_29.clear()
        self.ui.comboBox_30.clear()
        self.ui.comboBox_31.clear()
        self.ui.comboBox_32.clear()
        self.ui.comboBox_33.clear()
        self.ui.comboBox_34.clear()
        self.ui.comboBox_35.clear()
        self.ui.comboBox_36.clear()
        self.ui.comboBox_37.clear()
        self.ui.comboBox_38.clear()
        self.ui.comboBox_39.clear()
        self.ui.comboBox_40.clear()
        self.ui.comboBox_41.clear()
        self.ui.comboBox_42.clear()
        self.ui.comboBox_43.clear()
        self.ui.comboBox_44.clear()
        self.ui.comboBox_45.clear()
        self.ui.comboBox_46.clear()
        self.ui.comboBox_47.clear()
        self.ui.comboBox_48.clear()
        self.ui.comboBox_49.clear()
        self.ui.comboBox_50.clear()
        self.ui.comboBox_51.clear()
        self.ui.comboBox_52.clear()
        self.ui.comboBox_53.clear()
        self.ui.comboBox_54.clear()
        self.ui.comboBox_55.clear()
        self.ui.comboBox_56.clear()
        self.ui.comboBox_57.clear()
        self.ui.comboBox_58.clear()
        self.ui.comboBox_59.clear()
        self.ui.comboBox_60.clear()

        self.ui.comboBox_eutid.clear()
        self.ui.comboBox_sensortyplistid.clear()
        self.ui.comboBox_testloadid.clear()
        self.ui.comboBox_ambtempid.clear()


        # Laden der ambient temps
        for i in self.__dbSELECT.get_all_ambientTemps():
            # DEBUG Ausgabe
            print("DEBUG: \nValue: {}\tTyp: {}".format(i, type(i)))
            # String erstellen fuer eine Formatierte Ausgabe in der Liste
            txt = "{:3}| amb. {:5} °C".format(i[0], str(i[1]))
            self.ui.comboBox_ambtempid.addItem(str(txt))

        # Laden der Test Load List
        for i in self.__dbSELECT.get_all_testLoad():
            # DEBUG Ausgabe
            print("DEBUG: \nValue: {}\tTyp: {}".format(i, type(i)))
            # String erstellen fuer eine Formatierte Ausgabe in der Liste
            txt = "id: {:3}\t Name: {:35} all: {}".format(i[0], str(i[1]),
                                                          str(i))
            self.ui.comboBox_testloadid.addItem(str(txt))

        # Laden der EUTs in the list
        for i in self.__dbSELECT.get_all_eut():
            print("DEBUG: \nValue: {}\tTyp: {}".format(i, type(i)))
            txt = "id: {:7}\t Name: {:35} all: {}".format(i[0], str(i[1]),
                                                          str(i))
            self.ui.comboBox_eutid.addItem(str(txt))

        # Laden der Sensor Name List
        for i in self.__dbSELECT.get_all_sensorName():
            print("DEBUG: \nValue: {}\tTyp: {}".format(i, type(i)))
            txt = "id: {:7}\t Name: {:35} all: {}".format(i[0], str(i[1]),
                                                          str(i))
        # Laden der Sensor Typ list list
        for i in self.__dbSELECT.get_all_sensorTypList():
            print("DEBUG: \nValue: {}\tTyp: {}".format(i, type(i)))
            txt = "id: {:5}  Name: {:30} Info: {}".format(str(i[0]), i[1],
                                                          str(i))
            self.ui.list_sensorTypListofLists.addItem(str(txt))
            self.ui.comboBox_sensortyplistid.addItem(str(txt))

        # laden aller climatic measurements
        # ein temporary list erstellen
        xx_list = []
        xx_list = self.__dbSELECT.get_all_climaticMeasurment()
        xx_list = list(reversed(xx_list))

        # for i in self.__dbSELECT.get_all_climaticMeasurment():
        for i in xx_list:
            # der infostr enhaelt die sensor ValueId NameId MaxId
            infostr = "{}:{}:{}".format(str(i[8]).rjust(7,"."),
                                        str(i[7]).rjust(7,"."),
                                        str(i[9]).rjust(7,"."))

            txt2 = " {:7} |{}| {:30} : {:10} - {}".format(str(i[0]),
                                                          infostr,
                                                          str(i[1]),
                                                          str(i[2]),
                                                          str(i[3]))
            self.ui.list_cm.addItem(str(txt2))

        # Laden der Sensor Typ list list
        for i in self.__dbSELECT.get_all_sensorTyp():
            print("DEBUG: \nValue: {}\tTyp: {}".format(i, type(i)))
            # txt = "id: {:3}Type: {:30} Info: {}".format(str(i[0]), i[1], i[2])
            # self.ui.list_sensorTypList.addItem(str(txt))
            txt2 = "{:20} ID:{:3} Info: {}".format(str(i[1]), i[0], i[2])

            # Jetzt die Comboboxen der zu create sensor typ list erstellen mit
            # daten fuellen
            self.ui.comboBox.addItem(str(txt2))
            self.ui.comboBox_2.addItem(str(txt2))
            self.ui.comboBox_3.addItem(str(txt2))
            self.ui.comboBox_4.addItem(str(txt2))
            self.ui.comboBox_5.addItem(str(txt2))
            self.ui.comboBox_6.addItem(str(txt2))
            self.ui.comboBox_7.addItem(str(txt2))
            self.ui.comboBox_8.addItem(str(txt2))
            self.ui.comboBox_9.addItem(str(txt2))
            self.ui.comboBox_10.addItem(str(txt2))
            self.ui.comboBox_11.addItem(str(txt2))
            self.ui.comboBox_12.addItem(str(txt2))
            self.ui.comboBox_13.addItem(str(txt2))
            self.ui.comboBox_14.addItem(str(txt2))
            self.ui.comboBox_15.addItem(str(txt2))
            self.ui.comboBox_16.addItem(str(txt2))
            self.ui.comboBox_17.addItem(str(txt2))
            self.ui.comboBox_18.addItem(str(txt2))
            self.ui.comboBox_19.addItem(str(txt2))
            self.ui.comboBox_20.addItem(str(txt2))
            self.ui.comboBox_21.addItem(str(txt2))
            self.ui.comboBox_22.addItem(str(txt2))
            self.ui.comboBox_23.addItem(str(txt2))
            self.ui.comboBox_24.addItem(str(txt2))
            self.ui.comboBox_25.addItem(str(txt2))
            self.ui.comboBox_26.addItem(str(txt2))
            self.ui.comboBox_27.addItem(str(txt2))
            self.ui.comboBox_28.addItem(str(txt2))
            self.ui.comboBox_29.addItem(str(txt2))
            self.ui.comboBox_30.addItem(str(txt2))
            self.ui.comboBox_31.addItem(str(txt2))
            self.ui.comboBox_32.addItem(str(txt2))
            self.ui.comboBox_33.addItem(str(txt2))
            self.ui.comboBox_34.addItem(str(txt2))
            self.ui.comboBox_35.addItem(str(txt2))
            self.ui.comboBox_36.addItem(str(txt2))
            self.ui.comboBox_37.addItem(str(txt2))
            self.ui.comboBox_38.addItem(str(txt2))
            self.ui.comboBox_39.addItem(str(txt2))
            self.ui.comboBox_40.addItem(str(txt2))
            self.ui.comboBox_41.addItem(str(txt2))
            self.ui.comboBox_42.addItem(str(txt2))
            self.ui.comboBox_43.addItem(str(txt2))
            self.ui.comboBox_44.addItem(str(txt2))
            self.ui.comboBox_45.addItem(str(txt2))
            self.ui.comboBox_46.addItem(str(txt2))
            self.ui.comboBox_47.addItem(str(txt2))
            self.ui.comboBox_48.addItem(str(txt2))
            self.ui.comboBox_49.addItem(str(txt2))
            self.ui.comboBox_50.addItem(str(txt2))
            self.ui.comboBox_51.addItem(str(txt2))
            self.ui.comboBox_52.addItem(str(txt2))
            self.ui.comboBox_53.addItem(str(txt2))
            self.ui.comboBox_54.addItem(str(txt2))
            self.ui.comboBox_55.addItem(str(txt2))
            self.ui.comboBox_56.addItem(str(txt2))
            self.ui.comboBox_57.addItem(str(txt2))
            self.ui.comboBox_58.addItem(str(txt2))
            self.ui.comboBox_59.addItem(str(txt2))
            self.ui.comboBox_60.addItem(str(txt2))

        print("best Way")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    x = fcm_create_handler()
    x.show()
    app.exec_()
