from pywinauto.controls.uia_controls import ComboBoxWrapper, ListItemWrapper, \
    ListViewWrapper, TreeViewWrapper
from pywinauto.controls.uiawrapper import UIAWrapper
from pywinauto import WindowSpecification, Application

from .base_window import WindowInterface
from framework.elements import statusbar, titlebar


class CostSummary(WindowInterface):
    """Элементы окна 'Сводка затрат'."""
    # идентификаторы полей
    # ----------------------------------------------------------------------------------------------
    # Общие идентификаторы для всех разделов в окне "Сводка затрат"
    list_elements = [['Общие'], ['Подписи']]
    element_general = {'title': 'Общие', 'control_type': 'ListItem'}
    element_signatures = {'title': 'Подписи', 'control_type': 'ListItem'}
    # ----------------------------------------------------------------------------------------------
    # Идентификаторы для раздела "Общие" в окне "Сводка затрат"
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
    # ----------------------------------------------------------------------------------------------
    # Идентификаторы для раздела "Подписи" в окне "Сводка затрат"
    list_buttons_in_workspace_signatures = [
        '', 'Добавить', 'Удалить', 'Сохранить', 'Загрузить', 'Очистить'
    ]
    button_add = {'title': 'Добавить', 'control_type': 'Button'}
    button_del = {'title': 'Удалить', 'control_type': 'Button'}
    button_save_signatures = {'title': 'Сохранить', 'control_type': 'Button'}
    button_download = {'title': 'Загрузить', 'control_type': 'Button'}
    button_clear = {'title': 'Очистить', 'control_type': 'Button'}
    tree_for_workspace_signatures = 'Сводка затратTreeView'

    def __init__(self, app_: Application):
        super(CostSummary, self).__init__(
            titlebar_=titlebar.DefaultTitlebar(),
            statusbar_=statusbar.DefaultStatusbar(),
            )
        self.app = app_

    # ----------------------------------------------------------------------------------------------
    # Общие методы для всех разделов в окне "Сводка затрат"
    def titlebar(self):
        pass

    def statusbar(self):
        pass

    def connect_(self, **kwargs):
        """Подключение к окну сводка затрат"""
        if kwargs:
            return super(CostSummary, self).connect_(**kwargs)
        return super(CostSummary, self).connect_(title_re='Сводка затрат')

    def get_elements(self) -> ListViewWrapper:
        """Возвращает окно элементов"""
        return self.connect_()['Сводка затратListBox']

    def get_element_general(self) -> ListItemWrapper:
        """Возвращает элемент 'Общие' (кликабелен)"""
        return self.get_elements().child_window(**CostSummary.element_general)

    def get_element_signatures(self) -> ListItemWrapper:
        """Возвращает элемент 'Подписи' (кликабелен)"""
        return self.get_elements().child_window(**CostSummary.element_signatures)

    # ----------------------------------------------------------------------------------------------
    # Методы для работы с разделом "Общие" в окне "Сводка затрат"
    def get_combobox_rounding_of_values(self) -> ComboBoxWrapper:
        """Возвращает выпадающий список Округление стоимостей до"""
        return self.connect_()[CostSummary.combobox_rounding_of_values]

    def get_workspace_general(self) -> UIAWrapper | WindowSpecification:
        """Возвращает workspace для раздела общие"""
        return self.connect_().child_window(title="Номер:", control_type="Text").parent()

    # -------------------------------------------------------------------.---------------------------
    # Методы для работы с разделом "Подписи" в окне "Сводка затрат"
    def get_workspace_signatures(self) -> UIAWrapper | WindowSpecification:
        """Возвращает workspace раздела подписи"""
        return self.connect_()['Сводка затратGroupBox4']

    def get_tree_for_workspace_signatures(self) -> TreeViewWrapper:
        """Возвращает дерево workspace раздела подписи"""
        return self.connect_()[CostSummary.tree_for_workspace_signatures]
