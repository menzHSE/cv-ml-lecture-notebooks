# Markus Enzweiler, markus.enzweiler@hs-esslingen.de

import os
import sys
import subprocess

def clone(repo_url, repo_target_dir, verbose=1):
    
    # Check if the directory already exists using the absolute path
    if os.path.exists(repo_target_dir):
        if verbose:
            print(f"Repository {repo_target_dir} exists. Resetting to HEAD...")
        # reset to head
        reset_to_head_cmd(repo_target_dir)
    else:
        if verbose:
            print(f"Cloning repository {repo_url} ...")
        # Clone the repository if it doesn't exist
        clone_cmd(repo_url, repo_target_dir)
    
    if verbose:
        print(f"Repository {repo_target_dir} is ready.")
        

def clone_cmd(repo_url, repo_target_dir):
    subprocess.run(["git", "clone", repo_url, repo_target_dir])


def reset_to_head_cmd(repo_target_dir): 
    # Fetch the latest changes from the remote
    subprocess.run(["git", "-C", repo_target_dir, "fetch", "origin"])
    # Reset the local branch to the latest commit from the remote
    subprocess.run(["git", "-C", repo_target_dir, "reset", "--hard", "origin/HEAD"])
    