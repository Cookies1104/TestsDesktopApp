import pytest

from time import sleep
from pywinauto import keyboard, WindowSpecification

from .test_folder_in_main_window import WindowCreateFolder
from settings import TIMEOUT
from utils import close_window


class WindowLocalSmeta(WindowCreateFolder):
    """Окно локальная смета. Запуск, удаление, изменение, подключение."""
    def launch_window_local_smeta_in_main_window(self):
        """Запуск окна 'Сводка затрат' через главное меню"""
        self._menu('Общее->Создать')
        sleep(TIMEOUT)
        self.main_window.child_window(title="Создать смету", control_type="MenuItem").click_input()

    def connect_window_local_smeta(self) -> WindowSpecification:
        """Подключение к окну сводка затрат"""
        return self._connect_window(name_window='Локальная смета')


class TestLocalSmetaInMainWindow:
    """Функциональные тесты запуска окна локальной сметы в главном окне"""
    @pytest.fixture()
    def main_window(self):
        return WindowLocalSmeta()

    def test_launch_window_local_smeta_in_main_window(self, main_window):
        """Проверка создания сметы"""
        main_window.launch_window_local_smeta_in_main_window()
        sleep(TIMEOUT)
        window_local_smeta = main_window.connect_window_local_smeta()

        assert 'Локальная смета' in str(window_local_smeta.wrapper_object())
        assert window_local_smeta.exists()

        close_window(window_local_smeta)
