import sys
from time import sleep
from . import image_rc
from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt


class Splasher(QSplashScreen):
    def __init__(self, ctx):
        super(Splasher, self).__init__()
        message_font = QFont()
        message_font.setBold(True)
        message_font.setPointSize(14)
        message_font.setFamily("Consolas")
        self.setFont(message_font)
        pixmap = QPixmap(ctx.get_resource(
            "image/window_image/splash_tomato.png"))
        self.setPixmap(pixmap)
        self.show()
        for i in ([0, 1, 2, 3]):
            self.showMessage(
                f"""Lambol.Alee\nversion {ctx.build_settings["version"]}\nLoading{'.' * i}""", alignment=Qt.AlignCenter|Qt.AlignBottom, color=Qt.white
            )
            sleep(0.25)

    def mousePressEvent(self, evt):
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs):
        pass

    def enterEvent(self, *args, **kwargs):
        pass

    def mouseMoveEvent(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash_window = Splasher()
    app.processEvents()