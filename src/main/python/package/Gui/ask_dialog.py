# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ask_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 154)
        Dialog.setWindowTitle("")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 106, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 341, 31))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    font: normal bold 25px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Quick-setting"))
        self.lineEdit.setText(_translate("Dialog", "12m"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "i.e. 1h2m3s"))
        self.label.setText(_translate("Dialog", "Input your long rest time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
