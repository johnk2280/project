# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ProjectForm(object):
    def setupUi(self, ProjectForm):
        ProjectForm.setObjectName("ProjectForm")
        ProjectForm.resize(603, 198)
        ProjectForm.setMinimumSize(QtCore.QSize(603, 198))
        ProjectForm.setMaximumSize(QtCore.QSize(603, 198))
        self.gridLayout_3 = QtWidgets.QGridLayout(ProjectForm)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(ProjectForm)
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
        self.project_ledit = QtWidgets.QLineEdit(self.frame)
        self.project_ledit.setMinimumSize(QtCore.QSize(400, 23))
        self.project_ledit.setMaximumSize(QtCore.QSize(400, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.project_ledit.setFont(font)
        self.project_ledit.setMaxLength(12)
        self.project_ledit.setObjectName("project_ledit")
        self.gridLayout.addWidget(self.project_ledit, 1, 1, 1, 1)
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
        self.organization_cbox.setMinimumSize(QtCore.QSize(400, 23))
        self.organization_cbox.setSizeIncrement(QtCore.QSize(400, 23))
        self.organization_cbox.setEditable(True)
        self.organization_cbox.setObjectName("organization_cbox")
        self.gridLayout.addWidget(self.organization_cbox, 0, 1, 1, 1)
        self.project_label = QtWidgets.QLabel(self.frame)
        self.project_label.setMinimumSize(QtCore.QSize(153, 22))
        self.project_label.setMaximumSize(QtCore.QSize(153, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.project_label.setFont(font)
        self.project_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.project_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.project_label.setObjectName("project_label")
        self.gridLayout.addWidget(self.project_label, 1, 0, 1, 1)
        self.button_hlayout = QtWidgets.QHBoxLayout()
        self.button_hlayout.setContentsMargins(-1, 6, -1, 6)
        self.button_hlayout.setObjectName("button_hlayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_hlayout.addItem(spacerItem)
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
        self.gridLayout.addLayout(self.button_hlayout, 3, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(ProjectForm)
        QtCore.QMetaObject.connectSlotsByName(ProjectForm)

    def retranslateUi(self, ProjectForm):
        _translate = QtCore.QCoreApplication.translate
        ProjectForm.setWindowTitle(_translate("ProjectForm", "Добавление проекта"))
        self.organization_label.setText(_translate("ProjectForm", "Застройщик"))
        self.project_label.setText(_translate("ProjectForm", "Наименование проекта"))
        self.save_button.setText(_translate("ProjectForm", "Записать и закрыть"))
        self.cancel_button.setText(_translate("ProjectForm", "Отмена"))
