import pytest

from framework.windows.main_window import MainWindow
from framework.windows.window_create_folder import CreateFolder
from framework.windows.window_cost_summary import CostSummary


class TestLaunchWindowsInMainWindow:
    """Тесты по запуску всех окон для главного окна приложения"""
    @pytest.mark.positive
    @pytest.mark.parametrize(
        'name_window,title', [
            (MainWindow.create_folder, 'Создание папки'),
            (MainWindow.create_subfolder, 'Создание подпапки'),
            (MainWindow.create_object, 'Создать стройку'),
            (MainWindow.create_estimate, 'Локальная смета'),
            (MainWindow.create_object_estimate, 'Объектная смета'),
            (MainWindow.create_summary_estimate, 'Сводная смета'),
            (MainWindow.create_cost_summary, 'Сводка затрат'),
            (MainWindow.create_calculation, 'Калькуляция'),
        ]
    )
    def test_launch_windows_in_menu(self, main_window, name_window: dict, title):
        """Тест запуска окон через меню (Общее->Создать->...) главного окна приложения"""
        main_window.launch_window_in_menu(name_window)
        window = MainWindow().top_window_()

        text_error = f'Запуск окна "{title}" через меню провалился'

        assert window.exists() and title in str(window.wrapper_object()), text_error
        assert window.is_visible() and window.is_enabled(), text_error

        window.close()
