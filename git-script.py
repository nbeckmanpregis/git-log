from git import Repo
import os
import time
import sys


repo = Repo(os.getcwd())


def select_commit(repo):
    fifty_first_commits = list(repo.iter_commits("main", max_count=80))
    commit_list = [commit.message + str(commit) for commit in fifty_first_commits]
    commits = [str(x) + ": " + commit_list[x] + '\n' for x in range(len(commit_list))]
    print(*commits, sep = '\n')
    n = int(input("Which commit would you like to ammend? (select the index from the list provided)"))
    print("Commit #", n, " data:\n")
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
        return select_commit(repo)
    return commit


commit = select_commit(repo)
os.system("git rebase " + commit + "^ -i")

os.system("git commit --amend")

if(input("Press y to push changes")[0] == 'y'):
    os.system("git merge")
    os.system("git push")
else:
    os.system("git rebase --abort")

# edit