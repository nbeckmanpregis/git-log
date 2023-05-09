from git import Repo
import os
import time
import sys


repo = Repo(os.getcwd())

repo.git.checkout('main')



def select_commit():
    fifty_first_commits = list(repo.iter_commits("master", max_count=50))

    print("Commits: \n ", fifty_first_commits)
    n = int(input("Which commit would you like to ammend? (select the index from the list provided)"))
    print("Commit data:\n")
    print("authored time: ", fifty_first_commits[n].authored_datetime)
    print("commited time: ",fifty_first_commits[n].committed_datetime)
    print("commit message: ", fifty_first_commits[n].message)
    commit = fifty_first_commits[n].hexsha
    print("commit hash: ", commit)
    print("\n\n")

    com = input("press enter to continue, or type 'quit' to exit the program, or type 'dif' to select a different commit\n")
    if com == "quit":
        sys.exit()
    if com == "dif":
        return select_commit()
    return commit


commit = select_commit()
os.system("git rebase " + commit + "^ -i")

os.system("git commit --amend")

if(input("Press y to push changes")[0] == 'y'):
    os.system("git merge")
    os.system("git push")
else:
    os.system("git rebase --abort")
