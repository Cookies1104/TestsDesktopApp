from pywinauto.application import Application
from pywinauto import Desktop
import time
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard


class TestAdeptSmeta:
    """Автотесты для десктоп приложения адепты сметы"""

    def __init__(self, path_: str, backend_='uia'):
        """backend 'win32' для более старых приложений и 'uia' для новее. Адепт смета имеет интерфейс uia"""
        self.path = path_
        self.backend = backend_
        self.main_window = self._connect_main_window()
        self.menu = self._menu()

    @staticmethod
    def error_handler(func):
        """Обработка ошибок и логирование"""
        def wrapper(*args, **kwargs):
            try:
                func()
            except Exception:
                print(f'{func.__doc__}')
        return wrapper

    # @error_handler
    def _create_app(self):
        """Создание приложения"""
        return Application(backend=self.backend)

    # @error_handler
    def _create_desktop(self):
        """Создание окна рабочего стола"""
        return Desktop(backend=self.backend)

    # @error_handler
    def _start_main_window(self):
        """Запуск приложения Адепт:УС"""
        self._create_app().start(cmd_line=r'{}'.format(self.path))
        time.sleep(1)
        keyboard.send_keys('{ENTER}')

    # @error_handler
    def _connect_main_window(self):
        """Подключение к главному окну"""
        app_ = self._create_app().connect(path=r'{}'.format(self.path), title='Dialog')
        main_window = app_.Dialog
        main_window.set_focus()
        main_window.wait('active')
        return main_window

    # @error_handler
    def _menu(self):
        """Подключение к меню главного окна"""
        return self.main_window.GroupBox8

    # @error_handler
    def _window_create_folder(self):
        """Окно создания папки"""
        return self._create_app().connect(title='Создание папки').top_window()

    # @error_handler
    def _window_create_smeta(self):
        """Окно создания сметы"""
        return self._create_app().connect(title='Локальная смета').top_window()

    # @error_handler
    def test_launch_window_create_folder(self):
        """Проверка открытия окна 'Создание папки'"""
        self.menu.menu_select('Общее->Создать')
        time.sleep(0.5)
        keyboard.send_keys('{DOWN} {ENTER}')

    # @error_handler
    def test_create_folder(self):
        """Проверка создания папки"""
        self.test_launch_window_create_folder()

        window_create_folder = self._window_create_folder()
        window_create_folder.Edit.type_keys('Папка №1')
        window_create_folder.child_window(title="Сохранить", control_type="Button").wrapper_object().click()

    # @error_handler
    def test_launch_window_create_smeta(self):
        """Проверка открытия окна 'Локальная смета'"""
        self.menu.menu_select('Общее->Создать')
        time.sleep(0.5)
        keyboard.send_keys('{DOWN} {DOWN} {DOWN} {DOWN} {ENTER}')
        # raise Exception

    # @error_handler
    def test_create_smeta(self):
        """Проверка создания сметы"""
        self.test_launch_window_create_smeta()

        window_create_smeta = self._window_create_smeta()
        window_create_smeta.print_control_identifiers()
        raise Exception
        # window_create_smeta.child_window(title="Создать", control_type="Button")

    # @error_handler
    def start_tests(self):
        """Запуск тестов"""
        try:
            main_window = self._connect_main_window()
        except Exception:
            self._start_main_window()
            main_window = self._connect_main_window()

        # main_window.print_control_identifiers(depth=4)
        self.test_create_folder()
        self.test_create_smeta()


if __name__ == '__main__':
    backend = 'uia'
    path = r'C:\Adept\AUS-client\adept_us.exe'

    TestAdeptSmeta(path_=path).start_tests()

