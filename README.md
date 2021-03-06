# Listcord.py

An official wrapper for the listcord api!

> View https://listcord.xyz/apidocs to view the raw api documentation!

## Installation

```sh
pip install listcord.py
```

## Getting started

> Get your api token from https://listcord.xyz/me. The Listcord api is currently only available only for those who have bots registered in our botlist! After getting your token, make sure your token is kept somewhere secret!

```py
import listcord

client = listcord.Client("Replace this with your token!")
print(client.get_bot('some bot id'))
```

This package also supports asynchronous fetching too!

```py
import listcord
import asyncio

client = listcord.Client("Replace this with your token!")

@asyncio.coroutine
def main():
    bot = yield from client.get_bot_async('some bot id')
    print(bot)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## Methods

There are only some methods with the asynchronous ones too!

```py
client.get_bot('801976787264471120') # Returns the information of the bot!
await client.get_bot_async('801976787264471120') # Returns the information of the bot asynchronously!

client.get_bot_reviews('801976787264471120'); # Returns the array of reviews of the bot!
await client.get_bot_reviews_async('801976787264471120'); # Returns the array of reviews of the bot asynchronously!

client.get_review('user id', 'bot id'); # Returns the review details by the discord id of the reviewer and the bot which was reviewed!
await client.get_review_async('user id', 'bot id'); # Returns the review details by the discord id of the reviewer and the bot which was reviewed asynchronously!

client.has_voted('user id', 'bot id'); # Verify if the particular user has voted a paticular bot by id!
await client.has_voted_async('user id', 'bot id'); # Verify if the particular user has voted a paticular bot by id asynchronously!

client.search('shaz'); # Returns the array of the bots which matches your query!
await client.search_async('shaz'); # Returns the array of the bots which matches your query aynchronously!

client.get_pack('packid'); # Returns the pack which mathces your query!
await client.get_pack_async('packid'); # Returns the pack which matches your query asynchronously!

client.get_packs(); # Returns array of the packs!
await client.get_packs_async('packid'); # Returns the array of the packs asynchronously!

client.post_stats(bot_id , server_count); # Posts the server count of the bot to API!
await client.post_stats_async(bot_id , server_count); # Posts the server count of the bot to API asynchronously!
```

## Contact

- [Join our discord server](https://discord.gg/cMGAyhZXwW)
- [Website](https://listcord.xyz)
