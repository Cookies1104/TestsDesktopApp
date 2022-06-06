from pywinauto.application import WindowSpecification


def close_window(window: WindowSpecification) -> None:
    window.wrapper_object().close()


def clear_field(edit_field: WindowSpecification) -> None:
    edit_field.type_keys('{HOME} ^a {DEL}')
