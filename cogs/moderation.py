import discord
from discord import app_commands
from discord.ext import commands
import datetime

class ConfirmView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)
        self.value = None

    @discord.ui.button(label='Confirm', style=discord.ButtonStyle.danger)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        self.stop()
        button.disabled = True
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = False
        self.stop()
        button.disabled = True
        await interaction.response.edit_message(view=self)


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="purge", description="Deletes a specified number of messages.")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def purge(self, interaction: discord.Interaction, amount: int):
        await interaction.response.defer(ephemeral=True)
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.followup.send(f"Deleted {len(deleted)} messages.", ephemeral=True)

    @app_commands.command(name="kick", description="Kicks a user from the server.")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        if member.top_role >= interaction.user.top_role:
            await interaction.response.send_message("You cannot kick someone with an equal or higher role.", ephemeral=True)
            return

        view = ConfirmView()
        await interaction.response.send_message(f"Are you sure you want to kick {member.mention} for: `{reason}`?", view=view, ephemeral=True)
        await view.wait()

        if view.value is True:
            await member.kick(reason=reason)
            await interaction.edit_original_response(content=f"{member.mention} has been kicked. Reason: `{reason}`", view=None)
        else:
            await interaction.edit_original_response(content="Kick cancelled.", view=None)
    
    @app_commands.command(name="ban", description="Bans a user from the server.")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        if member.top_role >= interaction.user.top_role:
            await interaction.response.send_message("You cannot ban someone with an equal or higher role.", ephemeral=True)
            return
            
        view = ConfirmView()
        await interaction.response.send_message(f"Are you sure you want to ban {member.mention} for: `{reason}`?", view=view, ephemeral=True)
        await view.wait()

        if view.value is True:
            await member.ban(reason=reason)
            await interaction.edit_original_response(content=f"{member.mention} has been banned. Reason: `{reason}`", view=None)
        else:
            await interaction.edit_original_response(content="Ban cancelled.", view=None)
    
    @app_commands.command(name="mute", description="Timeouts a user for a specified duration.")
    @app_commands.describe(duration="Duration (e.g., 5m, 1h, 3d)")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def mute(self, interaction: discord.Interaction, member: discord.Member, duration: str, reason: str):
        if member.top_role >= interaction.user.top_role:
            await interaction.response.send_message("You cannot mute someone with an equal or higher role.", ephemeral=True)
            return

        seconds = 0
        if 'd' in duration:
            seconds += int(duration.split('d')[0]) * 86400
        if 'h' in duration:
            seconds += int(duration.split('h')[0].split('d')[-1]) * 3600
        if 'm' in duration:
            seconds += int(duration.split('m')[0].split('h')[-1]) * 60
        
        if seconds == 0:
            await interaction.response.send_message("Invalid duration format. Use 'd', 'h', 'm'.", ephemeral=True)
            return
        
        if seconds > 2419200:
            await interaction.response.send_message("Timeout duration cannot exceed 28 days.", ephemeral=True)
            return

        timeout_until = datetime.timedelta(seconds=seconds)
        await member.timeout(timeout_until, reason=reason)
        await interaction.response.send_message(f"{member.mention} has been muted for `{duration}`. Reason: `{reason}`")


async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))