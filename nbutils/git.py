# Markus Enzweiler, markus.enzweiler@hs-esslingen.de

import os

from nbutils import exec as nb_exec


def clone(repo_url, repo_target_dir, on_colab, verbose=True):
    # Check if the directory already exists using the absolute path
    if os.path.exists(repo_target_dir):
        if verbose:
            print(f"Repository {repo_target_dir} exists. Resetting to HEAD...")
        # reset to head
        reset_to_head_cmd(repo_target_dir, on_colab)
    else:
        if verbose:
            print(f"Cloning repository {repo_url} ...")
        # Clone the repository if it doesn't exist
        clone_cmd(repo_url, repo_target_dir, on_colab)

    if verbose:
        print(f"Repository {repo_target_dir} is ready.")


def clone_cmd(repo_url, repo_target_dir, on_colab):
    command = ["git", "clone", repo_url, repo_target_dir]
    nb_exec.executeCommand(command, on_colab)


def reset_to_head_cmd(repo_target_dir, on_colab):
    # Fetch the latest changes from the remote
    command = ["git", "-C", repo_target_dir, "fetch", "origin"]
    nb_exec.executeCommand(command, on_colab)

    # Reset the local branch to the latest commit from the remote
    command = ["git", "-C", repo_target_dir, "reset", "--hard", "origin/HEAD"]
    nb_exec.executeCommand(command, on_colab)
