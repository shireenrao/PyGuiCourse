from PySide.QtCore import *
from PySide.QtGui import *
import sys

import ShowGUI
import time

class MainDialog(QDialog, ShowGUI.Ui_mainDialog):

    #threadone = Signal(str )

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.showButton.setText("Process")
        self.showButton.setFocus()
        self.showButton.clicked.connect(self.processData)
        #self.connect(self.showButton, SIGNAL("clicked()"), self.showMessageBox)

    def processData(self):
        QMessageBox.information(self, "Hello!", "Hello there, " + self.nameEdit.text())


app = QApplication(sys.argv)
form = MainDialog()
form.show()
form.raise_()
app.exec_()
