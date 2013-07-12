import sys

from PySide.QtCore import *
from PySide.QtGui import *


__APPNAME__ = "Some Name"

class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        openButton = QPushButton("Open")
        saveButton = QPushButton("Save")
        dirButton = QPushButton("Other")
        closeButton = QPushButton("Close")

        #self.connect(openButton, SIGNAL("clicked()"), self.open)
        openButton.clicked.connect(self.open)

        layout = QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(saveButton)
        layout.addWidget(dirButton)
        layout.addWidget(closeButton)
        self.setLayout(layout)


    def open(self):

        dir = "."
        fileobj = QFileDialog.getOpenFileName(self, __APPNAME__ + ":Open File Dialog", dir=dir, filter="Text Files (*.txt)")
        print fileobj
        print type(fileobj)

        filename = fileobj[0]
        file = open(filename, 'r')
        read = file.read()
        file.close()
        print read


    def save(self):
        pass

    def other(self):
        pass

    def closefile(self):
        pass




app = QApplication(sys.argv)
form = Program()
form.show()
form.raise_()
app.exec_()