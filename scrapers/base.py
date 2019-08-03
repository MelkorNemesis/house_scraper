from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get_items(self):
        pass
