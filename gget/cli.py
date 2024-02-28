import click
from dotenv import load_dotenv
from ._get_remote_file import get_remote_file

# Load the environment variables
load_dotenv()


@click.command()
@click.argument("path", required=True)
@click.argument("destination", required=False)
@click.option(
    "--repo",
    "repo",
    envvar="GGET_REPO",
    help="The repo to get the file from",
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
    help="The owner of the repo to get the file from",
)
@click.option(
    "--provider",
    envvar="GGET_PROVIDER",
    default="github",
    type=click.Choice(["github"]),
    help=(
        "The remote repository provider to get the file from. Defaults to github"
        "Currently, only github is supported"
    ),
)
@click.option(
    "--ref",
    envvar="GGET_REF",
    default="master",
    help="Branch or commit to get the file from. Defaults to master",
)
def cli(path, destination, repo, from_, owner, provider, ref):
    """Get a file from a remote repository

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
        ref=ref,
    )
