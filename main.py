import yaml
from datetime import datetime
from git import Repo
from time import sleep
from random import randint
import logging

# Constants
FILE_TO_COMMIT_NAME = 'update_me.yaml'  # Name of the YAML file to update
REPO_PATH = '/path/to/your/repo'        # Path to the local Git repository

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def update_file_to_commit():
    """
    Updates the YAML file with:
    - The number of times it has been committed.
    - The timestamp of the last update.
    
    If the file doesn't exist or has invalid data, it initializes the data with default values.

    Returns:
        dict: The updated data, including the 'UPDATE_TIMES' and 'LAST_UPDATE'.
    """
    try:
        # Attempt to read and parse the existing YAML file
        with open(FILE_TO_COMMIT_NAME, 'r') as file:
            current_data = yaml.safe_load(file)
            # Increment the update count
            update_times = int(current_data['UPDATE_TIMES']) + 1
            # Record the current timestamp
            last_update = datetime.now().strftime("%A %B %d %Y at %X%p")
    except (FileNotFoundError, KeyError, TypeError, ValueError):
        # Handle cases where the file doesn't exist or has malformed data
        logging.warning(f"File not found or corrupted. Initializing new data.")
        update_times = 1
        last_update = datetime.now().strftime("%A %B %d %Y at %X%p")
    
    # Prepare the updated data
    updated_data = {
        'UPDATE_TIMES': update_times,
        'LAST_UPDATE': last_update
    }
    
    # Write the updated data back to the YAML file
    with open(FILE_TO_COMMIT_NAME, 'w') as file:
        yaml.dump(updated_data, file, default_flow_style=False, sort_keys=True)
    logging.info(f"YAML file updated with data: {updated_data}")
    return updated_data

def commit_repository(yaml_data, repo_path=REPO_PATH):
    """
    Commits the updated YAML file to the local Git repository and pushes the changes to the remote repository.

    Args:
        yaml_data (dict): The updated YAML data to include in the commit message.
        repo_path (str): Path to the local Git repository.

    Raises:
        Exception: If any Git operation fails, logs the error and skips the commit.
    """
    try:
        # Open the repository
        repo = Repo(repo_path)
        # Stage the updated YAML file
        repo.index.add([FILE_TO_COMMIT_NAME])
        # Create a commit message based on the updated data
        commit_message = f'Updated {yaml_data["UPDATE_TIMES"]} times. Last update was on {yaml_data["LAST_UPDATE"]}.'
        # Commit the changes
        repo.index.commit(commit_message)
        # Push the commit to the remote repository
        origin = repo.remote('origin')
        origin.push()
        logging.info(f"Commit pushed successfully: {commit_message}")
    except Exception as e:
        logging.error(f"Git operation failed: {e}")

if __name__ == '__main__':
    """
    Main script execution:
    - Runs an infinite loop to make 2-5 commits to the repository every day.
    - Randomizes the time between commits to simulate natural activity.
    - Sleeps for 24 hours after completing daily commits.
    """
    while True:
        # Make a random number of commits (2-5) each day
        for _ in range(randint(2, 5)):
            # Update the YAML file and commit the changes
            updated_yaml_data = update_file_to_commit()
            commit_repository(updated_yaml_data)
            # Sleep for a random time between 10 minutes to 1 hour before the next commit
            sleep(randint(600, 3600))  
        # Sleep for 24 hours before making the next day's commits
        sleep(86400)
