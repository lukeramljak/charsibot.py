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

3. Add the bot token:
    1. In the project directory, create a file named .env and add the following lines:

    ``TOKEN=your-bot-token-goes-here``  
    ``GUILD_ID=your-guild-id-goes-here``

## Deploying the Bot
The following steps assume you running the bot on a VPS with any Linux distro.

1. Ensure that python3-pip is installed.

2. cd into the bot directory and install dependencies as above.

3. Run the bot in the background:

`` nohup python3 bot.py & ``

- You may need to run this command frequently when making changes to the bot. To save time, create a shell script named '**bot-start**' in the '**~/.local/bin**' directory. By placing it here, it will be added to your PATH, allowing you to run it from anywhere without navigating to the specific directory.

``#!/bin/sh``  
``nohup python3 path-to-bot/src/bot.py &``

- Make the script executable by running the following command:

    ``chmod +x bot-start``

- Now, you can simply run bot-start to start the bot in the background.

4. If everything is working correctly, you should see a message like "**nohup: ignoring input and appending output to 'nohup.out'**". This indicates that the bot is running and any console output is being redirected to the '**nohup.out**' file.

5. Check Discord to ensure the bot's status is **Online**. 

6. Detach from the session by either using the '**exit**' command or '**Ctrl + D**'. This will leave the bot running in the background.

    1. When testing the bot locally, make sure to stop the bot process running on your VPS. Running multiple instances of the bot simultaneously can cause conflicts and unexpected behavior. By terminating the bot process on the VPS, you ensure that you are running only one instance of the bot for testing purposes.
    2. The quickest way to terminate the bot is with '**htop**'. Press F3 to search for '**bot.py**', then F9 to kill. You can also use tools like '**ps**' and '**kill**' to find the bot's process ID (PID) and terminate it. For example, you can use '**ps aux | grep bot.py**' to find the process ID and then use '**kill \<pid>**' to stop the bot.