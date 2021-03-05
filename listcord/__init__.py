import requests
import aiohttp

class Client():
    
    def __init__(self, token: str):
        self.token = token
        self.baseURL = 'https://listcord.xyz/api'
    
    def get_bot(self, id: str):
        data = requests.get(self.baseURL + '/bot/' + id, headers={ 'token': self.token })
        return data.json()

    async def get_bot_async(self, id: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.baseURL + '/bot/' + id, headers={ 'token': self.token }) as result:
                return await result.json()

    def get_bot_reviews(self, id: str):
        data = requests.get(self.baseURL + '/bot/' + id + '/reviews', headers={ 'token': self.token })
        return data.json()

    async def get_bot_reviews_async(self, id: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.baseURL + '/bot/' + id + '/reviews', headers={ 'token': self.token }) as result:
                return await result.json()

    def get_review(self, user_id: str, bot_id: str):
        reviews = self.get_bot_reviews(bot_id)

        if not isinstance(reviews, list): 
            return None

        for review in reviews:
            if review['author_id'] == user_id:
                return review

        return None

    async def get_review_async(self, user_id: str, bot_id: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.baseURL + '/bot/' + bot_id + '/reviews', headers={ 'token': self.token }) as result:
                reviews = await result.json()

                if not isinstance(reviews, list): 
                    return None

                for review in reviews:
                    if review['author_id'] == user_id:
                        return review

                return None

    def has_voted(self, user_id: str, bot_id: str):
        data = requests.get(self.baseURL + '/bot/' + bot_id + '/voted', params={ 'user_id': user_id }, headers={ 'token': self.token })
        return data.json()

    async def has_voted_async(self, user_id: str, bot_id: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.baseURL + '/bot/' + bot_id + '/voted', params={ 'user_id': user_id }, headers={ 'token': self.token }) as result:
                return await result.json()

    def search(self, q: str):
        data = requests.get(self.baseURL + '/bots', params={ 'q': q }, headers={ 'token': self.token })
        return data.json()

    async def search_async(self, q: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.baseURL + '/bots', params={ 'q': q }, headers={ 'token': self.token }) as result:
                return await result.json()

    def post_stats(self, id: str , count: int):
        result = requests.post(f"{self.baseURL}/bot/{id}/stats" , headers = {'Authorization' : self.token} , json = {'server_count' : count})
        return result.json()
              
    async def post_stats_async(self, id :str , count: int):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.baseURL}/bot/{id}/stats" , headers = {'Authorization' : self.token}, json = {'server_count' : count}) as result:
                return await result.json()        


    def __str__(self):
        return 'Listcord<Client>'

__version__ = '1.5.0'
