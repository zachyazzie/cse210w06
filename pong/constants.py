import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Pong"
FRAME_RATE = 120

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "pong/assets/fonts/bit5x3.ttf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "pong/assets/sounds/pong_hit.mp3"
WELCOME_SOUND = "pong/assets/sounds/start_game.mp3"
OVER_SOUND = "pong/assets/sounds/game_over.mp3"
WALL_SOUND = "pong/assets/sounds/wall.mp3"
SCORE_SOUND = "pong/assets/sounds/score.mp3"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
TOP_LEFT = 'a'
TOP_RIGHT = 'd'
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
PLAYER_ONE_WINS = 4
PLAYER_TWO_WINS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 0
MAXIMUM_LIVES = 5


# HUD
HUD_MARGIN = 15
TOP_GROUP = "top"
BOTTOM_GROUP = "bottom"
TOP_FORMAT = "TOP: {}"
BOTTOM_FORMAT = "BOTTOM: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "pong/assets/images/ball.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 4

# RACKET
BOTTOM_RACKET_GROUP = "bottom_rackets"
TOP_RACKET_GROUP = "top_rackets"
RACKET_IMAGES = [f"pong/assets/images/racket.png"]
RACKET_WIDTH = 83
RACKET_HEIGHT = 28
RACKET_RATE = 6
RACKET_VELOCITY = 7

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "GET READY..."
PLAYER_ONE_WIN_SCREEN = "TOP PLAYER WINS"
PLAYER_TWO_WIN_SCREEN = "BOTTOM PLAYER WINS"