from PyQt5.QtCore import QTimer, pyqtSignal, QObject
from PyQt5.QtWidgets import (QAction, QActionGroup, QInputDialog, QLineEdit,
                             QMainWindow, QMessageBox)

from ..Gui import image_rc
from ..Gui.pomodoro_gui import Ui_MainWindow
from .timeit import TimeController
from PyQt5 import sip


class Window(Ui_MainWindow, QMainWindow):

    quitCountDown = pyqtSignal()

    def __init__(self, ctx, *args, **kwargs):
        """
        Normally initialize the MainWindow and some attributes and slots
        """
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.ctx = ctx
        # A flag to distinguish between pausing and first running 
        # 1: first_run
        self.first_run = 1
        self.profileActions = {}        # A dict contains profiles
        self._profile_group = QActionGroup(self)

        self.init_menu()
        self.init_data()
        self.init_slots()
        self.init_buttons()
        self.init_profiles_for_menu()
        self.init_timer()

    def init_timer(self):
        """Initialize the timer and the TimeController"""
        # The status of continung(1) and pausing(-1)
        self.controlStatus = -1
        self.timer = QTimer()       # Initialize the timer
        self.controller = TimeController(self.ctx)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.controller.runner.minus)
        self.quitCountDown.connect(self.controller.quit_)

        self.controller.timeChanged.connect(self.update)
        self.controller.clearOld.connect(self.clearOld)
        self.controller.circleChanged.connect(self.updateLCD)
        self.controller.started.connect(self.timer.start)
        self.controller.finished.connect(self.reset)
        # After a whole counting down period, we say you eat a tomato.
        self.controller.eatTomato.connect(self.eat)
        self.controller.timerStart.connect(self.timer.start)
        self.controller.timerTempStop.connect(self.timer.stop)

    def init_data(self):
        """Display the data in the profile on the main window"""
        # Circle: work-rest period
        # Every 2 work-rest period, there is a long_rest.
        self.reload()
        self.workPB.setValue(0)
        self.restPB.setValue(0)
        self.long_restPB.setValue(0)

    def init_menu(self):
        """Initialize the mojarity of the actions placed in the menu"""
        self.actions = MenuActions(self.ctx)
        self.actionAbout.triggered.connect(self.actions.showAbout)
        self.actionMinimum.triggered.connect(self.showMinimized)
        self.actionQuit.triggered.connect(self.quit_)
        self.actionOptions.triggered.connect(self.actions.showOptions)
        self.actionDonate.triggered.connect(
            lambda: self.actions.donate(self)
        )

    def init_buttons(self):
        """Initialize the buttons lay out on the main window"""
        self.quitButton.clicked.connect(self.quit_)
        self.optionButton.clicked.connect(self.actions.showOptions)
        self.controlButton.clicked.connect(self.control)
        self.stopButton.clicked.connect(self.stop)
        self.stopButton.setEnabled(False)
        self.counterButton.clicked.connect(self.count)

    def init_slots(self):
        """Initialize the labels, lcdnumbers, statusbar and menubar"""
        # Initializethe slots of labels
        # These three label display the work time, rest time and long rest time.
        # To make the user interface more simple and keep your attention focused
        # on the task. I use the label instead of extra buttons to realize the
        # function of setting the time period quickly.
        # Also, you can find a full-functioned setting panel in the preference
        # menu and you can save these as a profile to quick load it when you use
        # the app next time as well.
        self.workLabel.doubleClicked.connect(self.setWorkTime)
        self.restLabel.doubleClicked.connect(self.setRestTime)
        self.longRestLabel.doubleClicked.connect(self.setLongRestTime)

        # Initialize the slots of circle lcdnumber
        self.circleTimesLCD.doubleClicked.connect(self.setCircleTimes)

        #Initialize the slots of profile_settings_window
        self.ctx.settings_gui.profileRemoved.connect(
            self.removeProfile)
        self.ctx.settings_gui.newProfileSig.connect(
            self.addProfileActions)
        self.ctx.settings_gui.updateSig.connect(
            self.refreshSelectedActionAndData)

    def init_profiles_for_menu(self):
        """Initialize the profiles found in the directory profiles and display them in the preferences menu. So you can get a easy access to use your profile quickly"""
        # Init the profile according to the global setting: "lastProfile"
        # Add the found profiles into the preferences menu and add them into
        # the ActionGroup, so you can only select one profile at one time
        self.ctx.profile.reloadObj.reloadSig.connect(self.reload)
        self.loadProfileActions()

    def refreshSelectedActionAndData(self):
        self.reload()
        self.profileActions[self.ctx.profile.name].setChecked(True)

    def addOneProfileAction(self, name):
        # QAction(name, parent)
        action = QAction(name, self)
        action.setCheckable(True)
        # connected with the reload method provided by profile object
        action.triggered.connect(
            lambda: self.ctx.profile.reload(action.text())
        )
        return action

    def addProfileActions(self, names):
        for name in names:
            action = self.addOneProfileAction(name)
            self.profileActions[name] = action
            self._profile_group.addAction(action)
            self.menuPreferences.addAction(action)

    def loadProfileActions(self):
        self.addProfileActions(self.ctx.profileList)
        self.profileActions[self.ctx.profile.name].setChecked(True)

    def removeProfile(self, name):
        try:
            action = self.profileActions.pop(name)
        except KeyError:
            pass
        else:
            self._profile_group.removeAction(action)
            self.menuPreferences.removeAction(action)
            sip.delete(action)

    def reload(self):
        """
        When reloadSig triggered, this reload method will update the data
        shown on the main window.
        """
        self.workCD.setText(self.ctx.profile["work"])
        self.restCD.setText(self.ctx.profile["rest"])
        self.long_restCD.setText(self.ctx.profile["long_rest"])
        self.circleTimesLCD.display(self.ctx.profile["circle_times"])
        if self.ctx.log4p.query(f"fatal:{self.ctx.profile.name}:"):
            self.controlButton.setEnabled(False)
        else:
            self.controlButton.setEnabled(True)

    def _set(self, name, attr, value):
        if value:
            self.ctx.profile[attr] = value
            if not self.ctx.inspector.check(value, attr):
                self.ctx.log4p.remove(f"fatal:{name}:{attr}")
        if self.ctx.log4p.query(f"fatal:{name}:") is None:
            self.controlButton.setEnabled(True)
        self.ctx.ask_dialog.close()

    def setWorkTime(self):
        f = lambda value: self._set(self.ctx.profile.name, "work", value)
        self.ctx.ask_dialog.replySig.connect(f)
        self.ctx.ask_dialog.ask("work", self.ctx.profile["work"])
        self.workCD.setText(self.ctx.profile["work"])
        self.workPB.setValue(0)
        self.ctx.ask_dialog.replySig.disconnect(f)

    def setRestTime(self):
        f = lambda value: self._set(self.ctx.profile.name, "rest", value)
        self.ctx.ask_dialog.replySig.connect(f)
        self.ctx.ask_dialog.ask("rest", self.ctx.profile["rest"])
        self.restCD.setText(self.ctx.profile["rest"])
        self.restPB.setValue(0)
        self.ctx.ask_dialog.replySig.disconnect(f)

    def setLongRestTime(self):
        f = lambda value: self._set(self.ctx.profile.name, "long_rest", value)
        self.ctx.ask_dialog.replySig.connect(f)
        self.ctx.ask_dialog.ask("long-resting", self.ctx.profile["long_rest"])
        self.long_restCD.setText(self.ctx.profile["long_rest"])
        self.long_restPB.setValue(0)
        self.ctx.ask_dialog.replySig.disconnect(f)

    def setCircleTimes(self):
        f = lambda value: self._set(
            self.ctx.profile.name, "circle_times", value)
        self.ctx.ask_dialog.replySig.connect(f)
        self.ctx.ask_dialog.ask("circle_times",self.ctx.profile["circle_times"])
        self.circleTimesLCD.display(self.ctx.profile["circle_times"])
        self.ctx.ask_dialog.replySig.disconnect(f)

    def reset(self):
        self.timer.stop()
        self.controlButton.setIcon(self.ctx.icontinue)
        self.stopButton.setEnabled(False)
        self.init_data()
        self.first_run = 1
        self.controlStatus = -1

    def eat(self):
        self.stopButton.setEnabled(False)
        self.ctx.global_setting["count"] += 1
        self.statusBar.showMessage("You have eaten a tomato just now!", 2000)

    def quit_(self):
        """Quit the app"""
        self.ctx.profile.save()
        self.ctx.global_setting["lastProfile"] = self._profile_group.checkedAction().text()
        self.ctx.saveGlobal()
        self.ctx.app.quit()

    def count(self):
        self.statusBar.showMessage("You have eaten {} tomatoes by now".format(
            self.ctx.global_setting["count"]), 1500
        )

    def update(self, type_, pc, time_gen):
        pb = type_ + "PB"
        label = type_ + "CD"
        getattr(self, label).setText("".join(time_gen))
        getattr(self, pb).setValue(100 - pc)

    def updateLCD(self):
        num = self.circleTimesLCD.intValue() - 1
        self.circleTimesLCD.display(num)

    def clearOld(self, type_):
        if type_ == "":
            type_ = "work"
        getattr(self, type_ + "PB").setValue(0)
        getattr(self, type_ + "CD").setText('0s')

    def control(self):
        self.controlStatus = -self.controlStatus
        if self.controlStatus == 1:     # pause counting down
            self.controlButton.setIcon(self.ctx.ipause)
            self.statusBar.showMessage("continue", 1000)
            if self.first_run:
                self.first_run = 0
                self.stopButton.setEnabled(True)
                self.statusBar.showMessage("preparing...", 2000)
                # Initialize the controller's counting down related data,
                # in order to keep the controller receiving
                # the newest profile data.
                self.controller.reset()
                self.controller.start()
            else:       # continue counting down
                self.timer.start()
        else:
            self.controlButton.setIcon(self.ctx.icontinue)
            self.statusBar.showMessage("paused")
            self.timer.stop()

    def stop(self):
        """Quit counting down but not quit the app"""
        self.quitCountDown.emit()
        self.statusBar.showMessage("stopped", 1000)


class MenuActions:
    """
    A class contains the mojarity of the callback functions used in menus
    """

    def __init__(self, ctx):
        self.ctx = ctx

    def showAbout(self):
        """Show the about window"""
        self.ctx.about_gui.exec_()

    def showOptions(self):
        self.ctx.settings_gui.reload_data()
        self.ctx.settings_gui.exec_()

    def donate(self, window):
        QMessageBox.information(window, "Hint", '<b style="color:gold;">氪金</b>通道暂未开启')
