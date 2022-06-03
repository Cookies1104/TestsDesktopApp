import time

from pywinauto import keyboard

from TestsAdeptSmeta.tests.test_main_window import TestMainWindow


class TestFolderInMainWindow(TestMainWindow):
    """Функциональные тесты папки в главном окне"""
    def _window_create_folder(self):
        """Окно создания папки"""
        return self._create_app().connect(title='Создание папки').top_window()

    def _test_launch_window_create_folder_v1(self):
        """Проверка открытия окна 'Создание папки' v1"""
        self.menu().menu_select('Общее->Создать')
        time.sleep(0.5)
        keyboard.send_keys('{DOWN} {ENTER}')

    def _test_launch_window_create_folder_v2(self):
        """Проверка открытия окна 'Создание папки' v2"""
        self.main_window.child_window(title="Создать", control_type="Button").wrapper_object().click()

    def test_create_folder(self):
        """Проверка создания папки"""
        self._test_launch_window_create_folder_v1()

        window_create_folder = self._window_create_folder()
        window_create_folder.Edit.type_keys('Папка №1')
        window_create_folder.child_window(title="Сохранить", control_type="Button").wrapper_object().click()

        self._test_launch_window_create_folder_v2()
