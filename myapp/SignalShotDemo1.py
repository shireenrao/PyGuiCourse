__author__ = 'shireenrao'
import sys

from PySide.QtCore import *
from PySide.QtGui import *

import math

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.dialer = QDial()
        self.dialer.setNotchesVisible(True)
        self.spinbox = QSpinBox()

        layout = QVBoxLayout()
        layout.addWidget(self.dialer)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        self.dialer.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dialer.setValue)

app = QApplication(sys.argv)
form = Form()
form.show()
form.raise_()
app.exec_()