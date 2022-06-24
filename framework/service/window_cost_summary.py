from pywinauto import WindowSpecification
from pywinauto.controls.uia_controls import EditWrapper, ComboBoxWrapper

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
    def __init__(self):
        super(CostSummary, self).__init__(
            titlebar_=titlebar.DefaultTitlebar(),
            statusbar_=statusbar.DefaultStatusbar(),
            )

    def workspace(self) -> WindowSpecification:
        """Возвращает workspace для окна (текстовые поля)"""
        return self.top_window_().child_window(title="Номер:", control_type="Text").parent()

    def field_number(self) -> EditWrapper:
        """Возвращает редактируемое поле Номера"""
        return self.top_window_()[field_number]

    def field_create_date(self) -> EditWrapper:
        """Возвращает редактируемое поле Дата составления"""
        return self.top_window_()[field_create_date]

    def field_situation(self) -> EditWrapper:
        """Возвращает редактируемое поле Составлена в ценах по состоянию на"""
        return self.top_window_()[field_situation]

    def field_object(self) -> EditWrapper:
        """Возвращает редактируемое поле Стройка"""
        return self.top_window_()[field_object]

    def field_customer(self) -> EditWrapper:
        """Возвращает редактируемое поле Заказчик"""
        return self.top_window_()[field_customer]

    def field_approved(self) -> EditWrapper:
        """Возвращает редактируемое поле Утверждена"""
        return self.top_window_()[field_approved]

    def field_approval_document(self) -> EditWrapper:
        """Возвращает редактируемое поле Документ об утверждении"""
        return self.top_window_()[field_approval_document]

    def combobox_rounding_of_values(self) -> ComboBoxWrapper:
        """Возвращает выпадающий список Округление стоимостей до"""
        return self.top_window_()[combobox_rounding_of_values]

    def elements(self):
        """Возвращает окно элементов"""
        return self.top_window_().child_window(title="Общие", control_type="ListItem").parent()

    def titlebar(self):
        pass

    def statusbar(self):
        pass
