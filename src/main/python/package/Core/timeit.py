from os.path import join
from re import findall
from queue import Queue
from winsound import PlaySound as Play 
from winsound import SND_FILENAME as SF
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtCore import QTimer, QThread, QObject

cdQueue = Queue()
play_music = lambda music:Play(music, SF)

hour = lambda timeint:timeint*3600
mins = lambda timeint:timeint*60
secs = lambda timeint:timeint
timefunc = {"h":hour, "m":mins, "s":secs}

def parse(time):
        sum_ = 0
        timeints = findall("\d+", time)
        timesufix = findall("[hms]", time)
        for sufix, ints in zip(timesufix, timeints):
            sum_ += timefunc[sufix](int(ints))
        return sum_

def strTime(time_name):

    def get_time(instance):
        return instance.__dict__[time_name]

    def set_time(instance, value):
        instance.__dict__[time_name] = parse(value)
    
    def del_time(instance):
        del instance.__dict__[time_name]

    return property(get_time, set_time, del_time)

class TimeController(QThread):

    timerTempStop = pyqtSignal()
    timerStart = pyqtSignal()
    clearOld = pyqtSignal(str)
    timeChanged = pyqtSignal(str, int, dict)
    circleChanged = pyqtSignal()
    eatTomato = pyqtSignal()

    work = strTime("work")
    rest = strTime("rest")
    long_rest = strTime("long_rest")

    def __init__(self, ctx):
        super(TimeController, self).__init__()
        self.ctx = ctx
        self.runner = TimeRunner(self)

    def reset(self):
        self.type_ = ""
        self.first_run = 1
        self.work = self.ctx.profile["work"]
        self.rest = self.ctx.profile["rest"]
        self.long_rest = self.ctx.profile["long_rest"]
        self.circle = self.ctx.profile["circle_times"]
        self.time_queue = self.flat()
        self.over = False

    def flat(self):
        time_queue = []
        for i in range(1, self.circle +1):
            time_queue.append((self.work +1, "work"))
            time_queue.append((self.rest +1, "rest"))
            if i % 2 == 0:
                time_queue.append((self.long_rest +1, "long_rest"))
        return iter(time_queue)

    def quit_(self):
        self.over = True
        self.first_run = 1
        cdQueue.put(1)

    @pyqtSlot()
    def run(self):
        try:
            while True:
                oldType = self.type_
                self.countdown, self.type_ = next(self.time_queue)

                if self.first_run:
                    self.first_run = 0
                else:
                    play_music(self.ctx.musics[self.type_])
                    self.clearOld.emit(oldType)

                if self.type_ == "rest":
                    self.circleChanged.emit()

                self.timerStart.emit()
                cdQueue.get()

                if self.over:
                    raise StopIteration
        except StopIteration:
            if not self.over:
                self.eatTomato.emit()
                play_music(self.ctx.musics["long_rest"])
            else:
                self.clearOld.emit(oldType)


class TimeRunner(QObject):
    def __init__(self, controller):
        super(TimeRunner, self).__init__()
        self.controller = controller

    def getPercent(self):
        return (self.controller.countdown / getattr(self.controller, self.controller.type_)) * 100

    def convert(self, num):
        m, s = divmod(num, 60)
        h, m = divmod(m, 60)
        return zip((h, m, s), ("h", "m", "s"))

    def minus(self):
        self.controller.countdown -= 1
        if self.controller.countdown < 0:
            self.controller.timerTempStop.emit()
            #print("finished one")
            cdQueue.put(1)
            return
        time = dict(self.convert(self.controller.countdown))
        self.controller.timeChanged.emit(
            self.controller.type_, self.getPercent(), time
        )
