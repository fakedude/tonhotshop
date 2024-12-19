"""
This type stub file was generated by pyright.
"""

from typing import Any
from .methods import Methods
from .scaffold import Scaffold
from .statictypes import statictypes
from .types import Cache

class PyTgCalls(Methods, Scaffold):
    WORKERS = ...
    CACHE_DURATION = ...
    @statictypes
    def __init__(self, app: Any, workers: int = ..., cache_duration: int = ...) -> None:
        ...
    
    @property
    def cache_user_peer(self) -> Cache:
        ...
    
    @property
    def mtproto_client(self): # -> Any:
        ...
    

