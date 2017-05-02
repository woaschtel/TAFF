import dbconnector.db_insert as db_insert
import dbconnector.db_delete as db_delete
import csv
import os
import settings


class addComponentsToDB:
    """     INFO: Class Discription
    Fuegt Komponenten zur Datenbank hinzu
    (die Komponenten koennen spaeter zur Configuration oder zur PCIe List
    hinzugefuegt werden.

    -  add (Komponenten einzelnt ueber terminal hinzufuegen
    -  add _CSV (ganze Liste an Komponenten hinzufügen

    """
    def __init__(self):
        """ constuctor """
        self.__dbINSERT = db_insert.dbinsert()
        self.__dbDELETE = db_delete.dbdelete()
        self.__componentFolder = (settings.settingsTaff.COMPONENTS_FOLDER_WIN
                                  if os.name == "nt" else
                                  settings.settingsTaff.COMPONENTS_FOLDER_UNIX)

    def addSystem(self):
        """ add system function """
        print("- Add System (Infos eingeben)")
        vname = input(" Name: ")
        vinfo = input(" Info: ")
        self.__dbINSERT.add_system(vname, vinfo)

    def addSystems_CSV(self):
        print("- Add System with CSV-File")
        # filename = input(" Please enter FileName: ")
        #reader = csv.DictReader(open(filename), delimiter=",")
        reader = csv.DictReader(open(self.__componentFolder +
                                     "comp_system.csv"), delimiter=",")
        for row in reader:
            print(row)
            self.__dbINSERT.add_system(row["name"],row["info"])

    def addPCIeController(self):
        """ add PCIe Controller """
        print(" - Add PCIe Ctrl. (Infos eingeben)")
        vname = input(" Name: ")
        vinfo = input(" Info: ")
        vctrl_type = input(" Ctrl. Type: ")
        vmaxtemp = input(" Max. Temp.: ")
        self.__dbINSERT.add_PCIeCtrl(vname, vinfo, vctrl_type, vmaxtemp)

    def addPCIeController_CSV(self):
        print("- Add PCIe Controller with CSV-File")
        # filename = input(" Please enter FileName: ")
        # reader = csv.DictReader(open(filename), delimiter=",")
        reader = csv.DictReader(open(self.__componentFolder +
                                     "comp_pciectrl.csv"), delimiter=",")
        for row in reader:
            print(row)
            self.__dbINSERT.add_PCIeCtrl(row["name"],row["info"],
                                        row["controllertyp"],
                                        row["maxtemp"])

    def addChassis(self):
        print(" - Add Chassis: ")
        vname = input(" Name: ")
        vinfo = input(" Info: ")

        self.__dbINSERT.add_chassis(vname, vinfo)

    def addChassis_CSV(self):
        print("- Add Chassis with CSV-File")
        # filename = input(" Please enter FileName: ")
        # reader = csv.DictReader(open(filename), delimiter=",")
        reader = csv.DictReader(open(self.__componentFolder +
                                     "comp_chassis.csv"),
                                delimiter=";")
        for row in reader:
            print(row)
            self.__dbINSERT.add_chassis(row["name"], row["info"])

    def addMoBo(self):
        print(" - Add MoBo: ")
        vname = input(" Name: ")
        vinfo = input(" Info: ")
        self.__dbINSERT.add_MoBo(vname, vinfo)

    def addMoBo_CSV(self):
        print("- Add MoBo with CSV-File")
        # filename = input(" Please enter FileName: ")
        # reader = csv.DictReader(open(filename), delimiter=",")
        reader = csv.DictReader(open(self.__componentFolder +
                                     "comp_mobo.csv"), delimiter=",")
        for row in reader:
            print(row)
            self.__dbINSERT.add_MoBo(row["name"],row["info"])

    def addHDD(self):
        print(" - Add HDD: ")
        vname = input(" Name: ")
        vinfo = input(" Info: ")
        vmaxtemp = input(" Max. Temp.: ")
        self.__dbINSERT.add_HDD(vname, vinfo, vmaxtemp)

    def addHDD_CSV(self):
        print("- Add HDD with CSV-File")
        # filename = input(" Please enter FileName: ")
        # reader = csv.DictReader(open(filename), delimiter=",")
        reader = csv.DictReader(open(self.__componentFolder +
                                     "comp_hdd.csv"), delimiter=",")
        for row in reader:
            print(row)
            self.__dbINSERT.add_HDD(row["name"], row["info"],
                                          row["maxtemp"])

    def addMEM(self):
        print(" - Ad MEM: ")
        vname = input(" Name: ")
        vinfo = input(" Info: ")
        vmaxtemp = input(" Max. Temp.: ")
        self.__dbINSERT.add_mem(vname, vinfo, vmaxtemp)

    def addMEM_CSV(self):
        print("- Add Memory with CSV-File")
        # filename = input(" Please enter FileName: ")
        # reader = csv.DictReader(open(filename), delimiter=",")
        reader = csv.DictReader(open(self.__componentFolder +
                                     "comp_mem.csv"), delimiter=",")
        for row in reader:
            print(row)
            self.__dbINSERT.add_mem(row["name"], row["info"],
                                          row["maxtemp"])

    def addCPU(self):
        print(" - Ad MEM: ")
        vname = input(" Name: ")
        vinfo = input(" Info: ")
        vmaxtemp = input(" Max. Temp.: ")
        vTDP = input(" TDP (Power): ")
        self.__dbINSERT.add_CPU(vname, vinfo, vmaxtemp, vTDP)

    def addCPU_CSV(self):
        print("- Add Memory with CSV-File")
        # filename = input(" Please enter FileName: ")
        # reader = csv.DictReader(open(filename), delimiter=",")
        reader = csv.DictReader(open(self.__componentFolder +
                                     "comp_cpu.csv"), delimiter=",")
        for row in reader:
            print(row)
            self.__dbINSERT.add_CPU(row["name"], row["info"],
                                    row["maxtemp"], row["tdp"])

    def addPSU_CSV(self):
        print("- Add psu  with CSV-File")
        # filename = input(" Please enter FileName: ")
        # reader = csv.DictReader(open(filename), delimiter=",")
        reader = csv.DictReader(open(self.__componentFolder +
                                     "comp_psu.csv"), delimiter=",")

        for row in reader:
            print(row)
            self.__dbINSERT.add_PSU(row["name"], row["info"], row["maxtemp"])

    def addsensorTyp_CSV(self):
        print("- Add Memory with CSV-File")
        # filename = input(" Please enter FileName: ")
        # reader = csv.DictReader(open(filename), delimiter=",")
        reader = csv.DictReader(open(self.__componentFolder +
                                     "eut_sensorTyp.csv"), delimiter=",")
        for row in reader:
            print(row)
            self.__dbINSERT.add_sensorTyp(row["name"],row["info"])

    def addeutTestLoad_CSV(self):
        print("- Add Memory with CSV-File")
        # filename = input(" Please enter FileName: ")
        # reader = csv.DictReader(open(filename), delimiter=",")
        reader = csv.DictReader(open(self.__componentFolder +
                                     "eut_testLoad.csv"), delimiter=",")
        for row in reader:
            print(row)
            self.__dbINSERT.add_testLoad(row["name"], row["info"])

    def addambientTemp_CSV(self):
        print("- Add ambient temperature with CSV-File")
        # filename = input(" Please enter FileName: ")
        # reader = csv.DictReader(open(filename), delimiter=",")
        reader = csv.DictReader(open(self.__componentFolder +
                                     "eut_ambientTemp.csv"), delimiter=",")
        x = 0
        for row in reader:
            print(x)
            print(row)
            self.__dbINSERT.add_ambientTemp(row["name"], row["info"])
            x = x +1

    def addALLComps_CSV(self):
        print("""
              ----> laden aller eintraege aus allen csv files in die datenbank


              """)

        # Erstmal all Eintraege der Tabelle loeschen
        self.__dbDELETE.del_resetComponentTabels()

        self.addCPU_CSV()
        self.addChassis_CSV()
        self.addHDD_CSV()
        self.addMEM_CSV()
        self.addMoBo_CSV()
        self.addPCIeController_CSV()
        self.addSystems_CSV()
        self.addeutTestLoad_CSV()
        self.addsensorTyp_CSV()
        self.addambientTemp_CSV()
        self.addPSU_CSV()


if __name__ == "__main__":
    print("Test of the module addComponentsToDB\n" +
          "start the test and add all component CSV Files to the db\n")

    a = addComponentsToDB()
    # a.addCPU_CSV()
    # a.addChassis_CSV()
    # a.addHDD_CSV()
    # a.addMEM_CSV()
    # a.addMoBo_CSV()
    # a.addPCIeController_CSV()
    # a.addSystems_CSV()
    # a.addeutTestLoad_CSV()
    # a.addsensorTyp_CSV()
    a.addALLComps_CSV()

    print("\n\nTest is DONE and PASS")
