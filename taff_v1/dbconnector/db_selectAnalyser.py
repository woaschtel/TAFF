import sqlite3
import os
import settings


class dbselect:
    def __init__ (self):
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

    def get_all_Cmeasurement(self):

        self.__cursor.execute("""
                                    SELECT
                                    climaticmeasurment.id_cm,
                                    climaticmeasurment.name_cm,
                                    testload.name_tl,
                                    eut.name_eut,
                                    system.name_system,
                                    configuration.name_cfg

                                    FROM climaticmeasurment

                                    INNER JOIN eut
                                    ON climaticmeasurment.eut_id=eut.id_eut

                                    INNER JOIN testload
                                    ON climaticmeasurment.testload_id=testload.id_tl

                                    INNER JOIN system
                                    ON eut.system_id=system.id_system

                                    INNER JOIN configuration
                                    ON eut.configuration_id=configuration.id_cfg
                              """)
        res = self.__cursor.fetchall()
        return res

    def get_Cmeasurement_by_id(self, idd):

        self.__cursor.execute("""
                                    SELECT
                                    climaticmeasurment.id_cm,
                                    climaticmeasurment.name_cm,
                                    testload.name_tl,
                                    eut.name_eut,
                                    system.name_system,
                                    configuration.name_cfg

                                    FROM climaticmeasurment

                                    INNER JOIN eut
                                    ON climaticmeasurment.eut_id=eut.id_eut

                                    INNER JOIN testload
                                    ON climaticmeasurment.testload_id=testload.id_tl

                                    INNER JOIN system
                                    ON eut.system_id=system.id_system

                                    INNER JOIN configuration
                                    ON eut.configuration_id=configuration.id_cfg
                                    WHERE climaticmeasurment.id_cm = {};
                              """.format(idd))

        res = self.__cursor.fetchall()
        return res

    def get_Cmeasurement_INFO_by_id(self, idd):

        self.__cursor.execute("""
                              SELECT

                              climaticmeasurment.id_cm,
                              climaticmeasurment.name_cm,
                              climaticmeasurment.info_cm,
                              testload.name_tl,
                              eut.name_eut,
                              eut.info_eut,
                              system.name_system,
                              configuration.name_cfg,
                              configuration.info_cfg,
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

                              WHERE climaticmeasurment.id_cm = {}
                              """.format(idd))

        res = self.__cursor.fetchall()
        return res

    def get_Cmeasurement_sensorValues_by_id(self, idd):
        """
        get climatic measure sensor values by id

        WICHTIG : nicht loeschen wird noch gebraucht

        gitb eine lange liste in der alle spaten follgender tabellen hinterlegt
        sing:
            climaticmeasurement
            sensorname
            sensorvalue
            sensormax
            sensortyplist

        WICHTIG:    nicht loeschen diese funktion wird von der
                    gui_analyser_handler class gebraucht
        """
        try:
            print("Checkpoint")
            self.__cursor.execute("""
                                  SELECT 	*
                                  FROM climaticmeasurment
                                  INNER JOIN sensorname
                                  ON climaticmeasurment.sensorname_id=sensorname.id_snl
                                  INNER JOIN sensorvalue
                                  ON climaticmeasurment.sensorvalue_id=sensorvalue.id_svl
                                  INNER JOIN sensormax
                                  ON climaticmeasurment.sensormax_id=sensormax.id_sml
                                  INNER JOIN sensortyplist
                                  ON climaticmeasurment.sensortype_id=sensortyplist.id_stl
                                  WHERE climaticmeasurment.id_cm = {};
                                  """.format(idd))

            res = self.__cursor.fetchall()
            return res
        except:
            print("ERROR")

    def get_sensorTyp_name_by_id(self, idd):
        self.__cursor.execute("""
                                SELECT name_st
                                FROM sensortyp

                                WHERE sensortyp.id_st = {};
                              """.format(idd))

        res = self.__cursor.fetchall()
        return res
