from pywinauto import Application, WindowSpecification
from time import sleep

from pywinauto.findwindows import ElementNotFoundError

import settings


class BaseWindow(WindowSpecification):
    """"""
    def __init__(self, title_re: str, run_window_func, timeout=settings.TIMEOUT):
        self.timeout = timeout
        self.allow_magic_lookup = True
        try:
            self._connect_app(title_re=title_re)
        except ElementNotFoundError:
            run_window_func()
            self._connect_app(title_re=title_re)

        super(BaseWindow, self).__init__(search_criteria={'title_re': title_re, 'backend': settings.BACKEND},
                                         allow_magic_lookup=True)

    def __app(self):
        """"""
        return Application(settings.BACKEND)

    def _connect_app(self, title_re: str) -> WindowSpecification:
        """"""
        sleep(self.timeout)
        return self.__app().connect(title_re=f'{title_re}').top_window()

    def close_window(self, window: WindowSpecification) -> None:
        """Закрытие окна (как процесс в диспетчере задач)"""
        window.wrapper_object().close()
