from PyQt5.QtWidgets import QLabel, QLCDNumber
from PyQt5.QtCore import pyqtSignal



class CircleLCD(QLCDNumber):
    # Double click for setting the circle times
    doubleClicked = pyqtSignal()

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()


class MyLabel(QLabel):
    # Double click the label you can enter the quick settng panel of each item
    doubleClicked = pyqtSignal()

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()