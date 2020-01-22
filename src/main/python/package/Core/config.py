from json import load, dump
from os.path import basename
from os.path import join
from collections import UserDict
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject

class ReloadSig(QObject):
    reloadSig = pyqtSignal()
    def __init__(self):
        super(ReloadSig, self).__init__()

class Profile(UserDict):

    def __init__(self, ctx):
        self.ctx = ctx
        self.reloadObj = ReloadSig()
        # load the last used json profile
        self._loadProfile(self.ctx.global_setting["lastProfile"])

    def _operate(self, flag, new=False):
        file_ = self.current_profile
        if flag == 'r':
            if new:
                file_ = self.ctx.default_profile
            with open(file_, 'r') as f:
                self.data = load(f)
        else:
            with open(file_, 'w') as f:
                dump(self.data, f)

    def _loadProfile(self, name):
        new = False
        self.name = name
        try:
            self.current_profile = self.ctx.get_resource(
                f'profiles/{self.name}.json'
            )
        except FileNotFoundError:
            new = True
            self.current_profile = join(
                self.ctx.profilesDir, f'{self.name}.json'
            )
        self._operate('r', new=new)

    def save(self):
        if self.name == "default":
            return
        self._operate('w')

    def reload(self, name):
        if self.name != "default":
            self.save()
        if name != self.name:
            self._loadProfile(name)
            self.reloadObj.reloadSig.emit()
