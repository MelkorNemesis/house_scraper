from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self, host, path):
        self.host = host
        self.path = path

    @abstractmethod
    def get_items(self):
        pass

    def get_url(self, path):
        return self.host + path
