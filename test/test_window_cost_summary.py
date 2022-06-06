import pytest

import utils

from time import sleep
from pywinauto import WindowSpecification

from .test_main_window import BaseClass
from .test_folder_in_main_window import WindowCreateFolder
from settings import TIMEOUT


def workspace_in_cost_summary(window_cost_summary) -> WindowSpecification:
    """Подключение к рабочей области окна"""
    return window_cost_summary['Номер:GroupBox2']


class WindowCostSummary(WindowCreateFolder):
    """Окно сваодка затрат. Запуск, удаление, изменение, подключение, поля."""
    def launch_window_cost_summary_in_main_window(self):
        """Запуск окна 'Сводка затрат' через главное меню"""
        self._menu('Общее->Создать')
        sleep(TIMEOUT)
        self.main_window.child_window(title="Создать сводку затрат", control_type="MenuItem").click_input()

    def connect_window_cost_summary(self) -> WindowSpecification:
        """Подключение к окну сводка затрат"""
        return self._connect_window(name_window='Сводка затрат')


class TestCostSummaryInMainWindow:
    """Функциональные тесты запуска окна сводка затрат в главном окне"""
    @pytest.fixture(scope='class')
    def main_window(self):
        return WindowCostSummary()

    def test_launch_window_cost_summary_in_main_window(self, main_window):
        """Запуск окна 'Сводка затрат' через главное меню"""
        main_window.launch_window_cost_summary_in_main_window()
        sleep(TIMEOUT)
        window_cost_summary = main_window.connect_window_cost_summary()

        assert 'Сводка затрат' in str(window_cost_summary.wrapper_object())
        assert window_cost_summary.exists()

        utils.close_window(window_cost_summary)

    def test_launch_window_cost_summary_in_toolbar(self, main_window):
        """Запуск окна 'Сводка затрат' через панель инструментов"""
        pass

    def test_launch_window_cost_summary_in_tree_toolbar(self, main_window):
        """Запуск окна 'Сводка затрат' через дерево на панели инструментов"""
        pass


class TestWindowCostSummary:
    """Функциональные тесты"""

    @pytest.fixture(scope='class')
    def window_cost_summary(self):
        """Предусловия для тестов в классе"""
        main_window = WindowCostSummary()  # используем класс для запуска нужных окон
        main_window.launch_window_cost_summary_in_main_window()  # запуск окна сводка затрат
        window_cost_summary = main_window.connect_window_cost_summary()  # подключение к окну
        yield window_cost_summary
        utils.close_window(window_cost_summary)  # закрытие окна

    @staticmethod
    def connect_entry_field(field_id: str, window: WindowSpecification, text: str):
        workspace = workspace_in_cost_summary(window)
        field = workspace[f'{field_id}']
        utils.clear_edit_field(field)
        field.type_keys(f'{text}')
        sleep(TIMEOUT)
        return field

    def test_positive_entry_for_number_field_in_cost_summary(self, window_cost_summary):
        """Позитивная проверка поля 'Номер' в окне сводка затрат"""
        number_field = workspace_in_cost_summary(window_cost_summary)
        utils.clear_edit_field(number_field.Edit)
        number_field.Edit.type_keys('555')
        sleep(TIMEOUT)

        assert '555' == utils.get_text_for_edit_field(number_field.Edit)

    def test_positive_entry_for_create_date_field_in_cost_summary(self, window_cost_summary):
        """Позитивная проверка поля 'Дата составления' в окне сводка затрат"""
        create_date_field = workspace_in_cost_summary(window_cost_summary)
        utils.clear_edit_field(create_date_field.Edit2)
        create_date_field.Edit2.type_keys('10052022')
        sleep(TIMEOUT)

        assert '10.05.2022' == utils.get_text_for_edit_field(create_date_field.Edit2)

    def test_positive_entry_for_situation_field_in_cost_summary(self, window_cost_summary):
        """Позитивная проверка поля 'Составлена в ценах по состоянию на' в окне сводка затрат"""
        situation_field = workspace_in_cost_summary(window_cost_summary)
        utils.clear_edit_field(situation_field.Edit3)
        situation_field.Edit3.type_keys('Текущий момент', with_spaces=True)
        sleep(TIMEOUT)

        assert 'Текущий момент' == utils.get_text_for_edit_field(situation_field.Edit3)

    def test_positive_entry_for_object_field_in_cost_summary(self, window_cost_summary):
        """Позитивная проверка поля 'Объект' в окне сводка затрат"""
        object_field = workspace_in_cost_summary(window_cost_summary)
        utils.clear_edit_field(object_field.Edit4)
        object_field.Edit4.type_keys('Объект', with_spaces=True)
        sleep(TIMEOUT)

        assert 'Объект' == utils.get_text_for_edit_field(object_field.Edit4)

    def test_positive_entry_for_customer_field_in_cost_summary(self, window_cost_summary):
        """Позитивная проверка поля 'Заказчик' в окне сводка затрат"""
        customer_field = workspace_in_cost_summary(window_cost_summary)
        utils.clear_edit_field(customer_field.Edit5)
        customer_field.Edit5.type_keys('Заказчик', with_spaces=True)
        sleep(TIMEOUT)

        assert 'Заказчик' == utils.get_text_for_edit_field(customer_field.Edit5)


