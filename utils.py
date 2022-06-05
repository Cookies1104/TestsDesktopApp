from pywinauto.application import WindowSpecification


def close_window(window: WindowSpecification) -> None:
    window.wrapper_object().close()
