
from dbconnector import db_select, db_insert, db_selectAnalyser
import eut
from report import plot_cm
from time import clock


class climaticMeasure:
    def __init__(self, _id, LOAD_EUT='yes'):
        """
        climatic Measurement object

        para:
            - id            = die id der messungen (datanbank table id)
            - LOAD_EUT      = eut datan landen ?
                              default = No
                              option = yes
        """

        self.__LOAD_EUT = LOAD_EUT

        self.__dbSELECT = db_select.dbselect()
        self.__dbSELECTAnalyser = db_selectAnalyser.dbselect()
        self.__dbINSERT = db_insert.dbinsert()

        self._id = _id
        self._name = str("")
        self._datum = str("")
        self._info = str("")
        self._eutID = int(0)
        self._ambientTempID = int(0)
        self._ambientTempText = ""
        self._testloadID = int(0)
        self._testloadText = ""

        # die ids der sensor listen
        self._sensorNameID = int(0)
        self._sensorValueID = int(0)
        self._sensorMaxID = int(0)
        self._sensorTypListID = int(0)

        # Listen der sensor werte
        #  alle listen sind 60 lang
        #  sie werden spaeter aus der id generiert
        self.sensorName_list = []
        self.sensorValue_list = []
        self.sensorMax_list = []
        self.sensorTyp_list = []
        self.sensorTypName_list = []
        self.sensorDiff_list = []

        # aufrufen der funktion __createCM_byID
        # uebergeben der id die mit den konstructor uebergeben  wurde
        self.__load_cm_byID(self._id)

        # hier muessen die messungs informationen ausgegeben werden
        self.__load_cmNames()

        if self.__LOAD_EUT == "no":
            self._eut = "No EUT init"
        elif self.__LOAD_EUT == "yes":
            self._eut = eut.eut(self._eutID)

        # self.print_info_cm()

    def __load_cm_byID(self, id_):
        """
        (private) create cm by id
           erstellen des cm objekts anhand der id
        """
        datarear = self.__dbSELECTAnalyser.get_Cmeasurement_sensorValues_by_id(
            id_)

        #
        # Jetzt muss die liste ausgepackt und aufgeteilt
        #
        print("-----------------------------------")

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
        # # DEBUG:
        # #  Hilft bei der analyse der richtigen aufteillung in die verschiedenen
        # #  listen
        # x = 0
        # for i in datalist:
        #     print("{:3} - inhalt: {:40}".format(x, i))
        #     x = x + 1

        # self._id = int(datalist[0])

        self._name = str(datalist[1])
        self._datum = str(datalist[2])
        self._info = str(datalist[3])
        self._eutID = int(datalist[4])
        self._ambientTempID = int(datalist[5])
        self._testloadID = int(datalist[6])

        self.sensorName_list = list(datalist[11:73])
        # die list.pop Befehle helfen die liste zu formatieren
        self.sensorName_list.pop(0)
        self.sensorName_list.pop(0)
        self.sensorValue_list = list(datalist[73:134])
        self.sensorValue_list.pop(0)
        self.sensorMax_list = list(datalist[134:196])
        self.sensorMax_list.pop(0)
        self.sensorMax_list.pop(0)
        self.sensorTyp_list = list(datalist[196:])
        self.sensorTyp_list.pop(0)
        self.sensorTyp_list.pop(0)
        # die typlist besteht nur aus den ID's der sensor typen
        # deswegen wird noch eine typlist mit namen erstellt
        # self.sensorTypName_list = []
        temp_sensor_typlist_name_list = []

        """
        Die beiden schleifen koennen bestimmt noch verschoenert werden
        aber so funktioniert es schonmal
        TODO:   die schleifen zusammenfuegen damit man resaurcen
                spart und ein schleife
        """
        # for i in range(len(self.sensorValue_list)):
        for i in range(len(self.sensorTyp_list)):
            temp_sensor_typlist_name_list.append(
                self.__dbSELECTAnalyser.get_sensorTyp_name_by_id(
                    self.sensorTyp_list[i]))

        for i in temp_sensor_typlist_name_list:
            x = i[0]
            y = x[0]
            self.sensorTypName_list.append(y)


        # Differenz Liste erstellen
        for i in range(len(self.sensorValue_list)):
            # sicherstellen das eine (int) zahl in der liste steht
            if self.sensorMax_list[i] == "":
                self.sensorMax_list[i] = 0
            if self.sensorValue_list[i] == "":
                self.sensorValue_list[i] == 0

            # differenz berechnen
            diff = int(self.sensorMax_list[i]) - int(self.sensorValue_list[i])
            # an die liste fuegen
            self.sensorDiff_list.append(diff)

        # # DEBUG CODE
        # #
        # # Ausgabe der fertig gestellten temperatur liste

        # """

        # DEBUG CODE

        #   - kann auch einfach zur ausgabe im term dienen
        #     die tabelle schaut echt gut aus

        # """

        # # teabellen header zeichnen
        # print("{:3} | {:20} | {:10} | {:10} | {:10} | {:10} | {:10}".format(
        #     "ID:",
        #     "Name: {}".format(len(self.sensorName_list)),
        #     "Value:{}".format(len(self.sensorValue_list)),
        #     "Max:  {}".format(len(self.sensorMax_list)),
        #     "TYP:  {}".format(len(self.sensorTyp_list)),
        #     "TYPn: {}".format(len(self.sensorTypName_list)),
        #     "diff: {}".format(len(self.sensorDiff_list))))
        # print("------------------------------------------------")

        # # jetzt die einzelnen zeilen ausgeben
        # a = 1
        # for i in range(len(self.sensorName_list)):
        #     print("{:3} | {:20} | {:10} | {:10} | {:10} |{:10}| {:10}".format(
        #         a,
        #         self.sensorName_list[i],
        #         self.sensorValue_list[i],
        #         self.sensorMax_list[i],
        #         self.sensorTyp_list[i],
        #         self.sensorTypName_list[i],
        #         self.sensorDiff_list[i]))
        #     a = a + 1

        # """

        # DEBUG CODE ENDE

        # """

    def __load_cmNames(self):

        # laden des datensatzes anhand der id
        print("DEBUG: abient temp id {}".format(self._ambientTempID))
        rear = self.__dbSELECT.get_ambient_byID(self._ambientTempID)
        # die da nur ein element in der liste ist das erste element laden
        rear2 = rear[0]
        # tuple aufbau (id, name , info, ...)
        # deswegen das [1] element laden -- das ist der name z.B.: X540-T2
        # jetzt noch abspeichern
        self._ambientTempText = rear2[1]
        # diese 3 schritte werden jetzt mit jeder controller id gemacht

        rear = self.__dbSELECT.get_testload_byID(self._testloadID)
        rear2 = rear[0]
        self._testloadText = rear2[1]

    def print_info_cm(self):

        a = "+-{:60}-+"
        b = "| {:15}{:35}{:10} |"
        d = "| {:60} |"

        print(a.format("-"*60))
        print(d.format(""))
        print(d.format("     CM Information "))
        print(d.format("    ~~~~~~~~~~~~~~~~~"))
        print(a.format("-"*60))
        print(b.format("", "", "        id"))
        print(b.format("id:", str(self._id), ""))
        print(b.format("name:", self._name, ""))
        print(b.format("info:", self._info, ""))
        print(b.format("amb:", self._ambientTempText, self._ambientTempID))
        print(b.format("testload:", self._testloadText,  self._testloadID))
        print(a.format("-"*60))

        if self.__LOAD_EUT == "no":
            print("DEBUG: No EUT availible")
        elif self.__LOAD_EUT == "yes":
            self._eut.print_info_eut()
            self._eut._configuration.print_info_eutConfig()
            self._eut._configuration._pcieTable.print_info_pcieTable()

        print()
        print()
        print()

        # teabellen header zeichnen
        print("{:3} | {:20} | {:10} | {:10} | {:10} | {:10} | {:10}".format(
            "ID:",
            "Name: {}".format(len(self.sensorName_list)),
            "Value:{}".format(len(self.sensorValue_list)),
            "Max:  {}".format(len(self.sensorMax_list)),
            "TYP:  {}".format(len(self.sensorTyp_list)),
            "TYPn: {}".format(len(self.sensorTypName_list)),
            "diff: {}".format(len(self.sensorDiff_list))))
        print("------------------------------------------------")

        # jetzt die einzelnen zeilen ausgeben
        a = 1
        for i in range(len(self.sensorName_list)):
            print("{:3} | {:20} | {:10} | {:10} | {:10} | {:10} | {:10}".format(
                a,
                self.sensorName_list[i],
                self.sensorValue_list[i],
                self.sensorMax_list[i],
                self.sensorTyp_list[i],
                self.sensorTypName_list[i],
                self.sensorDiff_list[i]))
            a = a + 1

    def get_sensorName_list(self):
        """
        get sensor name list-format
          gibt die sensor name liste zuruek

          sensor | name1 - name60
          list   |  [0]  -  [59]
        """
        pass

    def get_sensorValue_list(self):
        pass

    def get_sensorMax_list(self):
        pass

    def get_sensorTyp_list(self):
        pass

    def get_sensorTypName_list(self):
        pass


if __name__ == '__main__':

    t1 = clock()

    a = climaticMeasure(2, LOAD_EUT='yes')
    plot_cm.plot_cm(a.sensorName_list, a.sensorValue_list, a.sensorMax_list,
                    a.sensorDiff_list)
    a.print_info_cm()

    t2 = clock()

    t3 = clock()

    a = climaticMeasure(3, LOAD_EUT='yes')
    # cm_plot.plot_cm(a.sensorName_list, a.sensorValue_list, a.sensorMax_list,
    #                 a.sensorDiff_list)
    a.print_info_cm()

    t4 = clock()

    zeit1 = "t1 {} t2 {} t {}".format(t1, t2, t2 - t1)
    zeit2 = "t1 {} t2 {} t {}".format(t3, t4, t4 - t2)

    print(zeit1)
    print(zeit2)
