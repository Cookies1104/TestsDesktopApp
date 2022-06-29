import pytest
import time

from pywinauto import keyboard

from framework.windows.login_window import LoginWindow
from framework.windows.main_window import MainWindow
from framework.windows.window_cost_summary import CostSummary
from framework.windows.window_create_folder import CreateFolder
from settings import TIMEOUT


def launch_login_window() -> LoginWindow:
    """Запуск окна входа и закрытие приложение"""
    window = LoginWindow()
    window.run_app()
    return window


def launch_main_window() -> MainWindow:
    """Запуск главного окна"""
    login_window = launch_login_window()
    login_window.get_button_login().click()
    window = MainWindow(app_=login_window.app)
    window.connect_()
    return window


@pytest.fixture(scope='class')
def login_window_for_class() -> LoginWindow:
    window = launch_login_window()
    yield window
    window.close_app()


@pytest.fixture(scope='class')
def main_window_for_class() -> MainWindow:
    """Запуск главного окна"""
    window = launch_main_window()
    yield window
    window.close_app()


@pytest.fixture(scope='class')
def window_create_folder_in_menu(main_window_for_class) -> CreateFolder:
    main_window_for_class.launch_context_menu_for_creating_entities_in_menu(
        MainWindow.create_folder)
    window = CreateFolder(app_=main_window_for_class.app)
    window.connect_()
    return window


@pytest.fixture(scope='class')
def window_cost_summary_in_menu(main_window_for_class) -> CostSummary:
    """Запуск окна 'Сводка затрат' через главное меню"""
    main_window_for_class.launch_context_menu_for_creating_entities_in_menu(
        MainWindow.create_cost_summary)
    window = CostSummary(app_=main_window_for_class.app)
    window.connect_()
    return window


@pytest.fixture(scope='class')
def window_cost_summary_in_toolbar(main_window_for_class) -> CostSummary:
    """Запуск окна 'Сводка затрат' через панель инструментов"""
    main_window_for_class.launch_window_in_toolbar(MainWindow.create_cost_summary)
    time.sleep(TIMEOUT)
    window = CostSummary(app_=main_window_for_class.app)
    window.connect_()
    return window


@pytest.fixture(scope='class')
def signatures_section_in_window_cost_summary(window_cost_summary_in_menu) -> CostSummary:
    """Переход в раздел 'Подписи' в окне 'Сводка затрат'"""
    window_cost_summary_in_menu.get_element_signatures().click_input()
    return window_cost_summary_in_menu

