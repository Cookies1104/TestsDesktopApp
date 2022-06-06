import time

from pywinauto import Desktop, keyboard
from pywinauto.application import Application, ProcessNotFoundError, WindowSpecification

import settings


class BaseClass:
    """Инициализация приложения. Подключение к основным элементам главного окна."""
    def __init__(self):
        """backend 'win32' для более старых приложений и 'uia' для новее. Адепт смета имеет интерфейс uia"""
        self.path = settings.PATH
        self.backend = settings.BACKEND
        try:
            self.main_window = self._connect_main_window()
        except ProcessNotFoundError:
            self._start_main_window()
            self.main_window = self._connect_main_window()
        print('Инициализация главного окна')

    def _create_app(self):
        """Создание приложения"""
        return Application(backend=self.backend)

    # def _create_desktop(self):
    #     """Создание окна рабочего стола"""
    #     return Desktop(backend=self.backend)

    def _start_main_window(self):
        """Запуск приложения Адепт:УС"""
        self._create_app().start(cmd_line=r'{}'.format(self.path))
        time.sleep(1)
        keyboard.send_keys('{ENTER}')

    def _connect_main_window(self) -> WindowSpecification:
        """Подключение к главному окну"""
        app_ = self._create_app().connect(path=r'{}'.format(self.path), title='Dialog')
        main_window = app_.Dialog
        main_window.set_focus()
        main_window.wait('active')
        return main_window

    def _menu(self, path: str) -> None:
        """Подключение к меню главного окна"""
        self.main_window.GroupBox8.menu_select(path)

    def toolbar(self):
        """Подключение к панели инструментов главного окна"""
        return self.main_window.child_window(auto_id="MainWindowUI.centralwidget.mainVerticalSplitter.swTopSmetaAndTree.smetaPage.topHorizontalSplitter.leftTopBox", control_type="Custom")

    def _connect_window(self, name_window: str) -> WindowSpecification:
        """Подключение к окну"""
        return self._create_app().connect(title_re=f'{name_window}').top_window()


    def print_identifiers(self):
        """Получение информации о главном окне в нужный момент"""
        return self.main_window.print_control_identifiers()
