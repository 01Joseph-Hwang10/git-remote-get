from os import makedirs
from os.path import join, dirname
from gget.platform import Dirent, File, Directory


class DirentWriter:
    def write_file(
        self,
        file: File,
        path: str,
    ) -> None:
        makedirs(dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(file.get_contents())

    def write_directory(
        self,
        directory: Directory,
        path: str,
    ) -> None:
        makedirs(path, exist_ok=True)
        self.write_many(directory.get_children(), prefix=path)

    def write(
        self,
        dirent: Dirent,
        path: str,
    ) -> None:
        if isinstance(dirent, File):
            self.write_file(dirent, path)
        elif isinstance(dirent, Directory):
            self.write_directory(dirent, path)
        else:
            raise ValueError(f"Unknown dirent type: {type(dirent)}")

    def write_many(self, dirents: list[Dirent], prefix: str) -> None:
        for dirent in dirents:
            self.write(dirent, join(prefix, dirent.name))
