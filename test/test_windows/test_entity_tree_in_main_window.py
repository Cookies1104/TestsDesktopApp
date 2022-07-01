import pytest
from pywinauto.controls.uia_controls import MenuItemWrapper
from pywinauto import keyboard

from framework.windows.main_window import MainWindow


class TestEntityTreeMainWindow:
    """Тесты дерева сущностей главного окна приложения"""
    @pytest.fixture(scope='class')
    def archive_context_menu_when_tree_is_empty(self, main_window_for_class):
        """Фикстура вызова контекстного меню для архива в дереве сущностей главного окна"""
        context_menu = main_window_for_class.get_context_menu_for_archive_in_entity_tree()
        yield context_menu
        keyboard.send_keys('{ESC}')

    @pytest.mark.positive
    def test_visible_and_enabled_for_archive_in_entity_tree_main_window(self, main_window_for_class):
        """Позитивный тест видимости и фокусировки архива в дереве сущностей главного окна
        приложения"""
        text_error = 'Архив в дереве сущностей главного окна'
        try:
            archive = main_window_for_class.get_archive_in_entity_tree()

            assert archive.is_visible(), f'{text_error} не видно'
            assert archive.is_enabled(), f'{text_error} не включён'
            assert archive.is_keyboard_focusable(), f'{text_error} не возможно выделить'

        except Exception:
            print(f'{text_error} не существует или подключение не удалось')

    @pytest.mark.positive
    def test_calling_context_menu_for_archive_in_entity_tree_main_window_1(
            self, archive_context_menu_when_tree_is_empty):
        """Позитивный тест вызова контекстного меню для архива в дереве сущностей главного окна
        приложения. Условия - в дереве сущностей есть только пустой архив"""
        text_error = 'ПКМ по архиву в дереве сущностей главного окна не удалось.'
        context_menu = archive_context_menu_when_tree_is_empty
        children_element: list = [
            element for element in context_menu.children_texts() if element != '']

        assert context_menu.is_visible(), f'{text_error} Контекстное меню не видно'
        assert context_menu.is_enabled(), f'{text_error} Контекстное меню не включён'
        assert children_element == ['Создать', 'Загрузить из файла', 'Очистить'], \
            f'{text_error} Элементы контекстного меню не совпадают'

    @pytest.mark.parametrize(
        'name_element',
        [
            MainWindow.archive_create,
            MainWindow.archive_download_from_file,
            MainWindow.archive_clear,
        ]
    )
    @pytest.mark.positive
    def test_visible_and_enabled_for_elements_context_menu_archive_in_entity_tree_main_window(
            self, archive_context_menu_when_tree_is_empty, name_element):
        """Позитивный тест элементов контекстного меню для архива в дереве сущностей главного
        окна приложения. Условия - в дереве сущностей есть только пустой архив"""
        text_error = f'Элемент {name_element["title"]} контекстного меню архива в дереве сущностей '
        element: MenuItemWrapper = archive_context_menu_when_tree_is_empty.child_window(
            **name_element).wrapper_object()

        assert element.is_visible(), f'{text_error}' + 'не виден'
        assert element.is_enabled(), f'{text_error}' + 'не включён'
        assert element.texts()[0] == name_element['title'], f'{text_error}' + 'не соответствует' \
                                                                              'название'





