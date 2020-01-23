from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtWidgets import (QAction, QActionGroup, QInputDialog, QLineEdit,
                             QMainWindow)

from ..Gui import image_rc
from ..Gui.pomodoro_gui import Ui_MainWindow
from .timeit import TimeController


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

        self.init_slots()
        self.init_menu()
        self.init_buttons()
        self.init_profiles_for_menu()
        self.init_data()
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
        self.circleTimesLCD.display(self.ctx.profile["circle_times"])
        self.workCD.setText(self.ctx.profile["work"])
        self.workPB.setValue(0)
        self.restCD.setText(self.ctx.profile["rest"])
        self.restPB.setValue(0)
        self.long_restCD.setText(self.ctx.profile["long_rest"])
        self.long_restPB.setValue(0)

    def init_menu(self):
        """Initialize the mojarity of the actions placed in the menu"""
        self.actions = MenuActions(self.ctx)
        self.actionAbout.triggered.connect(self.actions.showAbout)
        self.actionMinimum.triggered.connect(self.showMinimized)
        self.actionQuit.triggered.connect(self.quit_)
        self.actionOptions.triggered.connect(self.actions.showOptions)

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

    def init_profiles_for_menu(self):
        """Initialize the profiles found in the directory profiles and display them in the preferences menu. So you can get a easy access to use your profile quickly"""
        # Init the profile according to the global setting: "lastProfile"
        # Add the found profiles into the preferences menu and add them into
        # the ActionGroup, so you can only select one profile at one time
        self.ctx.profile.reloadObj.reloadSig.connect(self.reload)
        self.loadProfileActions()

    def addOneProfileAction(self, p):
        # QAction(name, parent)
        action = QAction(p, self)
        action.setCheckable(True)
        # connected with the reload method provided by profile object
        action.triggered.connect(
            lambda: self.ctx.profile.reload(action.text())
        )
        return action

    def loadProfileActions(self):
        for i in self.ctx.profileList:
            action = self.addOneProfileAction(i)
            # We can get the action by its name
            self.profileActions[i] = action
            self._profile_group.addAction(action)
            self.menuPreferences.addAction(action)

        self.profileActions[self.ctx.profile.name].setChecked(True)

    def reload(self):
        """
        When reloadSig triggered, this reload method will update the data
        shown on the main window.
        """
        self.workCD.setText(self.ctx.profile["work"])
        self.restCD.setText(self.ctx.profile["rest"])
        self.long_restCD.setText(self.ctx.profile["long_rest"])
        self.circleTimesLCD.display(self.ctx.profile["circle_times"])

    def _setTime(self, title, information, default_set):
        # A wrapped function used for set*Time methods
        time, ok = QInputDialog.getText(
            self, f"Quick-settings:{title}", information, QLineEdit.Normal,
            default_set
        )
        # We will add config into it, so the following code is a simple test.
        if not ok:
            return default_set
        else:
            return time

    def setWorkTime(self):
        self.ctx.profile["work"] = self._setTime(
            "Quick-settings:Working Time", "Input your single working time", self.ctx.profile["work"]
        )
        self.workCD.setText(self.ctx.profile["work"])
        self.workPB.setValue(0)

    def setRestTime(self):
        self.ctx.profile["rest"] = self._setTime(
            "Quick-settings:Resting Time", "Input your single resting time",
            self.ctx.profile["rest"]
        )
        self.restCD.setText(self.ctx.profile["rest"])
        self.restPB.setValue(0)

    def setLongRestTime(self):
        self.ctx.profile["long_rest"] = self._setTime(
            "Quick-settings:Long-resting Time", "Input your single long-resting time", self.ctx.profile["long_rest"]
        )
        self.long_restCD.setText(self.ctx.profile["long_rest"])
        self.long_restPB.setValue(0)

    def setCircleTimes(self):
        times, ok = QInputDialog.getInt(
            self, "Quick-settings:Circle Times", "Input your circle times", self.ctx.profile[
                "circle_times"], 1, 9, 1
        )
        if not ok:
            times = self.ctx.profile["circle_times"]
        self.ctx.profile["circle_times"] = times
        self.circleTimesLCD.display(times)

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
        print("show to you!")
