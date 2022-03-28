# Template for making new class of commands
# READ ONLY PLEASE - only meant for copy/paste


import discord
from discord.ext import commands


class YOUR_COMMAND_CLASS_NAME(commands.Cog):
    """YOUR EXPLANATION OF THIS CLASS FUNCTIONALITY"""

    def __init__(self, client):
        self.client = client


    # Actual command definition
    @commands.command()
    async def NAME_OF_COMMAND(self, ctx, *msgs):
        """EXPLANATION OF WHAT THE COMMAND DOES WHEN USER USES !help"""

        await ctx.send("hello world")


def setup(client):
    client.add_cog(YOUR_COMMAND_CLASS_NAME(client))