import time

from pywinauto import WindowSpecification
from pywinauto.controls.uiawrapper import UIAWrapper
from pywinauto.controls.uia_controls import ToolbarWrapper

from framework.service.base_window import WindowInterface
from framework.service.elements import statusbar, titlebar


class MainWindow(WindowInterface):
    """Реализация главного окна приложения Адепт: УС"""
    # идентификаторы для запуска окон в главном окне приложения
    cost_summary = {'title': "Создать сводку затрат", 'control_type': "MenuItem"}
    create_folder = {'title': "Создать папку", 'control_type': "MenuItem"}

    def __init__(self):
        super(MainWindow, self).__init__(
            titlebar_=titlebar.DefaultTitlebar(),
            statusbar_=statusbar.DefaultStatusbar(),
        )

    def menu(self) -> UIAWrapper:
        """Возвращает меню"""
        return self.top_window_().child_window(
            title='Общее', control_type="MenuItem").parent().parent()

    def toolbar(self) -> ToolbarWrapper:
        """Возвращает панель инструментов"""
        return self.top_window_().child_window(title="Создать", control_type="Button").parent()

    def titlebar(self):
        return self._titlebar.titlebar(self.top_window_())

    def statusbar(self):
        return self._statusbar.statusbar()

    def __main_window(self) -> WindowSpecification:
        """Подключение к главному окну (верхний процесс в диспетчере задач)"""
        return self._connect().Dialog

    def launch_window_in_menu(self, name_window: dict) -> None:
        """Запуск окна (любого) через главное меню"""
        self.menu().menu_select('Общее->Создать')
        time.sleep(self.timeout / 2)
        self.__main_window().child_window(**name_window).click_input()
        time.sleep(self.timeout)

    def launch_window_in_toolbar(self, name_window) -> None:
        """Запуск окна (любого) через панель инструментов"""
        self.toolbar().button('Создать').click_input()
        time.sleep(self.timeout * 2)
        self.__main_window().child_window(**name_window).click_input()
        time.sleep(self.timeout)
