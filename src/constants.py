from os import path
from typing import Final, Tuple

GAME_TITLE: Final[str] = "Breakout!"

INITIAL_SCORE: Final[int] = 0
INITIAL_LIVES: Final[int] = 3

FPS: Final[int] = 60

SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 600
SCREEN_COLOR: Final[str] = "#000000"

PLAYGROUND_TOP_LEFT_COORD: Final[Tuple[int, int]] = (80, 32)
PLAYGROUND_WIDTH: Final[int] = 500
PLAYGROUND_HEIGHT: Final[int] = 568

PLAYGROUND_SCORE_TITLE: Final[str] = "Score"
PLAYGROUND_SCORE_TITLE_COORD: Final[Tuple[int, int]] = (608, 16)
PLAYGROUND_SCORE_VALUE_COORD: Final[Tuple[int, int]] = (608, 66)
PLAYGROUND_LIVES_TITLE: Final[str] = "Lives"
PLAYGROUND_LIVES_TITLE_COORD: Final[Tuple[int, int]] = (608, 106)
PLAYGROUND_LIVES_VALUE_COORD: Final[Tuple[int, int]] = (608, 156)

TITLE_FONT_SIZE: Final[int] = 70
TITLE_FONT_COLOR: Final[str] = "#ffffff"
CONTENT_FONT_SIZE: Final[int] = 62
CONTENT_FONT_COLOR: Final[str] = "#d62d24"

CONTENT_FOLDER_PATH: Final[str] = path.abspath(path.join(path.dirname(__file__), "..", "content"))

IMAGES_FOLDER_PATH: Final[str] = path.join(CONTENT_FOLDER_PATH, "images")
BRICK_IMAGES_FOLDER_PATH: Final[str] = path.join(IMAGES_FOLDER_PATH, "bricks")
PLAYER_IMAGES_FOLDER_PATH: Final[str] = path.join(IMAGES_FOLDER_PATH, "player")
STAGE_IMAGES_FOLDER_PATH: Final[str] = path.join(IMAGES_FOLDER_PATH, "stage")

FONTS_FOLDER_PATH: Final[str] = path.join(CONTENT_FOLDER_PATH, "fonts")
