import settings
from window import BaseWindow
from pywinauto import Application, WindowSpecification


# class StartWindow:
#     """"""
#     def __init__(self, title_re: str, run_window_func, timeout=settings.TIMEOUT):
#         try:
#             self.window = self._connect_app(title_re=title_re, timeout=timeout)
#         except:
#             run_window_func()
#             self.window = self._connect_app(title_re=title_re, timeout=timeout)


class LoginWindow:
    def __init__(self):
        self.window = BaseWindow(title_re='Соединение с',
                                  run_window_func=self._launch_login_window,
                                  )
        print('Соединение с окном приложения')
        print(self.window.print_control_identifiers())

    @staticmethod
    def _launch_login_window():
        Application(backend=settings.BACKEND).start(cmd_line=f'{settings.PATH}')


LoginWindow()
