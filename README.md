# charsibot.py

A straightforward Discord bot built with [Pycord](https://pycord.dev/).

This bot was created specifically for a personal project and is tailored to a specific Discord server. Because of this, it might not be appropriate for use in other servers.

## Requirements

Make sure you have the following installed before running the bot:

- Python 3.8 or higher

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

3. To quickly start and stop the bot, create a script named '**charsibot**' in '**~/.local/bin**':

    ```bash
    #!/bin/bash
    
    case "$1" in
      "start")
        cd /path/to/bot/src && nohup python3 bot.py >/dev/null 2>&1 &
        ;;
      "stop")
        pkill -f "python3 bot.py"
        ;;
      *)
        echo "Usage: charsibot [start|stop]"
        exit 1
        ;;
    esac
    
    ```

    - Make the script executable:

        ```bash
        chmod +x charsibot
        ```

    - Run **charsibot start**.

4. Check Discord to ensure the bot's status is **Online**.

## Testing the Bot

When testing the bot locally, make sure to stop the existing bot process, to prevent running multiple instances of the bot.
Optionally, create a test branch and a new Discord application to avoid bot downtime.
