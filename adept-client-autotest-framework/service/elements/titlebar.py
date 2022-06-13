from abc import ABC, abstractmethod

from pywinauto import WindowSpecification


class TitlebarInterface(ABC):
    """Интерфейс для titlebar разных окон приложения Адепт: УС"""
    def __init__(self, current_window: WindowSpecification):
        self._window = current_window

    @abstractmethod
    def titlebar(self):
        pass


class NotTitlebar(TitlebarInterface):
    """Реализация titlebar для окон, где оно отсутствует"""
    def titlebar(self):
        return None


class DefaultTitlebar(TitlebarInterface):
    """Стандартная реализация titlebar"""
    def titlebar(self):
        return self._window.TitleBar


