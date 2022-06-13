from abc import ABC, abstractmethod
from pywinauto import WindowSpecification

from .elements import menu, statusbar, titlebar, workspace


class WindowInterface(ABC):
    """Интерфейс для реализации окон клиента Адепт"""
    def __init__(self,
                 window: WindowSpecification,
                 menu_: menu.MenuInterface,
                 workspace_: workspace.WorkspaceInterface,
                 titlebar_: titlebar.TitlebarInterface,
                 statusbar_: statusbar.StatusbarInterface,
                 ):
        self.window = window

        self._menu = menu_
        self._workspace = workspace_
        self._titlebar = titlebar_
        self._statusbar = statusbar_

    @abstractmethod
    def menu(self):
        pass

    @abstractmethod
    def workspace(self):
        pass

    @abstractmethod
    def titlebar(self):
        pass

    @abstractmethod
    def statusbar(self):
        pass
