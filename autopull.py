#!/usr/bin/env python3

from pathlib import Path
from git import Repo

repo_dir = Path("")


def get_repo():
    try:
        repo = Repo(repo_dir)

    except Exception as err:
        print(f"Path is invalid! -- : {err}")
        repo = None
    print(f"path given: '{repo_dir}'")
    assert repo, "invalid repo path"


def main():
    get_repo()
    print("Nothing here yet")


if __name__ == "__main__":
    main()