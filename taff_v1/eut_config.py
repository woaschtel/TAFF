from dbconnector import db_select, db_insert, db_selectAnalyser
import eut_pcietable


class eut_config:
    def __init__(self, _id):
        """
        eut configuratoin  object


        """

        self.__dbSELECT = db_select.dbselect()
        self.__dbSELECTAnalyser = db_selectAnalyser.dbselect()
        self.__dbINSERT = db_insert.dbinsert()

        self._id = _id
        self._name = str("")
        self._info = str("")
        self._chassisID = int(0)
        self._chassisText = str("")
        self._moboID = int(0)
        self._moboText = str("")
        self._hddAnz = int(0)
        self._hddID = int(0)
        self._hddText = str("")
        self._cpuAnz = int(0)
        self._cpuID = int(0)
        self._cpuText = str("")
        self._memAnz = int(0)
        self._memID = int(0)
        self._memText = str("")
        self._psuAnz = int(0)
        self._psuID = int(0)
        self._psuText = str("")
        self._pcieTableID = int(1)

        # laden das datenstazes zu einer eindeutigen id
        # aus der datenbank
        self.__load_eutConfig_byID(self._id)
        # jetzt wird noch der ensprechende text zu den komponenten ids geladen
        # z.B.: cpu_id(1) -> E3-1280v3
        # nach dieser funktion sollte in allen text variablen der passende
        # text zu der ID stehen
        self.__load_eutConfigNames()

        # pcie tabel objekt erstellen anhand der pcieTable ID
        self._pcieTable = eut_pcietable.eut_pcietable(self._pcieTableID)

    def __load_eutConfig_byID(self, idd):

        eutList_rear = self.__dbSELECT.get_configuration_byID(idd)
        eutList = eutList_rear[0]

        print("DEBUG: load configuration list {} - len(){} ".format(
            eutList, len(eutList)))

        self._name = str(eutList[1])
        self._info = str(eutList[2])
        self._chassisID = int(eutList[3])
        self._moboID = int(eutList[4])
        self._hddAnz = int(eutList[5])
        self._hddID = int(eutList[6])
        self._cpuAnz = int(eutList[7])
        self._cpuID = int(eutList[8])
        self._memAnz = int(eutList[9])
        self._memID = int(eutList[10])
        self._psuAnz = int(eutList[11])
        self._psuID = int(eutList[12])
        self._pcieTableID = int(eutList[13])

    def __load_eutConfigNames(self):

        # laden des datensatzes anhand der id
        rear = self.__dbSELECT.get_chassis_byID(self._chassisID)
        # die da nur ein element in der liste ist das erste element laden
        rear2 = rear[0]
        # tuple aufbau (id, name , info, ...)
        # deswegen das [1] element laden -- das ist der name z.B.: X540-T2
        # jetzt noch abspeichern
        self._chassisText = rear2[1]
        # diese 3 schritte werden jetzt mit jeder controller id gemacht

        rear = self.__dbSELECT.get_MoBo_byID(self._moboID)
        rear2 = rear[0]
        self._moboText = rear2[1]

        rear = self.__dbSELECT.get_HDD_byID(self._hddID)
        rear2 = rear[0]
        self._hddText = rear2[1]

        rear = self.__dbSELECT.get_cpu_byID(self._cpuID)
        rear2 = rear[0]
        self._cpuText = rear2[1]

        rear = self.__dbSELECT.get_mem_byID(self._memID)
        rear2 = rear[0]
        self._memText = rear2[1]

        rear = self.__dbSELECT.get_psu_byID(self._psuID)
        rear2 = rear[0]
        self._psuText = rear2[1]

    def print_info_eutConfig(self):

        a = "+-{:60}-+"
        b = "| {:15}{:35}{:10} |"
        c = "| {:12} | {:3} |{:3} | {:34} |"

        print(a.format("-"*60))
        print(b.format("config id:", str(self._id), ""))
        print(b.format("config name:", self._name, ""))
        print(b.format("config info:", self._info, ""))
        print(a.format("-"*60))
        print(c.format("-", "cnt", " id", "ctrl name"))
        print(a.format("-"*60))
        print(c.format("Chassis: ", "  -", self._chassisID, self._chassisText))
        print(c.format("MoBo: ", "  -", self._moboID, self._moboText))
        print(c.format("HDD: ", self._hddAnz, self._hddID, self._hddText))
        print(c.format("CPU: ", self._cpuAnz, self._cpuID, self._cpuText))
        print(c.format("Memory: ", self._memAnz, self._memID, self._memText))
        print(c.format("PSU: ", self._psuAnz, self._psuID, self._psuText))
        print(a.format("-"*60))
        print()


if __name__ == '__main__':

    a = eut_config(1)
