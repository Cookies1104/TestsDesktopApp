import time
import pytest

from framework.service import window_cost_summary as wcs


class TestWindowCostSummary:
    """Тесты окна 'Сводка затрат'"""
    @pytest.mark.positive
    @pytest.mark.parametrize(
        'name_field,text,text_error', [
            (wcs.field_number, '555', 'Позитивный тест текстового поля "номер" '
                                      'в окне "Сводка затрат"'),
            (wcs.field_create_date, '12.05.2022', 'Позитивный тест текстового поля '
                                                  '"Дата составления" в окне "Сводка затрат"'),
            (wcs.field_situation, 'Сейчас', 'Позитивный тест текстового поля "Составлена в ценах по'
                                            ' состоянию на" в окне "Сводка затрат"'),
            (wcs.field_object, 'Объект', 'Позитивный тест текстового поля "Стройка"'
                                         ' в окне "Сводка затрат"'),
            (wcs.field_customer, 'Заказчик', 'Позитивный тест текстового поля "Заказчик"'
                                             ' в окне "Сводка затрат"'),
            (wcs.field_approved, '12.05.2022', 'Позитивный тест текстового поля "Утверждена"'
                                               ' в окне "Сводка затрат"'),
            (wcs.field_approval_document, 'приказ', 'Позитивный тест текстового поля "Документ об'
                                                    ' утверждении" в окне "Сводка затрат"'),
        ]
    )
    def test_positive_entry_for_fields_in_cost_summary(self, window_cost_summary_in_menu,
                                                       name_field, text, text_error):
        """Позитивная проверка текстовых полей в окне сводка затрат"""
        window = window_cost_summary_in_menu
        field = window.get_edit_field(name_field)

        window.clear_edit_field(field)
        field.type_keys(text.replace('.', ''))

        assert text == window.get_text_for_edit_field(field), text_error

    @pytest.mark.positive
    def test_positive_entry_for_rounding_of_values_field_in_cost_summary(
            self, window_cost_summary_in_menu
    ):
        """Позитивная проверка выпадающего списка "Округление стоимостей до"
        в окне "Сводка затрат"."""
        combobox = window_cost_summary_in_menu.combobox_rounding_of_values()

        value_ = '0'
        if combobox.selected_text() == value_:
            value_ = '5'

        combobox.select(f'{value_}')
        time.sleep(window_cost_summary_in_menu.timeout)

        text_error = 'Позитивный тест изменения значения выпадающего списка "Округление ' \
                     'стоимостей до" в окне "Сводка затрат"'
        assert value_ == combobox.selected_text(), text_error

    @pytest.mark.positive
    def test_list_elements_for_rounding_of_values_field_in_cost_summary(
            self, window_cost_summary_in_menu
    ):
        """Проверка списка элементов для поля 'Округление стоимостей до' в окне сводка затрат"""
        listbox = window_cost_summary_in_menu.combobox_rounding_of_values()

        text_error = 'Позитивный тест значений выпадающего списка "Округление стоимостей до"' \
                     ' в окне "Сводка затрат"'
        assert wcs.list_rounding_of_values == listbox.texts(), text_error
