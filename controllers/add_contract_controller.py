from PyQt5 import QtWidgets, QtCore
from gui.contract_widget import ContractForm
from controllers.widget_controller import WidgetForm


class AddContractForm(ContractForm, WidgetForm):
    def __init__(self):
        super(AddContractForm, self).__init__()
        self.setupUi(self)

        self.save_button.clicked.connect(self.save)
        self.cancel_button.clicked.connect(self.hide_widget)

