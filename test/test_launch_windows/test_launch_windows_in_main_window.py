import pytest

from framework.service.main_window import MainWindow
from framework.service.window_create_folder import CreateFolder
from framework.service.window_cost_summary import CostSummary


class TestLaunchWindowsInMainWindow:
    """Тесты по запуску всех окон для главного окна приложения"""
    @pytest.mark.positive
    @pytest.mark.parametrize(
        'name_window,obj,title', [
            (MainWindow.create_folder, CreateFolder, 'Создание папки'),
            (MainWindow.cost_summary, CostSummary, 'Сводка затрат'),
        ]
    )
    def test_launch_windows_in_menu(self, main_window, name_window: dict, obj, title):
        """Тест запуска окон через меню (Общее->Создать->...) главного окна приложения"""
        main_window.launch_window_in_menu(name_window)
        window = obj().top_window_()

        text_error = f'Запуск окна "{title}" через меню провалился'
        assert window.is_visible() and window.is_enabled(), text_error
        assert window.exists() and title in str(window.wrapper_object()), text_error

        window.close()
