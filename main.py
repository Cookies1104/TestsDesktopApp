import time

from TestsAdeptSmeta.tests.test_smeta_in_main_window import TestSmetaInMainWindow

if __name__ == '__main__':
    backend = 'uia'
    path = r'C:\Adept\AUS-client\adept_us.exe'

    # Запускаем приложение и выполняем подключение к главному окну
    app = TestSmetaInMainWindow(path, backend)
    time.sleep(1)

    # Тестируем создание папки в главном окне
    app.test_create_folder()
    time.sleep(1)

    # Тестируем создание сметы в главном окне
    app.test_create_smeta()
    time.sleep(1)

    app.print_identifiers()


