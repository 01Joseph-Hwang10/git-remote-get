import requests
from typing import TypeAlias
from dataclasses import dataclass
from github.Repository import Repository
from github.ContentFile import ContentFile
from .._dirent import File, Directory


@dataclass
class GithubFile(File):
    repo: Repository
    ref: str
    file: ContentFile

    @staticmethod
    def from_remote_file(
        remote_file: ContentFile,
        repo: Repository,
        ref: str,
    ) -> "GithubFile":
        return GithubFile(
            name=remote_file.name,
            path=remote_file.path,
            repo=repo,
            ref=ref,
            file=remote_file,
        )

    def get_contents(self) -> str | bytes:
        # Decode the file contents
        # or fetch the file contents from `download_url`
        file_contents = None
        if len(self.file.content) > 0:
            file_contents = self.file.decoded_content
        else:
            file_contents = requests.get(self.file.download_url).content
        return file_contents


@dataclass
class GithubDirectory(Directory):
    repo: Repository
    ref: str
    directory: ContentFile

    @staticmethod
    def from_remote_file(
        remote_file: ContentFile,
        repo: Repository,
        ref: str,
    ) -> "GithubDirectory":
        return GithubDirectory(
            name=remote_file.name,
            path=remote_file.path,
            repo=repo,
            ref=ref,
            directory=remote_file,
        )

    def get_children(
        self,
        recursive: bool = False,
    ) -> list["GithubDirent"]:
        remote_files: list[ContentFile] = self.repo.get_contents(
            self.path,
            ref=self.ref,
        )
        dirents = []
        for remote_file in remote_files:
            # Case #1: Content is a file
            if remote_file.type == "file":
                dirents.append(
                    GithubFile.from_remote_file(
                        remote_file,
                        repo=self.repo,
                        ref=self.ref,
                    )
                )
                continue

            directory: GithubDirectory = GithubDirectory.from_remote_file(
                remote_file,
                repo=self.repo,
                ref=self.ref,
            )

            # Case #2: Content is a directory,
            # and recursive search is disabled
            dirents.append(directory)

            # Case #3: Content is a directory,
            # and recursive search is enabled
            if recursive:
                dirents.extend(directory.get_children(recursive))

        return dirents


GithubDirent: TypeAlias = GithubFile | GithubDirectory
