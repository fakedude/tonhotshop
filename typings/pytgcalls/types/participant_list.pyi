"""
This type stub file was generated by pyright.
"""

from ..types.chats import GroupCallParticipant

class ParticipantList:
    def __init__(self, input_id: int) -> None:
        ...
    
    def update_participant(self, participant: GroupCallParticipant): # -> GroupCallParticipant:
        ...
    
    def get_participants(self): # -> List:
        ...
    

