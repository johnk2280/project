# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mechanism_type_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MechTypeForm(object):
    def setupUi(self, MechTypeForm):
        MechTypeForm.setObjectName("MechTypeForm")
        MechTypeForm.resize(603, 198)
        MechTypeForm.setMinimumSize(QtCore.QSize(603, 198))
        MechTypeForm.setMaximumSize(QtCore.QSize(603, 198))
        self.gridLayout_3 = QtWidgets.QGridLayout(MechTypeForm)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(MechTypeForm)
        self.frame.setMinimumSize(QtCore.QSize(585, 180))
        self.frame.setMaximumSize(QtCore.QSize(585, 180))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mechanism_type_ledit = QtWidgets.QLineEdit(self.frame)
        self.mechanism_type_ledit.setMinimumSize(QtCore.QSize(400, 23))
        self.mechanism_type_ledit.setMaximumSize(QtCore.QSize(400, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mechanism_type_ledit.setFont(font)
        self.mechanism_type_ledit.setMaxLength(12)
        self.mechanism_type_ledit.setObjectName("mechanism_type_ledit")
        self.gridLayout.addWidget(self.mechanism_type_ledit, 0, 1, 1, 1)
        self.mechanism_type_label = QtWidgets.QLabel(self.frame)
        self.mechanism_type_label.setMinimumSize(QtCore.QSize(153, 22))
        self.mechanism_type_label.setMaximumSize(QtCore.QSize(153, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mechanism_type_label.setFont(font)
        self.mechanism_type_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mechanism_type_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mechanism_type_label.setObjectName("mechanism_type_label")
        self.gridLayout.addWidget(self.mechanism_type_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.button_hlayout = QtWidgets.QHBoxLayout()
        self.button_hlayout.setContentsMargins(-1, 6, -1, 6)
        self.button_hlayout.setObjectName("button_hlayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_hlayout.addItem(spacerItem1)
        self.save_button = QtWidgets.QPushButton(self.frame)
        self.save_button.setMinimumSize(QtCore.QSize(160, 30))
        self.save_button.setMaximumSize(QtCore.QSize(160, 30))
        self.save_button.setObjectName("save_button")
        self.button_hlayout.addWidget(self.save_button)
        self.cancel_button = QtWidgets.QPushButton(self.frame)
        self.cancel_button.setMinimumSize(QtCore.QSize(160, 30))
        self.cancel_button.setMaximumSize(QtCore.QSize(160, 30))
        self.cancel_button.setObjectName("cancel_button")
        self.button_hlayout.addWidget(self.cancel_button)
        self.gridLayout.addLayout(self.button_hlayout, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(MechTypeForm)
        QtCore.QMetaObject.connectSlotsByName(MechTypeForm)

    def retranslateUi(self, MechTypeForm):
        _translate = QtCore.QCoreApplication.translate
        MechTypeForm.setWindowTitle(_translate("MechTypeForm", "Добавление типа механизма"))
        self.mechanism_type_label.setText(_translate("MechTypeForm", "Тип механизма"))
        self.save_button.setText(_translate("MechTypeForm", "Записать и закрыть"))
        self.cancel_button.setText(_translate("MechTypeForm", "Отмена"))
