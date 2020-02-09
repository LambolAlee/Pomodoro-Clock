from ..Gui.ask_dialog import Ui_Dialog
from .inspection import timeValidator, circleValidator
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal

class Ask_Dialog(Ui_Dialog, QDialog):

    replySig = pyqtSignal(str)

    def __init__(self):
        super(Ask_Dialog, self).__init__()
        self.setupUi(self)
        self.init_slots()

    def init_slots(self):
        self.buttonBox.accepted.connect(lambda: self.reply(True))
        self.buttonBox.rejected.connect(lambda: self.reply(False))

    def ask(self, title, default):
        if title == "circle_times":
            self.lineEdit.setPlaceholderText("Range from 0 to 9")
            self.lineEdit.setValidator(circleValidator)
            self.lineEdit.setText(default)
            self.label.setText("Input your circle times: ")
        else:
            self.lineEdit.setPlaceholderText("i.e. 1h2m3s")
            self.lineEdit.setValidator(timeValidator)
            self.lineEdit.setText(default)
            self.label.setText(f"Input your {title} time: ")
        self.exec_()

    def reply(self, flag):
        if flag:
            self.replySig.emit(self.lineEdit.text())
        else:
            self.replySig.emit("")