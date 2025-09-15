import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

class moderationBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=intents) 

    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f'Loaded Cog: {filename}')
                except Exception as e:
                    print(f'Failed to load cog {filename}: {e}')
        
        # guild = discord.Object(id=YOUR_SERVER_ID_HERE) 
        # self.tree.copy_global_to(guild=guild)
        # await self.tree.sync(guild=guild)
        await self.tree.sync()


    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

bot = moderationBot()

bot.run(TOKEN) 
