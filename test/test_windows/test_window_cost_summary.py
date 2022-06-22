import time


class TestWindowCostSummary:
    """Тесты окна 'Сводка затрат'"""
    def test_positive_entry_for_number_field_in_cost_summary(self, window_cost_summary_in_menu):
        """Позитивная проверка поля 'Номер' в окне сводка затрат"""
        window = window_cost_summary_in_menu
        field = window.field_number()
        window.clear_edit_field(field)
        field.type_keys('555')
        time.sleep(window.timeout)

        assert '555' == window.get_text_for_edit_field(field)
