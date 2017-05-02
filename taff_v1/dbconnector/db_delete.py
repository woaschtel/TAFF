import sqlite3
import os
import settings


class dbdelete():
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

    def del_resetComponentTabels(self):
        self.__cursor.execute(" DELETE FROM chassis")
        self.__cursor.execute(" DELETE FROM cpu")
        self.__cursor.execute(" DELETE FROM hdd")
        self.__cursor.execute(" DELETE FROM mem")
        self.__cursor.execute(" DELETE FROM mobo")
        self.__cursor.execute(" DELETE FROM psu")
        self.__cursor.execute(" DELETE FROM pciectrl")
        self.__cursor.execute(" DELETE FROM system")
        self.__cursor.execute(" DELETE FROM sensorTyp")
        self.__cursor.execute(" DELETE FROM testLoad")
        self.__cursor.execute(" DELETE FROM ambienttemp")
        self.__connection.commit()

    def del_climaticMeasurement_byID(self, cmID):
        """
        Function to delete a climatic measurement by id
        """

        print("INFO: Try to delete the cm by id -- {}".format(str(cmID)))
        self.__cursor.execute("""
                              DELETE FROM climaticmeasurment
                              WHERE id_cm = {}""".format(str(cmID)))
        self.__connection.commit()
        print("INFO: climatic measurement -{}-ID- is deleted".format(cmID))


if __name__ == "__main__":
    a = dbdelete()
    a.del_resetComponentTabels()
