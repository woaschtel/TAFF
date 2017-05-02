import sqlite3
import os

import settings


class dbcreate:
    def __init__(self):
        """
        db_create -- stellt die Verbindung zu datenbank her.
        SQL - CREATE - Befehl zum erstellen der Tabellen
        """
        self.__connection = sqlite3.connect(
            settings.settingsTaff.DATABASE_FILE_WIN
            if os.name == "nt" else
            settings.settingsTaff.DATABASE_FILE_UNIX)

        self.__cursor = self.__connection.cursor()

    def createAllTabels(self):
        """ erstellt die Komplette Database tableis """

        self.createTable_sensorName()
        self.createTable_sensorTypList()
        self.createTable_sensorValue()
        self.createTable_sensorMax()
        self.createTable_climaticMeasurement()
        self.createTable_ambienttemp()
        self.createTable_testLoad()
        self.createTable_sensorTyp()
        self.createTable_eut()
        self.createTable_system()
        self.createTable_configuration()
        self.createTable_chassis()
        self.createTable_mobo()
        self.createTable_hdd()
        self.createTable_mem()
        self.createTable_cpu()
        self.createTable_psu()
        self.createTable_pcieCtrl_Table()
        self.createTable_pcieCtrl()

    def createTable_sensorValue(self):
        text = ""

        for i in range(1, 60):
            text = text + "v" + str(i) + " INTEGER, "

        txt = str("CREATE TABLE sensorValue (id_svl INTEGER PRIMARY KEY, " +
                  "{}".format(text) + "v60 INTEGER );")

        try:
            self.__cursor.execute(txt)
            self.__connection.commit()
        except:
            print("\nERROR: cannot create {}".format(txt))

    def createTable_sensorName(self):
        text = ""

        for i in range(1, 60):
            text = text + "n" + str(i) + " TEXT, "

        txt = str("CREATE TABLE sensorName (id_snl INTEGER PRIMARY KEY, " +
                  "name TEXT, " + "{}".format(text) + "n60 TEXT );")

        try:
            self.__cursor.execute(txt)
            self.__connection.commit()
        except:
            print("\nERROR: cannot create {}".format(txt))

    def createTable_sensorMax(self):
        text = ""

        for i in range(1, 60):
            text = text + "vm" + str(i) + " INTEGER, "

        txt = str("CREATE TABLE sensorMax (id_sml INTEGER PRIMARY KEY, " +
                  "name TEXT, " + "{}".format(text) + "vm60 INTEGER );")

        try:
            self.__cursor.execute(txt)
            self.__connection.commit()
        except:
            print("\nERROR: cannot create {}".format(txt))

    def createTable_sensorTypList(self):
        text = ""

        for i in range(1, 60):
            text = text + "typ" + str(i) + " INTEGER, "

        txt = str("CREATE TABLE sensorTypList (id_stl INTEGER PRIMARY KEY, " +
                  "name TEXT," + "{}".format(text) + "typ60 INTEGER );")

        try:
            self.__cursor.execute(txt)
            self.__connection.commit()
        except:
            print("\nERROR: cannot create {}".format(txt))

    def createTable_climaticMeasurement(self):
        try:
            # climaticMeasurment - create table
            self.__cursor.execute("""CREATE TABLE climaticMeasurment (
                id_cm INTEGER PRIMARY KEY,
                name_cm TEXT,
                datum TEXT,
                info_cm TEXT,
                eut_id INTEGER,
                ambientTemp_id INTEGER,
                testLoad_id INTEGER,
                sensorName_id INTEGER,
                sensorValue_id INTEGER,
                sensorMax_id INTEGER,
                sensorType_id INTEGER
            );""")
            self.__connection.commit()
        except:
            print("\nERROR: connot craete \n")

    def createTable_ambienttemp(self):
        try:
            self.__cursor.execute("""CREATE TABLE ambienttemp (
                id_amb INTEGER PRIMARY KEY,
                name_amb TEXT,
                info_amb TEXT);""")
            self.__connection.commit()
        except:
            print("\nERROR: connot craete \n {}")

    def createTable_testLoad(self):
        """
            erstellt die testLoad tabelle in der db
        """
        try:
            self.__cursor.execute("""CREATE TABLE testLoad (
                id_tl INTEGER PRIMARY KEY,
                name_tl TEXT,
                info_tl TEXT
            );""")
            self.__connection.commit()
        except:
            print("\nERROR: connot craete \n {}")

    def createTable_sensorTyp(self):
        """
            erstellt die testLoad tabelle in der db
        """
        try:
            self.__cursor.execute("""CREATE TABLE sensorTyp (
                id_st INTEGER PRIMARY KEY,
                name_st TEXT,
                info_st TexT
            );""")
            self.__connection.commit()
        except:
            print("\n Error connot create table")

    def createTable_eut(self):
        """
            erstellt die eut tabelle in der db
        """
        try:
            # eut - create table
            self.__cursor.execute("""CREATE TABLE eut (
                id_eut INTEGER PRIMARY KEY,
                name_eut TEXT,
                info_eut TEXT,
                system_id INTEGER,
                configuration_id INTEGER
                );""")
            self.__connection.commit()
        except:
            print("\n ERROR: connot create table")

    def createTable_system(self):
        """
            erstellt die eut tabelle in der db
        """
        try:
            # system - create table
            self.__cursor.execute("""CREATE TABLE system (
                id_system INTEGER PRIMARY KEY,
                name_system TEXT,
                info_system TEXT
                );""")
            self.__connection.commit()
        except:
            print("\n ERROR: connot create table")

    def createTable_configuration(self):
        """
            erstellt die eut tabelle in der db
        """
        try:
            # configuration
            self.__cursor.execute("""CREATE TABLE configuration (
                id_cfg INTEGER PRIMARY KEY,
                name_cfg TEXT,
                info_cfg TEXT,
                chassis_id INTEGER,
                MoBo_id INTEGER,
                HDDAnz INTEGER,
                HDD_id INTEGER,
                CPUAnz INTEGER,
                CPU_id INTEGER,
                MEMAnz INTEGER,
                MEM_id INTEGER,
                PSUAnz INTEGER,
                PSU_id INTEGER,
                PCIeTable_id INTEGER
            );""")
            self.__connection.commit()
        except:
            print("\n ERROR: connot create table")

    def createTable_chassis(self):
        """
            erstellt die eut tabelle in der db
        """
        try:
            # chassis - create table
            self.__cursor.execute("""CREATE TABLE chassis (
                id_ch INTEGER PRIMARY KEY,
                name_ch TEXT,
                info_ch TEXT
            );""")
            self.__connection.commit()
        except:
            print("\n ERROR: connot create table")

    def createTable_mobo(self):
        """
            erstellt die eut tabelle in der db
        """
        try:
            # MoBo - create table
            self.__cursor.execute("""CREATE TABLE MoBo (
                id_mobo INTEGER PRIMARY KEY,
                name_mobo TEXT,
                info_mobo TEXT
            );""")
            self.__connection.commit()
        except:
            print("\n ERROR: connot create table")

    def createTable_hdd(self):
        """
            erstellt die eut tabelle in der db
        """

        try:
            # HDD - create table
            self.__cursor.execute("""CREATE TABLE HDD (
                id_hdd INTEGER PRIMARY KEY,
                name_hdd TEXT,
                info_hdd TEXT,
                maxTemp_hdd REAL
            );""")
            self.__connection.commit()
        except:
            print("\n ERROR: connot create table")

    def createTable_mem(self):
        """
            erstellt die eut tabelle in der db
        """
        try:
            # MEM - create table
            self.__cursor.execute("""CREATE TABLE MEM (
                id_mem INTEGER PRIMARY KEY,
                name_mem TEXT,
                info_mem TEXT,
                maxTemp_mem REAL
            );""")
            self.__connection.commit()
        except:
            print("\n ERROR: connot create table")

    def createTable_cpu(self):
        """
            erstellt die eut tabelle in der db
        """
        try:
            # CPU - create table
            self.__cursor.execute("""CREATE TABLE CPU (
                id_cpu INTEGER PRIMARY KEY,
                name_cpu TEXT,
                info_cpu TEXT,
                maxTemp_cpu REAL,
                TDP_cpu REAL
            );""")
            self.__connection.commit()
        except:
            print("\n ERROR: connot create table")

    def createTable_psu(self):
        """
            erstellt die eut tabelle in der db
        """
        try:
            # PSU - create table
            self.__cursor.execute("""CREATE TABLE psu (
                id_psu INTEGER PRIMARY KEY,
                name_psu TEXT,
                info_psu TEXT,
                maxTemp_psu REAL
            );""")
            self.__connection.commit()
        except:
            print("\n ERROR: cannot create psu table")

    def createTable_pcieCtrl_Table(self):
        """
            erstellt die eut tabelle in der db
        """
        try:
            # PCIeTable - create table
            self.__cursor.execute("""CREATE TABLE PCIeTable (
                id_pcit INTEGER PRIMARY KEY,
                name_pcit TEXT,
                info_pcit TEXT,
                pcie1_pcit INTEGER,
                pcie2_pcit INTEGER,
                pcie3_pcit INTEGER,
                pcie4_pcit INTEGER,
                pcie5_pcit INTEGER,
                pcie6_pcit INTEGER,
                pcie7_pcit INTEGER,
                pcie8_pcit INTEGER,
                pcie9_pcit INTEGER,
                pcie10_pcit INTEGER,
                pcie11_pcit INTEGER,
                pcie12_pcit INTEGER,
                pcie13_pcit INTEGER,
                pcie14_pcit INTEGER,
                pcie15_pcit INTEGER
            );""")
            self.__connection.commit()
        except:
            print("\n ERROR: connot create table")

    def createTable_pcieCtrl(self):
        """
            erstellt die eut tabelle in der db
        """

        try:
            # PCIe Controler - create table
            self.__cursor.execute("""CREATE TABLE PCIeCtrl (
                id_pcictrl INTEGER PRIMARY KEY,
                name_pcictrl TEXT,
                info_pcictrl TEXT,
                type_pcictrl TEXT,
                maxTemp_pcictrl REAL
            );""")

            self.__connection.commit()
        except:
            print("\n ERROR: connot create table")


if __name__ == "__main__":
    print("""Test of module db_create
          create all db tables
          """)
    a = dbcreate()
    a.createAllTabels()
