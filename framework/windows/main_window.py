from pywinauto import Application, WindowSpecification
from pywinauto.controls.uiawrapper import UIAWrapper
from pywinauto.controls.uia_controls import ToolbarWrapper, TreeViewWrapper, MenuWrapper, \
    TreeItemWrapper
from pywinauto.findwindows import ElementNotFoundError

from framework.windows.base_window import WindowInterface
from framework.elements import statusbar, titlebar


class MainWindow(WindowInterface):
    """Реализация главного окна приложения Адепт: УС"""
    # идентификаторы для запуска окон в главном окне приложения
    title = 'Адепт:УC'

    # идентификаторы контекстного меню для создания сущностей
    create_folder = {'title': "Создать папку", 'control_type': "MenuItem"}
    create_subfolder = {'title': "Создать подпапку", 'control_type': "MenuItem"}
    create_object = {'title': "Создать стройку", 'control_type': "MenuItem"}
    create_estimate = {'title': "Создать смету", 'control_type': "MenuItem"}
    create_object_estimate = {'title': "Создать Об.смету", 'control_type': "MenuItem"}
    create_summary_estimate = {'title': "Создать Св.смету", 'control_type': "MenuItem"}
    create_cost_summary = {'title': "Создать сводку затрат", 'control_type': "MenuItem"}
    create_calculation = {'title': "Создать калькуляцию", 'control_type': "MenuItem"}

    # идентификаторы контекстного меню при нажатии ПКМ по архиву в дереве сущностей
    archive_create = {'title': "Создать", 'control_type': "MenuItem"}
    archive_download_from_file = {'title': "Загрузить из файла", 'control_type': "MenuItem"}
    archive_clear = {'title': "Очистить", 'control_type': "MenuItem"}

    def __init__(self, app_: Application):
        super(MainWindow, self).__init__(
            titlebar_=titlebar.DefaultTitlebar(),
            statusbar_=statusbar.DefaultStatusbar(),
        )
        self.app = app_

    def titlebar(self):
        return self._titlebar.titlebar(self.connect_())

    def statusbar(self):
        return self._statusbar.statusbar()

    def connect_(self, **kwargs):
        if kwargs:
            return super(MainWindow, self).connect_(**kwargs)
        return super(MainWindow, self).connect_(title_re=MainWindow.title, **kwargs)

    # ----------------------------------------------------------------------------------------------
    # Методы для работы с меню
    def menu(self) -> WindowSpecification | UIAWrapper:
        """Возвращает меню для возможности вызова метода menu_select()"""
        return self.connect_().child_window(
            title='Общее', control_type="MenuItem").parent().parent()

    def launch_context_menu_general_in_menu(self) -> WindowSpecification:
        """Запуск контекстного меню "Общее" через меню"""
        self.connect_()
        self.menu().menu_select('Общее')
        context_menu = self.app.window(title_re=MainWindow.title).child_window(
            title="Поиск элементов", control_type="MenuItem").parent()
        return context_menu

    def launch_context_menu_for_creating_entities_in_menu(self, name_window: dict) -> None:
        """Запуск окна (любого) через главное меню"""
        self.connect_()
        self.menu().menu_select('Общее->Создать')
        context_menu = self.app.window(title_re=MainWindow.title)
        context_menu.child_window(**name_window).click_input()

    # ----------------------------------------------------------------------------------------------
    # Методы для работы с панелью инструментов
    def toolbar(self) -> ToolbarWrapper:
        """Возвращает панель инструментов"""
        return self.connect_().child_window(title="Создать", control_type="Button").parent()

    def launch_context_menu_for_creating_entities_in_toolbar(self) -> WindowSpecification:
        """Запуск контекстного меню создания сущностей в панели инструментов"""
        self.connect_()
        self.toolbar().button('Создать').click_input()
        return self.connect_()

    def launch_window_in_toolbar(self, name_window) -> None:
        """Запуск окна (любого) через панель инструментов"""
        context_menu = self.launch_context_menu_for_creating_entities_in_toolbar()
        context_menu.child_window(**name_window).click_input()

    # ----------------------------------------------------------------------------------------------
    # Методы для работы с деревом сущностей
    def tree(self) -> WindowSpecification | TreeViewWrapper:
        """Возвращает дерево"""
        return self.connect_().child_window(
            auto_id="MainWindowUI.centralwidget.mainVerticalSplitter.swTopSmetaAndTree.smetaPage."
                    "topHorizontalSplitter.leftTopBox", control_type="Custom").TreeView

    def get_archive_in_entity_tree(self) -> WindowSpecification | TreeItemWrapper:
        """Возвращает архив в дереве сущностей"""
        return self.tree().get_item(path=r'\Архив')

    def get_context_menu_for_archive_in_entity_tree(self) -> WindowSpecification | UIAWrapper:
        """Запускает и возвращает контекстное меню для архива в дереве"""
        self.get_archive_in_entity_tree().click_input(button='right')
        return self.connect_(title='adept_us')

    def launch_context_menu_for_tree(self) -> WindowSpecification:
        """Запуск контекстного меню для дерева (ПКМ по средине окна)"""
        self.tree().click_input(button='right')
        return self.connect_()

    def launch_context_menu_for_creating_entities_in_tree(
            self) -> WindowSpecification | MenuWrapper:
        """Запуск контекстного меню создания сущностей через дерево"""
        self.launch_context_menu_for_tree().child_window(
            title="Создать", control_type="MenuItem").click_input()
        context_menu = self.connect_().Menu
        return context_menu

    def launch_window_in_tree(self, name_window) -> None:
        """Запуск окна (любого) через дерево"""
        context_menu = self.launch_context_menu_for_creating_entities_in_tree()
        context_menu.item_by_path(f'{name_window["title"]}').click_input()

    # ----------------------------------------------------------------------------------------------
    # Остальные методы
    def check_launch_window_in_main_window(self, title: str, where: str):
        """Проверка запущенного окна в главном меню"""
        try:
            window = self.connect_()
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


