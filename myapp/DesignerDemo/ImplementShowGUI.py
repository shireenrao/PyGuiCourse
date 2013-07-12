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
        self.workerThread = workerThread()
        #self.workerThread.threadDone.connect(self.threadDone, Qt.DirectConnection)
        #self.connect(self.workerThread, SIGNAL("threadDone(QString)"), self.threadDone, Qt.DirectConnection)
        self.workerThread.threadone.connect(self.threadDone)
        #self.threadone.connect(self.threadDone)

    def processData(self):
        self.workerThread.start()
        #QMessageBox.information(self, "Hello!", "Hello there, " + self.nameEdit.text())

    def threadDone(self, txtMsg):
        self.nameEdit.setText(txtMsg)

class workerThread(QThread):

    threadone = Signal(str)

    def __init__(self, parent=None):
        super(workerThread, self).__init__(parent)

    def run(self):
        time.sleep(6)
        self.threadone.emit("Confirmation that the thread is complete.")
        #self.emit(SIGNAL("threadDone(QString)"), "Confirmation that the thread is complete.")

app = QApplication(sys.argv)
form = MainDialog()
form.show()
form.raise_()
app.exec_()