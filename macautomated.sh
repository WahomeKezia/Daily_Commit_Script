                                                                
#!/bin/bash
set -euxo pipefail  # 🔍 This enables error tracing and debugging

echo "🔁 Starting run.sh"

# Navigate to project directory
cd "$(dirname "$0")"

echo "📁 Changed directory to: $(pwd)"

# Check what's in the folder
echo "📂 Listing contents of project folder..."
ls -la

# Activate the virtual environment
echo "🐍 Activating virtual environment..."
source /Users/keziawahome/Scripts/DailyCommit/env/bin/activate

# Print which Python is active
which python3
python3 --version

# Run the Python script
echo "📜 Running Python script..."
python3 main.py

echo "✅ Done running main.py"


































^G Get Help                       ^O WriteOut                       ^R Read File                      ^Y Prev Pg                        ^K Cut Text                       ^C Cur Pos                        
^X Exit                           ^J Justify                        ^W Where is                       ^V Next Pg                        ^U UnCut Text                     ^T To Spell                       
