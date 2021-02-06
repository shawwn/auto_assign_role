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

Whenever `you#1234` or `someone#9999` joins the server (or sends a message), the bot will verify that they have roles `role1` and `role2`.

NOTE: In `server settings -> roles`, your bot's role must be **above all the roles you wish to grant** in the roles list. This confused me for some time. :)

(The bot also needs the "Manage Roles" permission, obviously. I also gave it "View Channels" for good measure, though I have no idea whether this is required.)

# license

MIT.

# credits

[Thanks to Lucas Nestler for the initial proof of concept!](https://twitter.com/_clashluke/status/1357832350118338562)
