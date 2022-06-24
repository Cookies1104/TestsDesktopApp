import time
from abc import ABC, abstractmethod
from pywinauto import WindowSpecification, Application
from pywinauto.application import ProcessNotFoundError
from pywinauto.controls.uia_controls import EditWrapper
from pywinauto.findwindows import ElementNotFoundError

from framework.service.elements import statusbar, titlebar
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
        self.path_client = PATH_CLIENT

    @abstractmethod
    def titlebar(self):
        pass

    @abstractmethod
    def statusbar(self):
        pass

    @staticmethod
    def _app() -> Application:
        """Инициализация приложения pywinauto"""
        return Application(backend='uia')

    def _connect(self) -> Application:
        """Подключение к приложению Адепт: УС (основной процесс в диспетчере задач)"""
        try:
            return self._app().connect(title_re='Адепт')
        except ElementNotFoundError:
            return self._app().connect(path=self.path_client, title='Dialog')

    def top_window_(self) -> WindowSpecification:
        """Получение верхнего (активного) окна приложения."""
        window = self._connect().top_window()
        window.wait('ready')
        return window

    def close_current_window(self) -> None:
        """Закрытие текущего (верхнего) окна как процесс в windows.
        Не работает для самого приложения."""
        self.top_window_().close()

    def close_app(self) -> None:
        """Закрытие приложения"""
        while True:
            try:
                self._connect().kill()
            except ElementNotFoundError:
                break
            except ProcessNotFoundError:
                break

    @staticmethod
    def clear_edit_field(field: EditWrapper) -> None:
        """Очистка текстового (даты) поля"""
        field.set_text('')

    def get_edit_field(self, name_field: str):
        """Возвращает редактируемое поле"""
        return self.top_window_()[name_field]

    @staticmethod
    def get_text_for_edit_field(field: EditWrapper) -> str:
        """Получение значения в текстовом поле"""
        return field.get_value()
