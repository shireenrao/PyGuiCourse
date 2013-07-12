import sys

from PySide.QtCore import *
from PySide.QtGui import *


__APPNAME__ = "Tenth Video"

class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__APPNAME__)
        openButton = QPushButton("Open Dialog")
        self.mainSpinBox = QSpinBox()
        self.mainCheckbox = QCheckBox("Main Checkbox Value")

        #self.connect(openButton, SIGNAL("clicked()"), self.open)
        openButton.clicked.connect(self.dialogOpen)

        layout = QVBoxLayout()
        layout.addWidget(self.mainSpinBox)
        layout.addWidget(self.mainCheckbox)
        layout.addWidget(openButton)
        self.setLayout(layout)

    def dialogOpen(self):
        initValues = {"spinboxvalue": self.mainSpinBox.value(), "checkboxvalue": self.mainCheckbox.isChecked()}
        dialog = Dialog(initValues)
        if dialog.exec_():
            self.mainCheckbox.setChecked(dialog.checkbox.isChecked())
            self.mainSpinBox.setValue(dialog.spinbox.value())



class Dialog(QDialog):

    def __init__(self, initValues, parent=None):
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

        self.checkbox.setChecked(initValues["checkboxvalue"])
        self.spinbox.setValue((initValues["spinboxvalue"]))
        btnOK.setFocus()

        #self.connect(btnOK, SIGNAL("clicked()"), self, SLOT("accept()"))
        btnOK.clicked.connect(self.accept)
        #self.connect(btnCancel, SIGNAL("clicked()"), self, SLOT("reject()"))
        btnCancel.clicked.connect(self.reject)

    def accept(self):

        class GreaterThanFive(Exception): pass
        class IsZero(Exception):pass

        try:
            if self.spinbox.value() > 5:
                raise GreaterThanFive, ("The Spinbox value can not be greater than 5")
            elif self.spinbox.value() == 0:
                raise IsZero, ("The Spinbox value can not be 0")
            else:
                QDialog.accept(self)

        except GreaterThanFive, e:
            QMessageBox.warning(self, __APPNAME__, str(e))
            self.spinbox.selectAll()
            self.spinbox.setFocus()
            return

        except IsZero, e:
            QMessageBox.warning(self, __APPNAME__, str(e))
            self.spinbox.selectAll()
            self.spinbox.setFocus()
            return


app = QApplication(sys.argv)
form = Program()
form.show()
form.raise_()
app.exec_()