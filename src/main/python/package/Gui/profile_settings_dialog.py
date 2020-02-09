# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\profile_settings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_Dialog(object):
    def setupUi(self, ctx, settings_Dialog):
        settings_Dialog.setObjectName("settings_Dialog")
        settings_Dialog.resize(701, 463)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        settings_Dialog.setFont(font)
        settings_Dialog.setStyleSheet("")
        self.container = QtWidgets.QListWidget(settings_Dialog)
        self.container.setGeometry(QtCore.QRect(0, 0, 141, 463))
        self.container.setFocusPolicy(QtCore.Qt.NoFocus)
        self.container.setStyleSheet("QListWidget {\n"
"    background:qlineargradient(spread:pad,x1:1,y1:0,x2:0,y2:0,stop:0 rgb(213,198,175),stop:1 #D5C09E);\nfont-size:25px;\nfont-family:\"Consolas\";\n"
"}\n"
"QListWidget::Item{padding-top:20px; padding-bottom:4px;color:rgb(77,77,77);}\n"
"QListWidget::Item:hover{background:skyblue;}\n"
"QListWidget::item:selected{background:lightgray; color:white;}\n"
"QListWidget::item:selected:!active{border-width:0px; background:lightgreen;}")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Plain)
        self.container.setObjectName("container")
        self.groupBox_pr = QtWidgets.QGroupBox(settings_Dialog)
        self.groupBox_pr.setGeometry(QtCore.QRect(170, 10, 501, 361))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_pr.setFont(font)
        self.groupBox_pr.setStyleSheet("QGroupBox#groupBox_pr, #groupBox2, #groupBox_2 {\n"
"    border-radius: 10px;\n"
"    border: 1px solid #555;\n"
"}\n"
"\n"
"QGroupBox#groupBox_pr::title {\n"
"    border-radius: 10px;\n"
"    border: 1px solid #555;\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: left top;\n"
"}")
        self.groupBox_pr.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_pr.setFlat(False)
        self.groupBox_pr.setObjectName("groupBox_pr")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_pr)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 40, 461, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.work_musicReturn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.work_musicReturn.setEnabled(False)
        self.work_musicReturn.setMinimumSize(QtCore.QSize(25, 25))
        self.work_musicReturn.setMaximumSize(QtCore.QSize(25, 25))
        self.work_musicReturn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.work_musicReturn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ctx.get_resource("image/profile_panel/arrow-return.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.work_musicReturn.setIcon(icon)
        self.work_musicReturn.setObjectName("work_musicReturn")
        self.gridLayout.addWidget(self.work_musicReturn, 4, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.work_musicShow = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.work_musicShow.setStyleSheet(
                "#work_musicShow{background:transparent;}")
        self.work_musicShow.setReadOnly(True)
        self.work_musicShow.name = "work_music"
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_musicShow.sizePolicy().hasHeightForWidth())
        self.work_musicShow.setSizePolicy(sizePolicy)
        self.work_musicShow.setBaseSize(QtCore.QSize(56, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.work_musicShow.setFont(font)
        self.work_musicShow.setText("")
        self.work_musicShow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.work_musicShow.setObjectName("work_musicShow")
        self.horizontalLayout.addWidget(self.work_musicShow)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.workMusicTB = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workMusicTB.sizePolicy().hasHeightForWidth())
        self.workMusicTB.setSizePolicy(sizePolicy)
        self.workMusicTB.setMinimumSize(QtCore.QSize(52, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.workMusicTB.setFont(font)
        self.workMusicTB.setObjectName("workMusicTB")
        self.horizontalLayout.addWidget(self.workMusicTB)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.long_restReturn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.long_restReturn.setEnabled(False)
        self.long_restReturn.setMinimumSize(QtCore.QSize(25, 25))
        self.long_restReturn.setMaximumSize(QtCore.QSize(25, 25))
        self.long_restReturn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.long_restReturn.setText("")
        self.long_restReturn.setIcon(icon)
        self.long_restReturn.setObjectName("long_restReturn")
        self.gridLayout.addWidget(self.long_restReturn, 2, 2, 1, 1)
        self.workEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.workEdit.name = "work"
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workEdit.sizePolicy().hasHeightForWidth())
        self.workEdit.setSizePolicy(sizePolicy)
        self.workEdit.setMinimumSize(QtCore.QSize(150, 27))
        self.workEdit.setMaximumSize(QtCore.QSize(168, 27))
        self.workEdit.setPlaceholderText("i.e. 1h2m3s")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.workEdit.setFont(font)
        self.workEdit.setText("")
        self.workEdit.setMaxLength(9)
        self.workEdit.setDragEnabled(True)
        self.workEdit.setReadOnly(False)
        self.workEdit.setObjectName("workEdit")
        self.gridLayout.addWidget(self.workEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.restReturn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.restReturn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restReturn.sizePolicy().hasHeightForWidth())
        self.restReturn.setSizePolicy(sizePolicy)
        self.restReturn.setMinimumSize(QtCore.QSize(25, 25))
        self.restReturn.setMaximumSize(QtCore.QSize(25, 25))
        self.restReturn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.restReturn.setText("")
        self.restReturn.setIcon(icon)
        self.restReturn.setObjectName("restReturn")
        self.gridLayout.addWidget(self.restReturn, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.restEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.restEdit.name = "rest"
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restEdit.sizePolicy().hasHeightForWidth())
        self.restEdit.setSizePolicy(sizePolicy)
        self.restEdit.setMinimumSize(QtCore.QSize(150, 27))
        self.restEdit.setMaximumSize(QtCore.QSize(168, 27))
        self.restEdit.setPlaceholderText("i.e. 1h2m3s")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.restEdit.setFont(font)
        self.restEdit.setMaxLength(9)
        self.restEdit.setDragEnabled(True)
        self.restEdit.setObjectName("restEdit")
        self.gridLayout.addWidget(self.restEdit, 1, 1, 1, 1)
        self.circle_timesReturn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.circle_timesReturn.setEnabled(False)
        self.circle_timesReturn.setMinimumSize(QtCore.QSize(25, 25))
        self.circle_timesReturn.setMaximumSize(QtCore.QSize(25, 25))
        self.circle_timesReturn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.circle_timesReturn.setText("")
        self.circle_timesReturn.setIcon(icon)
        self.circle_timesReturn.setObjectName("circle_timesReturn")
        self.gridLayout.addWidget(self.circle_timesReturn, 3, 2, 1, 1)
        self.circle_timesEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.circle_timesEdit.name = "circle_times"
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.circle_timesEdit.sizePolicy().hasHeightForWidth())
        self.circle_timesEdit.setSizePolicy(sizePolicy)
        self.circle_timesEdit.setMinimumSize(QtCore.QSize(150, 27))
        self.circle_timesEdit.setMaximumSize(QtCore.QSize(168, 27))
        self.circle_timesEdit.setPlaceholderText("0 to 9")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.circle_timesEdit.setFont(font)
        self.circle_timesEdit.setMaxLength(9)
        self.circle_timesEdit.setObjectName("circle_timesEdit")
        self.gridLayout.addWidget(self.circle_timesEdit, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rest_musicShow = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.rest_musicShow.setStyleSheet(
                "#rest_musicShow{background:transparent;}")
        self.rest_musicShow.setReadOnly(True)
        self.rest_musicShow.name = "rest_music"
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rest_musicShow.sizePolicy().hasHeightForWidth())
        self.rest_musicShow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.rest_musicShow.setFont(font)
        self.rest_musicShow.setText("")
        self.rest_musicShow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rest_musicShow.setObjectName("rest_musicShow")
        self.horizontalLayout_2.addWidget(self.rest_musicShow)
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.restMusicTB = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restMusicTB.sizePolicy().hasHeightForWidth())
        self.restMusicTB.setSizePolicy(sizePolicy)
        self.restMusicTB.setMinimumSize(QtCore.QSize(52, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.restMusicTB.setFont(font)
        self.restMusicTB.setObjectName("restMusicTB")
        self.horizontalLayout_2.addWidget(self.restMusicTB)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)
        self.rest_musicReturn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.rest_musicReturn.setEnabled(False)
        self.rest_musicReturn.setMinimumSize(QtCore.QSize(25, 25))
        self.rest_musicReturn.setMaximumSize(QtCore.QSize(25, 25))
        self.rest_musicReturn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rest_musicReturn.setText("")
        self.rest_musicReturn.setIcon(icon)
        self.rest_musicReturn.setObjectName("rest_musicReturn")
        self.gridLayout.addWidget(self.rest_musicReturn, 5, 2, 1, 1)
        self.long_restEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.long_restEdit.name = "long_rest"
        self.long_restEdit.setMinimumSize(QtCore.QSize(150, 27))
        self.long_restEdit.setMaximumSize(QtCore.QSize(168, 27))
        self.long_restEdit.setPlaceholderText("i.e. 1h2m3s")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.long_restEdit.setFont(font)
        self.long_restEdit.setMaxLength(9)
        self.long_restEdit.setDragEnabled(True)
        self.long_restEdit.setObjectName("long_restEdit")
        self.gridLayout.addWidget(self.long_restEdit, 2, 1, 1, 1)
        self.workReturn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.workReturn.setEnabled(False)
        self.workReturn.setMinimumSize(QtCore.QSize(25, 25))
        self.workReturn.setMaximumSize(QtCore.QSize(25, 25))
        self.workReturn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.workReturn.setText("")
        self.workReturn.setIcon(icon)
        self.workReturn.setObjectName("workReturn")
        self.gridLayout.addWidget(self.workReturn, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.end_musicShow = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.end_musicShow.setStyleSheet(
                "#end_musicShow{background:transparent;}")
        self.end_musicShow.setReadOnly(True)
        self.end_musicShow.name = "end_music"
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_musicShow.sizePolicy().hasHeightForWidth())
        self.end_musicShow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.end_musicShow.setFont(font)
        self.end_musicShow.setText("")
        self.end_musicShow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.end_musicShow.setObjectName("end_musicShow")
        self.horizontalLayout_4.addWidget(self.end_musicShow)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.endMusicTB = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endMusicTB.sizePolicy().hasHeightForWidth())
        self.endMusicTB.setSizePolicy(sizePolicy)
        self.endMusicTB.setMinimumSize(QtCore.QSize(52, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.endMusicTB.setFont(font)
        self.endMusicTB.setObjectName("endMusicTB")
        self.horizontalLayout_4.addWidget(self.endMusicTB)
        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 1, 1, 1)
        self.end_musicReturn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.end_musicReturn.setEnabled(False)
        self.end_musicReturn.setMinimumSize(QtCore.QSize(25, 25))
        self.end_musicReturn.setMaximumSize(QtCore.QSize(25, 25))
        self.end_musicReturn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.end_musicReturn.setText("")
        self.end_musicReturn.setIcon(icon)
        self.end_musicReturn.setObjectName("end_musicReturn")
        self.gridLayout.addWidget(self.end_musicReturn, 6, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 3, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(settings_Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(440, 400, 232, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(settings_Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(170, 400, 211, 42))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.plusButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusButton.sizePolicy().hasHeightForWidth())
        self.plusButton.setSizePolicy(sizePolicy)
        self.plusButton.setMinimumSize(QtCore.QSize(0, 34))
        self.plusButton.setMaximumSize(QtCore.QSize(40, 34))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.plusButton.setFont(font)
        self.plusButton.setStyleSheet("QPushButton#plusButton {\n"
"    border: none;\n"
"}")
        self.plusButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(ctx.get_resource("image/profile_panel/plus-circle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plusButton.setIcon(icon1)
        self.plusButton.setIconSize(QtCore.QSize(32, 32))
        self.plusButton.setObjectName("plusButton")
        self.horizontalLayout_3.addWidget(self.plusButton)
        self.minusButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minusButton.sizePolicy().hasHeightForWidth())
        self.minusButton.setSizePolicy(sizePolicy)
        self.minusButton.setMinimumSize(QtCore.QSize(40, 34))
        self.minusButton.setMaximumSize(QtCore.QSize(40, 34))
        self.minusButton.setStyleSheet("QPushButton#minusButton {\n"
"    border: none;\n"
"}")
        self.minusButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(ctx.get_resource("image/profile_panel/minus-circle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minusButton.setIcon(icon2)
        self.minusButton.setIconSize(QtCore.QSize(32, 32))
        self.minusButton.setObjectName("minusButton")
        self.horizontalLayout_3.addWidget(self.minusButton)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_3)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.saveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.saveButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setMinimumSize(QtCore.QSize(0, 34))
        self.saveButton.setMaximumSize(QtCore.QSize(80, 34))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(ctx.get_resource("image/profile_panel/disk-return.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon3)
        self.saveButton.setIconSize(QtCore.QSize(16, 16))
        self.saveButton.setCheckable(False)
        self.saveButton.setChecked(False)
        self.saveButton.setDefault(False)
        self.saveButton.setFlat(True)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_3.addWidget(self.saveButton)

        self.retranslateUi(settings_Dialog)
        settings_Dialog.setTabOrder(self.workEdit, self.restEdit)
        settings_Dialog.setTabOrder(self.restEdit, self.circle_timesEdit)
        settings_Dialog.setTabOrder(self.circle_timesEdit, self.long_restEdit)
        settings_Dialog.setTabOrder(self.long_restEdit, self.workMusicTB)
        settings_Dialog.setTabOrder(self.workMusicTB, self.restMusicTB)
        settings_Dialog.setTabOrder(self.restMusicTB, self.saveButton)
        settings_Dialog.setTabOrder(self.saveButton, self.plusButton)
        settings_Dialog.setTabOrder(self.plusButton, self.minusButton)
        settings_Dialog.setTabOrder(self.minusButton, self.container)

    def retranslateUi(self, settings_Dialog):
        _translate = QtCore.QCoreApplication.translate
        settings_Dialog.setWindowTitle(_translate("settings_Dialog", "Profile Settings"))
        self.groupBox_pr.setTitle(_translate("settings_Dialog", "Profile"))
        self.label_3.setText(_translate("settings_Dialog", "long rest"))
        self.label_5.setText(_translate("settings_Dialog", "work music"))
        self.label_2.setText(_translate("settings_Dialog", "rest"))
        self.workMusicTB.setText(_translate("settings_Dialog", "..."))
        self.label_4.setText(_translate("settings_Dialog", "circle times"))
        self.label.setText(_translate("settings_Dialog", "work"))
        self.label_6.setText(_translate("settings_Dialog", "rest music"))
        self.restMusicTB.setText(_translate("settings_Dialog", "..."))
        self.label_7.setText(_translate("settings_Dialog", "end music"))
        self.endMusicTB.setText(_translate("settings_Dialog", "..."))
        self.saveButton.setText(_translate("settings_Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settings_Dialog = QtWidgets.QDialog()
    ui = Ui_settings_Dialog()
    ui.setupUi(settings_Dialog)
    settings_Dialog.show()
    sys.exit(app.exec_())
