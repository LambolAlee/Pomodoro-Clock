from collections import UserDict, namedtuple
from json import dump, load, loads
from os.path import basename, join, exists
from os import remove as remove_file


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
        self.name = "default"
        self.reloadObj = ReloadSig()
        # load the last used json profile
        self.reload(self.ctx.global_setting["lastProfile"], init=True)

    @property
    def checkGroup(self):
        return self["work"], self["rest"], self["long_rest"], self["circle_times"]

    def _operate(self, file_, flag, data=None, new=False):
        """
        read profile from the specific profile file,
        or write the changed profile data back into the file.

        if the profile is new, the method will return the default settings.
        """
        if flag == 'r':
            if new:
                file_ = self.ctx.default_profile
            with open(file_, 'r') as f:
                data = load(f)
                if new:
                    self.ctx.log4p.logModify(
                        name=self.name,
                        modified_attrs=data,
                        new=new)
            return data
        else:
            with open(file_, 'w') as f:
                dump(data, f)

    def _loadProfile(self, name):
        """
        Help to load the profile by its name using ._operate method, 
        the method will judge whether the profile exists or not.
        """
        new = False
        self.name = name
        self.current_profile = self.ctx.compose(name)
        if not exists(self.current_profile):
            new = True
        data = self._operate(self.current_profile, 'r', new=new)
        return data

    def save(self, custom_file=None, data=None):
        if self.name == "default":
            return
        file_ = self.current_profile
        data_ = self.data
        if custom_file:
            file_ = custom_file
            data_ = data
        self._operate(file_, 'w', data_)

    def reload(self, name, init=False):
        if self.name != "default":
            self.save()
        if name != self.name or init:
            self.data = self._loadProfile(name)
            self.ctx.inspector.checkOneProfile(name, self.data)
            self.reloadObj.reloadSig.emit()
        return self.data

    def remove(self, name):
        remove_file(self.ctx.compose(name))
