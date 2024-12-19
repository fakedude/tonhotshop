"""
This type stub file was generated by pyright.
"""

from typing import Optional, Union
from ...mtproto_required import mtproto_required
from ...mutex import mutex
from ...scaffold import Scaffold
from ...statictypes import statictypes
from ...types import CallConfig, GroupCallConfig
from ...types.raw import Stream

py_logger = ...
class Play(Scaffold):
    @mutex
    @statictypes
    @mtproto_required
    async def play(self, chat_id: Union[int, str], stream: Optional[Stream] = ..., config: Optional[Union[CallConfig, GroupCallConfig]] = ...): # -> None:
        ...
    

