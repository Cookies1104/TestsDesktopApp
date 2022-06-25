from time import sleep

from framework.windows.base_window import WindowInterface
from framework.elements.titlebar import DefaultTitlebar
from framework.elements.statusbar import DefaultStatusbar


class LoginWindow(WindowInterface):
    """Интерфейс реализации окна входа в приложение"""
    def __init__(self):
        super(LoginWindow, self).__init__(
            titlebar_=DefaultTitlebar(),
            statusbar_=DefaultStatusbar(),
            )

    def titlebar(self):
        """Вызов titlebar"""
        return self._titlebar.titlebar(self.top_window_())

    def statusbar(self):
        """Вызов statusbar (отсутствует)"""
        return None

    def run_app(self):
        """Запуск приложения"""
        self._app().start(cmd_line=self.path_client)
        sleep(self.timeout * 2)
