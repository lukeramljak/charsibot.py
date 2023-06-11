# charsibot.py
A basic Discord bot built with [Pycord](https://pycord.dev/). This bot is specifically designed for a personal project and tailored to a specific Discord server. As a result, it may not be suitable for general use or easily adaptable to other servers. 

Feel free to explore the codebase, but please keep in mind that it is primarily maintained for personal use.

## Prerequisites
Before running the bot, make sure you have the following installed:
- Python 3.8 or higher
- Required Python packages (listed in requirements.txt)

## Getting Started
1. Create a virtual environment.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Add the bot token:
- In the project directory, create a file named .env and add the following lines:

```ini
TOKEN=your-bot-token-goes-here
GUILD_ID=your-guild-id-goes-here
```

## Deploying the Bot
The following steps assume you running the bot on Linux or macOS.

1. Ensure that python3-pip is installed.

2. cd into the bot directory and install dependencies as above.

3. To quickly start the bot from anywhere, create a shell script named '**bot_start**' in '**~/.local/bin**':

```bash
#!/bin/bash

# Full path to the bot script
BOT_SCRIPT="/path/to/bot/bot.py"

# Check if the bot script file exists
if [ ! -f "$BOT_SCRIPT" ]; then
    echo "Bot script file does not exist: $BOT_SCRIPT"
    exit 1
fi

# Check if the bot is already running
if pgrep -f "$BOT_SCRIPT" >/dev/null; then
    echo "Bot is already running."
    exit 1
fi

# Start the bot
nohup python3 "$BOT_SCRIPT" >/dev/null 2>&1 &
echo "Bot started."
```

- Make the script executable:

```bash
chmod +x bot_start
```

- Run bot_start.

4. Check Discord to ensure the bot's status is **Online**. 

## Testing the Bot

When testing the bot locally, make sure to stop the existing bot process, to prevent running multiple instances of the bot.

Create a shell script called '**bot_stop**':

```bash
#!/bin/sh

# Find the process ID (PID) of the bot
PID=$(ps aux | grep 'bot.py' | grep -v 'grep' | awk '{print $2}')

# Check if the PID is found
if [ -n "$PID" ]; then
    # Terminate the bot process
    kill "$PID"
    echo "Bot stopped."
else
    echo "Bot is not running."
fi
```

- Again, make the script executable:

```bash
chmod +x bot_stop
```