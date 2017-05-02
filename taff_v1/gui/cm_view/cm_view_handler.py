import sys
import csv
from PyQt5 import QtWidgets, QtCore
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QAction, QActionGroup, QApplication, QColorDialog,
        QComboBox, QDialog, QFontDialog, QGroupBox, QHBoxLayout, QLabel,
        QMainWindow, QMessageBox, QPushButton, QTableWidget,
        QTableWidgetItem, QToolBar)


if __name__ == '__main__':
    print("INFO: create_eut_handler class import as '__main__'")
    import cm_view
    # from ....dbconnector import db_select, db_insert
else:
    print("INFO: create_eut_handler class import as '__module__'")
    from gui.cm_view import cm_view
    from dbconnector import db_select, db_insert, db_selectAnalyser
    from dbconnector import db_select_cmView


class cm_view_handler(QtWidgets.QWidget):
    """
    Class:          cm_view_handler
    Beschreibung:   handler Klasse der cm View gui
                    zum sortieren der CMs

    Haendler fuer die buttons:

        Button load_cmData  - laed die daten einer messung
                              kann bald entfernt werden

        button load cm      - laedt die messungen anhand sortier kritierien

    """
    def __init__(self):
        """
            keine uebergabe von parametern beim erstellen der objekte
        """
        super(cm_view_handler, self).__init__()
        self.ui = cm_view.Ui_Form()
        self.ui.setupUi(self)

        self.__dbSELECT = db_select.dbselect()
        self.__dbSELECTAnalyser = db_selectAnalyser.dbselect()
        self.__dbSELECTViewer = db_select_cmView.db_select_cmView()
        self.__dbINSERT = db_insert.dbinsert()

        # Button connection --> clicked
        self.ui.btn_initGUI.clicked.connect(self.eventBtn_initGUI)
        self.ui.btn_load_cm.clicked.connect(self.eventBtn_load_cm)
        self.ui.btn_load_cmData.clicked.connect(self.eventBtn_load_cmData)

        print("best Way")

        # Jetzt koennen auch schon die daten in die gui geladen werden.
        # sicher ist sicher
        # das ist eigentich ein Button event -- aber kein Problem

        #  hier muss eine try except anweisung hin
        #  wenn in der daten bank noch keine climatic measuremants sind dann
        #  kommt hier ein fehler auf
        try:
            self.eventBtn_initGUI()
        except:
            print("ERROR: cm_view_handler - line 44 - eventBtn_initGui")

    def eventBtn_load_cmData(self):
        _cmID = self.ui.lineEdit_cmIDinput.text()
        self.__loadCmInfo(_cmID)
        self.__loadCmValues(_cmID)

    def __loadCmValues(self, cmID):
        """
        event Btn Load cm values
        laden der messwerte
        """

        # id der messung aus der lineEdit lesen
        # den speziellen datensatz aus der datenbank lesen
        datarear = self.__dbSELECTAnalyser.get_Cmeasurement_sensorValues_by_id(
            cmID)

        #
        # Jetzt muss die liste ausgepackt und aufgeteilt
        #
        print("\-----------------------------------")

        # da der befehl nur eine liste ausgibt einfach  mit [0] den ersten
        # eintrag nehmen
        datalist = datarear[0]

        # Aufteilung der listen in:
        #    - name
        #    - value
        #    - max
        #    - typ
        #    - typname - umgewandete typ list - id wird gegen den namen
        #                                       eingetauscht
        #
        # DEBUG:
        #  Hilft bei der analyse der richtigen aufteillung in die verschiedenen
        #  listen
        x = 0
        for i in datalist:
            print("{:3} - inhalt: {}".format(x, i))
            x = x + 1

        sensor_name_list = list(datalist[11:73])
        # die list.pop Befehle helfen die liste zu formatieren
        sensor_name_list.pop(0)
        sensor_name_list.pop(0)
        sensor_value_list = list(datalist[73:134])
        sensor_value_list.pop(0)
        sensor_max_list = list(datalist[134:196])
        sensor_max_list.pop(0)
        sensor_max_list.pop(0)
        sensor_typlist_list = list(datalist[196:])
        sensor_typlist_list.pop(0)
        sensor_typlist_list.pop(0)
        # die typlist besteht nur aus den ID's der sensor typen
        # deswegen wird noch eine typlist mit namen erstellt
        sensor_typlist_name_list = []
        temp_sensor_typlist_name_list = []

        """
        Die beiden schleifen koennen bestimmt noch verschoenert werden
        aber so funktioniert es schonmal
        TODO:   die schleifen zusammenfuegen damit man resaurcen
                spart und ein schleife
        """
        for i in range(len(sensor_value_list)):
            temp_sensor_typlist_name_list.append(
                self.__dbSELECTAnalyser.get_sensorTyp_name_by_id(
                    sensor_typlist_list[i]))

        for i in temp_sensor_typlist_name_list:
            x = i[0]
            y = x[0]
            sensor_typlist_name_list.append(y)

        #
        # Jetzt wird noch eine differenzliste erstellt
        sensor_diff_list = []

        # Differenz Liste erstellen
        for i in range(len(sensor_name_list)):
            print("TTTTTTTTT")
            print(i)
            # sicherstellen das eine int zahl in der liste steht
            if sensor_max_list[i] == "" or sensor_max_list[i] == None:
                sensor_max_list[i] = 0
            if sensor_value_list[i] == "" or sensor_max_list[i] == None:
                sensor_value_list[i] == 0

            # differenz berechnen
            diff = int(sensor_max_list[i]) - int(sensor_value_list[i])
            # an die liste fuegen
            sensor_diff_list.append(diff)

        # DEBUG CODE
        #
        # Ausgabe der fertig gestellten temperatur liste

        """

        DEBUG CODE

          - kann auch einfach zur ausgabe im term dienen
            die tabelle schaut echt gut aus

        """

        # teabellen header zeichnen
        print("{:3} | {:20} | {:10} | {:10} | {:10} | {:10} | {:10}".format(
            "ID:",
            "Name:{}".format(len(sensor_name_list)),
            "Value:{}".format(len(sensor_value_list)),
            "Max:{}".format(len(sensor_max_list)),
            "TYP:{}".format(len(sensor_typlist_list)),
            "TYPn:{}".format(len(sensor_typlist_name_list)),
            "diff:{}".format(len(sensor_diff_list))))
        print("------------------------------------------------")

        # jetzt die einzelnen zeilen ausgeben
        a = 1
        for i in range(len(sensor_name_list)):
            print("{:3} | {:20} | {:10} | {:10} | {:10} | {:10} | {:10}".format(
                a,
                sensor_name_list[i],
                sensor_value_list[i],
                sensor_max_list[i],
                sensor_typlist_list[i],
                sensor_typlist_name_list[i],
                sensor_diff_list[i]))
            a = a + 1

        """

        DEBUG CODE ENDE

        """


        #
        # QTableWidget
        #   - jezt wird der QTableWidget gefuellt

        # erstmal die complete tabelle loeschen
        for i in range(self.ui.table_sensorvalues.rowCount()):
            self.ui.table_sensorvalues.removeRow(0)

        for i in range(len(sensor_name_list)):
            # Anzahle der Zeilen in der Tabelle auslesen
            rowcount = self.ui.table_sensorvalues.rowCount()
            print("DEBUG: die Tabelle hat {} Zeilen. ".format(rowcount))
            # Neue Zeile in der Tabelle erstellen mit dem neuen Zeilen Nummer
            self.ui.table_sensorvalues.insertRow(rowcount)
            print("DEBUG: Zeiel {} erstelt".format(rowcount))
            # Jetzt in die Zeile einen eintrag machen
            self.ui.table_sensorvalues.setItem(rowcount, 0,
                                            QTableWidgetItem(
                                                sensor_name_list[i]))
            self.ui.table_sensorvalues.setItem(rowcount, 1,
                                            QTableWidgetItem(
                                                sensor_typlist_name_list[i]))
            self.ui.table_sensorvalues.setItem(rowcount, 2,
                                            QTableWidgetItem(str(
                                                sensor_max_list[i])))
            self.ui.table_sensorvalues.setItem(rowcount, 3,
                                            QTableWidgetItem(str(
                                                sensor_value_list[i])))
            self.ui.table_sensorvalues.setItem(rowcount, 4,
                                            QTableWidgetItem(str(
                                                sensor_diff_list[i])))

    def __loadCmInfo(self, cmID):
        """
        eventBtnLoadcmInfo -- Funktion
        ist das event vom Btn load Info
        hier werden Informationen der Messung geladen und die dazugehörigen
        Messwerte
        """


        # Jetzt die Informationen aus der datenbank laden
        infos_list = self.__dbSELECTAnalyser.get_Cmeasurement_INFO_by_id(cmID)
        infos = infos_list[0]

        # jetzt die informationen in die dafuer vorgesehenen lineEdits laden
        self.ui.lineEdit_cminfo01.setText(str(infos[0]))
        self.ui.lineEdit_cminfo02.setText(str(infos[1]))
        self.ui.lineEdit_cminfo03.setText(str(infos[2]))
        self.ui.lineEdit_cminfo04.setText(str(infos[3]))
        self.ui.lineEdit_cminfo05.setText(str(infos[4]))
        self.ui.lineEdit_cminfo06.setText(str(infos[5]))
        self.ui.lineEdit_cminfo07.setText(str(infos[6]))
        self.ui.lineEdit_cminfo08.setText(str(infos[7]))
        self.ui.lineEdit_cminfo09.setText(str(infos[8]))
        self.ui.lineEdit_cminfo10.setText(str(infos[9]))
        self.ui.lineEdit_cminfo11.setText(str(infos[9]))
        self.ui.lineEdit_cminfo12.setText(str(infos[10]))
        self.ui.lineEdit_cminfo13.setText(str(infos[12]))
        self.ui.lineEdit_cminfo14.setText(str(infos[13]))
        self.ui.lineEdit_cminfo15.setText(str(infos[14]))
        self.ui.lineEdit_cminfo16.setText(str(infos[15]))
        self.ui.lineEdit_cminfo17.setText(str(infos[16]))

    def eventBtn_initGUI(self):
        """
        event funktion for the button init GUI

        diese funktion laedt alle daten in die gui
        """

        # erstmal die comboBoxen loeschen
        self.ui.comboBox_eut.clear()
        self.ui.comboBox_config.clear()
        self.ui.comboBox_cpu.clear()
        self.ui.comboBox_ctrl.clear()
        self.ui.comboBox_system.clear()

        # jetzt die daten in die comboboxen laden

        # laden der euts
        for i in self.__dbSELECT.get_all_eut():
            txt = "{:5} | {:20} | all: {}".format(i[0], str(i[1]), str(i))
            self.ui.comboBox_eut.addItem(str(txt))

        # laden der system
        for i in self.__dbSELECT.get_all_system():
            txt = "{:5} | {:20} | all: {}".format(i[0], str(i[1]), str(i))
            self.ui.comboBox_system.addItem(str(txt))

        # laden der configurations
        for i in self.__dbSELECT.get_all_configuration():
            txt = "{:5} | {:20} | all: {}".format(i[0], str(i[1]), str(i))
            self.ui.comboBox_config.addItem(str(txt))

        # laden der cpu
        for i in self.__dbSELECT.get_all_CPU():
            txt = "{:5} | {:20} | all: {}".format(i[0], str(i[1]), str(i))
            self.ui.comboBox_cpu.addItem(str(txt))

        # laden der controller
        for i in self.__dbSELECT.get_all_PCIeCtrl():
            txt = "{:5} | {:20} | all: {}".format(i[0], str(i[1]), str(i))
            self.ui.comboBox_ctrl.addItem(str(txt))

        #
        # hier mussen auch noch die anderen components comboboxen initialisiert
        # werden

    def eventBtn_load_cm(self):
        # checkbox abfrage um herrauszufinden nach welchen kritierien gesucht
        # werden soll
        # dem entsprichent die richtige select methde aus dem file
        # db_select_viewer aufrfen und den autput in die listview laden
        # Erstmal die Listen loeschen
        self.ui.list_climatcMeasur.clear()

        # Momentan kann nach follgenden komponenten gesucht werden
        checkEut = bool(self.ui.checkBox_eut.isChecked())
        checkSystem = bool(self.ui.checkBox_system.isChecked())
        checkConfig = bool(self.ui.checkBox_config.isChecked())
        checkCPU = bool(self.ui.checkBox_cpu.isChecked())
        checkCtrl = bool(self.ui.checkBox_ctrl.isChecked())

        """
        Checkbox abfrage
         fuer jede obtion gibt es einen eigenen funktion
         die fangen immer mit __load_cm an
         und dann gibt es all, by_eut_id, by_system_id, u.s.w.
        """

        # Abfrage nach all
        # wenn alle false sind
        if(checkEut is False and
           checkSystem is False and
           checkConfig is False and
           checkCPU is False and
           checkCtrl is False):

            self.__load_cm_all()

        # Abfrage nach EUT ID
        #  wenn check EUT == True
        elif(checkEut is True and
             checkSystem is False and
             checkConfig is False and
             checkCPU is False and
             checkCtrl is False):

            self.__load_cm_by_eut_id()

        # Abfrage nach System ID
        #  wenn checkSystem == True
        elif(checkEut is False and
             checkSystem is True and
             checkConfig is False and
             checkCPU is False and
             checkCtrl is False):

            self.__load_cm_by_system_id()

        # Abfrage nach Config ID
        #  wenn checkConfig == True
        elif(checkEut is False and
             checkSystem is False and
             checkConfig is True and
             checkCPU is False and
             checkCtrl is False):

            self.__load_cm_by_config_id()

        # Abfrage nach CPU ID
        #  wenn checkCPU == True
        elif(checkEut is False and
             checkSystem is False and
             checkConfig is False and
             checkCPU is True and
             checkCtrl is False):

            self.__load_cm_by_cpu_id()

        # Abfrage nach Ctrl ID
        #  wenn checkCtrl == True
        elif(checkEut is False and
             checkSystem is False and
             checkConfig is False and
             checkCPU is False and
             checkCtrl is True):

            self.__load_cm_by_ctrl_id()

        # Ausgebe fehler in der checkbox auswahl
        #   wenn mehr als nur eine checkbox ausgewaehlt wurde
        else:
            txtt = "Please check the search input"
            self.ui.label_status01.setText(txtt)

    def __load_cm_all(self):
        # text formatierung
        txtt = "Load all Climatic Measurements"
        # jetzt das label beschreiben
        self.ui.label_status01.setText(txtt)

        a = reversed(self.__dbSELECTViewer.getCm_all())
        for i in a:
            self.ui.list_climatcMeasur.addItem(str(i))

    def __load_cm_by_eut_id(self):
        # erstmal die eut id auslesen
        eutIDD = int(self.ui.comboBox_eut.currentIndex() + 1)
        # text formatierung
        txtt = "Searching for CM with {} id {}".format("EUT", eutIDD)
        # jetzt das label beschreiben
        self.ui.label_status01.setText(txtt)
        # umgedrehte liste ausgeben damit die hoechste id ganz oben steht
        #   die hoechste id ist auch immer die neuste

        a = reversed(self.__dbSELECTViewer.getCm_by_eutId(eutIDD))

        # jetzt die liste ausgeben
        for i in a:
            self.ui.list_climatcMeasur.addItem(str(i))

    def __load_cm_by_system_id(self):
        # erstmal die system id auslesen
        systemIDD = int(self.ui.comboBox_system.currentIndex() + 1)
        # text formatierung
        txtt = "Searching for CM with {} id {}".format("System", systemIDD)
        # jetzt das label beschreiben
        self.ui.label_status01.setText(txtt)
        # umgedrehte liste ausgeben damit die hoechste id ganz oben steht
        #   die hoechste id ist auch immer die neuste

        a = reversed(
            self.__dbSELECTViewer.getCm_by_systemId(systemIDD))
        # jetzt die liste ausgeben
        for i in a:
            self.ui.list_climatcMeasur.addItem(str(i))

    def __load_cm_by_config_id(self):
        # erstmal die config id auslesen
        configIDD = int(self.ui.comboBox_config.currentIndex() + 1)
        # text formatierung
        txtt = "Searching for CM with {} id {}".format("config", configIDD)
        # jetzt das label beschreiben
        self.ui.label_status01.setText(txtt)

        a = reversed(
            self.__dbSELECTViewer.getCM_by_configId(configIDD))

        for i in a:
            self.ui.list_climatcMeasur.addItem(str(i))

    def __load_cm_by_cpu_id(self):
        # erstmal die cpu id auslesen
        cpuIDD = int(self.ui.comboBox_cpu.currentIndex() + 1)
        # text formatierung
        txtt = "Searching for CM with {} id {}".format("cpu", cpuIDD)
        # jetzt das label beschreiben
        self.ui.label_status01.setText(txtt)

        a = reversed(
            self.__dbSELECTViewer.getCM_by_cpuId(cpuIDD))

        for i in a:
            self.ui.list_climatcMeasur.addItem(str(i))

    def __load_cm_by_ctrl_id(self):
        # erstmal die ctrl id auslesen
        ctrlIDD = int(self.ui.comboBox_ctrl.currentIndex() + 1)
        # text formatierung
        txtt = "Searching for CM with {} id {}".format("ctrl", ctrlIDD)
        # jetzt das label beschreiben
        self.ui.label_status01.setText(txtt)

        # Nur eine Info das die Funktion noch nicht eingebaut ist.
        # Es muss dazu ein passender SQL String erzeugt werden und abgefragt
        # werden. die Funktion des SQL Strings sollt in die datei
        #   - db_select_vmView.py
        # kommen.
        for i in range(5):
            self.ui.list_climatcMeasur.addItem(
                "Diese Funktion laeuft noch nicht!")
            self.ui.list_climatcMeasur.addItem(
                "---------------------------------")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    x = cm_view_handler()
    x.show()
    app.exec_()
