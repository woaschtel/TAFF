"""
gui_handler class



"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


if __name__ == '__main__':
    print("INFO: gui_handler class import as '__main__'")
    import gui
    from createeut import create_eut_handler
else:
    print("INFO: gui_handler class import as '__module__'")
    from gui import gui
    from gui.cm_create import cm_create_handler
    from gui.cm_info import cm_info_handler
    from gui.cm_table import cm_table_handler
    from gui.cm_view import cm_view_handler
    from gui.createeut import create_eut_handler
    from gui.db_admin import db_admin_handler
    from gui.fcm_create import fcm_create_handler

"""

"""


class gui_handler(QtWidgets.QWidget):
    """
    GUI Handler - class discription

     - ist die oberste GUI Klasse des Thermal Analyser F? Framework

     Diese GUI besitzt ein Qt mdiArea in dieses weiter QWidgets geladen werden

     Liste der Qt Widget die in das mdiArea geladen werden:
        -  from gui.cm_create import cm_create_handler
        -  from gui.cm_info import cm_info_handler
        -  from gui.cm_table import cm_table_handler
        -  from gui.cm_view import cm_view_handler
        -  from gui.createeut import create_eut_handler
        -  from gui.db_admin import db_admin_handler
        -  from gui.fcm_create import fcm_create_handler

    """
    def __init__(self):
        super(gui_handler, self).__init__()

        self.ui = gui.Ui_Form()
        self.ui.setupUi(self)

        # button clicked function connect
        # test button
        self.ui.btn_test.clicked.connect(self.event_btn_test)
        self.ui.btn_openCM.clicked.connect(self.event_btn_openCM)
        self.ui.btn_cmCreate.clicked.connect(self.event_btn_cmCreate)
        self.ui.btn_cmView.clicked.connect(self.event_btn_cmView)
        self.ui.btn_cmCreateMCPS.clicked.connect(self.event_btn_cmCreateMCPS)
        self.ui.btn_dbAdmin.clicked.connect(self.event_btn_dbAdmin)
        self.ui.btn_createEUT.clicked.connect(self.event_btn_createEUT)

    def event_btn_test(self):
        print("INFO: Test Funktion is not implemented")
        pass

    def event_btn_openCM(self):
        # create a QWidget object from the "create_eut_handler" class

        try:
            if self.ui.checkBox_openData.isChecked():
                cmId = int(self.ui.lineEdit.text())
                subwindow = cm_table_handler.cm_table_handler(cmId)
                print(self.ui.lineEdit.text())
                # add the QWidget object to the mdiAre
                self.ui.mdiArea.addSubWindow(subwindow)
                # now show the QWidget
                subwindow.show()

            if self.ui.checkBox_openInfo.isChecked():
                cmId = int(self.ui.lineEdit.text())
                subwindow2 = cm_info_handler.cm_info_handler(cmId)
                print(self.ui.lineEdit.text())
                # add the QWidget object to the mdiAre
                self.ui.mdiArea.addSubWindow(subwindow2)
                # now show the QWidget
                subwindow2.show()
        except:
            QMessageBox.question(self, "ID eingeben",
                                 "bitte eine id eingeben")

    def event_btn_cmView(self):
        # create a QWidget object from the "create_cm_view" class
        subwindow = cm_view_handler.cm_view_handler()
        # add the QWidget object to the mdiAre
        self.ui.mdiArea.addSubWindow(subwindow)
        # now show the QWidget
        subwindow.show()

    def event_btn_cmCreate(self):
        subwin = cm_create_handler.cm_create_handler()
        self.ui.mdiArea.addSubWindow(subwin)
        subwin.show()

    def event_btn_cmCreateMCPS(self):
        """
            Aufruf der gui - fcm_create (damit ist fast cm create gemeint)
        """
        subwin = fcm_create_handler.fcm_create_handler()
        self.ui.mdiArea.addSubWindow(subwin)
        subwin.show()

    def event_btn_dbAdmin(self):
        subwin = db_admin_handler.db_admin_handler()
        self.ui.mdiArea.addSubWindow(subwin)
        subwin.show()

    def event_btn_createEUT(self):
        # create a QWidget object from the "create_eut_handler" class
        subwindow = create_eut_handler.create_eut_handler()
        # add the QWidget object to the mdiAre
        self.ui.mdiArea.addSubWindow(subwindow)
        # now show the QWidget
        subwindow.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    x = gui_handler()
    x.show()
    app.exec_()
