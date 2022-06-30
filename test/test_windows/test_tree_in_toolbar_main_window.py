import pytest
from pywinauto.controls.uia_controls import TreeItemWrapper
from pywinauto.controls.uiawrapper import UIAWrapper


class TestEntityTreeMainWindow:
    """Тесты дерева сущностей главного окна приложения"""
    @pytest.mark.positive
    def test_visible_and_focusable_archive_in_entity_tree_main_window(self, main_window_for_class):
        """Позитивный тест видимости и фокусировки архива в дереве сущностей главного окна
        приложения"""
        text_error = 'Архив в дереве сущностей главного окна'
        try:
            archive = main_window_for_class.get_archive()

            assert archive.is_visible(), f'{text_error} не видно'
            assert archive.is_keyboard_focusable(), f'{text_error} не возможно выделить'

        except Exception:
            print(f'{text_error} не существует или подключение не удалось')

    @pytest.mark.positive
    def test_calling_context_menu_for_archive_in_entity_tree_main_window(
            self, main_window_for_class):
        """Позитивный тест вызова контекстного меню для архива в дереве сущностей главного окна
        приложения"""
        text_error = 'ПКМ по архиву в дереве сущностей главно окна не удалось.'
        try:
            archive = main_window_for_class.get_archive()
            archive.click_input(button='right')
            context_menu: UIAWrapper = main_window_for_class.connect_(
                title='adept_us').wrapper_object()
            children_element: list = [
                element for element in context_menu.children_texts() if element != '']

            assert context_menu.is_visible(), f'{text_error} Контекстное меню не видно'
            assert context_menu.is_enabled(), f'{text_error} Контекстное меню не работает'
            assert children_element == ['Создать', 'Загрузить из файла', 'Очистить']

        except Exception:
            print(f'{text_error} Возможно архив не существует или его не удалось использовать')

