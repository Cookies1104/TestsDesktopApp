import pytest

from time import sleep
from pywinauto import WindowSpecification

from .test_main_window import BaseClass
from .test_folder_in_main_window import WindowCreateFolder
from settings import TIMEOUT
from utils import close_window


class WindowSvodkaZatrat(WindowCreateFolder):
    """Окно сваодка затрат. Запуск, удаление, изменение, подключение."""
    def launch_window_svodka_zatrat_in_main_window(self):
        """Запуск окна 'Сводка затрат' через главное меню"""
        self._menu('Общее->Создать')
        sleep(TIMEOUT)
        self.main_window.child_window(title="Создать сводку затрат", control_type="MenuItem").click_input()

    def connect_window_svodka_zatrat(self) -> WindowSpecification:
        """Подключение к окну сводка затрат"""
        return self._connect_window(name_window='Сводка затрат')


class TestSvodkaZatratInMainWindow:
    """Функциональные тесты запуска окна сводка затрат в главном окне"""
    @pytest.fixture()
    def main_window(self):
        return WindowSvodkaZatrat()

    def test_launch_window_svodka_zatrat_in_main_window(self, main_window):
        """Запуск окна 'Сводка затрат' через главное меню"""
        main_window.launch_window_svodka_zatrat_in_main_window()
        sleep(TIMEOUT)
        window_svodka_zatrat = main_window.connect_window_svodka_zatrat()

        assert 'Сводка затрат' in str(window_svodka_zatrat.wrapper_object())
        assert window_svodka_zatrat.exists()

        close_window(window_svodka_zatrat)

    def test_launch_window_svodka_zatrat_in_toolbar(self, main_window):
        """Запуск окна 'Сводка затрат' через панель инструментов"""
        pass

    def test_launch_window_svodka_zatrat_in_tree_toolbar(self, main_window):
        """Запуск окна 'Сводка затрат' через дерево на панели инструментов"""
        pass



