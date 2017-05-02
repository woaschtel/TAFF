import sqlite3
import os
import settings


class dbinsert:

    def __init__(self):
        """
            db_insert -- stellt die Verbindung zu datenbank her.
            SQL - INSERT - Befehl zum eifuegen einer Zeile in eine Tabelle
        """
        self.__connection = sqlite3.connect(
            settings.settingsTaff.DATABASE_FILE_WIN
            if os.name == "nt" else
            settings.settingsTaff.DATABASE_FILE_UNIX)

        self.__cursor = self.__connection.cursor()
        pass

    # Add Funktionen -- generiert einen eintrag in der Datenbank
    def add_cimaticMeasurment(self, name, datum, info, eut_id, ambtemp_id,
                              testload_id,
                              sensorName_id,
                              sensorValue_id,
                              sensorMax_id,
                              sensorType_id):
        """
            Add climatc Measurment
            Fuegt einen neuen Eintrag in die Tabele climatic Measurment
        """
        # INFO --- Done

        werte = (name, datum, info, eut_id, ambtemp_id, testload_id,
                 sensorName_id, sensorValue_id, sensorMax_id, sensorType_id)
        sql = ' INSERT INTO climaticMeasurment VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_climaticMeasurementList(self, value):
        """ add Funktion zum -- Namen der Sensoren"""
        # INFO --- Done

        werte = tuple(value)
        sql = " INSERT INTO climaticMeasurment  VALUES (NULL" + ", ?" * 7 + ");"
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_EUT(self, name, info, system_id, configuration_id):
        """ Fuegt einen EUT in die tabelle eut ein """
        # INFO --- Done

        werte = (name, info, system_id, configuration_id)
        sql = ' INSERT INTO eut VALUES (NULL, ?, ?, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_system(self, name, info):
        """ Fuegt einen System hinzu das an einen eut gebunden werden kann """
        # INFO --- Done

        werte = (name, info)
        sql = ' INSERT INTO system VALUES (NULL, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_configuration(self, name, info, chassis_id, MoBo_id, HDDAnz, HDD_id,
                          CPUAnz, CPU_id, MEMAnz, MEM_id, PSUAnz, PSU_id,
                          PCIeTable_id):
        """ Erstellt eine Configuration table in der db ist teil eines EUTs """
        # INFO --- Done

        werte = (name, info, chassis_id, MoBo_id, HDDAnz, HDD_id, CPUAnz,
                 CPU_id, MEMAnz, MEM_id, PSUAnz, PSU_id, PCIeTable_id)
        sql = """INSERT INTO
                 configuration
                 VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_chassis(self, name, info):
        """ Teil der Konfiguration -- erstellt einen table in der db"""
        # INFO --- Done

        werte = (name, info)
        sql = ' INSERT INTO chassis VALUES (NULL, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_MoBo(self, name, info):
        """ erstellt einen mobo eintrag in der db table mobo"""
        # INFO --- Done

        werte = (name, info)
        sql = ' INSERT INTO MoBo VALUES (NULL, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_HDD (self, name, info, maxtemp):
        """ erstellt einen hdd eintrag in der db table hdd"""
        # INFO --- Done

        werte = (name, info, maxtemp)
        sql = ' INSERT INTO hdd VALUES (NULL, ?, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_mem(self, name, info, maxtemp):
        """ mem eintrag in der mem table der db"""
        # INFO --- Done

        werte = (name, info, maxtemp)
        sql = ' INSERT INTO MEM VALUES (NULL, ?, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_CPU(self, name, info, maxtemp, tdp_power):
        """ mem eintrag in der mem table der db"""
        # INFO --- Done

        werte = (name, info, maxtemp, tdp_power)
        sql = ' INSERT INTO CPU VALUES (NULL, ?, ?, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_PSU(self, name, info, maxtemp):
        """ mem eintrag in der mem table der db"""
        # INFO --- Done

        werte = (name, info, maxtemp)
        sql = ' INSERT INTO psu VALUES (NULL, ?, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_PCIeTableList(self, pcieList):
        """ Es wird der komplette parameter befehl in einer liste uebergeben
        """
        werte = tuple(pcieList)
        sql = ' INSERT INTO PCIeTable VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_PCIeTable(self, name, info, pcie1=None, pcie2=None, pcie3=None,
                      pcie4=None, pcie5=None, pcie6=None, pcie7=None,
                      pcie8=None, pcie9=None, pcie10=None, pcie11=None,
                      pcie12=None, pcie13=None, pcie14=None, pcie15=None):
        """ Teil der Konfiguration -- erstellt einen table in der db"""
        # INFO --- Done

        werte = (name, info, pcie1, pcie2, pcie3, pcie4, pcie5, pcie6, pcie7,
                 pcie8, pcie9, pcie10, pcie11, pcie12, pcie13, pcie14, pcie15)
        sql = ' INSERT INTO PCIeTable VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_PCIeCtrl(self, name, info, ctrl_type, maxtemp):
        """ controller eintrag in der PCIeCtrl table der db"""
        # INFO --- Done

        werte = (name, info, ctrl_type, maxtemp)
        sql = ' INSERT INTO PCIeCtrl VALUES (NULL, ?, ?, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_sensorName(self, name):
        """ add Funktion zum -- Namen der Sensoren"""
        # INFO --- Done

        werte = tuple(name)
        sql = " INSERT INTO sensorName  VALUES (NULL" + ", ?" * 61 + ");"
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_sensorValue(self, value):
        """
        add_sensorValue ( value list )
        erwartet eine liste mit 60 interger werten
        und fuegt diese in die datenbank ein
        """
        # INFO --- Done

        werte = tuple(value)
        sql = " INSERT INTO sensorValue  VALUES (NULL" + ", ?" * 60 + ");"
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_sensorMax(self, value):
        """ add Funktion zum -- Namen der Sensoren"""
        # INFO --- Done

        werte = tuple(value)
        sql = " INSERT INTO sensorMax  VALUES (NULL" + ", ?" * 61 + ");"
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_sensorTypList(self, typeList):
        """ add a list of sensorTyps to the database """
        werte = tuple(typeList)
        sql = " INSERT INTO sensorTypList  VALUES (NULL" + ", ?" * 61  + ");"
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_sensorTyp(self, sensortyp, info):
        werte2 = (sensortyp, info)
        sql = ' INSERT INTO sensorTyp VALUES (NULL, ?,?);'
        self.__cursor.execute(sql, werte2)
        self.__connection.commit()

    def add_testLoad(self, testloadList, info):
        werte = (testloadList, info)
        sql = ' INSERT INTO testLoad VALUES (NULL, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()

    def add_ambientTemp(self, ambtemp, info):
        werte = (ambtemp, info)
        sql = 'INSERT INTO ambienttemp VALUES (NULL, ?, ?);'
        self.__cursor.execute(sql, werte)
        self.__connection.commit()


if __name__ == "__main__":
    a = dbinsert()
    a.add_system("TEST FJ", "")
    print("ONLY TEST \n" +
          "and the test is done")
