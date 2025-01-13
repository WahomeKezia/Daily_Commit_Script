import os
from git import Repo
import random
import schedule
import time
from datetime import datetime

# Configure your repo path
REPO_PATH = "/path/to/your/repo"
COMMIT_MESSAGES = [
    "Update documentation",
    "Refactor code",
    "Fix minor bug",
    "Add new feature",
    "Update README",
]

def make_commit():
    repo = Repo(REPO_PATH)
    if repo.is_dirty():
        print("Repository has uncommitted changes. Aborting.")
        return

    # Make changes
    file_path = os.path.join(REPO_PATH, "dummy.txt")
    with open(file_path, "a") as f:
        f.write(f"Update at {datetime.now()}\n")

    # Add and commit
    repo.git.add(file_path)
    commit_message = random.choice(COMMIT_MESSAGES)
    repo.git.commit(m=commit_message)
    print(f"Committed: {commit_message}")

    # Push changes
    origin = repo.remote(name="origin")
    origin.push()
    print("Changes pushed to GitHub.")

def schedule_commits():
    # Randomly schedule 2 to 5 commits in a day
    commits_today = random.randint(2, 5)
    for _ in range(commits_today):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        schedule_time = f"{hour:02}:{minute:02}"
        schedule.every().day.at(schedule_time).do(make_commit)
        print(f"Scheduled commit at {schedule_time}")

if __name__ == "__main__":
    schedule_commits()
    while True:
        schedule.run_pending()
        time.sleep(1)
