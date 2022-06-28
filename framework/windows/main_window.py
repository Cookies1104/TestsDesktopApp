from pywinauto.controls.uiawrapper import UIAWrapper
from pywinauto.controls.uia_controls import ToolbarWrapper, TreeViewWrapper
from pywinauto.findwindows import ElementNotFoundError

from framework.windows.base_window import WindowInterface
from framework.elements import statusbar, titlebar


class MainWindow(WindowInterface):
    """Реализация главного окна приложения Адепт: УС"""
    # идентификаторы для запуска окон в главном окне приложения
    create_folder = {'title': "Создать папку", 'control_type': "MenuItem"}
    create_subfolder = {'title': "Создать подпапку", 'control_type': "MenuItem"}
    create_object = {'title': "Создать стройку", 'control_type': "MenuItem"}
    create_estimate = {'title': "Создать смету", 'control_type': "MenuItem"}
    create_object_estimate = {'title': "Создать Об.смету", 'control_type': "MenuItem"}
    create_summary_estimate = {'title': "Создать Св.смету", 'control_type': "MenuItem"}
    create_cost_summary = {'title': "Создать сводку затрат", 'control_type': "MenuItem"}
    create_calculation = {'title': "Создать калькуляцию", 'control_type': "MenuItem"}

    def __init__(self):
        super(MainWindow, self).__init__(
            titlebar_=titlebar.DefaultTitlebar(),
            statusbar_=statusbar.DefaultStatusbar(),
        )

    def menu(self) -> UIAWrapper:
        """Возвращает меню"""
        return self.connect_().child_window(
            title='Общее', control_type="MenuItem").parent().parent()

    def toolbar(self) -> ToolbarWrapper:
        """Возвращает панель инструментов"""
        return self.connect_().child_window(title="Создать", control_type="Button").parent()

    def tree(self) -> TreeViewWrapper:
        """Возвращает дерево"""
        pass

    def titlebar(self):
        return self._titlebar.titlebar(self.connect_())

    def statusbar(self):
        return self._statusbar.statusbar()

    def connect_(self, title_re='Адепт'):
        return super(MainWindow, self).connect_(title_re)

    def launch_window_in_menu(self, name_window: dict) -> None:
        """Запуск окна (любого) через главное меню"""
        self.menu().menu_select('Общее->Создать')
        self.connect_()
        self._main_window().child_window(**name_window).click_input()

    def launch_window_in_toolbar(self, name_window) -> None:
        """Запуск окна (любого) через панель инструментов"""
        self.toolbar().button('Создать').click_input()
        self.connect_().child_window(**name_window).click_input()

    def launch_window_in_tree(self, name_window) -> None:
        pass

    def check_launch_window_in_main_window(self, title: str, where: str):
        """Проверка запущенного окна в главном меню"""
        try:
            window = self.connect_(title_re=title)
        except ElementNotFoundError:
            window = self._connect_to_exe_file().top_window()

        text_error = f'Запуск окна "{title}" через {where} провалился.'

        if title in str(window.wrapper_object()):
            assert window.is_visible() and window.is_enabled(), text_error
            window.close()
        elif 'Адепт' in str(window.wrapper_object()):
            raise ElementNotFoundError(text_error)
        else:
            window.close()
            raise ElementNotFoundError(text_error + ' Название окна не совпадает.')


