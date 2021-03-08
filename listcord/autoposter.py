from typing import Callable, Mapping, TypedDict
import asyncio, aiohttp, discord

class Options(TypedDict):

    interval: int
    start: bool

class AutoPoster():

    token: str
    interval: int
    bot: discord.Client
    stopped: bool
    _events: Mapping[str, Callable]

    def __init__(self, token: str, bot: discord.Client, options: Options = {
        'interval': 900000,
        'start': True
    }):
        self.token = token
        self.bot = bot

        if 'interval' not in options: options['interval'] = 900000
        else:
            if not isinstance(options['interval'], int) or options['interval'] < 900000: raise TypeError('Invalid interval duration!')

        if 'start' not in options: options['start'] = True

        self.interval = options['interval']
        self.stopped = not options['start']

        def on_post(self) -> None:
            return None

        def on_error(self) -> None:
            return None

        self._events = {
            'post': on_post,
            'error': on_error
        }
    
    def on(self, event: str) -> Callable[[Callable], None]:
        def add_listener(callback: Callable):
            self._events[event] = callback
        
        return add_listener

    def emit(self, event: str, data):
        if event in self._events: self._events[event](data)

    async def init(self):
        while not self.stopped:
            async with aiohttp.ClientSession() as session:
                async with session.post(f"https://listcord.xyz/api/bot/{self.bot.user.id}/stats" , headers = {'Authorization' : self.token}, json = {'server_count': len(self.bot.guilds)}) as result:
                    if result.status != 200: self.emit('error', await result.json())
                    else: self.emit('post', await result.json())

            await asyncio.sleep(self.interval)

    def start(self):
        self.stopped = False

    def stop(self):
        self.stopped = True
