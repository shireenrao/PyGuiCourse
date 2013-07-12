
from PySide.QtCore import *
from PySide.QtGui import *
import sys
import mainGUI

class MainDialog(QDialog, mainGUI.Ui_mainDialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
form = MainDialog()
form.show()
form.raise_()
app.exec_()
