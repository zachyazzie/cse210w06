
from constants import *
from game.casting.animation import Animation
from game.casting.ball import Ball
from game.casting.body import Body
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.top_racket import Top_racket
from game.casting.bottom_racket import Bottom_racket
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_top_racket_action import CollideTopRacketAction
from game.scripting.collide_bottom_racket_action import CollideBottomRacketAction
from game.scripting.control_top_racket_action import ControlTopRacketAction
from game.scripting.control_bottom_racket_action import ControlBottomRacketAction
from game.scripting.draw_ball_action import DrawBallAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_top_racket_action import DrawTopRacketAction
from game.scripting.draw_bottom_racket_action import DrawBottomRacketAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_ball_action import MoveBallAction
from game.scripting.move_top_racket_action import MoveTopRacketAction
from game.scripting.move_bottom_racket_action import MoveBottomRacketAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_TOP_RACKET_ACTION = CollideTopRacketAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_BOTTOM_RACKET_ACTION = CollideBottomRacketAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_TOP_RACKET_ACTION = ControlTopRacketAction(KEYBOARD_SERVICE)
    CONTROL_BOTTOM_RACKET_ACTION = ControlBottomRacketAction(KEYBOARD_SERVICE)
    DRAW_BALL_ACTION = DrawBallAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_TOP_RACKET_ACTION= DrawTopRacketAction(VIDEO_SERVICE)
    DRAW_BOTTOM_RACKET_ACTION= DrawBottomRacketAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_BALL_ACTION = MoveBallAction()
    MOVE_TOP_RACKET_ACTION = MoveTopRacketAction()
    MOVE_BOTTOM_RACKET_ACTION = MoveBottomRacketAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == PLAYER_ONE_WINS:    
            self._prepare_player_one_wins(cast, script)
        elif scene == PLAYER_TWO_WINS:    
            self._prepare_player_two_wins(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._top_player(cast)
        self._bottom_player(cast)

        self._add_ball(cast)
        self._add_top_racket(cast)
        self._add_bottom_racket(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        self._add_ball(cast)
        self._add_top_racket(cast)
        self._add_bottom_racket(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        self._add_ball(cast)
        self._add_top_racket(cast)
        self._add_bottom_racket(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        self._activate_ball(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_TOP_RACKET_ACTION)
        script.add_action(INPUT, self.CONTROL_BOTTOM_RACKET_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_player_one_wins(self, cast, script):
        self._add_ball(cast)
        self._add_top_racket(cast)
        self._add_bottom_racket(cast)
        self._add_dialog(cast, PLAYER_ONE_WIN_SCREEN)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)
    
    def _prepare_player_two_wins(self, cast, script):
        self._add_ball(cast)
        self._add_top_racket(cast)
        self._add_bottom_racket(cast)
        self._add_dialog(cast, PLAYER_TWO_WIN_SCREEN)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_ball(self, cast):
        ball = cast.get_first_actor(BALL_GROUP)
        ball.release()

    def _add_ball(self, cast):
        cast.clear_actors(BALL_GROUP)
        x = CENTER_X - BALL_WIDTH / 2
        y = CENTER_Y - BALL_WIDTH / 2
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP, ball)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _top_player(self, cast):
        cast.clear_actors(TOP_GROUP)
        text = Text(TOP_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(TOP_GROUP, label)

    def _bottom_player(self, cast):
        cast.clear_actors(BOTTOM_GROUP)
        text = Text(BOTTOM_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(BOTTOM_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_bottom_racket(self, cast):
        cast.clear_actors(BOTTOM_RACKET_GROUP)
        x = CENTER_X - RACKET_WIDTH / 2
        y = SCREEN_HEIGHT - RACKET_HEIGHT
        position = Point(x, y)
        size = Point(RACKET_WIDTH, RACKET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(RACKET_IMAGES, RACKET_RATE)
        bottom_racket = Bottom_racket(body, animation)
        cast.add_actor(BOTTOM_RACKET_GROUP, bottom_racket)

    def _add_top_racket(self, cast):
        cast.clear_actors(TOP_RACKET_GROUP)
        x = CENTER_X - RACKET_WIDTH / 2
        y = FIELD_TOP
        position = Point(x, y)
        size = Point(RACKET_WIDTH, RACKET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(RACKET_IMAGES, RACKET_RATE)
        top_racket = Top_racket(body, animation)
        cast.add_actor(TOP_RACKET_GROUP, top_racket)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION)
        script.add_action(OUTPUT, self.DRAW_TOP_RACKET_ACTION)
        script.add_action(OUTPUT, self.DRAW_BOTTOM_RACKET_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_BALL_ACTION)
        script.add_action(UPDATE, self.MOVE_TOP_RACKET_ACTION)
        script.add_action(UPDATE, self.MOVE_BOTTOM_RACKET_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
   
        script.add_action(UPDATE, self.COLLIDE_TOP_RACKET_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BOTTOM_RACKET_ACTION)
        script.add_action(UPDATE, self.MOVE_TOP_RACKET_ACTION)
        script.add_action(UPDATE, self.MOVE_BOTTOM_RACKET_ACTION)
