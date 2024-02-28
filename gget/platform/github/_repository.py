from github.Repository import Repository
from github.ContentFile import ContentFile
from .._repository import GitRepository
from ._dirent import GithubFile, GithubDirectory, GithubDirent


class GithubRepository(GitRepository):
    def __init__(
        self,
        repo: Repository,
    ):
        self.repo = repo

    def _get_content(
        self,
        content: ContentFile,
        ref: str,
    ) -> GithubDirent:
        return (
            GithubDirectory.from_remote_file(
                remote_file=content,
                repo=self.repo,
                ref=ref,
            )
            if content.type == "dir"
            else GithubFile.from_remote_file(
                remote_file=content,
                repo=self.repo,
                ref=ref,
            )
        )

    def get_contents(
        self,
        path: str,
        ref: str,
    ) -> list[GithubDirent] | GithubDirent:
        contents = self.repo.get_contents(path, ref=ref)
        if isinstance(contents, list):
            return [self._get_content(content, ref=ref) for content in contents]
        else:
            return self._get_content(contents, ref=ref)
