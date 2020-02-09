# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, version, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(714, 306)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/window_image/tomato.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(580, 260, 112, 34))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 521, 171))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 161, 171))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(version, Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, version, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About this-Eat Tomatoes！"))
        self.pushButton.setText(_translate("Dialog", "close"))
        self.label.setText(_translate("Dialog", "About Eat tomatoes!"))
        self.label_2.setText(_translate("Dialog", f"<html><head/><body><p><span style=\" font-size:10pt;\">Version </span><span style=\" font-size:10pt; font-weight:600;\">{version} </span></p><p><span style=\" font-size:10pt;\">This program is used to keep you focused.</span></p><p><span style=\" font-size:10pt;\">It is based on the theory of Pomodoro.</span><br/></p><p><span style=\" font-family:\'font/han.otf\',\'PingFang SC\',\'Lantinghei SC\',\'Microsoft Yahei\',\'Hiragino Sans GB\',\'Microsoft Sans Serif\',\'WenQuanYi Micro Hei\',\'sans\'; color:#6e4832; background-color:#f9f5ed;\">Icons by </span><a href=\"http://p.yusukekamiyamane.com/\"><span style=\" font-family:\'font/han.otf\',\'PingFang SC\',\'Lantinghei SC\',\'Microsoft Yahei\',\'Hiragino Sans GB\',\'Microsoft Sans Serif\',\'WenQuanYi Micro Hei\',\'sans\'; text-decoration: underline; color:#4484c2; background-color:#f9f5ed;\">Yusuke Kamiyamane</span></a><span style=\" font-family:\'font/han.otf\',\'PingFang SC\',\'Lantinghei SC\',\'Microsoft Yahei\',\'Hiragino Sans GB\',\'Microsoft Sans Serif\',\'WenQuanYi Micro Hei\',\'sans\'; color:#6e4832; background-color:#f9f5ed;\">.</span></p><p><span style=\" font-family:\'font/han.otf\',\'PingFang SC\',\'Lantinghei SC\',\'Microsoft Yahei\',\'Hiragino Sans GB\',\'Microsoft Sans Serif\',\'WenQuanYi Micro Hei\',\'sans\'; color:#6e4832; background-color:#f9f5ed;\">Licensed under a </span><a href=\"http://creativecommons.org/licenses/by/3.0/\"><span style=\" font-family:\'font/han.otf\',\'PingFang SC\',\'Lantinghei SC\',\'Microsoft Yahei\',\'Hiragino Sans GB\',\'Microsoft Sans Serif\',\'WenQuanYi Micro Hei\',\'sans\'; text-decoration: underline; color:#4484c2; background-color:#f9f5ed;\">Creative Commons Attribution 3.0 License</span></a><span style=\" font-family:\'font/han.otf\',\'PingFang SC\',\'Lantinghei SC\',\'Microsoft Yahei\',\'Hiragino Sans GB\',\'Microsoft Sans Serif\',\'WenQuanYi Micro Hei\',\'sans\'; color:#6e4832; background-color:#f9f5ed;\">.</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/window_image/about_tomato.png\"/></p></body></html>"))
from . import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
