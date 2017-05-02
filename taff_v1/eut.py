from dbconnector import db_select, db_insert, db_selectAnalyser
import eut_config


class eut:
    def __init__(self, _id):
        """
        eut class
          - para = _id -- the database id from the eut which is stored in the
                          database table eut

        generate a eut object from the database

        wenn call this function it will ganarate automaticly a object
          -- configuraion --
        by the configuration id from the eut
        """

        self.__dbSELECT = db_select.dbselect()
        self.__dbSELECTAnalyser = db_selectAnalyser.dbselect()
        self.__dbINSERT = db_insert.dbinsert()

        self._id = _id
        self._name = str("")
        self._info = str("")
        self._systemID = int(0)
        self._systemText = str("")
        self._configurationID = int(0)

        # laden das datenstazes zu einer eindeutigen id
        # aus der datenbank
        self.__load_eut_byIID(self._id)
        # jetzt wird noch der ensprechende text zu den komponenten ids geladen
        # z.B.: cpu_id(1) -> E3-1280v3
        # nach dieser funktion sollte in allen text variablen der passende
        # text zu der ID stehen
        self.__load_eutNames()

        # pcie tabel objekt erstellen anhand der pcieTable ID
        self._configuration = eut_config.eut_config(
            self._configurationID)

        # DEBUGGING
        # self.print_info_eut()

    def __load_eut_byIID(self, idd):

        eutList_rear = self.__dbSELECT.get_eut_byID(idd)
        eutList = eutList_rear[0]

        print("DEBUG: load eut list {} - len(){} ".format(
            eutList, len(eutList)))

        self._name = str(eutList[1])
        self._info = str(eutList[2])
        self._systemID = int(eutList[3])
        self._configurationID = int(eutList[4])

    def __load_eutNames(self):

        # laden des datensatzes anhand der id
        rear = self.__dbSELECT.get_system_byID(self._systemID)
        # die da nur ein element in der liste ist das erste element laden
        rear2 = rear[0]
        # tuple aufbau (id, name , info, ...)
        # deswegen das [1] element laden -- das ist der name z.B.: X540-T2
        # jetzt noch abspeichern
        self._systemText = rear2[1]
        # diese 3 schritte werden jetzt mit jeder controller id gemacht

    def print_info_eut(self):

        a = "+-{:60}-+"
        b = "| {:15}{:35}{:10} |"
        d = "| {:60} |"

        print(a.format("-"*60))
        print(d.format(""))
        print(d.format("     EUT Information "))
        print(d.format("    ~~~~~~~~~~~~~~~~~"))
        print(a.format("-"*60))
        print(b.format("", "", "        id"))
        print(b.format("eut id:", str(self._id), ""))
        print(b.format("eut  name:", self._name, ""))
        print(b.format("eut info:", self._info, ""))
        print(b.format("system:", self._systemText, self._systemID))
        print(b.format("config:",  str(type(self._configuration)),
                       self._configurationID))
        print(a.format("-"*60))

        # DEBUG Code:
        # self._configuration.print_info_eutConfig()
        # self._configuration._pcieTable.print_info_pcieTable()


if __name__ == '__main__':

    a = eut(1)
