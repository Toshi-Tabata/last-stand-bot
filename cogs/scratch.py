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
        import subprocess
        await ctx.send(f"Attempting to restart!")
        shellscript = subprocess.Popen(["/home/pi/programming/python/laststand/lastStandBot/update_from_github.sh"])
        out = shellscript.wait()  # blocks until shellscript is done
        await ctx.send(out)

    @commands.command()
    async def ping(self, ctx, *msgs):
        """pong!"""
        print(msgs)
        await ctx.send("stop procrastinating pickle")



def setup(client):
    client.add_cog(Scratch(client))