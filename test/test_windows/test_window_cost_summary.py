import time
import pytest
from pywinauto import ElementNotFoundError
from pywinauto.controls.uia_controls import EditWrapper, ListItemWrapper

from framework.service.window_cost_summary import CostSummary


class TestWindowCostSummary:
    """Тесты окна 'Сводка затрат'"""
    @pytest.mark.positive
    @pytest.mark.parametrize(
        'name_field,text', [
            (CostSummary.field_number, '555'),
            (CostSummary.field_create_date, '12.05.2022'),
            (CostSummary.field_situation, 'Сейчас'),
            (CostSummary.field_object, 'Объект'),
            (CostSummary.field_customer, 'Заказчик'),
            (CostSummary.field_approved, '12.05.2022'),
            (CostSummary.field_approval_document, 'приказ'),
        ]
    )
    def test_positive_entry_for_fields_in_window_cost_summary(
            self, window_cost_summary_in_menu, name_field, text,
    ):
        """Позитивный тест текстовых полей в окне сводка затрат"""
        field: EditWrapper = window_cost_summary_in_menu.get_edit_field(name_field)
        field.set_text(text)

        text_error = f'Позитивный тест текстового поля {name_field} в окне "Сводка затрат"'
        assert field.is_visible(), text_error + '. Поле не видно'
        assert field.is_editable(), text_error + '. Поле не редактируется'
        assert text == field.get_value(), text_error

    @pytest.mark.positive
    def test_positive_entry_for_rounding_of_values_field_in_window_cost_summary(
            self, window_cost_summary_in_menu
    ):
        """Позитивный тест выпадающего списка "Округление стоимостей до"
        в окне "Сводка затрат"."""
        combobox = window_cost_summary_in_menu.get_combobox_rounding_of_values()

        value_ = '0'
        if combobox.selected_text() == value_:
            value_ = '5'

        combobox.select(f'{value_}')
        time.sleep(window_cost_summary_in_menu.timeout)

        text_error = 'Позитивный тест выпадающего списка "Округление ' \
                     'стоимостей до" в окне "Сводка затрат"'

        assert combobox.is_visible(),\
            text_error + '. Не видно'
        assert not combobox.is_editable(),\
            text_error + '. Является редактируемым клавиатурой (не правильно)'
        assert value_ == combobox.selected_text(),\
            text_error + '. Не удалось установить значение'
        assert CostSummary.list_rounding_of_values == combobox.texts(),\
            text_error + '. Не соответствие элементов в списке'

    @pytest.mark.postive
    def test_elements_in_window_cost_summary(self, window_cost_summary_in_menu):
        """Тест списка элементов в окне 'Сводка затрат'"""
        text_error = 'Элементы в окне "Сводка затрат" не соответствуют'
        assert window_cost_summary_in_menu.get_elements().texts() == CostSummary.list_elements,\
            text_error

    @pytest.mark.positive
    @pytest.mark.parametrize(
        'element',
        [
            CostSummary.element_general,
            CostSummary.element_signatures
        ],
    )
    def test_element_in_window_cost_summary(self, window_cost_summary_in_menu, element):
        """Тест элементов в окне 'Сводка затрат'"""
        element_window: ListItemWrapper = window_cost_summary_in_menu.top_window_(
            ).child_window(**element)

        text_error = f'Элемент {element["title"]} в окне "Сводка затрат" '
        element_window.select()
        assert element_window.is_visible(), text_error + 'не виден'
        assert element_window.is_selected(), text_error + 'не возможно выбрать'
        assert element_window.is_keyboard_focusable(), text_error + 'не возможно выбрать' \
                                                                    'клавиатурой'

    @pytest.mark.positive
    def test_transition_in_signatures_section_in_window_cost_summary(
            self, signatures_section_in_window_cost_summary
    ):
        """Тест перехода в раздел 'Подписи' в окне 'Сводка затрат'."""
        assert signatures_section_in_window_cost_summary.get_workspace_signatures(), \
            'Переключение в окно "Подписи" в окне "Сводка затрат" не произошло'

    @pytest.mark.positive
    @pytest.mark.parametrize(
        'identifier,name', [
            (CostSummary.button_add, CostSummary.button_add['title']),
            (CostSummary.button_del, CostSummary.button_del['title']),
            (CostSummary.button_save_signatures, CostSummary.button_save_signatures['title']),
            (CostSummary.button_download, CostSummary.button_download['title']),
            (CostSummary.button_clear, CostSummary.button_clear['title']),
        ]
    )
    def test_buttons_in_signatures_section_in_window_cost_summary(
            self, signatures_section_in_window_cost_summary, identifier, name
    ):
        """Тест кнопок рабочего пространства раздела 'Подписи' окна 'Сводка затрат'"""
        workspace = signatures_section_in_window_cost_summary.get_workspace_signatures()
        try:
            button = workspace.child_window(**identifier)
        except ElementNotFoundError:
            button = None
        assert button, f'Кнопка {name} не существует раздела "Подписи" в окне "Сводка затрат" не ' \
                       f'существует'
        assert button.window_text() == name, f'Текст кнопки {name} раздела "Подписи" в окне' \
                                             f'"Сводка затрат" не соответствует'

    @pytest.mark.positive
    def test_roots_tree_in_signatures_section_in_window_cost_summary(
            self, signatures_section_in_window_cost_summary
    ):
        """Тест корневых элементов дерева в workspace раздела 'Подписи' в окне 'Сводка затрат'"""
        tree = signatures_section_in_window_cost_summary.get_tree_for_workspace_signatures()

        assert tree.roots()
