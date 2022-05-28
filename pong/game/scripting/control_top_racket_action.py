from constants import *
from game.scripting.action import Action


class ControlTopRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(TOP_RACKET_GROUP)
        if self._keyboard_service.is_key_down(TOP_LEFT): 
            racket.swing_left()
        elif self._keyboard_service.is_key_down(TOP_RIGHT): 
            racket.swing_right()  
        else: 
            racket.stop_moving()        