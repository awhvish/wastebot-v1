import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping.py is connected successfully")
        
    @commands.command()
    async def ping(self, ctx):
        latency = self.client.latency * 1000
        await ctx.send(f"Your Ping is {latency} ms.")



class Echo(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.command()
    async def echo(self, ctx, arg):
        await ctx.send(arg)
        

class Invite(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.command()
    async def invite(self,ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=1128352140310614126&permissions=8&scope=bot")

async def setup(client):
    await client.add_cog(Ping(client))
    await client.add_cog(Echo(client))
    await client.add_cog(Invite(client))
    