@echo off
rem Change to the script directory
cd C:\Users\Hp\Desktop\Daily_Commit_Script

rem Activate the virtual environment
call C:\Users\Hp\Desktop\Daily_Commit_Script\DailyCommit\Scripts\activate.bat

rem Run the Python script
python main.py

rem Pause to keep the window open (optional)
pause
