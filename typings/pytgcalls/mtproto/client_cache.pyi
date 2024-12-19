"""
This type stub file was generated by pyright.
"""

from typing import Any, List, Optional
from ..types.chats import GroupCallParticipant
from .bridged_client import BridgedClient

py_logger = ...
class ClientCache:
    def __init__(self, cache_duration: int, app: BridgedClient) -> None:
        ...
    
    async def get_full_chat(self, chat_id: int) -> Optional[Any]:
        ...
    
    def set_participants_cache(self, input_id: int, participant: GroupCallParticipant) -> Optional[GroupCallParticipant]:
        ...
    
    async def get_participant_list(self, chat_id: int) -> Optional[List[GroupCallParticipant]]:
        ...
    
    def get_chat_id(self, input_group_call_id: int) -> Optional[int]:
        ...
    
    def set_cache(self, chat_id: int, input_call: Any) -> None:
        ...
    
    def drop_cache(self, chat_id) -> None:
        ...
    
    def set_phone_call(self, chat_id: int, phone_call: Any) -> None:
        ...
    
    def get_phone_call(self, chat_id: int) -> Optional[Any]:
        ...
    
    def get_user_id(self, phone_call_id: int) -> Optional[int]:
        ...
    
    def drop_phone_call(self, chat_id: int) -> None:
        ...
    

