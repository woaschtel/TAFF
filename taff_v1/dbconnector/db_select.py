import sqlite3
import os
import settings


class dbselect:
    """
        DB Select - description

        enthaelt fuer jede tablle folgende funktionen:
            get_all_*       = alle spalten der tabelle
            get_*_byID      = eine spalte der tablle anhand der ID
            MaxId_*         = die hoechste id
            count_*         = die anzahl an spalten der tabelle
    """
    def __init__(self):
        """
            db_select -- stellt die Verbindung zu datenbank her.
            SQL - SELECT - Befehl zum Auslesen der datenbank
        """
        self.__connection = sqlite3.connect(
            settings.settingsTaff.DATABASE_FILE_WIN
            if os.name == "nt" else
            settings.settingsTaff.DATABASE_FILE_UNIX)

        self.__cursor = self.__connection.cursor()
        pass

    def get_all_climaticMeasurment(self):
        self.__cursor.execute(" SELECT * FROM climaticMeasurment")
        res = self.__cursor.fetchall()
        return res

        pass

    def get_all_eut(self):
        self.__cursor.execute(" SELECT * FROM eut")
        res = self.__cursor.fetchall()
        return res

    def get_eut_byID(self, eutID):
        self.__cursor.execute("""
                              SELECT *
                              FROM eut
                              WHERE eut.id_eut= {};
                              """.format(eutID))

        res = self.__cursor.fetchall()
        return res

    def get_all_system(self):
        self.__cursor.execute(" SELECT * FROM system")
        res = self.__cursor.fetchall()
        return res

    def get_system_byID(self, sysID):
        """
        get a system by id from the database
        """
        self.__cursor.execute("""
                              SELECT *
                              FROM system
                              WHERE system.id_system= {};
                              """.format(sysID))

        res = self.__cursor.fetchall()
        return res

    def get_all_configuration(self):
        self.__cursor.execute(" SELECT * FROM configuration")
        res = self.__cursor.fetchall()
        return res

    def get_configuration_byID(self, confID):
        self.__cursor.execute("""
                              SELECT *
                              FROM configuration
                              WHERE configuration.id_cfg= {};
                              """.format(confID))

        res = self.__cursor.fetchall()
        return res

    def get_all_chassis(self):
        self.__cursor.execute(" SELECT * FROM chassis")
        res = self.__cursor.fetchall()
        return res

    def get_chassis_byID(self, chassisID):
        self.__cursor.execute("""
                              SELECT *
                              FROM chassis
                              WHERE chassis.id_ch= {};
                              """.format(chassisID))

        res = self.__cursor.fetchall()
        return res

    def get_all_MoBo(self):
        self.__cursor.execute(" SELECT * FROM Mobo")
        res = self.__cursor.fetchall()
        return res

    def get_MoBo_byID(self, moboID):
        self.__cursor.execute("""
                              SELECT *
                              FROM mobo
                              WHERE mobo.id_mobo= {};
                              """.format(moboID))

        res = self.__cursor.fetchall()
        return res

    def get_all_HDD(self):
        self.__cursor.execute(" SELECT * FROM hdd")
        res = self.__cursor.fetchall()
        return res

    def get_HDD_byID(self, hddID):
        self.__cursor.execute("""
                              SELECT *
                              FROM hdd
                              WHERE hdd.id_hdd= {};
                              """.format(hddID))

        res = self.__cursor.fetchall()
        return res

    def get_all_mem(self):
        self.__cursor.execute(" SELECT * FROM mem")
        res = self.__cursor.fetchall()
        return res

    def get_mem_byID(self, memID):
        self.__cursor.execute("""
                              SELECT *
                              FROM mem
                              WHERE mem.id_mem= {};
                              """.format(memID))

        res = self.__cursor.fetchall()
        return res

    def get_all_psu(self):
        self.__cursor.execute(" SELECT * FROM psu")
        res = self.__cursor.fetchall()
        return res

    def get_psu_byID(self, psuID):
        self.__cursor.execute("""
                              SELECT *
                              FROM psu
                              WHERE psu.id_psu = {};
                              """.format(psuID))

        res = self.__cursor.fetchall()
        return res

    def get_all_CPU(self):
        self.__cursor.execute(" SELECT * FROM cpu")
        res = self.__cursor.fetchall()
        return res

    def get_cpu_byID(self, cpuID):
        self.__cursor.execute("""
                              SELECT *
                              FROM cpu
                              WHERE cpu.id_cpu= {};
                              """.format(cpuID))

        res = self.__cursor.fetchall()
        return res

    def get_all_PCIeTable(self):
        self.__cursor.execute(" SELECT * FROM PCIeTable")
        res = self.__cursor.fetchall()
        return res

    def get_pcieTable_byID(self, pcieID):

        self.__cursor.execute("""
                              SELECT *
                              FROM PCIeTable
                              WHERE pcietable.id_pcit = {};
                              """.format(pcieID))

        res = self.__cursor.fetchall()
        return res

    def get_all_PCIeCtrl(self):
        self.__cursor.execute(" SELECT * FROM PCIeCtrl")
        res = self.__cursor.fetchall()
        return res

    def get_pcieCtrl_byID(self, pciectrlID):
        self.__cursor.execute("""
                              SELECT *
                              FROM PCIectrl
                              WHERE pciectrl.id_pcictrl = {};
                              """.format(pciectrlID))

        res = self.__cursor.fetchall()
        return res

    def get_all_testLoad(self):
        self.__cursor.execute(" SELECT * FROM testLoad")
        res = self.__cursor.fetchall()
        return res

    def get_testload_byID(self, testid):

        self.__cursor.execute("""
                              SELECT *
                              FROM testload
                              WHERE testload.id_tl = {};
                              """.format(testid))

        res = self.__cursor.fetchall()
        return res

    def get_all_sensorName(self):
        self.__cursor.execute(" SELECT * FROM sensorName")
        res = self.__cursor.fetchall()
        return res

    def get_all_sensorMaxValue(self):
        self.__cursor.execute(" SELECT * FROM sensorMax")
        res = self.__cursor.fetchall()
        return res

    def get_all_sensorValue(self):
        self.__cursor.execute(" SELECT * FROM sensorValue")
        res = self.__cursor.fetchall()
        return res

    def get_all_sensorTypList(self):
        self.__cursor.execute(" SELECT * FROM sensorTypList")
        res = self.__cursor.fetchall()
        return res

    def get_all_sensorTyp(self):
        self.__cursor.execute(" SELECT * FROM sensorTyp")
        res = self.__cursor.fetchall()
        return res

    def get_sensorTyp_byID(self, typid):

        self.__cursor.execute("""
                              SELECT *
                              FROM sensorTyp
                              WHERE sensorTyp.id_st = {};
                              """.format(typid))

        res = self.__cursor.fetchall()
        return res

    def get_all_ambientTemps(self):
        self.__cursor.execute(" SELECT * FROM ambienttemp")
        res = self.__cursor.fetchall()
        return res

    def get_ambient_byID(self, ambid):

        self.__cursor.execute("""
                              SELECT *
                              FROM ambienttemp
                              WHERE ambienttemp.id_amb = {};
                              """.format(ambid))

        res = self.__cursor.fetchall()
        return res

    def MaxId_sensorValue(self):
        test = self.__cursor.execute(" SELECT max(id_svl) FROM sensorValue")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_sensorName(self):
        """ gibt die die hoechste id der sensor name liste zuruck
        was auch meistens die zuletzt zur datanbank hinzugefuegt worden ist

        wird von der fccmg gebraucht um mcps file automatisch in die datenbank
        hinzufuegen zu koennen
        """
        test = self.__cursor.execute(" SELECT max(id_snl) FROM sensorName")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_sensorMax(self):
        test = self.__cursor.execute(" SELECT max(id_sml) FROM sensorMax")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_sensorTypList(self):
        test = self.__cursor.execute(" SELECT max(id_stl) FROM sensortyplist")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_sensorTyp(self):
        test = self.__cursor.execute(" SELECT max(id_st) FROM sensortyp")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_cmeasurement(self):
        test = self.__cursor.execute(
            " SELECT max(id_cm) FROM climaticmeasurment")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_eut(self):
        test = self.__cursor.execute(
            " SELECT max(id_eut) FROM eut")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_system(self):
        test = self.__cursor.execute(
            " SELECT max(id_system) FROM system")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_ambientTemp(self):
        test = self.__cursor.execute(
            " SELECT max(id_amb) FROM ambientTemp")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_testLoad(self):
        test = self.__cursor.execute(
            " SELECT max(id_tl) FROM testload")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_config(self):
        test = self.__cursor.execute(" SELECT max(id_cfg) FROM configuration")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_chassis(self):
        test = self.__cursor.execute(" SELECT max(id_ch) FROM chassis")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_cpu(self):
        test = self.__cursor.execute(" SELECT max(id_cpu) FROM cpu")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_hdd(self):
        test = self.__cursor.execute(" SELECT max(id_hdd) FROM hdd")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_memory(self):
        test = self.__cursor.execute(" SELECT max(id_mem) FROM mem")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_mobo(self):
        test = self.__cursor.execute(" SELECT max(id_mobo) FROM mobo")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_psu(self):
        test = self.__cursor.execute(" SELECT max(id_psu) FROM psu")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_pcieCtrlList(self):
        test = self.__cursor.execute(" SELECT max(id_pcit) FROM pcietable")
        maxid = test.fetchone()[0]
        return maxid

    def MaxId_pcieCtrl(self):
        test = self.__cursor.execute(" SELECT max(id_pcictrl) FROM pciectrl")
        maxid = test.fetchone()[0]
        return maxid

    def count_sensorValue(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM sensorValue")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_sensorName(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM sensorName")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_sensorMax(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM sensorMax")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_sensorTypList(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM sensorTypList")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_sensorTyp(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM sensorTyp")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_climaticMeasurement(self):
        """
        function to get the Count of the Climatic measurements
        gibt die Anzahl der Zeilen in der climatic measurement tablle zuruek
        """
        test = self.__cursor.execute(
            """ SELECT count(*) FROM climaticmeasurment""")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_eut(self):
        """
        function to get the Count of the Climatic measurements
        gibt die Anzahl der Zeilen in der climatic measurement tablle zuruek
        """
        test = self.__cursor.execute(
            """ SELECT count(*) FROM eut""")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_system(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM system")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_ambientTemp(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM ambientTemp")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_testLoad(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM testLoad")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_config(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM configuration")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_chassis(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM chassis")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_cpu(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM cpu")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_hdd(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM hdd")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_memory(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM mem")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_mobo(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM mobo")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_psu(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM psu")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_pcieCtrlList(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM pcietable")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count

    def count_pcieCtrl(self):
        test = self.__cursor.execute(
            " SELECT count(*) FROM pciectrl")
        self.__connection.commit()
        count = test.fetchone()[0]
        return count





