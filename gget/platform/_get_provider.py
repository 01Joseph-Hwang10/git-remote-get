from typing import Literal
from ._provider import GitProvider


def get_git_provider(
    provider: Literal["github"],
    provider_options: dict | None = None,
) -> GitProvider:
    if provider == "github":
        from gget.platform.github import GithubProvider

        return GithubProvider(**(provider_options or {}))
    else:
        raise ValueError(f"Provider {provider} is not supported")
