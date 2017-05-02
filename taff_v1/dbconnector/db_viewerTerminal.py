
if __name__ == "__main__":
    import db_select
else:
    from dbconnector import db_select


class dbviewerTerminal:

    def __init__(self):
        self.dbConect = db_select.dbselect()

    def all_climaticMeasurments(self):
        """ Formatierte Ausgabe der DB Tabelle eut """

        f = " {:5}|  {:20}|  {:15}"
        print()
        print()
        print("               Liste aller climatic Measurments:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:", "Info:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_climaticMeasurment():
            print(f.format(str(i[0]),
                           str(i[1]),
                           str(i[2])))

    def all_EUT(self):
        """ Formatierte Ausgabe der DB Tabelle eut """

        f = " {:5}|  {:20}|  {:15}"
        print()
        print()
        print("               Liste aller EUT:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:", "Info:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_eut():
            print(f.format(str(i[0]),
                           str(i[1]),
                           str(i[2])))

    def all_system(self):
        """ Formatierte Ausgabe der DB Tabelle system """

        f = " {:5}|  {:20}|  {:15}"
        print()
        print()
        print("               Liste aller System:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:", "Info:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_system():
            print(f.format(str(i[0]),
                           str(i[1]),
                           str(i[2])))

    def all_configs(self):
        """ Formatierte Ausgabe der DB Tabelle system """

        f = " {:5}|  {:20}|  {:15}"
        print()
        print()
        print("               Liste aller Configs:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:", "Info:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_configuration():
            print(f.format(str(i[0]),
                           str(i[1]),
                           str(i[2])))

    def all_chassis(self):
        """ Formatierte Ausgabe der DB Tabelle system """

        f = " {:5}|  {:20}|  {:15}"
        print()
        print()
        print("               Liste aller Chassis:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:", "Info:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_chassis():
            print(f.format(str(i[0]),
                           str(i[1]),
                           str(i[2])))

        pass

    def all_MoBo(self):
        """ Formatierte Ausgabe der DB Tabelle system """

        f = " {:5}|  {:20}|  {:15}"
        print()
        print()
        print("               Liste aller MoBo:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:", "Info:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_MoBo():
            print(f.format(str(i[0]),
                           str(i[1]),
                           str(i[2])))

    def all_HDD(self):
        """ Formatierte Ausgabe der DB Tabelle system """

        f = " {:5}|  {:20}|  {:15}|  {:10}"
        print()
        print()
        print("               Liste aller HDD:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:", "Info:", "max Temp:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_HDD():
            print(f.format(str(i[0]),
                           str(i[1]),
                           str(i[2]),
                           str(i[3])))

    def all_mem(self):
        """ Formatierte Ausgabe der DB Tabelle system """

        f = " {:5}|  {:20}|  {:15}|  {:10}"
        print()
        print()
        print("               Liste aller MEM:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:", "Info:", "max Temp:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_mem():
            print(f.format(str(i[0]),
                           str(i[1]),
                           str(i[2]),
                           str(i[3])))

    def all_CPU(self):
        """ Formatierte Ausgabe der DB Tabelle system """

        f = " {:5}|  {:20}|  {:15}|  {:10}"
        print()
        print()
        print("               Liste aller CPU:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:", "Info:", "max Temp:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_CPU():
            print(f.format(str(i[0]),
                           str(i[1]),
                           str(i[2]),
                           str(i[3])))

    def all_PCIeTables(self):
        """ Formatierte Ausgabe der DB Tabelle system """

        f = ("{:5}|{:20}|{:50}|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}|{:4}")
        print()
        print()
        print("               Liste aller PCIe Liste / Tables:")
        print("------------------------------------------------" * 2)
        print(f.format("ID:", "Name:", "Info:", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"))
        print("------------------------------------------------" * 2)

        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_PCIeTable():
            print(f.format(str(i[0]),
                           str(i[1]),
                           str(i[2]),
                           str(i[3]),
                           str(i[4]),
                           str(i[5]),
                           str(i[6]),
                           str(i[7]),
                           str(i[8]),
                           str(i[9]),
                           str(i[10]),
                           str(i[11]),
                           str(i[12]),
                           str(i[13]),
                           str(i[14]),
                           str(i[15]),
                           str(i[16]),
                           str(i[17])))

        print("\n\n")

    def all_PCIeCtrl(self):
        """ Formatierte Ausgabe der DB Tabelle PCIeCtrl """


        f = " {:5}|  {:20}|  {:20}|  {:10}|  {:10}"
        print()
        print()
        print("               Liste aller PCIe Controller:")
        print("--------------------------------------------------------------------------")
        print(f.format("ID:", "Name:", "Info:", "Type:", "MaxTemp:"))
        print("--------------------------------------------------------------------------")

        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_PCIeCtrl():
            print(f.format(str(i[0]),
                           str(i[1]),
                           str(i[2]),
                           str(i[3]),
                           str(i[4])))

    def all_sensor_name(self):
        """ Formatierte Ausgabe der DB Tabelle system """

        f = " {:5}|  {:20}"
        print()
        print()
        print("        Sensor Name Lists:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_sensorName():
            print(f.format(str(i[0]),
                           str(i[1])))

        pass

    def all_sensor_max(self):
        """ Formatierte Ausgabe der DB Tabelle system """

        f = " {:5}|  {:20}"
        print()
        print()
        print("        Sensor Max List:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_sensorMaxValue():
            print(f.format(str(i[0]),
                           str(i[1])))

        pass

    def all_sensor_typList(self):
        """ Formatierte Ausgabe der DB Tabelle system """

        f = " {:5}|  {:20}"
        print()
        print()
        print("        alle sensor typ listen:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_sensorTyp():
            print(f.format(str(i[0]),
                           str(i[1])))

    def all_sensor_Typ(self):
        """ Formatierte Ausgabe der DB Tabelle system """

        f = " {:5}|  {:20}|  {:15}"
        print()
        print()
        print("               Liste sensor Typ:")
        print("------------------------------------------------")
        print(f.format("ID:", "Name:", "Info:"))
        print("------------------------------------------------")
        # Schleife zum ausgeben der daten
        for i in self.dbConect.get_all_sensorTyp():
            print(f.format(str(i[0]),
                           str(i[1]),
                           str(i[2])))

    def all_databaseTabels(self):
        self.all_CPU()
        self.all_EUT()
        self.all_HDD()
        self.all_MoBo()
        self.all_PCIeCtrl()
        self.all_PCIeTables()
        self.all_chassis()
        self.all_configs()
        self.all_climaticMeasurments()
        self.all_mem()
        self.all_sensor_Typ()
        self.all_sensor_max()
        self.all_sensor_name()
        self.all_system()
        self.all_sensor_typList()


if __name__ == "__main__":
    a = dbviewerTerminal()
    a.all_databaseTabels()
