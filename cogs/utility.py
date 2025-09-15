import discord
from discord import app_commands
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="userinfo", description="Displays information about a user.")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user
        
        embed = discord.Embed(
            title=f"User Information - {member.display_name}",
            color=member.color
        )
        embed.set_thumbnail(url=member.avatar.url)
        
        embed.add_field(name="Username", value=member, inline=True)
        embed.add_field(name="User ID", value=member.id, inline=True)
        
        embed.add_field(name="Account Created", value=discord.utils.format_dt(member.created_at, style='R'), inline=True)
        embed.add_field(name="Joined Server", value=discord.utils.format_dt(member.joined_at, style='R'), inline=True)

        roles = [role.mention for role in member.roles[1:]]
        if roles:
            embed.add_field(name=f"Roles [{len(roles)}]", value=" ".join(reversed(roles)), inline=False)
        
        embed.set_footer(text=f"Requested by {interaction.user.display_name}", icon_url=interaction.user.avatar.url)

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Utility(bot))