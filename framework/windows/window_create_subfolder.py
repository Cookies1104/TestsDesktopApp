from .base_window import WindowInterface
from framework.elements import statusbar, titlebar


class CreateSubfolder(WindowInterface):
    def __init__(self):
        super(CreateSubfolder, self).__init__(
            titlebar_=titlebar.DefaultTitlebar(),
            statusbar_=statusbar.DefaultStatusbar(),
            )

    def titlebar(self):
        pass

    def statusbar(self):
        pass
