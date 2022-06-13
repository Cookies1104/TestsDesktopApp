from pywinauto import WindowSpecification

from .base_window import WindowInterface
from .elements import menu, statusbar, titlebar, workspace


class MainWindow(WindowInterface):
    """Реализация главного окна приложения Адепт: УС"""
    def __init__(self, window: WindowSpecification):
        super(MainWindow, self).__init__(
            window=window,
            menu_=menu.MenuMainWindow(window),
            workspace_=workspace.WorkspaceMainWindow(window),
            titlebar_=titlebar.DefaultTitlebar(window),
            statusbar_=statusbar.DefaultStatusbar(window),
        )
        self.window = window

    def menu(self):
        return self._menu.menu()

    def titlebar(self):
        return self._titlebar.titlebar()

    def statusbar(self):
        return self._statusbar.statusbar()

    def workspace(self):
        return self._workspace.workspace()
