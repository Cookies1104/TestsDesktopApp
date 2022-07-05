import pytest

from framework.windows.main_window import MainWindow

from pywinauto import keyboard


param = {'argnames': 'name_window,title', 'argvalues': [
            (MainWindow.create_folder, 'Создание папки'),
            (MainWindow.create_subfolder, 'Создание подпапки'),
            (MainWindow.create_object, 'Создать стройку'),
            (MainWindow.create_estimate, 'Локальная смета'),
            (MainWindow.create_object_estimate, 'Объектная смета'),
            (MainWindow.create_summary_estimate, 'Сводная смета'),
            (MainWindow.create_cost_summary, 'Сводка затрат'),
            (MainWindow.create_calculation, 'Калькуляция'),
        ]}


class TestLaunchWindowsInToolbarInMainWindow:
    """Функциональные тесты по запуску всех окон через панель инструментов в главном окне
     приложения"""
    @pytest.mark.positive
    @pytest.mark.parametrize(**param)
    def test_launch_windows_in_toolbar_in_main_window(self, main_window_for_class,
                                                      name_window: dict, title: str):
        """Тест запуска окна через панель инструментов в главном окне приложения"""
        try:
            main_window_for_class.launch_window_in_toolbar(name_window)
            main_window_for_class.check_launch_window_in_main_window(title, 'панель инструментов')
        except Exception:
            keyboard.send_keys('{ESC} {ESC}')


class TestLaunchWindowsInMenuInMainWindow:
    """Функциональные тесты по запуску всех окон через меню в главном окне приложения"""
    @pytest.mark.positive
    @pytest.mark.parametrize(**param)
    def test_launch_windows_in_menu_in_main_window(self, main_window_for_class, name_window,
                                                   title):
        """Тест запуска окна через меню в главном окне приложения"""
        try:
            main_window_for_class.launch_context_menu_for_creating_entities_in_menu(name_window)
            main_window_for_class.check_launch_window_in_main_window(title, 'меню')
        except Exception:
            keyboard.send_keys('{ESC} {ESC}')


class TestLaunchWindowsInTreeInMainWindow:
    """Функциональные тесты по запуску всех окон через дерево в главном окне
     приложения"""
    @pytest.mark.positive
    @pytest.mark.parametrize(**param)
    def test_launch_windows_in_tree_in_main_window(self, main_window_for_function, name_window,
                                                   title):
        """Тест запуска окна через дерево в главном окне приложения"""
        try:
            main_window_for_function.launch_window_in_tree(name_window)
            main_window_for_function.check_launch_window_in_main_window(title, 'дереве')
        except Exception:
            keyboard.send_keys('{ESC} {ESC}')
