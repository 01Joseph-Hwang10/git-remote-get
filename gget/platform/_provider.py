import abc
from ._repository import GitRepository


class GitProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_repository(self, owner: str, repo: str) -> "GitRepository":
        pass
