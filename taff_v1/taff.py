"""

    Taff by woastel


    LALALALAL
    

"""



import sys
import os
from PyQt5 import QtWidgets

# import the dbconector modules
from dbconnector import addComponentsToDB
from dbconnector import db_create
from dbconnector import db_delete
from dbconnector import db_viewerTerminal

# import the gui - handler
from gui import gui_handler
from gui.createeut import create_eut_handler
from gui.cm_create import cm_create_handler
from gui.cm_table import cm_table_handler
from gui.fcm_create import fcm_create_handler
from gui.cm_view import cm_view_handler
from gui.db_admin import db_admin_handler
import climaticMeasure
import settings
from report import plot_cm

import read_mcps


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class taff:
    def __init__(self):

        self.__mastermode = False

        # db conector objects
        self.__dbCreate = db_create.dbcreate()
        self.__dbDelete = db_delete.dbdelete()
        self.__dbViewTerm = db_viewerTerminal.dbviewerTerminal()
        self.__dbAddComps = addComponentsToDB.addComponentsToDB()

        # QApplication erstellen
        self.__app = QtWidgets.QApplication(sys.argv)

        # gui handler object erstellen
        #   - gui               --> analyser gui is the gui with midArea
        #   - gui_createEut     --> gui for create euts
        #   - gui_createCm      --> gui for create climatic measurements
        #   - gui_viewCm        --> gui for view climatic measurements

        self.__gui = gui_handler.gui_handler()
        self.__gui_ereateEut = create_eut_handler.create_eut_handler()
        self.__gui_createCM = cm_create_handler.cm_create_handler()
        self.__gui_fcreateCM = fcm_create_handler.fcm_create_handler()
        self.__gui_viewCM = cm_view_handler.cm_view_handler()

        # abfragen ob eine neue db erstellt werden soll
        # wenn ja dann gleich erstellen
        self.__initDatabase()

    def __initDatabase(self):
        """
        Function __initDatabase
         - create a database if user input is "initnew"
        """
        self.__clearScreen()

        # erstmal den header ausgeben
        print(" +-{:70}-+".format(70*"-"))
        self.__headerScreen()
        print(" +-{:70}-+".format(70*"-"))

        print("")

        print("     TAFF Settings / Information:")
        print("    ------------------------------")
        aaa = "       - {:25} | {}"
        print(aaa.format(" TAFF Version:",
                         settings.settingsTaff.VERSION))
        print(aaa.format(" User Name:",
                         settings.settingsTaff.USERNAME))
        print(aaa.format(" Database Name:",
                         settings.settingsTaff.DATABASE_NAME))
        print(aaa.format(" Database File:",
                         settings.settingsTaff.DATABASE_FILE_WIN))
        print(aaa.format(" Components Folder:",
                         settings.settingsTaff.COMPONENTS_FOLDER_WIN))

        print("")

        print("INFO: do you like to create a new database")
        print("      please enter 'init new db'")
        print("      else hit the enter key")

        print("")

        xx = input(">> ")

        if xx == "init new db":
            self.__dbCreate.createAllTabels()
            print("\nINFO: the new database created sucessful")
            input("\nhit the enter key")

        else:
            print("\nINFO: the program will use a availabile database")
            input("\nhit the enter key")

    def __clearScreen(self):
        """
        __clearScreen [private]
        Function to clear the screen
        """

        # clear the screen with os.system function
        # differenc between unix and windows
        os.system('cls' if os.name == 'nt' else 'clear')

    def __headerScreen(self):

        # header line
        l1 = " _________    ________    ________   ________ "
        l2 = "|\___   ___\ |\   __  \  |\  _____\ |\  _____\\"
        l3 = "\|___ \  \_| \ \  \|\  \ \ \  \__/  \ \  \__/ "
        l4 = "     \ \  \   \ \   __  \ \ \   __\  \ \   __\\"
        l5 = "      \ \  \   \ \  \ \  \ \ \  \_|   \ \  \_|"
        l6 = "       \ \__\   \ \__\ \__\ \ \__\     \ \__\ "
        l7 = "        \|__|    \|__|\|__|  \|__|      \|__| "
        l8 = ""

        print(" | {:19}{:51} |".format("                   ", l1))
        print(" | {:19}{:51} |".format("                   ", l2))
        print(" | {:19}{:51} |".format("    [T]hermal      ", l3))
        print(" | {:19}{:51} |".format("    [A]nalyse      ", l4))
        print(" | {:19}{:51} |".format("    [F]?           ", l5))
        print(" | {:19}{:51} |".format("    [F]ramework    ", l6))
        print(" | {:19}{:51} |".format("                   ", l7))
        print(" | {:19}{:51} |".format("                   ", l8))

    def __mainScreen(self):
        """
        __mainScreen [private]
            - funktion print the main screen information
        """

        # fist clear the screen
        self.__clearScreen()

        # Header Screen
        print(" +-{:70}-+".format(70*"-"))
        self.__headerScreen()
        print(" +-{:70}-+".format(70*"-"))

        a = " |      {:17}{:48} |"
        b = " |   {:67}  |"
        bwarn = " |   " + bcolors.WARNING + "{:67}" + bcolors.ENDC + "  |"
        bgreen = " |   " + bcolors.OKGREEN + "{:67}" + bcolors.ENDC + "  |"
        bblue = " |   " + bcolors.OKBLUE + "{:67}" + bcolors.ENDC + "  |"

        # Commands
        print(b.format(""))
        print(bwarn.format("GUI - Tools:"))
        print(b.format("~~~~~~~~~~~~"))
        print(a.format(" gui   ", "  - analyser gui"))
        print(a.format(" ceutg", "  - create eut gui"))
        print(a.format(" ccmg ", "  - create climatic measure gui"))
        print(a.format("fccmg ", "  - fast create climatic measure gui"))
        print(a.format(" vcmg ", "  - view climatic measure gui"))
        print(a.format(" license ", "  - license info GPLv3"))
        print(b.format(""))
        print(bwarn.format("Analyser - Tools:"))
        print(b.format("~~~~~~~~~~~~~~~~~"))
        print(a.format(" plotCm", "  - plot a climatic measurement"))
        print(a.format(" plotCm_save", "  - gen plot .png"))
        print(a.format(" readmcps ", "  - read mcps statistic file"))
        print(a.format("", "    dosent create a cm in db (use 'fccmg')"))
        print(b.format(""))
        print(bwarn.format("Database - Tools:"))
        print(b.format("~~~~~~~~~~~~~~~~~"))
        print(a.format("initcomp    ", "  - init the database comp."))
        # print(a.format("viewalldata ", "  - init the database comp."))
        print(b.format(""))
        print(bwarn.format("Develop. - Tools:"))
        print(b.format("~~~~~~~~~~~~~~~~~"))
        print(a.format("masteron", "  - master mode on"))

        # Commands Master Mode
        if self.__mastermode is True:
            print(b.format(""))
            print(" +-{:70}-+".format(70*"-"))
            print(b.format(""))
            print(bgreen.format(" Mastermode:"))

            print(b.format("~~~~~~~~~~~~~~~~~"))
            print(a.format("masteroff ", "  - master off"))
            print(a.format("test      ", "  - analyser gui"))

        # exit line
        print(b.format(""))
        print(" +-{:70}-+".format(70*"-"))
        print(bblue.format(" exit / xxx --> for exit the framework"))
        print(" +-{:70}-+".format(70*"-"))
        print("")

    def __print_GPL(self):
        print("""

              This program use code under the GPL
                    PyQt5

              Copyright (C) [2016]  [Sebastian Schilling]

              This program is free software; you can redistribute it and/or
              modify it under the terms of the GNU General Public License as
              published by the Free Software Foundation; either version 3 of
              the License, or (at your option) any later version.

              This program is distributed in the hope that it will be useful,
              but WITHOUT ANY WARRANTY; without even the implied warranty of
              MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
              See the GNU General Public License for more details.

              You should have received a copy of the GNU General Public License
              along with this program;
              if not, see <http://www.gnu.org/licenses/>.
              """)

    def run(self):
        """
        run function
         - runs the first user interface to select a tool
        """

        print(" Welcome by TAFF \n")
        print("DEBUG: the taff.run() function is running")

        while(True):
            self.__mainScreen()

            # Eingaba abfrage
            eingabe = input("input >> ")

            if eingabe == "gui":
                self.__gui.show()
                self.__app.exec()

            elif eingabe == "ceutg":
                self.__gui_ereateEut.show()
                self.__app.exec()

            elif eingabe == "ccmg":
                self.__gui_createCM.show()
                self.__app.exec()

            elif eingabe == "fccmg":
                print("Create FAST climatic measurement")
                self.__gui_fcreateCM.show()
                self.__app.exec()

            elif eingabe == "vcmg":
                self.__gui_viewCM.show()
                self.__app.exec()

            elif eingabe == "license":
                self.__clearScreen()
                self.__print_GPL()
                input()

            elif eingabe == "plotCm" or eingabe == "plotCm_save":
                while(True):

                    self.__clearScreen()
                    print()

                    if eingabe == "plotCm_save":
                        print(bcolors.FAIL +
                              "SAVE PLOT AS .png MODE" +
                              bcolors.ENDC)

                    print("Enter a cm id or x")
                    a = input("Bitte eine cm_id eingeben:")

                    if a == 'x':
                        print("Exit")
                        break

                    else:
                        try:
                            cm_nn = climaticMeasure.climaticMeasure(
                                a, LOAD_EUT='no')

                            sn = cm_nn.sensorName_list
                            sv = cm_nn.sensorValue_list
                            sd = cm_nn.sensorDiff_list
                            sm = cm_nn.sensorMax_list

                            if eingabe == "plotCm":
                                plot = plot_cm.plot_cm(a, sn, sv, sm, sd)
                            elif eingabe == "plotCm_save":
                                plot = plot_cm.plot_cm(a, sn, sv, sm, sd,
                                                       SAVE_FIGURE="yes")
                            plot.show()
                        except TypeError:
                            print("ERROR: TypError -- except")
                            input("Probiers nochmal")
                        except IndexError:
                            print("ERROR: Index Error -- except")
                            input("Probiers nochmal")

            elif eingabe == "readmcps":
                while(True):

                    self.__clearScreen()

                    print("filename or 'x'")
                    print("")

                    ieo = input("Filename >> ")

                    if ieo == "x":
                        print("Exit")
                        break

                    reader = read_mcps.read_mcpsStatisticFile(ieo)
                    reader.print_sensorData()
                    input()

                    # try:
                    #     reader = read_mcps.read_mcpsStatisticFile(ieo)
                    #     reader.print_sensorData()
                    #     input()
                    # except:
                    #     print("ERROR: File not avalible")
                    #     input("Probiers nochmal")

            elif eingabe == "initcomp":
                # Erstmal alle Tabellen loeschen
                self.__dbDelete.del_resetComponentTabels()

                # jetzt alle componenten in den datanbank laden
                # aus den csv files im folder components
                self.__dbAddComps.addALLComps_CSV()

            # Set Master mode

            elif eingabe == "masteron":
                print(bcolors.WARNING + "INFO: godmode is online" +
                      bcolors.ENDC)
                print("MASTER MODE IS ON")
                self.__mastermode = True

            elif eingabe == "masteroff":
                print(bcolors.WARNING + "INFO: godmode is offline" +
                      bcolors.ENDC)
                self.__mastermode = False

            # Mastermode Options

            elif eingabe == "test" and self.__mastermode is True:
                self.__clearScreen()
                print("Bitte geben sie eine cm id ein:")
                cmidsearch = input(">> ")
                a = climaticMeasure.climaticMeasure(cmidsearch)
                a.print_info_cm()

            # Programm beenden

            elif eingabe == "xxx" or eingabe == "exit":
                print("\nexit program\n")
                break

            else:
                print("\nERROR: cmd \"{}\" not found - try again".format(
                    eingabe))
            input("\nenter key ...")


if __name__ == '__main__':

    """
        TAFF Runner test
    """

    x = taff()
    x.run()

    """
        GUI Test
    """

    # app = QtWidgets.QApplication(sys.argv)

    # # x = gui_handler.gui_handler()
    # # x = cm_table_handler.cm_table_handler(1)
    # # x = cm_view_handler.cm_view_handler()
    # x = db_admin_handler.db_admin_handler()
    # # x = create_eut_handler.create_eut_handler()

    # x.show()
    # app.exec_()
