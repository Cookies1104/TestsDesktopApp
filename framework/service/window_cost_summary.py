from pywinauto.controls.uia_controls import ComboBoxWrapper, ListItemWrapper, \
    ListViewWrapper
from pywinauto.controls.uiawrapper import UIAWrapper

from .base_window import WindowInterface
from .elements import statusbar, titlebar


# идентификаторы полей
field_number = 'Номер:Edit'
field_create_date = 'Дата составления:Edit'
field_situation = 'Составлена в ценах по состоянию на:Edit'
field_object = 'Стройка:Edit'
field_customer = 'Заказчик:Edit'
field_approved = 'Утверждена:Edit'
field_approval_document = 'Документ об утверждении:Edit'

combobox_customer = 'Заказчик:ComboBox'
combobox_rounding_of_values = 'Округление стоимостей доComboBox'
list_rounding_of_values = ['0', '1', '2', '3', '4', '5']


class CostSummary(WindowInterface):
    """Элементы окна 'Сводка затрат'."""
    # идентификаторы полей
    field_number = 'Номер:Edit'
    field_create_date = 'Дата составления:Edit'
    field_situation = 'Составлена в ценах по состоянию на:Edit'
    field_object = 'Стройка:Edit'
    field_customer = 'Заказчик:Edit'
    field_approved = 'Утверждена:Edit'
    field_approval_document = 'Документ об утверждении:Edit'

    combobox_customer = 'Заказчик:ComboBox'
    combobox_rounding_of_values = 'Округление стоимостей доComboBox'
    list_rounding_of_values = ['0', '1', '2', '3', '4', '5']
    list_elements = [['Общие'], ['Подписи']]

    def __init__(self):
        super(CostSummary, self).__init__(
            titlebar_=titlebar.DefaultTitlebar(),
            statusbar_=statusbar.DefaultStatusbar(),
            )

    def get_combobox_rounding_of_values(self) -> ComboBoxWrapper:
        """Возвращает выпадающий список Округление стоимостей до"""
        return self.top_window_()[combobox_rounding_of_values]

    def get_elements(self) -> ListViewWrapper:
        """Возвращает окно элементов"""
        return self.top_window_()['Сводка затратListBox']

    def get_element_general(self) -> ListItemWrapper:
        """Возвращает элемент 'Общие' (кликабелен)"""
        return self.top_window_().child_window(title="Общие", control_type="ListItem")

    def get_workspace_general(self) -> UIAWrapper:
        """Возвращает workspace для окна общие"""
        return self.top_window_().child_window(title="Номер:", control_type="Text").parent()

    def get_element_signatures(self) -> ListItemWrapper:
        """Возвращает элемент 'Подписи' (кликабелен)"""
        return self.top_window_().child_window(title="Подписи", control_type="ListItem")

    def get_workspace_signatures(self) -> UIAWrapper:
        """Возвращает workspace для окна подписи"""
        return self.top_window_().child_window(
            auto_id="AdeptDialog.AdeptDialogFrame", control_type="Custom")

    def titlebar(self):
        pass

    def statusbar(self):
        pass
