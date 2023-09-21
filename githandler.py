"""
Git Handler - Handles git, so you don't have to!
"""

import git

class GitRepo:
    def __init__(self, repo):
        # Initializes the GitRepo class with a repository
        self.repo = git.Repo(repo)

    def clone(self):
        """
        Clones the repository.

        Returns:
            None
        """
        # Clones the repository
        self.repo.clone()

    def pull(self):
        """
        Pulls the latest changes from the remote repository.
        """
        # Pulls the latest changes from the remote repository
        self.repo.remotes.origin.pull()

    def push(self):
        """
        Pushes the changes in the local repository to the remote repository.

        Parameters:
            None

        Return:
            None
        """
        # Pushes the changes in the local repository to the remote repository
        self.repo.remotes.origin.push()