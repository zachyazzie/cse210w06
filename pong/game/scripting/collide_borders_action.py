from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        wall_sound = Sound(WALL_SOUND)
        over_sound = Sound(OVER_SOUND)
        score_sound = Sound(SCORE_SOUND)
                
        if x < FIELD_LEFT:
            ball.bounce_x()
            self._audio_service.play_sound(wall_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball.bounce_x()
            self._audio_service.play_sound(wall_sound)

        if y < FIELD_TOP:
            stats = cast.get_first_actor(STATS_GROUP)
            stats.player_two_gain_point()
            
            if stats.get_player_two_score() < 5:
                callback.on_next(TRY_AGAIN) 
                self._audio_service.play_sound(score_sound)
            else:
                callback.on_next(PLAYER_TWO_WINS)
                self._audio_service.play_sound(over_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            stats = cast.get_first_actor(STATS_GROUP)
            stats.player_one_gain_point()
            
            if stats.get_player_one_score() < 5:
                callback.on_next(TRY_AGAIN)
                self._audio_service.play_sound(score_sound)
            else:
                callback.on_next(PLAYER_ONE_WINS)
                self._audio_service.play_sound(over_sound)