import pytest

from time import sleep
from pywinauto.application import WindowSpecification

from .test_main_window import BaseClass
from .test_folder_in_main_window import WindowCreateFolder
from settings import TIMEOUT
from utils import close_window


class WindowSvodkaZatrat(BaseClass, WindowCreateFolder):
    """���� ������ ������. ������, ��������, ���������, �����������."""
    def _launch_window_svodka_zatrat_in_main_window(self):
        """������ ���� '������ ������' ����� ������� ����"""
        self.menu('�����->�������')
        sleep(TIMEOUT)
        self.main_window.child_window(title="������� ������� ������", control_type="MenuItem").click_input()

    def _connect_window_svodka_zatrat(self) -> WindowSpecification:
        """����������� � ���� ������ ������"""
        return self._create_app().connect(title_re='������ ������').top_window()


class TestSvodkaZatratInMainWindow:
    """�������������� ����� ����� � ������� ����"""
    @pytest.fixture()
    def main_window(self):
        return WindowSvodkaZatrat()

    def test_launch_window_svodka_zatrat_in_main_window(self, main_window):
        """������ ���� '������ ������' ����� ������� ����"""
        main_window._launch_window_svodka_zatrat_in_main_window()  # ��������� ���� '������ ������' ����� ������� ����
        sleep(TIMEOUT)
        window_svodka_zatrat = main_window._connect_window_svodka_zatrat()

        assert '������ ������' in str(window_svodka_zatrat.wrapper_object())
        assert  window_svodka_zatrat.exists()

        close_window(window_svodka_zatrat)

