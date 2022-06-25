import pytest
import time

from pywinauto import keyboard

from framework.windows.login_window import LoginWindow
from framework.windows.main_window import MainWindow
from framework.windows.window_cost_summary import CostSummary
from framework.windows.window_create_folder import CreateFolder
from settings import TIMEOUT


@pytest.fixture(scope='session')
def login_window() -> LoginWindow:
    """Запуск окна входа и закрытие приложение"""
    window = LoginWindow()
    window.run_app()
    yield window
    window.close_app()


@pytest.fixture(scope='session')
def main_window(login_window) -> MainWindow:
    """Запуск главного окна"""
    keyboard.send_keys('{ENTER}')
    time.sleep(TIMEOUT)
    window = MainWindow()
    return window


@pytest.fixture(scope='class')
def window_create_folder_in_menu(main_window) -> CreateFolder:
    main_window.launch_window_in_menu(MainWindow.create_folder)
    window = CreateFolder()
    return window


@pytest.fixture(scope='class')
def window_cost_summary_in_menu(main_window) -> CostSummary:
    """Запуск окна 'Сводка затрат' через главное меню"""
    main_window.launch_window_in_menu(MainWindow.create_cost_summary)
    window = CostSummary()
    return window


@pytest.fixture(scope='class')
def window_cost_summary_in_toolbar(main_window) -> CostSummary:
    """Запуск окна 'Сводка затрат' через панель инструментов"""
    main_window.launch_window_in_toolbar(MainWindow.create_cost_summary)
    time.sleep(TIMEOUT)
    window = CostSummary()
    return window


@pytest.fixture(scope='class')
def signatures_section_in_window_cost_summary(window_cost_summary_in_menu) -> CostSummary:
    """Переход в раздел 'Подписи' в окне 'Сводка затрат'"""
    window_cost_summary_in_menu.get_element_signatures().click_input()
    return window_cost_summary_in_menu

