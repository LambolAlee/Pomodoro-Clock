import sys
from json import dump, load
from os import listdir
from os.path import basename, join

from fbs_runtime.application_context.PyQt5 import (ApplicationContext,
                                                   cached_property)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog

from package.Core.config import Profile
from package.Core.pomodoro import Window
from package.Gui.about_dialog_gui import Ui_Dialog
from package.Gui.splasher import Splasher


class AppContext(ApplicationContext):

    def __init__(self):
        super(AppContext, self).__init__()

        self.getName = lambda filename: basename(filename).split('.')[0]

    def run(self):
        splash_window = Splasher(self)
        self.app.processEvents()

        ui = Window(self)
        ui.setStyleSheet(self.style)
        ui.show()

        splash_window.finish(ui)
        return self.app.exec_()

    def loadGlobal(self, globalProfile):
        with open(globalProfile, 'r') as f:
            global_setting = load(f)
        return global_setting

    def saveGlobal(self):
        with open(self.globalSettingFile, 'w') as f:
            dump(self.global_setting, f)

    @cached_property
    def style(self):
        with open(self.get_resource('style.qss'), 'r') as f:
            style_data = f.read()
        return style_data

    @cached_property
    def musics(self):
        _musics = {
            "work": join(self.musicsDir, self.profile["work_music"]),
            "rest": join(self.musicsDir, self.profile["rest_music"]),
            "long_rest": join(self.musicsDir, self.profile["end_music"])
        }
        return _musics

    @cached_property
    def profile(self):
        return Profile(self)

    @cached_property
    def profileList(self):
        profile_list = []
        for i in listdir(self.get_resource("profiles")):
            profile_list.append(self.getName(i))
        return profile_list

    @cached_property
    def default_profile(self):
        return self.get_resource("profiles/default.json")

    @cached_property
    def globalSettingFile(self):
        return self.get_resource('launcher.json')

    @cached_property
    def global_setting(self):
        return self.loadGlobal(self.globalSettingFile)

    @cached_property
    def musicsDir(self):
        return self.get_resource('musics')

    @cached_property
    def profilesDir(self):
        return self.get_resource('profiles')

    @cached_property
    def icontinue(self):
        continue_pic = QIcon()
        continue_pic.addPixmap(QPixmap(self.get_resource('image/control_panel/continue.png')))
        return continue_pic

    @cached_property
    def ipause(self):
        pause_pic = QIcon()
        pause_pic.addPixmap(QPixmap(self.get_resource('image/control_panel/pause.png')))
        return pause_pic

    @cached_property
    def about_gui(self):
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(self.build_settings["version"], Dialog)
        return Dialog


if __name__ == '__main__':
    appctxt = AppContext()       # 1. Instantiate ApplicationContext
    sys.exit(appctxt.run())
