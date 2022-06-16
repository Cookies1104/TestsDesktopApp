from pywinauto import WindowSpecification, Application
from time import sleep

from service import login_window, main_window, window_cost_summary
from service.base_window import WindowInterface


class AdeptFacade(object):
    """Фасад для работы с приложением"""
    _instance = None  # для реализации Singleton

    def __new__(cls, *args, **kwargs):
        """Реализация Singleton для фасада."""
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, path_client: str, path_server: str, timeout=0.5):
        """Перечень существующих окон в приложении"""
        self.path_client = path_client
        self.path_server = path_server
        self.timeout = timeout

        self.__current_window = None
        self.__wrapper = None

        self.__login_window = login_window.LoginWindow
        self.__main_window = main_window.MainWindow
        self.__window_cost_summary = window_cost_summary.CostSummary

    @staticmethod
    def __app():
        """Инициализация приложения pywinauto"""
        return Application(backend='uia')

    def run_app(self):
        """Запуск приложение Адепт: УС"""
        try:
            self.get_top_window()
            sleep(self.timeout * 4)
        except:
            self.__app().start(cmd_line=self.path_client)
            sleep(self.timeout * 4)

    def get_wrapper_for_current_window(self) -> WindowInterface:
        """Логика авто выбора обёртки (класса) для работы с разными окнами."""
        windows = {'Адепт': self.__main_window,
                   'Соединение с': self.__login_window,
                   'Сводка затрат': self.__window_cost_summary,
                   }
        title_window = self.__current_window.window_text()

        for keys in windows.keys():
            if keys in title_window:
                wrapper_ = windows[keys]
                break
        return wrapper_(self.__current_window)

    def get_top_window(self) -> WindowSpecification:
        """Подключение к верхнему окну приложения"""
        sleep(self.timeout)
        try:
            self.__current_window = self.__app().connect(title_re='Адепт').top_window()
        except:
            self.__current_window = self.__app().connect(path=self.path_client, title='Dialog').top_window()
        self.__wrapper = self.get_wrapper_for_current_window()

        return self.__current_window

    def close_current_window(self):
        """Закрытие текущего (верхнего) окна как процесс в windows"""
        self.get_top_window().close()
        self.__current_window = None
        self.__wrapper = None
