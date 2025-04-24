from os import path
from typing import Final, Tuple

import pygame

# General constants
GAME_TITLE: Final[str] = "Breakout!"

INITIAL_SCORE: Final[int] = 0
INITIAL_LIVES: Final[int] = 3

FPS: Final[int] = 60

SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 600
SCREEN_COLOR: Final[Tuple[int, int, int]] = (0, 0, 0)

# Playground constants
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
TITLE_FONT_COLOR: Final[Tuple[int, int, int]] = (255, 255, 255)
CONTENT_FONT_SIZE: Final[int] = 62
CONTENT_FONT_COLOR: Final[Tuple[int, int, int]] = (214, 45, 36)

SHADOW_COLOR: Final[Tuple[int, int, int, int]] = (0, 0, 0, 150)
SHADOW_OFFSET: Final[pygame.math.Vector2] = pygame.math.Vector2(10, 10)

# Bat constants
BAT_INITIAL_COORD: Final[Tuple[float, float]] = (PLAYGROUND_WIDTH / 2 + PLAYGROUND_TOP_LEFT_COORD[0], 526)
BAT_VELOCITY: Final[float] = 350.0

MOVE_RIGHT_DIRECTION: Final[pygame.math.Vector2] = pygame.math.Vector2(1.0, 0.0)
MOVE_LEFT_DIRECTION: Final[pygame.math.Vector2] = pygame.math.Vector2(-1.0, 0.0)

KEYS_TO_DIRECTIONS_MAPPING: Final[dict[int, pygame.math.Vector2]] = {
  pygame.K_RIGHT: MOVE_RIGHT_DIRECTION,
  pygame.K_d: MOVE_RIGHT_DIRECTION,
  pygame.K_KP6: MOVE_RIGHT_DIRECTION,
  pygame.K_LEFT: MOVE_LEFT_DIRECTION,
  pygame.K_a: MOVE_LEFT_DIRECTION,
  pygame.K_KP4: MOVE_LEFT_DIRECTION,
}

# File system constants
CONTENT_FOLDER_PATH: Final[str] = path.abspath(path.join(path.dirname(__file__), "..", "content"))

IMAGES_FOLDER_PATH: Final[str] = path.join(CONTENT_FOLDER_PATH, "images")
BRICK_IMAGES_FOLDER_PATH: Final[str] = path.join(IMAGES_FOLDER_PATH, "bricks")
PLAYER_IMAGES_FOLDER_PATH: Final[str] = path.join(IMAGES_FOLDER_PATH, "player")
STAGE_IMAGES_FOLDER_PATH: Final[str] = path.join(IMAGES_FOLDER_PATH, "stage")

FONTS_FOLDER_PATH: Final[str] = path.join(CONTENT_FOLDER_PATH, "fonts")
