import discord
from discord.ext import commands
import json

class Logging(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.log_channel_id = self._load_config().get("log_channel_id")

    def _load_config(self):
        with open('config.json', 'r') as f:
            return json.load(f)

    async def get_log_channel(self):
        return self.bot.get_channel(self.log_channel_id)

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.guild is None or message.author.bot:
            return

        log_channel = await self.get_log_channel()
        if not log_channel:
            return

        embed = discord.Embed(
            title="Message Deleted",
            color=discord.Color.orange(),
            timestamp=discord.utils.utcnow()
        )
        embed.add_field(name="Author", value=message.author.mention, inline=True)
        embed.add_field(name="Channel", value=message.channel.mention, inline=True)
        if message.content: 
            embed.add_field(name="Content", value=f"```{message.content}```", inline=False)
        
        embed.set_footer(text=f"Author ID: {message.author.id} | Message ID: {message.id}")
        
        await log_channel.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Logging(bot))