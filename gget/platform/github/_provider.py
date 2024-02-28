import os
from github import Github
from github.Auth import Token
from .._provider import GitProvider
from ._repository import GithubRepository


class GithubProvider(GitProvider):
    def __init__(self, token: str = None):
        pat = token or os.environ.get("GITHUB_PAT", None)
        if pat is None:
            raise ValueError("GITHUB_PAT environment variable is not defined")

        self.github = Github(auth=Token(pat))

    def get_repository(self, owner: str, repo: str) -> GithubRepository:
        repo = self.github.get_repo(f"{owner}/{repo}")
        return GithubRepository(repo)
