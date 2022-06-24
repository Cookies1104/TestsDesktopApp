class TestLaunchWindowsInMainWindow:
    """Тесты по запуску всех окон для главного окна приложения"""
    def test_launch_window_cost_summary_in_menu(self, window_cost_summary_in_menu):
        """Тест запуска окна 'Сводка затрат' через меню главного окна приложения"""
        window = window_cost_summary_in_menu

        text_error = 'Запуск окна сводки затрат через меню провалился'
        assert window.top_window_().is_visible() and window.top_window_().is_enabled(), \
            text_error
        assert window.top_window_().exists() and 'Сводка затрат' in str(window.top_window_(
        ).wrapper_object()), text_error

        window.close_current_window()

    def test_launch_window_create_folder_in_menu(self, window_create_folder_in_menu):
        """Тест запуска окна 'Создание папки' через меню главного окна приложения"""
        window = window_create_folder_in_menu

        text_error = 'Запуск окна создание папки через меню провалился'
        assert window.top_window_().is_visible() and window.top_window_().is_enabled(), \
            text_error
        assert window.top_window_().exists() and 'Создание папки' in str(window.top_window_(
        ).wrapper_object()), text_error

        window.close_current_window()
