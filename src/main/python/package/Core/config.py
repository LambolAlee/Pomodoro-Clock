from collections import UserDict
from json import dump, load
from os.path import basename, join

from PyQt5.QtCore import QObject, pyqtSignal


class ReloadSig(QObject):
    reloadSig = pyqtSignal()
    def __init__(self):
        super(ReloadSig, self).__init__()

class Profile(UserDict):
    """
    The Profile class is used to handle profile settings.

    reloadObj:
        send a reloadSig to the pomodoro module to adjust the cntents 
        displayed in the main window.
    
    reload:
        load the config by passing the name of the profile to it.
    
    save:
        save the changed profile.
    """
    def __init__(self, ctx):
        self.ctx = ctx
        self.reloadObj = ReloadSig()
        # load the last used json profile
        self._loadProfile(self.ctx.global_setting["lastProfile"])

    def _operate(self, flag, new=False):
        """
        read profile from the specific profile file,
        or write the changed profile data back into the file.

        if the profile is new, the method will return the default settings.
        """
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
        """
        Help to load the profile by its name using ._operate method, 
        the method will judge whether the profile exists or not.
        """
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
