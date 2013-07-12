__author__ = 'shireenrao'
import sys

from PySide.QtCore import *
from PySide.QtGui import *

import math

class ZeroSpinBox(QSpinBox):

    zeros = 0
    atZero = Signal(int, int)

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)

        self.valueChanged.connect(self.check_zero)

    def check_zero(self, value):
        if value ==0:
            self.zeros += 1
            self.constant = 5
            self.atZero.emit(self.zeros, self.constant)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.dialer = QDial()
        self.dialer.setNotchesVisible(True)

        self.spinbox = ZeroSpinBox()

        layout = QVBoxLayout()
        layout.addWidget(self.dialer)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        self.dialer.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dialer.setValue)
        self.spinbox.atZero.connect(self.printvalue)

    def printvalue(self, zeros, constant):
        print "The spin box has been at zero {0} times".format(zeros)
        print "The constant value is {0}".format(constant)


app = QApplication(sys.argv)
form = Form()
form.show()
form.raise_()
app.exec_()