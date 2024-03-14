from typing import Literal
from os import getcwd
from os.path import join, isabs
from .platform import get_git_provider
from .writer import DirentWriter


def get_remote_file(
    path: str,
    reponame: str,
    owner: str,
    output: str,
    *,
    provider: Literal["github"] = "github",
    provider_options: dict | None = None,
    ref: str = "HEAD",
):
    """Get a file from a remote repository"""
    # Get git provider according to the specified provider
    git_provider = get_git_provider(
        provider,
        provider_options,
    )

    # Get the file from the remote repository
    repo = git_provider.get_repository(owner, reponame)
    contents = repo.get_contents(path, ref=ref)

    # Resolve full path
    output = join(getcwd(), output) if not isabs(output) else output

    # Write the file to the specified output
    writer = DirentWriter()
    if isinstance(contents, list):
        writer.write_many(contents, output)
    else:
        writer.write(contents, output)
