from typing import AsyncGenerator
from abc import ABC, abstractmethod
from property import Property


class Base(ABC):
    def __init__(self, path):
        self.path = path

    @property
    @abstractmethod
    def host(self):
        """Site host we're scraping"""
        pass

    @abstractmethod
    def get_items(self) -> AsyncGenerator[Property, None]:
        pass

    def get_url(self, path):
        return self.host + path
