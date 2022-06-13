from pywinauto import WindowSpecification

from .base_window import WindowInterface
from .elements import menu, statusbar, titlebar, workspace


class CostSummary(WindowInterface):
    def __init__(self, window: WindowSpecification):
        super(CostSummary, self).__init__(
            window=window,
            menu_=menu.MenuMainWindow(window),
            workspace_=workspace.WorkspaceMainWindow(window),
            titlebar_=titlebar.DefaultTitlebar(window),
            statusbar_=statusbar.StatusbarInterface(window),
            )

    def menu(self):
        pass

    def workspace(self):
        pass

    def titlebar(self):
        pass

    def statusbar(self):
        pass
