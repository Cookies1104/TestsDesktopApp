from abc import ABC, abstractmethod

from pywinauto import WindowSpecification


class WorkspaceInterface(ABC):
    """Интерфейс для рабочего пространства разных окон приложения Адепт: УС"""
    def __init__(self, current_window: WindowSpecification):
        self._window = current_window

    @abstractmethod
    def workspace(self):
        pass


class NotWorkspace(WorkspaceInterface):
    """Реализация рабочего пространства для окон, где оно отсутствует"""
    def workspace(self):
        return None


class WorkspaceMainWindow(WorkspaceInterface):
    """Реализация рабочего пространства для главного окна"""
    def workspace(self):
        return self._window.GroupBox



