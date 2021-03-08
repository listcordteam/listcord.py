import Client from listcord
import discord
import asyncio

class AutoPost():
    def __init__(self,token: str, bot:discord.Client):
        self.token = token
        self.bot = bot
        self.client = Client(self.token)
        
    def start(self , interval:int = 30):
        self.bot.loop.create_task(self.auto_post(interval))

    async def auto_post(self, interval):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            await self.client.post_stats_async(self.bot.user.id, len(self.bot.guilds))
            await asyncio.sleep(interval * 60)
