# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spec_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class SpecForm(object):
    def setupUi(self, SpecForm):
        SpecForm.setObjectName("SpecForm")
        SpecForm.resize(603, 350)
        SpecForm.setMinimumSize(QtCore.QSize(603, 350))
        SpecForm.setMaximumSize(QtCore.QSize(603, 350))
        self.gridLayout_2 = QtWidgets.QGridLayout(SpecForm)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(SpecForm)
        self.frame.setMinimumSize(QtCore.QSize(585, 332))
        self.frame.setMaximumSize(QtCore.QSize(585, 332))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.organization_label = QtWidgets.QLabel(self.frame)
        self.organization_label.setMinimumSize(QtCore.QSize(153, 22))
        self.organization_label.setMaximumSize(QtCore.QSize(153, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.organization_label.setFont(font)
        self.organization_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.organization_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.organization_label.setObjectName("organization_label")
        self.gridLayout.addWidget(self.organization_label, 0, 0, 1, 1)
        self.organization_cbox = QtWidgets.QComboBox(self.frame)
        self.organization_cbox.setEnabled(True)
        self.organization_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.organization_cbox.setMaximumSize(QtCore.QSize(400, 23))
        self.organization_cbox.setEditable(True)
        self.organization_cbox.setObjectName("organization_cbox")
        self.gridLayout.addWidget(self.organization_cbox, 0, 1, 1, 1)
        self.contractor_label = QtWidgets.QLabel(self.frame)
        self.contractor_label.setMinimumSize(QtCore.QSize(153, 22))
        self.contractor_label.setMaximumSize(QtCore.QSize(153, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contractor_label.setFont(font)
        self.contractor_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.contractor_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.contractor_label.setObjectName("contractor_label")
        self.gridLayout.addWidget(self.contractor_label, 1, 0, 1, 1)
        self.contractor_cbox = QtWidgets.QComboBox(self.frame)
        self.contractor_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.contractor_cbox.setMaximumSize(QtCore.QSize(400, 23))
        self.contractor_cbox.setEditable(True)
        self.contractor_cbox.setObjectName("contractor_cbox")
        self.gridLayout.addWidget(self.contractor_cbox, 1, 1, 1, 1)
        self.project_label = QtWidgets.QLabel(self.frame)
        self.project_label.setMinimumSize(QtCore.QSize(153, 22))
        self.project_label.setMaximumSize(QtCore.QSize(153, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.project_label.setFont(font)
        self.project_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.project_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.project_label.setObjectName("project_label")
        self.gridLayout.addWidget(self.project_label, 2, 0, 1, 1)
        self.project_cbox = QtWidgets.QComboBox(self.frame)
        self.project_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.project_cbox.setMaximumSize(QtCore.QSize(400, 23))
        self.project_cbox.setEditable(True)
        self.project_cbox.setObjectName("project_cbox")
        self.gridLayout.addWidget(self.project_cbox, 2, 1, 1, 1)
        self.contract_label = QtWidgets.QLabel(self.frame)
        self.contract_label.setMinimumSize(QtCore.QSize(153, 22))
        self.contract_label.setMaximumSize(QtCore.QSize(153, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_label.setFont(font)
        self.contract_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.contract_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.contract_label.setObjectName("contract_label")
        self.gridLayout.addWidget(self.contract_label, 3, 0, 1, 1)
        self.contract_cbox = QtWidgets.QComboBox(self.frame)
        self.contract_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.contract_cbox.setMaximumSize(QtCore.QSize(400, 23))
        self.contract_cbox.setEditable(True)
        self.contract_cbox.setObjectName("contract_cbox")
        self.gridLayout.addWidget(self.contract_cbox, 3, 1, 1, 1)
        self.work_pack_label = QtWidgets.QLabel(self.frame)
        self.work_pack_label.setMinimumSize(QtCore.QSize(153, 22))
        self.work_pack_label.setMaximumSize(QtCore.QSize(153, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.work_pack_label.setFont(font)
        self.work_pack_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.work_pack_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.work_pack_label.setObjectName("work_pack_label")
        self.gridLayout.addWidget(self.work_pack_label, 4, 0, 1, 1)
        self.work_pack_cbox = QtWidgets.QComboBox(self.frame)
        self.work_pack_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.work_pack_cbox.setMaximumSize(QtCore.QSize(400, 23))
        self.work_pack_cbox.setEditable(True)
        self.work_pack_cbox.setObjectName("work_pack_cbox")
        self.gridLayout.addWidget(self.work_pack_cbox, 4, 1, 1, 1)
        self.spec_label = QtWidgets.QLabel(self.frame)
        self.spec_label.setMinimumSize(QtCore.QSize(153, 22))
        self.spec_label.setMaximumSize(QtCore.QSize(153, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spec_label.setFont(font)
        self.spec_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.spec_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spec_label.setObjectName("spec_label")
        self.gridLayout.addWidget(self.spec_label, 5, 0, 1, 1)
        self.spec_ledit = QtWidgets.QLineEdit(self.frame)
        self.spec_ledit.setMinimumSize(QtCore.QSize(400, 23))
        self.spec_ledit.setMaximumSize(QtCore.QSize(400, 23))
        self.spec_ledit.setObjectName("spec_ledit")
        self.gridLayout.addWidget(self.spec_ledit, 5, 1, 1, 1)
        self.from_date_label = QtWidgets.QLabel(self.frame)
        self.from_date_label.setMinimumSize(QtCore.QSize(153, 22))
        self.from_date_label.setMaximumSize(QtCore.QSize(153, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.from_date_label.setFont(font)
        self.from_date_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.from_date_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.from_date_label.setObjectName("from_date_label")
        self.gridLayout.addWidget(self.from_date_label, 6, 0, 1, 1)
        self.from_date_dateEdit = QtWidgets.QDateEdit(self.frame)
        self.from_date_dateEdit.setMinimumSize(QtCore.QSize(110, 23))
        self.from_date_dateEdit.setMaximumSize(QtCore.QSize(110, 23))
        self.from_date_dateEdit.setCalendarPopup(True)
        self.from_date_dateEdit.setObjectName("from_date_dateEdit")
        self.gridLayout.addWidget(self.from_date_dateEdit, 6, 1, 1, 1)
        self.amount_label = QtWidgets.QLabel(self.frame)
        self.amount_label.setMinimumSize(QtCore.QSize(153, 22))
        self.amount_label.setMaximumSize(QtCore.QSize(153, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.amount_label.setFont(font)
        self.amount_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.amount_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.amount_label.setObjectName("amount_label")
        self.gridLayout.addWidget(self.amount_label, 7, 0, 1, 1)
        self.amount_ledit = QtWidgets.QLineEdit(self.frame)
        self.amount_ledit.setMinimumSize(QtCore.QSize(400, 23))
        self.amount_ledit.setMaximumSize(QtCore.QSize(400, 23))
        self.amount_ledit.setObjectName("amount_ledit")
        self.gridLayout.addWidget(self.amount_ledit, 7, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
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
        self.gridLayout.addLayout(self.button_hlayout, 9, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(SpecForm)
        QtCore.QMetaObject.connectSlotsByName(SpecForm)

    def retranslateUi(self, SpecForm):
        _translate = QtCore.QCoreApplication.translate
        SpecForm.setWindowTitle(_translate("SpecForm", "Добавление спецификации"))
        self.organization_label.setText(_translate("SpecForm", "Застройщик"))
        self.contractor_label.setText(_translate("SpecForm", "Контрагент"))
        self.project_label.setText(_translate("SpecForm", "Проект"))
        self.contract_label.setText(_translate("SpecForm", "Номер договора"))
        self.work_pack_label.setText(_translate("SpecForm", "Пакет работ"))
        self.spec_label.setText(_translate("SpecForm", "Номер спецификации"))
        self.from_date_label.setText(_translate("SpecForm", "От"))
        self.amount_label.setText(_translate("SpecForm", "Сумма спецификации"))
        self.save_button.setText(_translate("SpecForm", "Записать и закрыть"))
        self.cancel_button.setText(_translate("SpecForm", "Отмена"))
