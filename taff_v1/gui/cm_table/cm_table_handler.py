import sys
import csv
from PyQt5 import QtWidgets, QtCore
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QAction, QActionGroup, QApplication, QColorDialog,
        QComboBox, QDialog, QFontDialog, QGroupBox, QHBoxLayout, QLabel,
        QMainWindow, QMessageBox, QPushButton, QTableWidget,
        QTableWidgetItem, QToolBar)

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt4 import QtGui, QtCore
import sys

import climaticMeasure


if __name__ == '__main__':
    print("INFO: create_eut_handler class import as '__main__'")
    import cm_table
    # from ....dbconnector import db_select, db_insert
else:
    print("INFO: create_eut_handler class import as '__module__'")
    from gui.cm_table import cm_table
    from dbconnector import db_select, db_insert, db_selectAnalyser


class cm_table_handler(QtWidgets.QWidget):
    def __init__(self, _id):
        self.__cm = climaticMeasure.climaticMeasure(_id)
        self.__cm.print_info_cm()
        super(cm_table_handler, self).__init__()
        self.ui = cm_table.Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(5)
        self.clip = QtWidgets.QApplication.clipboard()

        txt = "ID: {:} Name: {:} Datum: {:}"
        txt = txt.format(self.__cm._id, self.__cm._name, self.__cm._datum)
        self.ui.label.setText(txt)

        print(self.__cm._name)
        print("")

        for i in range(len(self.__cm.sensorName_list)):
            # Anzahle der Zeilen in der Tabelle auslesen
            rowcount = self.ui.tableWidget.rowCount()
            print("DEBUG: die Tabelle hat {} Zeilen. ".format(rowcount))
            # Neue Zeile in der Tabelle erstellen mit dem neuen Zeilen Nummer
            self.ui.tableWidget.insertRow(rowcount)
            print("DEBUG: Zeiel {} erstelt".format(rowcount))
            # Jetzt in die Zeile einen eintrag machen
            self.ui.tableWidget.setItem(rowcount, 0, QTableWidgetItem(
                str(self.__cm.sensorName_list[i])))
            self.ui.tableWidget.setItem(rowcount, 1, QTableWidgetItem(
                str(self.__cm.sensorTypName_list[i])))
            self.ui.tableWidget.setItem(rowcount, 2, QTableWidgetItem(
                str(self.__cm.sensorMax_list[i])))
            self.ui.tableWidget.setItem(rowcount, 3, QTableWidgetItem(
                str(self.__cm.sensorValue_list[i])))
            self.ui.tableWidget.setItem(rowcount, 4, QTableWidgetItem(
                str(self.__cm.sensorDiff_list[i])))

    def keyPressEvent(self, e):
        if (e.modifiers() & QtCore.Qt.ControlModifier):
            selected = self.ui.tableWidget.selectedRanges()

            if e.key() == QtCore.Qt.Key_V:  # past
                first_row = selected[0].topRow()
                first_col = selected[0].leftColumn()

                # copied text is split by '\n' and '\t' to paste to the cells
                for r, row in enumerate(self.clip.text().split('\n')):
                    for c, text in enumerate(row.split('\t')):
                        self.ui.tableWidget.setItem(
                            first_row+r, first_col+c,
                            QtWidgets.QTableWidgetItem(text))

            elif e.key() == QtCore.Qt.Key_C:  # copy
                s = ""
                for r in range(selected[0].topRow(),
                               selected[0].bottomRow() + 1):
                    for c in range(selected[0].leftColumn(),
                                   selected[0].rightColumn() + 1):
                        try:
                            s += str(
                                self.ui.tableWidget.item(r, c).text()) + "\t"
                        except AttributeError:
                            s += "\t"
                    s = s[:-1] + "\n"  # eliminate last '\t'
                self.clip.setText(s)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    x = cm_table_handler()
    x.show()
    app.exec_()
