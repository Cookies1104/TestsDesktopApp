from abc import ABC, abstractmethod

from pywinauto import WindowSpecification


class StatusbarInterface(ABC):
    """Интерфейс для меню разных окон приложения Адепт: УС"""
    def __init__(self, current_window: WindowSpecification):
        self._window = current_window

    @abstractmethod
    def statusbar(self):
        pass


class NotStatusbar(StatusbarInterface):
    """Реализация statusbar для окон, где оно отсутствует"""
    def statusbar(self):
        return None


class DefaultStatusbar(StatusbarInterface):
    """Стандартная реализация statusbar"""
    def statusbar(self):
        return self._window.StatusBar
