import abc
from ._dirent import Dirent


class GitRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_contents(self, path: str, ref: str) -> list[Dirent] | Dirent:
        pass
