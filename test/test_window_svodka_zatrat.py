import pytest

from time import sleep
from pywinauto.application import WindowSpecification

from .test_main_window import BaseClass
from .test_folder_in_main_window import WindowCreateFolder
from settings import TIMEOUT
from utils import close_window


class WindowSvodkaZatrat(BaseClass, WindowCreateFolder):
    """Окно сводка затрат. Запуск, удаление, изменение, подключение."""
    def _launch_window_svodka_zatrat_in_main_window(self):
        """Запуск окна 'Сводка затрат' через главное меню"""
        self.menu('Общее->Создать')
        sleep(TIMEOUT)
        self.main_window.child_window(title="Создать сваодку затрат", control_type="MenuItem").click_input()

    def _connect_window_svodka_zatrat(self) -> WindowSpecification:
        """Подключение к окну сводка затрат"""
        return self._create_app().connect(title_re='Сводка затрат').top_window()


class TestSvodkaZatratInMainWindow:
    """Функциональные тесты папки в главном окне"""
    @pytest.fixture()
    def main_window(self):
        return WindowSvodkaZatrat()

    def test_launch_window_svodka_zatrat_in_main_window(self, main_window):
        """Запуск окна 'Сводка затрат' через главное меню"""
        main_window._launch_window_svodka_zatrat_in_main_window()  # Запускаем окно 'Сводка затрат' через главное меню
        sleep(TIMEOUT)
        window_svodka_zatrat = main_window._connect_window_svodka_zatrat()

        assert 'Сводка затрат' in str(window_svodka_zatrat.wrapper_object())
        assert  window_svodka_zatrat.exists()

        close_window(window_svodka_zatrat)

