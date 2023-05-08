from git import Repo
import git
import git
import subprocess

rtpath = subprocess.check_output(["git", "rev-parse", "--show-toplevel"])
repo = git.Repo(rtpath.strip())



repo.git.add('--all')