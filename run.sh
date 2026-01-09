# #!/bin/bash
# set -euxo pipefail  #  This enables error tracing and debugging

# echo "🔁 Starting run.sh"

# # Navigate to project directory
# cd /Users/keziawahome/Desktop/Daily_Commit_Script
# echo "📁 Changed directory to: $(pwd)"

# # Check what's in the folder
# echo "📂 Listing contents of project folder..."
# ls -la

# # Activate the virtual environment
# echo "🐍 Activating virtual environment..."
# source env/bin/activate

# # Print which Python is active
# which python3
# python3 --version

# # Run the Python script
# echo "📜 Running Python script..."
# python3 main.py

# echo "✅ Done running main.py"
#!/bin/bash
set -euxo pipefail  # 🔍 This enables error tracing and debugging

echo "🔁 Starting run.sh"

# Navigate to project directory
cd /Users/keziawahome/Desktop/Daily_Commit_Script
echo "📁 Changed directory to: $(pwd)"

# Check what's in the folder
echo "📂 Listing contents of project folder..."
ls -la

# Activate the virtual environment
echo "🐍 Activating virtual environment..."
source env/bin/activate

# Print which Python is active
which python3
python3 --version

# Run the Python script
echo "📜 Running Python script..."
python3 main.py

echo "✅ Done running main.py"