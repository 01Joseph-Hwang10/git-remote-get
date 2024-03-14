from shutil import rmtree
from os.path import join, isdir, isfile
from gget import get_remote_file
from dotenv import load_dotenv

_TEST_FILE_DIST_PREFIX = "tests/dist"


def setup_module():
    load_dotenv()


def teardown_module():
    rmtree(
        _TEST_FILE_DIST_PREFIX,
        ignore_errors=True,
    )


def test_gget_file():
    # Run the get_remote_file function
    output = join(_TEST_FILE_DIST_PREFIX, "a.py")
    get_remote_file(
        "jtd_codebuild/__main__.py",
        "jtd-codebuild",
        "01Joseph-Hwang10",
        output,
    )

    # Assert the file exists
    assert isfile(output)

    # TODO: Check if contents are downloaded correctly
    #       with your eyes


def test_gget_folder():
    # Run the get_remote_file function
    output = join(_TEST_FILE_DIST_PREFIX, "some/folder")
    get_remote_file(
        "jtd_codebuild",
        "jtd-codebuild",
        "01Joseph-Hwang10",
        output,
    )

    # Assert the folder exists
    assert isdir(output)

    # TODO: Check if contents are downloaded correctly
    #       with your eyes


def test_gget_binary():
    # Run the get_remote_file function
    # for non human-readable file
    output = join(_TEST_FILE_DIST_PREFIX, "geist-banner.png")
    get_remote_file(
        ".docs/img/geist-banner--dark.png",
        "geist-font",
        "vercel",
        output,
    )

    # Assert the file exists
    assert isfile(output)

    # TODO: Check if contents are downloaded correctly
    #       with your eyes
