# discord-modmail
A light weight and simple Discord mod mail bot.

## How to self-host  
1. Install [Python](https://www.python.org/), [Pip](https://pypi.org/project/pip/) and [Git](https://git-scm.com/).
2. Install the [nextcord](https://pypi.org/project/nextcord/) and [Python-Dotenv](https://pypi.org/project/python-dotenv/) modules.
3. In the terminal or command prompt run `git clone https://github.com/yavda1/discord-modmail` and then `cd discord-modmail`.
4. Open the `main.py` file in any code/text editor and change lines 17 with your guilds ID.
5. Change line 44 with the channel you want all mod mails to go to.
6. Open the `.env` file in any code/text editor and put your bots token.
7. Run `python3 main.py`.

## What are the commands?

Each command is a discord application or `/` command for ease of use.

`/message [content] [user]` this command sends any message to any user.

`/ignore [user]` this command stops any user from using Mod Mail. This can be used if the user is spamming.

`/unignore [user]` this command unignores the user and allows them to use Mod Mail again.

## Credits

[yavda1](https://github.com/yavda1)


