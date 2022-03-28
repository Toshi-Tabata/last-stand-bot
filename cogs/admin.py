# Template for making new class of commands
# READ ONLY PLEASE - only meant for copy/paste


import discord
from discord.ext import commands

import subprocess


class AdminCommands(commands.Cog):
    """YOUR EXPLANATION OF THIS CLASS FUNCTIONALITY"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def pull(self, ctx, *msgs):
        """scratch command for testing things"""
        pickle_id = 104812942595272704
        if ctx.author.id != pickle_id:
            return

        was_unsuccessful = b"Already up to date.\n"

        pull_out = subprocess.run(["git", "pull"], cwd="/home/pi/programming/python/laststand/lastStandBot", stdout=subprocess.PIPE).stdout

        if pull_out == was_unsuccessful:
            await ctx.send(f"No changes. Not restarting")
        else:
            await ctx.send(f"Attempting to restart!")
            subprocess.Popen(["sudo", "systemctl", "restart",  "laststandbot"]).wait()
            print("this is after restart")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def restart(self, ctx, *msgs):
        """scratch command for testing things"""
        pickle_id = 104812942595272704
        if ctx.author.id != pickle_id:
            return

        await ctx.send(f"Attempting to restart!")
        subprocess.Popen(["sudo", "systemctl", "restart",  "laststandbot"]).wait()


def setup(client):
    client.add_cog(AdminCommands(client))