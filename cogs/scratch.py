# Scratch File for testing random things

import discord
from discord.ext import commands


class Scratch(commands.Cog):
    """Scratch class for testing anything"""

    def __init__(self, client):
        self.client = client


    # Actual command definition
    @commands.command()
    async def scratch(self, ctx, *msgs):
        """scratch command for testing things"""
        was_unsuccessful = "Already up to date."

        import subprocess
        await ctx.send(f"Attempting to restart!")
        pull_out = subprocess.Popen(["git", "pull"], cwd="/home/pi/programming/python/laststand/lastStandBot").wait()
        print(f"pull out was {pull_out}")
        if pull_out == was_unsuccessful:
            await ctx.send(f"No changes. Not restarting")
        else:
            subprocess.Popen(["sudo", "systemctl", "restart",  "laststandbot"]).wait()
            print("this is after restart")

    @commands.command()
    async def ping(self, ctx, *msgs):
        """pong!"""
        print(msgs)
        await ctx.send("stop procrastinating pickle")



def setup(client):
    client.add_cog(Scratch(client))