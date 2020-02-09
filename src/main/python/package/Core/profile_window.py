from os.path import basename, join, dirname
from shutil import move
from PyQt5.Qt import Qt
from PyQt5.QtGui import QFont, QDesktopServices
from PyQt5.QtCore import pyqtSignal, QEvent, QUrl
from PyQt5.QtWidgets import QDialog, QInputDialog, QLineEdit, QMessageBox
from PyQt5.QtWidgets import QListWidgetItem, QFileDialog
from PyQt5.QtCore import QObject
from ..Gui.profile_settings_dialog import Ui_settings_Dialog
from .inspection import *

def block_signals(func):
    def wrapper(self, *args, **kwargs):
        self.textChangedByProgram = True
        self.block(True)
        self.reload_rollback()
        func(self, *args, **kwargs)
        self.block(False)
        self.textChangedByProgram = False
    return wrapper


class ProfileSettingsDialog(Ui_settings_Dialog, QDialog):

    updateSig = pyqtSignal()
    newProfileSig = pyqtSignal(list)
    profileRemoved = pyqtSignal(str)

    def __init__(self, ctx, *args, **kwargs):
        super(ProfileSettingsDialog, self).__init__(*args, **kwargs)
        self.setupUi(ctx, self)
        self.ctx = ctx
        self.lastFatal = []
        self.musics = {}
        self.textChangedByProgram = True
        self.profile = self.ctx.profile
        self.logger = self.ctx.log4p
        self.inspector = self.ctx.inspector
        self.wrongStyle = "#{} {border:2px solid red; background:rgba(255, 0, 0, 100);}"
        self.loadList()
        self.init_slots()
        self.setCurrentItem(self.profile.name)
        self.init_validator()
        self.init_eventFilter()

    def init_validator(self):
        self.workEdit.setValidator(timeValidator)
        self.restEdit.setValidator(timeValidator)
        self.long_restEdit.setValidator(timeValidator)
        self.circle_timesEdit.setValidator(circleValidator)

    def init_eventFilter(self):
        self.workEdit.installEventFilter(self)
        self.restEdit.installEventFilter(self)
        self.long_restEdit.installEventFilter(self)
        self.circle_timesEdit.installEventFilter(self)

    def init_slots(self):
        self.container.currentItemChanged.connect(self._refresh)
        self.plusButton.clicked.connect(self.addProfile)
        self.minusButton.clicked.connect(self.removeProfile)
        self.saveButton.clicked.connect(self.save)
        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.cancel)
        self.workMusicTB.clicked.connect(
            lambda: self.getMusicFile(self.work_musicShow))
        self.restMusicTB.clicked.connect(
            lambda: self.getMusicFile(self.rest_musicShow))
        self.endMusicTB.clicked.connect(
            lambda: self.getMusicFile(self.end_musicShow))
        self.workReturn.clicked.connect(lambda: self.rollback("work"))
        self.restReturn.clicked.connect(lambda: self.rollback("rest"))
        self.long_restReturn.clicked.connect(lambda: self.rollback("long_rest"))
        self.circle_timesReturn.clicked.connect(
            lambda: self.rollback("circle_times"))
        self.work_musicReturn.clicked.connect(
            lambda: self.rollbackMusic("work_music"))
        self.rest_musicReturn.clicked.connect(
            lambda: self.rollbackMusic("rest_music"))
        self.end_musicReturn.clicked.connect(
            lambda: self.rollbackMusic("end_music"))
        self.workEdit.textChanged.connect(
            lambda text: self.change(self.workEdit, text))
        self.restEdit.textChanged.connect(
            lambda text: self.change(self.restEdit, text))
        self.long_restEdit.textChanged.connect(
            lambda text: self.change(self.long_restEdit, text))
        self.circle_timesEdit.textChanged.connect(
            lambda text: self.change(self.circle_timesEdit, text))

    def getMusicFile(self, obj):
        filename, _ = QFileDialog.getOpenFileName(self, 
            f"Select {obj.name} file",
            "C:/",
            "WAV Files (*.wav);;MP3 Files (*.mp3);;All Files (*)")
        if filename:
            base = basename(filename)
            self.musics[(self.profile.name, obj.name)] = filename
            getattr(self, obj.name + "Show").setText(base)
            getattr(self, obj.name + "Show").setCursorPosition(0)
            self.changeMusic(obj, base)

    def migrateMusicFiles(self):
        temp_dic = {}
        for (name, attr), file_ in self.musics.items():
            try:
                move(file_, join(self.ctx.musicsDir, basename(file_)))
            except PermissionError:
                self.migrateManually(file_)
                temp_dic[(name, attr)] = file_
            finally:
                self.logger.remove(f"modify:{name}:{attr}")
        self.musics = temp_dic

    def migrateManually(self, path):
        QMessageBox.information(
            self, "Hint", "You need to migrate the music file manually to the resource directory.")
        QDesktopServices.openUrl(QUrl("file:///"+self.ctx.musicsDir, QUrl.TolerantMode))

    def migrateAndCheck(self):
        self.migrateMusicFiles()
        res = True
        for (name, attr), file_ in self.musics.items():
            if not self.inspector.check(basename(file_), attr):
                continue
            self.logger.logFatal(name=name, attrs=attr)
            self.highlight(attr)
            res = False
        return res

    def markFatal(self):
        if self.logger.query(f"fatal:{self.profile.name}:"):
            self.lastFatal = self.logger["fatal"][self.profile.name]
            for i in self.lastFatal:
                self.highlight(i)
        else:
            self.lastFatal = []

    def clearStyle(self):
        for i in self.lastFatal:
            getattr(self, i + "Edit").setStyleSheet(None)

    def change(self, obj, text):
        if not self.textChangedByProgram:
            getattr(self, obj.name + "Return").setEnabled(True)
            if obj.styleSheet():
                obj.setStyleSheet(None)
        self.record(text, obj.name)
        if self.logger["modify"]:
            if not self.saveButton.isEnabled():
                self.saveButton.setEnabled(True)
        elif self.saveButton.isEnabled():
            self.saveButton.setEnabled(False)

    def changeMusic(self, obj, text):
        getattr(self, obj.name + "Return").setEnabled(True)
        if obj.styleSheet():
            obj.setStyleSheet(
                "#{}{background:transparent;}".replace("{}", obj.name + "Show")
            )
        self.logger.logModify(
            name=self.profile.name, modified_attrs={obj.name:text}
        )
        if self.logger["modify"]:
            if not self.saveButton.isEnabled():
                self.saveButton.setEnabled(True)
        elif self.saveButton.isEnabled():
            self.saveButton.setEnabled(False)

    def block(self, flag=True):
        self.workEdit.blockSignals(flag)
        self.restEdit.blockSignals(flag)
        self.long_restEdit.blockSignals(flag)
        self.circle_timesEdit.blockSignals(flag)
        self.work_musicShow.blockSignals(flag)
        self.rest_musicShow.blockSignals(flag)
        self.end_musicShow.blockSignals(flag)

    def clear_rollback(self):
        self.workReturn.setEnabled(False)
        self.restReturn.setEnabled(False)
        self.long_restReturn.setEnabled(False)
        self.circle_timesReturn.setEnabled(False)
        self.work_musicReturn.setEnabled(False)
        self.rest_musicReturn.setEnabled(False)
        self.end_musicReturn.setEnabled(False)

    def reload_rollback(self):
        if self.logger.query(f"modify:{self.profile.name}:"):
            if self.profile.name in self.logger["new"] and \
                self.profile != self.ctx.default_profile_data:

                for i in self.logger["modify"][self.profile.name]:
                    if i == "work_rest_period":
                        continue
                    getattr(self, i + "Return").setEnabled(True)
        else:
            self.clear_rollback()

    def rollback(self, name):
        self.textChangedByProgram = True
        getattr(self, name + "Return").setEnabled(False)
        getattr(self, name + "Edit").setText(self.profile[name])
        self.textChangedByProgram = False
        # self.inspector.rollback -= 1

    def rollbackMusic(self, attr):
        getattr(self, attr + "Return").setEnabled(False)
        getattr(self, attr + "Show").setText(self.profile[attr])
        getattr(self, attr + "Show").setCursorPosition(0)
        self.musics.pop((self.profile.name, attr))
        self.logger.remove(f"modify:{self.profile.name}:{attr}")
        if not self.logger["modify"]:
            self.saveButton.setEnabled(False)

    def reload_data(self):
        if self.container.currentItem().text() == self.profile.name:
            self.loadTextAndValue()
        self.setCurrentItem(self.profile.name)

    def highlight(self, name):
        if name in self.ctx.basic_musics:
            obj_name = name + "Show"
        else:
            obj_name = name + "Edit"
        getattr(self, obj_name).setStyleSheet(
            self.wrongStyle.replace('{}', obj_name)
        )

    def setCurrentItem(self, name):
        self.container.setCurrentItem(
            self.findItem(name)
        )

    def findItems(self, names):
        res = []
        for name in names:
            res.append(self.findItem(name))
        return res
    
    def findItem(self, name):
        return self.container.findItems(name, Qt.MatchFixedString)[0]

    @block_signals
    def loadTextAndValue(self):
        basic = self.logger.getModifiedData(
            self.profile.name, self.profile.copy())
        self.workEdit.setText(basic["work"])
        self.restEdit.setText(basic["rest"])
        self.long_restEdit.setText(basic["long_rest"])
        self.circle_timesEdit.setText(basic["circle_times"])
        self.work_musicShow.setText(self.profile["work_music"])
        self.work_musicShow.setCursorPosition(0)
        self.rest_musicShow.setText(self.profile["rest_music"])
        self.rest_musicShow.setCursorPosition(0)
        self.end_musicShow.setText(self.profile["end_music"])
        self.end_musicShow.setCursorPosition(0)
        self.markFatal()

    def loadList(self):
        self.container.addItems(self.ctx.profileList)

    def _refresh(self, item):
        self.clearStyle()
        self.profile.reload(item.text())
        self.loadTextAndValue()

    def rename(self):
        name, ok = QInputDialog.getText(self, 
                        "Profile name", 
                        "Enter name:", 
                        QLineEdit.Normal)
        return name, ok

    def askForReply(self, title, context):
        reply = QMessageBox.warning(
            self, title, context,
            QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        return reply

    def addProfile(self):
        name, ok = self.rename()
        if not ok:
            return

        self.profile.reload(name)
        self.container.addItem(name)
        self.ctx.profileList.append(name)
        self.setCurrentItem(name)
        #self.loadTextAndValue()
        self.saveButton.setEnabled(True)

    def remove(self, item):
        name = item.text()
        self.container.takeItem(self.container.row(item))
        self.logger.remove(f":{name}:")
        self.ctx.profileList.remove(name)
        self.ctx.profile.remove(name)
        if not self.logger["modify"]:
            self.saveButton.setEnabled(False)
        self.profileRemoved.emit(name)

    def removeProfile(self):
        item = self.container.currentItem()
        if item.text() == "default":
            QMessageBox.information(
                self, "Hint", "Can't remove the default profile!",
                QMessageBox.Yes,QMessageBox.Yes)
            return

        reply = self.askForReply(
            "Attention!", 
            "Do you really want to remove the current profile?")
        if reply == QMessageBox.No:
            return

        self.remove(item)

    def ok(self):
        if self.logger["modify"]:
            reply = self.askForReply(
                "Attention!", 
                "Do you want to save these changes?")
            if reply == QMessageBox.No:
                self.cancel()
            else:
                self.save()
        self.updateSig.emit()
        self.close()

    def cancel(self):
        for i in self.findItems(self.logger["new"]):
            self.container.takeItem(self.container.row(i))
        self.saveButton.setEnabled(False)
        self.updateSig.emit()
        self.musics.clear()
        self.logger["modify"].clear()
        self.logger["new"].clear()
        self.close()

    def save(self):
        self.ctx.profileList.extend(self.logger["new"])
        for name in self.logger["modify"]:
            data = self.logger.getModifiedData(name, self.profile.reload(name))
            self.profile.save(self.ctx.compose(name), data)
        if not self.migrateAndCheck():
            QMessageBox.warning(self, "warning", "There are still some problem with your music file. Please check it and try again later!")
            return
        self.saveButton.setEnabled(False)
        self.clear_rollback()
        self.newProfileSig.emit(self.logger["new"].copy())
        self.updateSig.emit()
        self.logger.reload()

    def eventFilter(self, watched, event):
        if not self.textChangedByProgram:
            if event.type() == QEvent.FocusIn:
                if watched.styleSheet():
                    watched.setStyleSheet(None)
            elif event.type() == QEvent.FocusOut:
                if self.inspector.check(watched.text(), watched.name):
                    self.highlight(watched.name)
        return QDialog.eventFilter(self, watched, event)

    def record(self, text, attr):
        query_str = f"{self.profile.name}:{attr}"

        def deduplicate(_query_str):
            if self.logger.query("modify:"+_query_str):
                self.logger.remove("modify:"+_query_str)
                # self.inspector.rollback -= 1
                # watched.blockSignals(False)
            getattr(self, attr + "Return").setEnabled(False)

        if attr == "circle_times":
            isaccepted = circleValidator.validate(text, 0)[0]
        else:
            isaccepted = timeValidator.validate(text, 0)[0]
        if isaccepted == QValidator.Acceptable:
            if text == self.profile[attr]:
                deduplicate(query_str)
            else:
                self.logger.logModify(
                    name=self.profile.name,
                    modified_attrs={attr:text})
                if self.logger.query("fatal:"+query_str):
                    self.logger.remove("fatal:"+query_str)
        else:
            if text == self.profile[attr]:
                deduplicate(query_str)
            else:
                self.logger.logModify(
                    name=self.profile.name,
                    modified_attrs={attr:text})
            self.logger.logFatal(
                name=self.profile.name, attrs={attr})
            self.highlight(attr)
