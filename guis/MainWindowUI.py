# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/rainx/dev/qtcreator/new_stock_robot/new_stock_robot/captcha_collect_cli.ui'
#
# Created: Wed Jul 27 17:30:21 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_captcha_collect_cli(object):
    def setupUi(self, captcha_collect_cli):
        captcha_collect_cli.setObjectName("captcha_collect_cli")
        captcha_collect_cli.resize(434, 369)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(captcha_collect_cli.sizePolicy().hasHeightForWidth())
        captcha_collect_cli.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(captcha_collect_cli)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.codeLabel = QtGui.QLabel(self.centralwidget)
        self.codeLabel.setText("")
        self.codeLabel.setObjectName("codeLabel")
        self.verticalLayout.addWidget(self.codeLabel)
        self.lineCode = QtGui.QLineEdit(self.centralwidget)
        self.lineCode.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lineCode.setFont(font)
        self.lineCode.setText("")
        self.lineCode.setObjectName("lineCode")
        self.verticalLayout.addWidget(self.lineCode)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonCancel = QtGui.QPushButton(self.groupBox)
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout_2.addWidget(self.buttonCancel)
        self.buttonOk = QtGui.QPushButton(self.groupBox)
        self.buttonOk.setObjectName("buttonOk")
        self.horizontalLayout_2.addWidget(self.buttonOk)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        captcha_collect_cli.setCentralWidget(self.centralwidget)

        self.retranslateUi(captcha_collect_cli)
        QtCore.QMetaObject.connectSlotsByName(captcha_collect_cli)

    def retranslateUi(self, captcha_collect_cli):
        captcha_collect_cli.setWindowTitle(QtGui.QApplication.translate("captcha_collect_cli", "验证码答案收集", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("captcha_collect_cli", "操作", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancel.setText(QtGui.QApplication.translate("captcha_collect_cli", "取消并跳过（ESC）", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOk.setText(QtGui.QApplication.translate("captcha_collect_cli", "确认（ENTER）", None, QtGui.QApplication.UnicodeUTF8))

