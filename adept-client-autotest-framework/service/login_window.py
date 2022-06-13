from pywinauto import WindowSpecification

from .base_window import WindowInterface
from .elements import menu, statusbar, titlebar, workspace


class LoginWindow(WindowInterface):
    """Интерфейс реализации окна клиента Адепт"""
    def __init__(self, window: WindowSpecification):
        super(LoginWindow, self).__init__(
            window=window,
            menu_=menu.NotMenu(window),
            workspace_=workspace.NotWorkspace(window),
            titlebar_=titlebar.DefaultTitlebar(window),
            statusbar_=statusbar.DefaultStatusbar(window),
            )

    def menu(self):
        pass

    def workspace(self):
        pass

    def titlebar(self):
        pass

    def statusbar(self):
        pass
