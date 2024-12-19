"""
This type stub file was generated by pyright.
"""

from typing import Dict, List, Optional, Union
from .types.raw import AudioParameters, VideoParameters

async def check_stream(ffmpeg_parameters: Optional[str], path: str, stream_parameters: Union[AudioParameters, VideoParameters], before_commands: Optional[List[str]] = ..., headers: Optional[Dict[str, str]] = ...): # -> None:
    ...

async def cleanup_commands(commands: List[str], process_name: Optional[str] = ..., blacklist: Optional[List[str]] = ...) -> List[str]:
    ...

def build_command(name: str, ffmpeg_parameters: Optional[str], path: Optional[str], stream_parameters: Union[AudioParameters, VideoParameters], before_commands: Optional[List[str]] = ..., headers: Optional[Dict[str, str]] = ..., is_livestream: bool = ...) -> List[str]:
    ...
