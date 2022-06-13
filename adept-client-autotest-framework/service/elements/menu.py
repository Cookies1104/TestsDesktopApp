from abc import ABC, abstractmethod
from pywinauto import WindowSpecification


class MenuInterface(ABC):
    """Интерфейс для меню разных окон приложения Адепт: УС"""
    def __init__(self, current_window: WindowSpecification):
        self._window = current_window

    @abstractmethod
    def menu(self):
        pass


class NotMenu(MenuInterface):
    """Реализация меню для окон, где оно отсутствует"""
    def menu(self):
        return None


class MenuMainWindow(MenuInterface):
    """Реализация меню для главного окна"""
    def menu(self):
        return self._window.child_window(title='Общее', control_type="MenuItem").parent().parent()
