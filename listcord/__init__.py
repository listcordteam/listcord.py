from typing import Coroutine, List, Union
from .structs import Botpack, Botpacks, PostResponse, Response, Bot, Review, VoteData
from .autoposter import AutoPoster
import requests
import aiohttp

class Client():

    token: str
    baseURL: str
    
    def __init__(self, token: str):
        self.token = token
        self.baseURL = 'https://listcord.gg/api'
        self.create_auto_poster = AutoPoster
    
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

    def post_stats(self, id: str, count: int) -> PostResponse:
        result = requests.post(f"{self.baseURL}/bot/{id}/stats" , headers = {'Authorization' : self.token} , json = {'server_count' : count})
        return result.json()
              
    async def post_stats_async(self, id: str, count: int) -> Coroutine[None, None, PostResponse]:
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.baseURL}/bot/{id}/stats" , headers = {'Authorization' : self.token}, json = {'server_count' : count}) as result:
                return await result.json()    

    def __str__(self):
        return 'Listcord<Client>'

__version__ = '2.1.0'
