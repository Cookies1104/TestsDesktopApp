from abc import ABC, abstractmethod

from pywinauto import WindowSpecification


class TitlebarInterface(ABC):
    """Интерфейс для titlebar разных окон приложения Адепт: УС"""

    @abstractmethod
    def titlebar(self, current_window: WindowSpecification):
        pass


class NotTitlebar(TitlebarInterface):
    """Реализация titlebar для окон, где оно отсутствует"""
    def titlebar(self, current_window: WindowSpecification):
        return None


class DefaultTitlebar(TitlebarInterface):
    """Стандартная реализация titlebar"""
    def titlebar(self, current_window: WindowSpecification):
        return current_window.TitleBar
