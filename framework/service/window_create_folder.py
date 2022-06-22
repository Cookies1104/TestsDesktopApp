from pywinauto import WindowSpecification

from .base_window import WindowInterface
from .elements import statusbar, titlebar


class CreateFolder(WindowInterface):
    def __init__(self):
        super(CreateFolder, self).__init__(
            titlebar_=titlebar.DefaultTitlebar(),
            statusbar_=statusbar.DefaultStatusbar(),
            )

    def titlebar(self):
        pass

    def statusbar(self):
        pass
