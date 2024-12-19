"""
This type stub file was generated by pyright.
"""

from ...types.py_object import PyObject
from ..flag import Flag

class Call(PyObject):
    class Status(Flag):
        PLAYING = ...
        PAUSED = ...
        IDLE = ...
    
    
    class Type(Flag):
        GROUP = ...
        PRIVATE = ...
    
    
    def __init__(self, chat_id: int, status: Status) -> None:
        ...
    

