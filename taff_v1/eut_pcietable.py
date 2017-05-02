from dbconnector import db_select, db_insert, db_selectAnalyser


class eut_pcietable:
    """
        eut pcietable


    """
    def __init__(self, _id):
        """
        class eut_pcietable
         - generate a pcietable object by id

        """

        self.__dbSELECT = db_select.dbselect()
        self.__dbSELECTAnalyser = db_selectAnalyser.dbselect()
        self.__dbINSERT = db_insert.dbinsert()

        # pcie table information
        # only the id that referent to the pcie controller
        self._id = _id
        self._name = str("")
        self._info = str("")
        self._pcie01 = int(0)
        self._pcie02 = int(0)
        self._pcie03 = int(0)
        self._pcie04 = int(0)
        self._pcie05 = int(0)
        self._pcie06 = int(0)
        self._pcie07 = int(0)
        self._pcie08 = int(0)
        self._pcie09 = int(0)
        self._pcie10 = int(0)
        self._pcie11 = int(0)
        self._pcie12 = int(0)
        self._pcie13 = int(0)
        self._pcie14 = int(0)
        self._pcie15 = int(0)

        # erstmal die pcie tabel anhand der id aus der datenbank laden
        self.__load_pcieTable_byID(self._id)

        # text variablen der pcie id
        # aufgeloeste version pcie id - pcie name
        self.__pcie01text = str("")
        self.__pcie02text = str("")
        self.__pcie03text = str("")
        self.__pcie04text = str("")
        self.__pcie05text = str("")
        self.__pcie06text = str("")
        self.__pcie07text = str("")
        self.__pcie08text = str("")
        self.__pcie09text = str("")
        self.__pcie10text = str("")
        self.__pcie11text = str("")
        self.__pcie12text = str("")
        self.__pcie13text = str("")
        self.__pcie14text = str("")
        self.__pcie15text = str("")

        # jetzt anhand der pcie id einen namen in die text varialen speichern
        self.__loadControllerNames()

    def __load_pcieTable_byID(self, idd):

        pcieList_rear = self.__dbSELECT.get_pcieTable_byID(idd)
        pcieList = pcieList_rear[0]

        print("DEBUG: load configuration list {} - len(){} ".format(
            pcieList, len(pcieList)))

        self._name = pcieList[1]
        self._info = pcieList[2]
        self._pcie01 = int(pcieList[3])
        self._pcie02 = int(pcieList[4])
        self._pcie03 = int(pcieList[5])
        self._pcie04 = int(pcieList[6])
        self._pcie05 = int(pcieList[7])
        self._pcie06 = int(pcieList[8])
        self._pcie07 = int(pcieList[9])
        self._pcie08 = int(pcieList[10])
        self._pcie09 = int(pcieList[11])
        self._pcie10 = int(pcieList[12])
        self._pcie11 = int(pcieList[13])
        self._pcie12 = int(pcieList[14])
        self._pcie13 = int(pcieList[15])
        self._pcie14 = int(pcieList[16])
        self._pcie15 = int(pcieList[17])

    def __loadControllerNames(self):
        """ wandelt eine id in einen text um
        """

        # laden des datensatzes anhand der id
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie01)
        # die da nur ein element in der liste ist das erste element laden
        rear2 = rear[0]
        # tuple aufbau (id, name , info, ...)
        # deswegen das [1] element laden -- das ist der name z.B.: X540-T2
        # jetzt noch abspeichern
        self.__pcie01text = rear2[1]
        # diese 3 schritte werden jetzt mit jeder controller id gemacht


        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie02)
        rear2 = rear[0]
        self.__pcie02text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie03)
        rear2 = rear[0]
        self.__pcie03text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie04)
        rear2 = rear[0]
        self.__pcie04text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie05)
        rear2 = rear[0]
        self.__pcie05text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie06)
        rear2 = rear[0]
        self.__pcie06text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie07)
        rear2 = rear[0]
        self.__pcie07text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie08)
        rear2 = rear[0]
        self.__pcie08text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie09)
        rear2 = rear[0]
        self.__pcie09text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie10)
        rear2 = rear[0]
        self.__pcie10text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie11)
        rear2 = rear[0]
        self.__pcie11text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie12)
        rear2 = rear[0]
        self.__pcie12text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie13)
        rear2 = rear[0]
        self.__pcie13text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie14)
        rear2 = rear[0]
        self.__pcie14text = rear2[1]
        rear = self.__dbSELECT.get_pcieCtrl_byID(self._pcie15)
        rear2 = rear[0]
        self.__pcie15text = rear2[1]

    def print_info_pcieTable(self):

        a = "+-{:60}-+"
        b = "| {:10}{:40}{:10} |"
        c = "| {:10} | {:10} | {:34} |"

        print(a.format("-"*60))
        print(b.format("id:", str(self._id), ""))
        print(b.format("name:", self._name, ""))
        print(b.format("info:", self._info, ""))
        print(a.format("-"*60))
        print(c.format("pcie slot", "ctrl id", "ctrl name"))
        print(a.format("-"*60))
        print(c.format(" 1", self._pcie01, self.__pcie01text))
        print(c.format(" 2", self._pcie02, self.__pcie02text))
        print(c.format(" 3", self._pcie03, self.__pcie03text))
        print(c.format(" 4", self._pcie04, self.__pcie04text))
        print(c.format(" 5", self._pcie05, self.__pcie05text))
        print(c.format(" 6", self._pcie06, self.__pcie06text))
        print(c.format(" 7", self._pcie07, self.__pcie07text))
        print(c.format(" 8", self._pcie08, self.__pcie08text))
        print(c.format(" 9", self._pcie09, self.__pcie09text))
        print(c.format("10", self._pcie10, self.__pcie10text))
        print(c.format("11", self._pcie11, self.__pcie11text))
        print(c.format("12", self._pcie12, self.__pcie12text))
        print(c.format("13", self._pcie13, self.__pcie13text))
        print(c.format("14", self._pcie14, self.__pcie14text))
        print(c.format("15", self._pcie15, self.__pcie15text))
        print(a.format("-"*60))



if __name__ == '__main__':


    a = eut_pcietable(1)
    a.print_info_pcieTable()

    c = eut_pcietable(2)
    c.print_info_pcieTable()
