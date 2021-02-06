# auto_assign_role

A discord bot to automatically assign roles to users whenever they rejoin the server.

# quickstart

Follow the discord [bot setup guide](https://discordpy.readthedocs.io/en/latest/discord.html). Then...

```sh
git clone https://github.com/shawwn/auto_assign_role
cd auto_assign_role
pip3 install -r requirements.txt

echo 'DISCORD_TOKEN=replace this text with your discord token' > .env

DISCORD_ROLES='role1,role2' DISCORD_USERS='you#1234,someone#9999' python3 auto_assign_role.py
```

# license

MIT.

# credits

[Thanks to Lucas Nestler for the initial proof of concept!](https://twitter.com/_clashluke/status/1357832350118338562)
