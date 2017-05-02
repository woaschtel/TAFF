import sqlite3
import os
import settings


class db_select_cmView:
    """
    db_selct_cmView class:

        in dieser classe gibt es einen sql befehl der fur unterschiedliche
        WHERE abfragen zu recht geschnitten wird.

        grund befehl ist in der funktion:
            __gererateSQLRequest
        hinterlegt.
        --> deswegen private

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

    def __generateSQLRequest(self, _string):
        self.__cursor.execute("""
                              SELECT
                              climaticmeasurment.id_cm,
                              climaticmeasurment.name_cm,
                              climaticmeasurment.info_cm,
                              testload.name_tl,
                              eut.id_eut,
                              eut.name_eut,
                              eut.info_eut,
                              eut.system_id,
                              system.id_system,
                              system.name_system,
                              configuration.id_cfg,
                              configuration.name_cfg,
                              configuration.info_cfg,
                              configuration.chassis_id,
                              chassis.name_ch,
                              mobo.name_mobo,
                              configuration.hddanz,
                              hdd.name_hdd,
                              configuration.cpuanz,
                              cpu.name_cpu,
                              configuration.memanz,
                              mem.name_mem

                              FROM climaticmeasurment
                              INNER JOIN eut
                              ON climaticmeasurment.eut_id=eut.id_eut
                              INNER JOIN testload
                              ON climaticmeasurment.testload_id=testload.id_tl
                              INNER JOIN system
                              ON eut.system_id=system.id_system
                              INNER JOIN configuration
                              ON eut.configuration_id=configuration.id_cfg
                              INNER JOIN chassis
                              ON configuration.chassis_id=chassis.id_ch
                              INNER JOIN mobo
                              ON configuration.mobo_id=mobo.id_mobo
                              INNER JOIN hdd
                              ON configuration.hdd_id=hdd.id_hdd
                              INNER JOIN cpu
                              ON configuration.cpu_id=cpu.id_cpu
                              INNER JOIN mem
                              ON configuration.mem_id=mem.id_mem
                              {};
                              """.format(_string))

        res = self.__cursor.fetchall()
        self.__connection.commit()
        return res

    def getCm_all(self):
        res = self.__generateSQLRequest("")
        return res

    def getCm_by_eutId(self, tid):
        txt = "WHERE eut.id_eut = {}".format(tid)
        res = self.__generateSQLRequest(txt)
        return res

    def getCM_by_systemId(self, tid):
        txt = "WHERE system.id_system = {}".format(tid)
        res = self.__generateSQLRequest(txt)
        return res

    def getCM_by_configId(self, tid):
        txt = "WHERE configuration.id_cfg = {}".format(tid)
        res = self.__generateSQLRequest(txt)
        return res

    def getCM_by_cpuId(self, tid):
        txt = "WHERE cpu.id_cpu = {}"
        res = self.__generateSQLRequest(txt)
        return res
