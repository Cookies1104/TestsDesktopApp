import time

from pywinauto import keyboard

from .test_folder_in_main_window import TestFolderInMainWindow


class TestSmetaInMainWindow(TestFolderInMainWindow):
    """Функциональные тесты сметы в главном окне"""

    def _window_create_smeta(self):
        """Окно создания сметы"""
        return self._create_app().connect(title='Локальная смета').top_window()

    def _test_launch_window_create_smeta(self):
        """Проверка открытия окна 'Локальная смета'"""
        self.menu().menu_select('Общее->Создать')
        time.sleep(0.5)
        keyboard.send_keys('{DOWN} {DOWN} {DOWN} {DOWN} {ENTER}')

    def test_create_smeta(self):
        """Проверка создания сметы"""
        self._test_launch_window_create_smeta()

        window_create_smeta = self._window_create_smeta()
        window_create_smeta['Наименование сметы:Edit'].type_keys('Смета №1')
        window_create_smeta.child_window(title="Создать", control_type="Button").wrapper_object().click()
