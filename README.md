```markdown
# Daily Commit Script

This script automates the process of committing changes to a Git repository and pushing them to a remote repository. It updates a YAML file with the number of commits and the last update timestamp.

## Setup

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/YourUsername/Daily_Commit_Script.git
cd Daily_Commit_Script
```

### 2. Create and Activate Virtual Environment
Create and activate a virtual environment:

```bash
python -m venv DailyCommit  # Create virtual environment
.\DailyCommit\Scripts\activate  # Activate (Windows)
source DailyCommit/bin/activate  # Activate (Linux/Mac)
```

### 3. Install Dependencies
Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Configure Git Repo
Ensure you have a Git repository set up and update the `REPO_PATH` in `main.py` to point to your repo.

### 5. Set Up Task Scheduler (Windows) / Cron (Linux/Mac)
To run the script periodically, set up Task Scheduler (Windows) or a cron job (Linux/macOS).

#### Windows Task Scheduler Example
Create a task to run `run.bat`:

```bash
@echo off
cd /path/to/your/project
call DailyCommit\Scripts\activate
python main.py
```

#### Cron (Linux/Mac) Example:
```bash
0 9 * * * cd /path/to/your/project && source DailyCommit/bin/activate && python main.py
```

### 6. .gitignore
Add the following to your `.gitignore` file:

```
DailyCommit/
__pycache__/
*.pyc
*.pyo
*.pyd
.idea/
.vscode/
run.bat
```

## License
MIT License
```

