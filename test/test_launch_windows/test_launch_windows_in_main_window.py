class TestLaunchWindowsInMainWindow:
    """Тесты по запуску всех окон для главного окна приложения"""
    def test_launch_window_cost_summary_in_menu(self, window_cost_summary_in_menu):
        window = window_cost_summary_in_menu

        assert window.top_window_().exists() and 'Сводка затрат' in str(window.top_window_().wrapper_object()), \
            'Окно "Сводка затрат" не существует'

        window.close_current_window()

    def test_launch_window_create_folder_in_menu(self, window_create_folder_in_menu):
        window = window_create_folder_in_menu

        assert window.top_window_().exists() and 'Создание папки' in str(window.top_window_().wrapper_object()), \
            'Окно "Создание папки" не существует'

        window.close_current_window()
