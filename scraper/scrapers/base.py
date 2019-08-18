from typing import AsyncGenerator
from abc import ABC, abstractmethod
from scraper.property import Property


class Base(ABC):
    def __init__(self, path):
        self.path = path

    def get_url(self, path):
        return self.hostname + path

    @property
    @abstractmethod
    def hostname(self):
        """Site host we're scraping"""
        pass

    @abstractmethod
    def get_items(self) -> AsyncGenerator[Property, None]:
        pass
