import yaml
from datetime import datetime
from git import Repo
from time import sleep
from random import randint
import logging

FILE_TO_COMMIT_NAME = 'update_me.yaml'
REPO_PATH = '/path/to/your/repo'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def update_file_to_commit():
    """Update the YAML file."""
    try:
        with open(FILE_TO_COMMIT_NAME, 'r') as file:
            current_data = yaml.safe_load(file)
            update_times = int(current_data['UPDATE_TIMES']) + 1
            last_update = datetime.now().strftime("%A %B %d %Y at %X%p")
    except (FileNotFoundError, KeyError, TypeError, ValueError):
        update_times = 1
        last_update = datetime.now().strftime("%A %B %d %Y at %X%p")
    updated_data = {
        'UPDATE_TIMES': update_times,
        'LAST_UPDATE': last_update
    }
    with open(FILE_TO_COMMIT_NAME, 'w') as file:
        yaml.dump(updated_data, file, default_flow_style=False, sort_keys=True)
    logging.info(f"File updated: {updated_data}")
    return updated_data

def commit_repository(yaml_data, repo_path=REPO_PATH):
    """Commit the updated file."""
    try:
        repo = Repo(repo_path)
        repo.index.add([FILE_TO_COMMIT_NAME])
        commit_message = f'Updated {yaml_data["UPDATE_TIMES"]} times. Last update was on {yaml_data["LAST_UPDATE"]}.'
        repo.index.commit(commit_message)
        origin = repo.remote('origin')
        origin.push()
        logging.info(f"Commit pushed: {commit_message}")
    except Exception as e:
        logging.error(f"Git operation failed: {e}")

if __name__ == '__main__':
    while True:
        for _ in range(randint(2, 5)):  # 2-5 commits daily
            updated_yaml_data = update_file_to_commit()
            commit_repository(updated_yaml_data)
            sleep(randint(600, 3600))  # 10-60 minutes between commits
        sleep(86400)  # Sleep for 24 hours
