import time

from pywinauto import Desktop, keyboard
from pywinauto.application import Application, ProcessNotFoundError


class TestMainWindow:
    """Инициализация приложения. Подключение к основным элементам главного окна."""
    def __init__(self, path_: str, backend_='uia'):
        """backend 'win32' для более старых приложений и 'uia' для новее. Адепт смета имеет интерфейс uia"""
        self.path = path_
        self.backend = backend_
        try:
            self.main_window = self._connect_main_window()
        except ProcessNotFoundError:
            self._start_main_window()
            self.main_window = self._connect_main_window()
        print('Инициализация главного окна')

    def _create_app(self):
        """Создание приложения"""
        return Application(backend=self.backend)

    def _create_desktop(self):
        """Создание окна рабочего стола"""
        return Desktop(backend=self.backend)

    def _start_main_window(self):
        """Запуск приложения Адепт:УС"""
        self._create_app().start(cmd_line=r'{}'.format(self.path))
        time.sleep(1)
        keyboard.send_keys('{ENTER}')

    def _connect_main_window(self):
        """Подключение к главному окну"""
        app_ = self._create_app().connect(path=r'{}'.format(self.path), title='Dialog')
        main_window = app_.Dialog
        main_window.set_focus()
        main_window.wait('active')
        return main_window

    def menu(self):
        """Подключение к меню главного окна"""
        return self.main_window.GroupBox8
