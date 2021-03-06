from typing import Generic, List, Mapping, Optional, TypeVar, Union
from typing_extensions import TypedDict

class Bot(TypedDict):

    id: str
    name: str
    avatar: str 
    description: TypedDict('BotDescription', {
        'short': str,
        'long': str
    })
    developers: List[str]
    required_permissions: int
    upvotes: int
    support_server: Optional[str]
    website: Optional[str]
    tags: List[str]
    prefix: str
    submitted_at: int
    approved: bool
    servers: int

class Review(TypedDict):

    author_id: str
    content: str
    stars: int
    sent_at: int

class VoteData(TypedDict):

    voted: bool
    upvoted_at: int
    next_at: int

class Botpack(TypedDict):

    name: str
    description: str
    bots: List[str]
    tags: List[str]

class PostResponse(TypedDict):

    success: Optional[bool]
    message: Optional[str]

class Error(TypedDict):

    message: str

T = TypeVar('T')
Response: Generic[T] = Union[T, Error]
Botpacks = Mapping[str, Botpack]