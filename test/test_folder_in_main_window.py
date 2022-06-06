import pytest

from time import sleep
from pywinauto import keyboard
from pywinauto.application import WindowSpecification

from .test_main_window import BaseClass
from settings import TIMEOUT
from utils import close_window


class WindowCreateFolder(BaseClass):
    """Окно создания папки. Запуск, удаление, изменение, подключение."""
    def launch_window_create_folder_in_main_window(self):
        """Запуск окна 'Создание папки' через главное меню"""
        self._menu('Общее->Создать')
        sleep(TIMEOUT)
        self.main_window.child_window(title="Создать папку", control_type="MenuItem").click_input()

    def launch_window_create_folder_in_toolbar(self):
        """Запуск окна 'Создание папки' через панель инструментов. Нужна доработка."""
        self.main_window.child_window(title="Создать", control_type="Button").click()
        sleep(TIMEOUT)
        keyboard.send_keys('{DOWN} {ENTER}')

    def connect_window_create_folder(self) -> WindowSpecification:
        """Подключение к окну создания папки"""
        return self._connect_window(name_window='Создание папки')


class TestFolderInMainWindow:
    """Функциональные тесты запуска окна создания папки в главном окне"""
    @pytest.fixture()
    def main_window(self):
        return WindowCreateFolder()

    def test_create_folder_in_main_window(self, main_window):
        """Запуск окна 'Создание папки' через главное меню"""
        main_window.launch_window_create_folder_in_main_window()  # Запускаем окно 'Создание папки' через главное меню
        sleep(TIMEOUT)
        window_create_folder = main_window.connect_window_create_folder()

        # Проверки соответствия (можно дополнить)
        assert 'Создание папки' in str(window_create_folder.wrapper_object())
        assert window_create_folder.exists()

        close_window(window_create_folder)  # Закрывает процесс окна 'Создание папки'

    def test_create_folder_in_toolbar(self, main_window):
        """Запуск окна 'Создание папки' через панель инструментов"""
        pass

    def test_create_folder_in_tree_toolbar(self, main_window):
        """Запуск окна 'Создание папки' через дерево на панели инструментов"""
        pass