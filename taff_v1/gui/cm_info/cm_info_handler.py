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
    import cm_info
    # from ....dbconnector import db_select, db_insert
else:
    print("INFO: create_eut_handler class import as '__module__'")
    from gui.cm_info import cm_info
    from dbconnector import db_select, db_insert, db_selectAnalyser


class cm_info_handler(QtWidgets.QWidget):
    def __init__(self, _id):
        """


        """

        self.__cm = climaticMeasure.climaticMeasure(_id)
        self.__cm.print_info_cm()
        super(cm_info_handler, self).__init__()
        self.ui = cm_info.Ui_Form()
        self.ui.setupUi(self)

        # erstmal den fenster titel setzen
        self.setWindowTitle("id: {} - name: {}".format(self.__cm._id,
                                                       self.__cm._name))

        txt = "ID: {:} Name: {:} Datum: {:}"
        txt = txt.format(self.__cm._id, self.__cm._name, self.__cm._datum)
        self.ui.label.setText(txt)

        self.__writeInformation()

    def __writeInformation(self):


        """
        Hier wird die textEdit von der form beschrieben
        """
        # Strings zur besseren formatierung
        aaa = "\n\t"
        bbb = "-"

        # texte fuer die textEdit
        nn1 = "Climatic Measurement ID"
        nn1n = str(self.__cm._id)
        nn2 = "Date"
        nn2n = str(self.__cm._datum)
        nn3 = "Name"
        nn3n = str(self.__cm._name)
        nn4 = "Info"
        nn4n = str(self.__cm._info)
        nn5 = "Ambient"
        nn5n = str(self.__cm._ambientTempText)
        nn6 = "Test Load"
        nn6n = str(self.__cm._testloadText)
        nn7 = "Sensor Info: "
        nn7n = "{}, {}, {}, {}".format(self.__cm._sensorNameID,
                                       self.__cm._sensorMaxID,
                                       self.__cm._sensorTypListID,
                                       self.__cm._sensorValueID)

        nn8 = "EUT ID:"
        nn8n = str(self.__cm._eutID)


        # text box fuellen
        self.ui.textEdit.append("{:30}:{}- {}".format(nn1, aaa, nn1n))
        self.ui.textEdit.append("{:15}:{}- {}".format(nn2, bbb, nn2n))
        self.ui.textEdit.append("{:15}:{}- {}".format(nn3, bbb, nn3n))
        self.ui.textEdit.append("{:15}:{}- {}".format(nn4, bbb, nn4n))
        self.ui.textEdit.append("{:15}:{}- {}".format(nn5, bbb, nn5n))
        self.ui.textEdit.append("{:15}:{}- {}".format(nn6, bbb, nn6n))
        self.ui.textEdit.append("{:15}:{}- {}".format(nn7, bbb, nn7n))
        self.ui.textEdit.append("{:15}:{}- {}".format(nn8, bbb, nn8n))

        self.ui.textEdit.append("\n\n Und noch vieles vieles mehr ... ")




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    x = cm_info_handler()
    x.show()
    app.exec_()
