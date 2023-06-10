# charsibot.py
A Python rewrite of my JavaScript Discord bot built with [Pycord](https://pycord.dev/). This bot is tailored to a specific Discord server, and is not plug and play.

## Prerequisites
Before running the bot, make sure you have the following installed:
- Python 3.8 or higher
- Required Python packages (listed in requirements.txt)

## Getting Started
1. Create a virtual environment.
2. Install the required dependencies:

`` pip install -r requirements.txt ``

3. In a VPS, run the bot:

`` nohup python3 bot.py & ``

4. Detach from the session by either using the '**exit**' command or '**Ctrl + D**'. This will leave the bot running in the background.

    1. Note: If you want to stop the bot at any time, you can use tools like '**ps**' and '**kill**' to find the bot's process ID (PID) and terminate it. For example, you can use '**ps aux | grep bot.py**' to find the process ID and then use '**kill \<pid>**' to stop the bot.