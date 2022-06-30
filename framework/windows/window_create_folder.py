from pywinauto import Application

from .base_window import WindowInterface
from framework.elements import statusbar, titlebar


class CreateFolder(WindowInterface):
    def __init__(self, app_: Application):
        super(CreateFolder, self).__init__(
            titlebar_=titlebar.DefaultTitlebar(),
            statusbar_=statusbar.DefaultStatusbar(),
            )
        self.app = app_

    def titlebar(self):
        pass

    def statusbar(self):
        pass

    def connect_(self, **kwargs):
        if kwargs:
            return super(CreateFolder, self).connect_(**kwargs)
        return super(CreateFolder, self).connect_(title_re='Создание папки')
