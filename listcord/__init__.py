from typing import Coroutine, List, Union
from .structs import Botpack, Botpacks, PostResponse, Response, Bot, Review, VoteData
import requests
import aiohttp
import discord

class Client():

    token: str
    baseURL: str
    
    def __init__(self, bot: discord.Client, token: str):
        self.bot = bot
        self.token = token
        self.baseURL = 'https://listcord.xyz/api'
    
    def get_bot(self, id: str) -> Response[Bot]:
        data = requests.get(f"{self.baseURL}/bot/{id}", headers={ 'Authorization': self.token })
        return data.json()

    async def get_bot_async(self, id: str) -> Coroutine[None, None, Response[Bot]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.baseURL}/bot/{id}", headers={ 'Authorization': self.token }) as result:
                return await result.json()

    def get_bot_reviews(self, id: str) -> Response[List[Review]]:
        data = requests.get(f"{self.baseURL}/bot/{id}/reviews", headers={ 'Authorization': self.token })
        return data.json()

    async def get_bot_reviews_async(self, id: str) -> Coroutine[None, None, Response[List[Review]]] :
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.baseURL}/bot/{id}/reviews", headers={ 'Authorization': self.token }) as result:
                return await result.json()

    def get_review(self, user_id: str, bot_id: str) -> Union[Review, None] :
        reviews = self.get_bot_reviews(bot_id)

        if not isinstance(reviews, list): 
            return None

        for review in reviews:
            if review['author_id'] == user_id:
                return review

        return None

    async def get_review_async(self, user_id: str, bot_id: str) -> Coroutine[None, None, Union[Review, None]]:
        async with self.get_bot_reviews(bot_id) as reviews: 
            if not isinstance(reviews, list): 
                return None

            for review in reviews:
                if review['author_id'] == user_id:
                    return review

            return None
                

    def has_voted(self, user_id: str, bot_id: str) -> Response[VoteData]:
        data = requests.get(f"{self.baseURL}/bot/{bot_id}/voted", params={ 'user_id': user_id }, headers={ 'Authorization': self.token })
        return data.json()

    async def has_voted_async(self, user_id: str, bot_id: str) -> Coroutine[None, None, Response[VoteData]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.baseURL}/bot/{bot_id}/voted", params={ 'user_id': user_id }, headers={ 'Authorization': self.token }) as result:
                return await result.json()
                
    def get_pack(self, id: str) -> Response[Botpack]:
        result = requests.get(f"{self.baseURL}/pack/{id}" , headers = {'Authorization' : self.token})
        return result.json()
        
    async def get_pack_async(self, id: str) -> Coroutine[None, None, Response[Botpack]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.baseURL}/pack/{id}" , headers = {'Authorization' : self.token}) as result:
                return await result.json()
                
    def get_packs(self) -> Response[Botpacks]:
        result = requests.get(f"{self.baseURL}/packs", headers = {'Authorization' : self.token})
        return result.json()
    
    async def get_packs_async(self) -> Coroutine[None, None, Response[Botpacks]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.baseURL}/packs", headers = {'Authorization' : self.token}) as result:
                return await result.json()

    def post_stats(self, count: int) -> PostResponse:
        result = requests.post(f"{self.baseURL}/bot/{self.bot.user.id}/stats" , headers = {'Authorization' : self.token} , json = {'server_count' : count})
        return result.json()
              
    async def post_stats_async(self, count: int) -> Coroutine[None, None, PostResponse]:
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.baseURL}/bot/{self.bot.user.id}/stats" , headers = {'Authorization' : self.token}, json = {'server_count' : count}) as result:
                return await result.json()
                
    def auto_post_stats(self , interval:int = 30):
        self.bot.loop.create_task(self.auto_post(interval))

    async def auto_post(self, interval):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            await self.post_stats_async(len(self.bot.guilds))
            await asyncio.sleep(interval * 60)

    def __str__(self):
        return 'Listcord<Client>'

__version__ = '2.1.0'
