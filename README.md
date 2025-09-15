# Dragon Moderation 🛡️

A powerful and configurable Discord moderation bot designed to keep communities safe and well-managed. Built with Python and the `discord.py` library, Dragon Moderation offers a suite of tools for both proactive auto-moderation and reactive manual moderation.

## ✨ Features

This bot is built with a scalable architecture using Cogs. Here are the core features currently implemented:

* **Modern Slash Commands:** All commands are registered as slash commands for a seamless user experience.
* **Core Moderation Suite:**
    * `/kick`: Remove a member from the server.
    * `/ban`: Ban a member permanently.
    * `/mute`: Timeout a member for a specified duration (e.g., `10m`, `2h`, `7d`).
    * `/purge`: Bulk delete messages from a channel.
* **Transparent Logging:**
    * Logs key events like deleted messages to a designated channel to maintain a clear audit trail.
* **Utility Commands:**
    * `/userinfo`: Get detailed information about a server member.
* **Secure Configuration:**
    * Uses a `.env` file to securely store the bot token.
    * Uses a `config.json` file for easy server-specific setup.

## 🚀 Getting Started

Follow these instructions to get a local copy up and running for development and testing purposes.

### Prerequisites

* Python 3.8 or newer
* A Discord Bot Account with a Token (and Privileged Intents enabled)

**⚠️IMPORTANT!** - Enable `Server Member Intent` and `Message Content Intent` under `Priviledged Gateway Intents` in the Bot section of the Application.

### Installation & Setup

1.  **Clone the repository**
    ```sh
    git clone [https://github.com/KanyKroxigar/Dragon-Moderation.git](https://github.com/KanyKroxigar/Dragon-Moderation.git)
    cd Dragon-Moderation
    ```

2.  **Create a `requirements.txt` file**
  
    For easy installation of dependencies, create a file named `requirements.txt` in your project folder with the following content:
    ```
    discord.py
    python-dotenv
    ```

4.  **Install dependencies**
  
    Run the following command in your terminal to install the necessary Python libraries:
    ```sh
    python -m pip install -r requirements.txt
    ```

5.  **Create the Environment File (`.env`)**
 
    Create a file named `.env` in the root of your project folder. This file securely stores your bot's token. **Never share this file or commit it to version control.**
    ```
    DISCORD_TOKEN="YOUR_BOT_TOKEN_HERE"
    ```

6.  **Configure the Bot (`config.json`)**
 
    Create a file named `config.json` to store server-specific settings. You will need to get the channel ID from Discord for your logging channel.
    ```json
    {
        "log_channel_id": 123456789012345678 
    }
    ```
    > **Tip:** To get a Channel ID in Discord, enable Developer Mode in `Settings > Advanced`, then right-click on the channel and select "Copy Channel ID".

7.  **Run the Bot**
   
    Execute the main script from your terminal:
    ```sh
    python main.py
    ```

## ⚙️ Usage

All commands are slash commands. Simply type `/` in your Discord server to see a list of available commands.

### Moderation Commands
* `/purge <amount>` - Deletes the specified number of messages.
* `/kick <member> <reason>` - Kicks the specified member.
* `/ban <member> <reason>` - Bans the specified member.
* `/mute <member> <duration> <reason>` - Times out the member for a given duration (e.g., `5m`, `1h`, `3d`).

### Utility Commands
* `/userinfo [member]` - Displays detailed information about the specified member, or yourself if no member is provided.

## 🛠️ Built With

* [Python](https://www.python.org/) - The programming language used.
* [discord.py](https://github.com/Rapptz/discord.py) - The Python wrapper for the Discord API.
* [python-dotenv](https://github.com/theskumar/python-dotenv) - For managing environment variables.

## 📜 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
