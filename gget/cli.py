import click
from os import getcwd
from os.path import join
from dotenv import load_dotenv
from ._get_remote_file import get_remote_file

# Load the environment variables from current working directory
load_dotenv(join(getcwd(), ".env"))


@click.command()
@click.argument("path", required=True)
@click.argument("destination", required=False)
@click.option(
    "--repo",
    "repo",
    envvar="GGET_REPO",
    help=(
        "The repo to get the file from. "
        "You can also set the GGET_REPO environment variable to set this option."
    ),
)
@click.option(
    "--from",
    "from_",
    help="Alias for --repo",
)
@click.option(
    "--owner",
    envvar="GGET_OWNER",
    required=True,
    help=(
        "The owner of the repo to get the file from. "
        "You can also set the GGET_OWNER environment variable to set this option."
    ),
)
@click.option(
    "--provider",
    envvar="GGET_PROVIDER",
    default="github",
    type=click.Choice(["github"]),
    help=(
        "The remote repository provider to get the file from. Defaults to github. "
        "Currently, only github is supported. "
        "You can set the GGET_PROVIDER environment variable to set this option. "
    ),
)
@click.option(
    "--token",
    help=(
        "The token to use to authenticate with the remote repository provider"
        "Since the program only supports github as the provider, "
        "this option is personal access token in context of github. "
        "You can set this option using the GITHUB_PAT environment variable."
    ),
)
@click.option(
    "--ref",
    envvar="GGET_REF",
    default="HEAD",
    help=(
        "Branch or commit to get the file from. Defaults to HEAD. "
        "You can set the GGET_REF environment variable to set this option."
    ),
)
def cli(
    path,
    destination,
    repo,
    from_,
    owner,
    provider,
    token,
    ref,
):
    """Get a file from a remote git repository

    Arguments:
        PATH: The path on the remote repository to get the file from
        DESTINATION: The path to save the file to. Defaults to the same as the path.
    """

    # Options validation
    reponame = from_ or repo
    if reponame is None:
        raise click.UsageError("Either --repo or --from must be provided")

    # Run the get_remote_file function
    get_remote_file(
        path=path,
        reponame=reponame,
        owner=owner,
        output=destination or path,
        provider=provider,
        provider_options={"token": token},
        ref=ref,
    )
