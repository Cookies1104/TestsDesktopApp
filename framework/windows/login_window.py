from pywinauto.controls.uia_controls import ButtonWrapper

from framework.windows.base_window import WindowInterface
from framework.elements.titlebar import DefaultTitlebar
from framework.elements.statusbar import DefaultStatusbar


class LoginWindow(WindowInterface):
    """Интерфейс реализации окна входа в приложение"""
    # Идентификаторы для окна
    button_login = {'title': "Логин", 'control_type': "Button"}

    def __init__(self):
        super(LoginWindow, self).__init__(
            titlebar_=DefaultTitlebar(),
            statusbar_=DefaultStatusbar(),
            )

    def titlebar(self):
        """Вызов titlebar"""
        return self._titlebar.titlebar(self.connect_())

    def statusbar(self):
        """Вызов statusbar (отсутствует)"""
        return None

    def connect_(self, **kwargs):
        """Подключение к окну входа в приложение"""
        if kwargs:
            return super(LoginWindow, self).connect_(**kwargs)
        return super(LoginWindow, self).connect_(title_re='Соединение с')

    def get_button_login(self) -> ButtonWrapper:
        """Получаем кнопку 'Логин'"""
        return self.connect_().child_window(**LoginWindow.button_login)
