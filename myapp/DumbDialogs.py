import sys

from PySide.QtCore import *
from PySide.QtGui import *


__APPNAME__ = "Ninth Video"

class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__APPNAME__)
        openButton = QPushButton("Open Dialog")
        self.label1 = QLabel("Label 1 Result")
        self.label2 = QLabel("Label 2 Result")

        #self.connect(openButton, SIGNAL("clicked()"), self.open)
        openButton.clicked.connect(self.dialogOpen)

        layout = QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)

    def dialogOpen(self):
        dialog = Dialog()
        if dialog.exec_():
            self.label1.setText("Spinbox value is " + str(dialog.spinbox.value()))
            self.label2.setText("Checkbox is " + str(dialog.checkbox.isChecked()))
        else:
            QMessageBox.warning(self, __APPNAME__, "Dialog Canceled!")


class Dialog(QDialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        self.checkbox = QCheckBox("Check me out!")
        self.spinbox = QSpinBox()
        btnOK = QPushButton("Ok")
        btnCancel = QPushButton("Cancel")

        layout = QGridLayout()
        layout.addWidget(self.spinbox, 0, 0)
        layout.addWidget(self.checkbox, 0, 1)
        layout.addWidget(self.checkbox, 0, 1)
        layout.addWidget(btnCancel)
        layout.addWidget(btnOK)
        self.setLayout(layout)

        #self.connect(btnOK, SIGNAL("clicked()"), self, SLOT("accept()"))
        btnOK.clicked.connect(self.accept)
        #self.connect(btnCancel, SIGNAL("clicked()"), self, SLOT("reject()"))
        btnCancel.clicked.connect(self.reject)


app = QApplication(sys.argv)
form = Program()
form.show()
form.raise_()
app.exec_()