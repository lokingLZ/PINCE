# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(658, 558)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget_Options = QtWidgets.QListWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_Options.sizePolicy().hasHeightForWidth())
        self.listWidget_Options.setSizePolicy(sizePolicy)
        self.listWidget_Options.setMaximumSize(QtCore.QSize(130, 16777215))
        self.listWidget_Options.setObjectName("listWidget_Options")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Options.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Options.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Options.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Options.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Options.addItem(item)
        self.horizontalLayout_2.addWidget(self.listWidget_Options)
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setMinimumSize(QtCore.QSize(500, 500))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_AutoUpdateAddressTable = QtWidgets.QCheckBox(self.page)
        self.checkBox_AutoUpdateAddressTable.setChecked(True)
        self.checkBox_AutoUpdateAddressTable.setObjectName("checkBox_AutoUpdateAddressTable")
        self.verticalLayout_2.addWidget(self.checkBox_AutoUpdateAddressTable)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.QWidget_UpdateInterval = QtWidgets.QWidget(self.page)
        self.QWidget_UpdateInterval.setObjectName("QWidget_UpdateInterval")
        self.horizontalLayout_UpdateInterval = QtWidgets.QHBoxLayout(self.QWidget_UpdateInterval)
        self.horizontalLayout_UpdateInterval.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_UpdateInterval.setObjectName("horizontalLayout_UpdateInterval")
        self.label = QtWidgets.QLabel(self.QWidget_UpdateInterval)
        self.label.setObjectName("label")
        self.horizontalLayout_UpdateInterval.addWidget(self.label)
        self.lineEdit_UpdateInterval = QtWidgets.QLineEdit(self.QWidget_UpdateInterval)
        self.lineEdit_UpdateInterval.setObjectName("lineEdit_UpdateInterval")
        self.horizontalLayout_UpdateInterval.addWidget(self.lineEdit_UpdateInterval)
        self.label_2 = QtWidgets.QLabel(self.QWidget_UpdateInterval)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_UpdateInterval.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.QWidget_UpdateInterval)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.checkBox_ShowMessageBox = QtWidgets.QCheckBox(self.page)
        self.checkBox_ShowMessageBox.setChecked(True)
        self.checkBox_ShowMessageBox.setObjectName("checkBox_ShowMessageBox")
        self.verticalLayout_5.addWidget(self.checkBox_ShowMessageBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.comboBox_GDBOutputMode = QtWidgets.QComboBox(self.page)
        self.comboBox_GDBOutputMode.setObjectName("comboBox_GDBOutputMode")
        self.horizontalLayout_3.addWidget(self.comboBox_GDBOutputMode)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.listWidget_Functions = QtWidgets.QListWidget(self.page_2)
        self.listWidget_Functions.setObjectName("listWidget_Functions")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Functions.addItem(item)
        self.verticalLayout_4.addWidget(self.listWidget_Functions)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_Hotkey = QtWidgets.QVBoxLayout()
        self.verticalLayout_Hotkey.setObjectName("verticalLayout_Hotkey")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_Hotkey.addWidget(self.label_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_Hotkey)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButton_ClearHotkey = QtWidgets.QPushButton(self.page_2)
        self.pushButton_ClearHotkey.setObjectName("pushButton_ClearHotkey")
        self.horizontalLayout_4.addWidget(self.pushButton_ClearHotkey)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.radioButton_SimpleDLopenCall = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_SimpleDLopenCall.setChecked(True)
        self.radioButton_SimpleDLopenCall.setObjectName("radioButton_SimpleDLopenCall")
        self.verticalLayout_7.addWidget(self.radioButton_SimpleDLopenCall)
        self.radioButton_AdvancedInjection = QtWidgets.QRadioButton(self.page_3)
        self.radioButton_AdvancedInjection.setEnabled(False)
        self.radioButton_AdvancedInjection.setObjectName("radioButton_AdvancedInjection")
        self.verticalLayout_7.addWidget(self.radioButton_AdvancedInjection)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem7)
        self.gridLayout_4.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.checkBox_BringDisassembleToFront = QtWidgets.QCheckBox(self.page_4)
        self.checkBox_BringDisassembleToFront.setChecked(True)
        self.checkBox_BringDisassembleToFront.setObjectName("checkBox_BringDisassembleToFront")
        self.verticalLayout_10.addWidget(self.checkBox_BringDisassembleToFront)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.lineEdit_InstructionsPerScroll = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_InstructionsPerScroll.setObjectName("lineEdit_InstructionsPerScroll")
        self.horizontalLayout_9.addWidget(self.lineEdit_InstructionsPerScroll)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem9)
        self.gridLayout_5.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.page_5)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_14.addWidget(self.label_9)
        self.lineEdit_UserFilesPath = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_UserFilesPath.setObjectName("lineEdit_UserFilesPath")
        self.horizontalLayout_14.addWidget(self.lineEdit_UserFilesPath)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self.pushButton_UserFilesPath = QtWidgets.QPushButton(self.page_5)
        self.pushButton_UserFilesPath.setText("")
        self.pushButton_UserFilesPath.setObjectName("pushButton_UserFilesPath")
        self.horizontalLayout_13.addWidget(self.pushButton_UserFilesPath)
        self.verticalLayout_11.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_101 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_101.setObjectName("horizontalLayout_101")
        self.label_7 = QtWidgets.QLabel(self.page_5)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_101.addWidget(self.label_7)
        self.lineEdit_GDBPath = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_GDBPath.setObjectName("lineEdit_GDBPath")
        self.horizontalLayout_101.addWidget(self.lineEdit_GDBPath)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_101)
        self.pushButton_GDBPath = QtWidgets.QPushButton(self.page_5)
        self.pushButton_GDBPath.setText("")
        self.pushButton_GDBPath.setObjectName("pushButton_GDBPath")
        self.horizontalLayout_11.addWidget(self.pushButton_GDBPath)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem10)
        self.gridLayout_6.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_ResetSettings = QtWidgets.QPushButton(Dialog)
        self.pushButton_ResetSettings.setObjectName("pushButton_ResetSettings")
        self.horizontalLayout.addWidget(self.pushButton_ResetSettings)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(4)
        self.listWidget_Functions.setCurrentRow(-1)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        __sortingEnabled = self.listWidget_Options.isSortingEnabled()
        self.listWidget_Options.setSortingEnabled(False)
        item = self.listWidget_Options.item(0)
        item.setText(_translate("Dialog", "General"))
        item = self.listWidget_Options.item(1)
        item.setText(_translate("Dialog", "Hotkeys"))
        item = self.listWidget_Options.item(2)
        item.setText(_translate("Dialog", "Code Injection"))
        item = self.listWidget_Options.item(3)
        item.setText(_translate("Dialog", "Disassemble"))
        item = self.listWidget_Options.item(4)
        item.setText(_translate("Dialog", "Debug"))
        self.listWidget_Options.setSortingEnabled(__sortingEnabled)
        self.checkBox_AutoUpdateAddressTable.setText(_translate("Dialog", "Auto-update address table"))
        self.label.setText(_translate("Dialog", "Update interval"))
        self.lineEdit_UpdateInterval.setText(_translate("Dialog", "0.5"))
        self.label_2.setText(_translate("Dialog", "sec"))
        self.checkBox_ShowMessageBox.setText(_translate("Dialog", "Show a MessageBox on InferiorRunning and GDBInitialize exceptions"))
        self.label_8.setText(_translate("Dialog", "GDB console output mode"))
        self.label_3.setText(_translate("Dialog", "Functions"))
        __sortingEnabled = self.listWidget_Functions.isSortingEnabled()
        self.listWidget_Functions.setSortingEnabled(False)
        item = self.listWidget_Functions.item(0)
        item.setText(_translate("Dialog", "Pause the process"))
        item = self.listWidget_Functions.item(1)
        item.setText(_translate("Dialog", "Break the process"))
        item = self.listWidget_Functions.item(2)
        item.setText(_translate("Dialog", "Continue the process"))
        self.listWidget_Functions.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("Dialog", "Hotkey"))
        self.pushButton_ClearHotkey.setText(_translate("Dialog", "Clear"))
        self.label_5.setText(_translate("Dialog", "Code injection method:"))
        self.radioButton_SimpleDLopenCall.setText(_translate("Dialog", "Simp&le dlopen call"))
        self.radioButton_AdvancedInjection.setText(_translate("Dialog", "Advanced In&jection"))
        self.checkBox_BringDisassembleToFront.setText(_translate("Dialog", "Bring disassemble screen to front when the inferior is stopped"))
        self.label_6.setText(_translate("Dialog", "Instructions shown per scroll"))
        self.label_9.setText(_translate("Dialog", "PINCE_USER_FILES Path"))
        self.label_7.setText(_translate("Dialog", "GDB Path"))
        self.pushButton_ResetSettings.setText(_translate("Dialog", "Reset Settings"))

