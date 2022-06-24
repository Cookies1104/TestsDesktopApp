class TestLaunchLoginWindow:
    """Тесты по запуску окна входа в приложение"""
    def test_launch_login_window(self, login_window):
        """Тест запуска окна входа"""
        window = login_window.top_window_()

        assert window.is_visible() and window.is_enabled(), 'Окно входа не видно или не работает'
        assert window.exists() and 'Соединение с 127.0.0.1:21600' in str(window.wrapper_object()),\
            'Окно входа в приложение не существует'
