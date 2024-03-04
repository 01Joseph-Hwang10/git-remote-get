# git-remote-get

[![PyPI version](https://badge.fury.io/py/git-remote-get.svg)](https://pypi.org/project/git-remote-get)
[![Testsuite](https://github.com/01Joseph-Hwang10/git-remote-get/workflows/Test%20and%20Lint/badge.svg)](https://github.com/01Joseph-Hwang10/git-remote-get/actions?query=workflow%3A"Test+and+Lint")
[![Python version](https://img.shields.io/pypi/pyversions/git-remote-get.svg)](https://pypi.org/project/git-remote-get)
[![Project Status](https://img.shields.io/pypi/status/git-remote-get.svg)](https://pypi.org/project/git-remote-get/)
[![Supported Interpreters](https://img.shields.io/pypi/implementation/git-remote-get.svg)](https://pypi.org/project/git-remote-get/)
[![License](https://img.shields.io/pypi/l/git-remote-get.svg)](https://github.com/pawelzny/git-remote-get/blob/master/LICENSE)

Download single files or directories from a git remote repository without cloning its entire contents.

## Installation

```bash
pip install git-remote-get
```

## Usage

```bash
Usage: git-remote-get [OPTIONS] PATH [DESTINATION]

  Get a file from a remote git repository

  Arguments:     
    PATH: The path on the remote repository to get the file from
    DESTINATION: The path to save the file to. Defaults to the same as the path.

Options:
  --repo TEXT          The repo to get the file from. You can also set the
                       GGET_REPO environment variable to set this option.
  --from TEXT          Alias for --repo
  --owner TEXT         The owner of the repo to get the file from. You can
                       also set the GGET_OWNER environment variable to set
                       this option.  [required]
  --provider [github]  The remote repository provider to get the file from.
                       Defaults to github. Currently, only github is
                       supported. You can set the GGET_PROVIDER environment
                       variable to set this option.
  --ref TEXT           Branch or commit to get the file from. Defaults to
                       master. You can set the GGET_REF environment variable
                       to set this option.
  --help               Show this message and exit.
```

You can also use the `gget` alias for `git-remote-get`.

## `.env` template

You can create a `.env` file in the root of your project 
to set default options for the program.

```bash
# .env
GGET_OWNER='<your-git-remote-repository-owner-name>'
GGET_REPO='<your-git-remote-repository-name>'
GGET_PROVIDER='github'
GGET_REF='<your-git-remote-repository-branch-or-commit>'
```

## Examples

```bash
# This will download the README file from the octocat/Hello-World repository
# and save it to the current directory with same name
gget README --owner=octocat --repo=Hello-World

# This will download the README file
# and save it to docs/README.md
gget README --owner=octocat --repo=Hello-World docs/README.md

# This will download `examples/tutorial`
# of flask repository and save it to the current directory.
#
# If destination is not provided, the program
# will create a directory with the same name as the PATH.
#
# In other words, you will get `examples/tutorial` directory
# and its contents inside that directory.
gget examples/tutorial --owner=pallets --repo=flask --ref=main

# This will download the `examples/tutorial`
# of flask repository and save it to `tutorial` directory.
#
# In this case, the destination is provided.
# Contents under `examples/tutorial` will be saved to `tutorial-contents` directory.
gget examples/tutorial --owner=pallets --repo=flask --ref=main tutorial-contents
```

## Contributing

Any contribution is welcome! Check out [CONTRIBUTING.md](https://github.com/01Joseph-Hwang10/git-remote-get/blob/master/.github/CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](https://github.com/01Joseph-Hwang10/git-remote-get/blob/master/.github/CODE_OF_CONDUCT.md) for more information on how to get started.

## License

`git-remote-get` is licensed under a [MIT License](https://github.com/01Joseph-Hwang10/git-remote-get/blob/master/LICENSE).
