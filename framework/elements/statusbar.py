from abc import ABC, abstractmethod


class StatusbarInterface(ABC):
    """Интерфейс для меню разных окон приложения Адепт: УС"""
    @abstractmethod
    def statusbar(self):
        pass


class NotStatusbar(StatusbarInterface):
    """Реализация statusbar для окон, где оно отсутствует"""
    def statusbar(self):
        return None


class DefaultStatusbar(StatusbarInterface):
    """Стандартная реализация statusbar"""
    def statusbar(self):
        return None
