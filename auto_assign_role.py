import typing
import discord
import os

from dotenv import load_dotenv
load_dotenv()


DISCORD_TOKEN = os.environ['DISCORD_TOKEN']  # Get one here: https://discord.com/developers/applications/
USER_NAMES = [x.strip() for x in os.environ.get('DISCORD_USERS', 'mule#8398,lucidrains#0266').split(',')]
ROLE_NAMES = [x.strip() for x in os.environ.get('DISCORD_ROLES', 'test').split(',')]

client = discord.Client()


@client.event
async def on_message(message: discord.Message):
    print('{0.author}: {0.content}'.format(message))
    if bool(int(os.environ.get('DEBUG', '0'))):
      import pdb; pdb.set_trace()
    if not hasattr(message, "guild"):
        print('no message.guild')
        return
    if str(message.author) in USER_NAMES:
      for role_name in ROLE_NAMES:
        if role_name not in message.author.roles:
          print('Attempting to grant role {} to user {}...'.format(role_name, message.author))
          target_role = discord.utils.get(message.guild.roles, name=role_name)
          await message.author.add_roles(target_role)
          print('Granted role {!r} to user {!r}!'.format(role_name, message.author))

print('Will grant roles {!r} to users {!r}'.format(ROLE_NAMES, USER_NAMES))
client.run(DISCORD_TOKEN)
