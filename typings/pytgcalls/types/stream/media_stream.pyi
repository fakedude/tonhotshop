"""
This type stub file was generated by pyright.
"""

from pathlib import Path
from typing import Dict, Optional, Union
from ...media_devices import DeviceInfo, ScreenInfo
from ...statictypes import statictypes
from ..flag import Flag
from ..raw.audio_parameters import AudioParameters
from ..raw.stream import Stream
from ..raw.video_parameters import VideoParameters
from ..stream.audio_quality import AudioQuality
from ..stream.video_quality import VideoQuality

class MediaStream(Stream):
    class Flags(Flag):
        AUTO_DETECT = ...
        REQUIRED = ...
        IGNORE = ...
        NO_LATENCY = ...
    
    
    @statictypes
    def __init__(self, media_path: Union[str, Path, ScreenInfo, DeviceInfo], audio_parameters: Union[AudioParameters, AudioQuality,] = ..., video_parameters: Union[VideoParameters, VideoQuality,] = ..., audio_path: Optional[Union[str, Path, DeviceInfo]] = ..., audio_flags: Optional[Flags] = ..., video_flags: Optional[Flags] = ..., headers: Optional[Dict[str, str]] = ..., ffmpeg_parameters: Optional[str] = ..., ytdlp_parameters: Optional[str] = ...) -> None:
        ...
    
    async def check_stream(self): # -> None:
        ...
    

