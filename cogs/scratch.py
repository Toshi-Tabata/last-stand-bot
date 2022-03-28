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
        shellscript = subprocess.Popen(["/home/pi/programming/python/laststand/lastStandBot/update_from_github.sh"])
        shellscript.wait()  # blocks until shellscript is done
        await ctx.send(f"I'm not sure if this shows up since the bot restarts LOL")


    @commands.command()
    async def ping(self, ctx, *msgs):
        """pong!"""
        print(msgs)
        await ctx.send("stop procrastinating pickle")



def setup(client):
    client.add_cog(Scratch(client))