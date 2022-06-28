class TestLaunchMainWindow:
    """Тесты по запуску главного окна приложения"""
    def test_launch_main_window(self, main_window_for_class):
        """Тест запуска главного окна приложения"""
        window = main_window_for_class.connect_()

        assert window.exists() and 'Адепт:УC' in str(window.wrapper_object()),\
            'Главное окно не существует'
