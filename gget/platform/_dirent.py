import abc
from typing import TypeAlias
from dataclasses import dataclass


@dataclass
class File(metaclass=abc.ABCMeta):
    name: str
    path: str

    @abc.abstractmethod
    def get_contents(self) -> str | bytes:
        raise NotImplementedError


@dataclass
class Directory(metaclass=abc.ABCMeta):
    name: str
    path: str

    @abc.abstractmethod
    def get_children(self, recursive: bool) -> "list[File | Directory]":
        raise NotImplementedError


Dirent: TypeAlias = File | Directory
