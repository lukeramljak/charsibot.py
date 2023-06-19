# charsibot.py

A straightforward Discord bot built with [Pycord](https://pycord.dev/).

This bot was created specifically for a personal project and is tailored to a specific Discord server. Because of this, it might not be appropriate for use in other servers.

## Requirements

Make sure you have the following installed before running the bot:

- Python 3.8 or higher

- Required Python packages (listed in requirements.txt)

## Getting Started

1. Create a virtual environment.

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Add the bot token:

    - In the main directory, create a file named .env and add the following lines:

        ```ini
        TOKEN=your-bot-token-goes-here
        GUILD_ID=your-guild-id-goes-here
        ```

## Deploying the Bot

The following steps assume you running the bot on Linux or macOS.

1. Ensure that **python3-pip** is installed.

2. Enter the bot directory and install dependencies as above.

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

    - Run **bot_start**.

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

Again, make the script executable:

```bash
chmod +x bot_stop
```
