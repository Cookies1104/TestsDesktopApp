from pywinauto.application import WindowSpecification


def close_window(window: WindowSpecification) -> None:
    """Закрытие окна (как процесс в диспетчере задач)"""
    window.wrapper_object().close()


def clear_edit_field(edit_field: WindowSpecification) -> None:
    """Очистка текстового поля"""
    edit_field.type_keys('{HOME} ^a {DEL}')


def get_text_for_edit_field(edit_field: WindowSpecification) -> str:
    """Получение значения в текстовом поле"""
    return edit_field.wrapper_object().get_value()
