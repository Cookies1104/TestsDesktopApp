from pywinauto import WindowSpecification

from .base_window import WindowInterface
from .elements import statusbar, titlebar


class CostSummary(WindowInterface):
    def __init__(self):
        super(CostSummary, self).__init__(
            titlebar_=titlebar.DefaultTitlebar(),
            statusbar_=statusbar.DefaultStatusbar(),
            )

    def workspace(self):
        """Возвращает workspace для окна (текстовые поля)"""
        return self.top_window_().child_window(title="Номер:", control_type="Text").parent()

    def field_number(self):
        """Возвращает редактируемое поля Номера"""
        return self.top_window_()['Номер:Edit']

    def elements(self):
        """Возвращает окно элементов"""
        return self.top_window_().child_window(title="Общие", control_type="ListItem").parent()

    def titlebar(self):
        pass

    def statusbar(self):
        pass
