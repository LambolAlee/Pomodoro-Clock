import re
from os.path import join, exists
from PyQt5.QtCore import QRegExp, QObject, pyqtSignal
from PyQt5.QtGui import QRegExpValidator, QValidator, QIntValidator
from PyQt5.QtWidgets import QMessageBox

timeValidator = QRegExpValidator(QRegExp(
    r"(?!^.*([hms]).*\1.*$)(?:[1-9]\d?[hms]){1,3}$"))

circleValidator = QIntValidator(0, 9)

class Inspector:
    def __init__(self, ctx):
        self.ctx = ctx
        self.rollback = 0

    def checkOneProfile(self, name, data):
        fatal_set = set()
        data = self.ctx.log4p.getModifiedData(name, data.copy())

        for i in self.ctx.toBeInspected:
            res = self.check(data[i], i)
            if res: fatal_set.add(i)

        if fatal_set:
            self.ctx.log4p.logFatal(name=name, attrs=fatal_set)

    def checkMore(self, profiles):
        for name, data in profiles.items():
            self.checkOne(name, data)

    def check(self, value, attr):
        if attr.endswith("_music"):
            if not exists(join(self.ctx.musicsDir, value)):
                return attr
        elif attr == "circle_times":
            if circleValidator.validate(value, 0)[0] != QValidator.Acceptable:
                return "circle_times"
        else:
            if timeValidator.validate(value, 0)[0] != QValidator.Acceptable:
                return attr
        return 0

    def checkRollBack(self):
        res = True if self.rollback > 0 else False
        return res
