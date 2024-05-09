import os
from github import Github
from github.Auth import Token
from .._provider import GitProvider
from ._repository import GithubRepository


class GithubProvider(GitProvider):
    def __init__(self, token: str | None = None):
        pat = token or os.environ.get("GITHUB_PAT", None)
        auth = None
        if pat is not None:
            auth = Token(pat)

        self.github = Github(auth=auth)

    def get_repository(self, owner: str, repo: str) -> GithubRepository:
        repo = self.github.get_repo(f"{owner}/{repo}")
        return GithubRepository(repo)
