import sys
from json import dump, loads
from os import listdir
from os.path import basename, join

from fbs_runtime.application_context.PyQt5 import (ApplicationContext,
                                                   cached_property)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog

from package.Core.profile import Profile
from package.Core.pomodoro import Window
from package.Core.profile_window import ProfileSettingsDialog
from package.Core.ask import Ask_Dialog
from package.Core.profilelogger import Log4P
from package.Core.inspection import Inspector
from package.Gui.about_dialog_gui import Ui_Dialog
from package.Gui.splasher import Splasher


class AppContext(ApplicationContext):

    def __init__(self):
        super(AppContext, self).__init__()

        self.getName = lambda filename: basename(filename).split('.')[0]
        self.compose = lambda name: join(self.profilesDir, f'{name}.json')

    def run(self):
        # load the splash window
        splash_window = Splasher(self)
        self.app.processEvents()
        # load the main window
        ui = Window(self)
        ui.setStyleSheet(self.style)
        ui.show()

        splash_window.finish(ui)
        return self.app.exec_()         # start event loop

    def loadFile(self, file_):
        with open(file_, 'r', encoding='utf-8') as f:
            data = f.read()
        return data

    def loadGlobal(self, globalSettingFile):
        return loads(self.loadFile(globalSettingFile), encoding='utf-8')

    def saveGlobal(self):
        with open(self.globalSettingFile, 'w') as f:
            dump(self.global_setting, f)

    @cached_property
    def basic(self):
        return ["work", "rest", "long_rest", "circle_times"]

    @cached_property
    def basic_musics(self):
        return ["work_music", "rest_music", "end_music"]

    @cached_property
    def style(self):
        return self.loadFile(self.get_resource("style.qss"))

    @cached_property
    def musics(self):
        _musics = {
            "work": join(self.musicsDir, self.profile["work_music"]),
            "rest": join(self.musicsDir, self.profile["rest_music"]),
            "long_rest": join(self.musicsDir, self.profile["end_music"])
        }
        return _musics

    @cached_property
    def toBeInspected(self):
        return self.basic + self.basic_musics

    @cached_property
    def profile(self):
        return Profile(self)

    @cached_property
    def shadowProfile(self):
        return ShadowProfile(self)

    @cached_property
    def inspector(self):
        return Inspector(self)

    @cached_property
    def log4p(self):
        return Log4P()

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
    def default_profile_data(self):
        return loads(self.loadFile(self.default_profile), encoding="utf-8")

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

    @cached_property
    def settings_gui(self):
        ui = ProfileSettingsDialog(self)
        return ui

    @cached_property
    def ask_dialog(self):
        ui = Ask_Dialog()
        return ui


if __name__ == '__main__':
    appctxt = AppContext()       # 1. Instantiate ApplicationContext
    sys.exit(appctxt.run())
