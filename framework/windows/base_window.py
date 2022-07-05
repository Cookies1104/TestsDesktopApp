import time
from abc import ABC, abstractmethod
from pywinauto import WindowSpecification, Application
from pywinauto.application import ProcessNotFoundError
from pywinauto.controls.uia_controls import EditWrapper
from pywinauto.findwindows import ElementNotFoundError

import settings
from framework.elements import statusbar, titlebar
from settings import PATH_CLIENT, TIMEOUT


class WindowInterface(ABC):
    """Интерфейс для реализации окон клиента Адепт"""
    _instance = None  # для реализации Singleton

    def __new__(cls, *args, **kwargs):
        """Реализация Singleton для фасада."""
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self,
                 titlebar_: titlebar.TitlebarInterface,
                 statusbar_: statusbar.StatusbarInterface,
                 timeout=TIMEOUT,
                 ):
        """Инициализация объекта класса"""
        # передаём реализацию titlebar и statusbar
        self._titlebar = titlebar_
        self._statusbar = statusbar_

        # передаём настройки для работы с приложением
        self.timeout = timeout
        self.backend = settings.BACKEND
        self.path_client = PATH_CLIENT
        self.app: Application | None = None

    def __app(self) -> Application:
        """Абстрактное приложение с нужным нам бекэндом"""
        return Application(backend=self.backend)

    def _connect_to_exe_file(self) -> Application:
        """Подключение к приложению Адепт, как к exe файлу"""
        return self.__app().connect(path=self.path_client)

    def close_app(self) -> None:
        """Закрытие приложения через диспетчер задач"""
        while True:
            try:
                self._connect_to_exe_file().kill()
            except (ElementNotFoundError, ProcessNotFoundError):
                break

    def run_app(self) -> None:
        """Запуск приложения"""
        self.close_app()
        self.__app().start(cmd_line=self.path_client)
        self.app = self._connect_to_exe_file()
        self.app.window().wait('ready')

    @abstractmethod
    def titlebar(self):
        pass

    @abstractmethod
    def statusbar(self):
        pass

    @abstractmethod
    def connect_(self, title_re) -> WindowSpecification:
        """Подключение к окну соответствующей сущности"""
        x = 0
        while True:
            try:
                x += 1
                window = self.app.window(title_re=title_re)
                window.wait('ready')
                return window
            except (ElementNotFoundError, TimeoutError):
                if x == 29:
                    self.close_app()
                    break
                time.sleep(self.timeout)

    @staticmethod
    def clear_edit_field(field: EditWrapper) -> None:
        """Очистка текстового (даты) поля"""
        field.set_text('')

    def get_edit_field(self, name_field: str) -> EditWrapper:
        """Возвращает редактируемое поле EditWrapper"""
        return self._connect_to_exe_file().top_window()[name_field]

    @staticmethod
    def get_text_for_edit_field(field: EditWrapper) -> str:
        """Получение значения в текстовом поле"""
        return field.get_value()
