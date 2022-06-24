import time
import pytest
from pywinauto import ElementNotFoundError
from pywinauto.controls.uia_controls import EditWrapper

from framework.service.window_cost_summary import CostSummary


class TestWindowCostSummary:
    """Тесты окна 'Сводка затрат'"""
    @pytest.mark.positive
    @pytest.mark.parametrize(
        'name_field,text,text_error', [
            (CostSummary.field_number, '555', 'Позитивный тест текстового поля "номер" '
                                              'в окне "Сводка затрат"'),
            (CostSummary.field_create_date, '12.05.2022', 'Позитивный тест текстового поля "Дата'
                                                          ' составления" в окне "Сводка затрат"'),
            (CostSummary.field_situation, 'Сейчас',
             'Позитивный тест текстового поля "Составлена в ценах по'
             ' состоянию на" в окне "Сводка затрат"'),
            (CostSummary.field_object, 'Объект', 'Позитивный тест текстового поля "Стройка"'
                                                 ' в окне "Сводка затрат"'),
            (CostSummary.field_customer, 'Заказчик', 'Позитивный тест текстового поля "Заказчик"'
                                                     ' в окне "Сводка затрат"'),
            (CostSummary.field_approved, '12.05.2022', 'Позитивный тест текстового поля '
                                                       '"Утверждена" в окне "Сводка затрат"'),
            (CostSummary.field_approval_document, 'приказ', 'Позитивный тест текстового поля '
                                                            '"Документ об утверждении" в окне'
                                                            ' "Сводка затрат"'),
        ]
    )
    def test_positive_entry_for_fields_in_window_cost_summary(
            self, window_cost_summary_in_menu, name_field, text, text_error,
    ):
        """Позитивный тест текстовых полей в окне сводка затрат"""
        field: EditWrapper = window_cost_summary_in_menu.get_edit_field(name_field)
        field.set_text(text)

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
    def test_buttons_in_signatures_section_in_cost_summary(
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


