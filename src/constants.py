import math
from os import path
from typing import Dict, Final, Tuple

import pygame

from src.notifications import NotificationType

# General constants
GAME_TITLE: Final[str] = "Breakout!"

INITIAL_SCORE: Final[int] = 0
INITIAL_LIVES: Final[int] = 3

FPS: Final[int] = 120

SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 600
SCREEN_COLOR: Final[Tuple[int, int, int]] = (0, 0, 0)

SHADOW_COLOR: Final[Tuple[int, int, int, int]] = (0, 0, 0, 150)
SHADOW_OFFSET: Final[pygame.math.Vector2] = pygame.math.Vector2(10, 10)

X_COORD: Final[int] = 0
Y_COORD: Final[int] = 1

X_RIGHT: Final[int] = 1
X_LEFT: Final[int] = -1

Y_UP: Final[int] = -1
Y_DOWN: Final[int] = 1

VECTOR_LEFT: Final[pygame.Vector2] = pygame.Vector2(X_LEFT, 0)
VECTOR_RIGHT: Final[pygame.Vector2] = pygame.Vector2(X_RIGHT, 0)

VECTOR_45_DEGREES_RIGHT_UP: Final[pygame.Vector2] = pygame.Vector2(X_RIGHT, Y_UP).normalize()
VECTOR_45_DEGREES_LEFT_UP: Final[pygame.Vector2] = pygame.Vector2(X_LEFT, Y_UP).normalize()

DEGREES_20_IN_RADIANS: Final[float] = math.radians(340)

VECTOR_20_DEGREES_RIGHT_UP: Final[pygame.Vector2] = pygame.Vector2(
  math.cos(DEGREES_20_IN_RADIANS),
  math.sin(DEGREES_20_IN_RADIANS)
)
VECTOR_20_DEGREES_LEFT_UP: Final[pygame.Vector2] = pygame.Vector2(
  -VECTOR_20_DEGREES_RIGHT_UP.x,
  VECTOR_20_DEGREES_RIGHT_UP.y
)

# Playground constants
BOUNDARIES_TOP_LEFT_COORD: Final[Tuple[int, int]] = (0, 0)

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

POINTS_FOR_BRICK: Final[int] = 1
POINTS_TO_GAIN_LIFE: Final[int] = 500

# Bat constants
BAT_INITIAL_COORD: Final[Tuple[float, float]] = (PLAYGROUND_WIDTH / 2 + PLAYGROUND_TOP_LEFT_COORD[X_COORD], 526)
BAT_SPEED: Final[float] = 500.0
BAT_QUARTER_WIDTH: Final[float] = 20

KEYS_TO_DIRECTIONS_MAPPING: Final[Dict[int, pygame.math.Vector2]] = {
  pygame.K_RIGHT: VECTOR_RIGHT,
  pygame.K_d: VECTOR_RIGHT,
  pygame.K_KP6: VECTOR_RIGHT,
  pygame.K_LEFT: VECTOR_LEFT,
  pygame.K_a: VECTOR_LEFT,
  pygame.K_KP4: VECTOR_LEFT
}

KEYS_TO_NOTIFICATION_MAPPING: Final[Dict[int, NotificationType]] = {
  pygame.K_SPACE: NotificationType.BALL_RELEASED
}

# Ball constants
BALL_INITIAL_COORD: Final[Tuple[float, float]] = (BAT_INITIAL_COORD[0], 515)
BALL_RADIUS: Final[int] = 4

BALL_SPEED_INITIAL: Final[float] = 300.0
BALL_SPEED_MAX: Final[float] = 1500.0
BALL_SPEED_INCREMENT: Final[float] = 20.0

# Brick constants
BRICKS_TOP_COORD: Final[Tuple[float, float]] = (80, 112)
BRICK_WIDTH: Final[float] = 50
BRICK_HEIGHT: Final[float] = 20

BRICKS_HORIZONTAL_COUNT: Final[int] = 10
BRICKS_VERTICAL_COUNT: Final[int] = 5

EXTRA_DATA_BRICK_RECT: Final[str] = "brick_rect"

# File system constants
CONTENT_FOLDER_PATH: Final[str] = path.abspath(path.join(path.dirname(__file__), "..", "content"))

IMAGES_FOLDER_PATH: Final[str] = path.join(CONTENT_FOLDER_PATH, "images")
BRICK_IMAGES_FOLDER_PATH: Final[str] = path.join(IMAGES_FOLDER_PATH, "bricks")
PLAYER_IMAGES_FOLDER_PATH: Final[str] = path.join(IMAGES_FOLDER_PATH, "player")
STAGE_IMAGES_FOLDER_PATH: Final[str] = path.join(IMAGES_FOLDER_PATH, "stage")

FONTS_FOLDER_PATH: Final[str] = path.join(CONTENT_FOLDER_PATH, "fonts")

AUDIO_FOLDER_PATH: Final[str] = path.join(CONTENT_FOLDER_PATH, "audio")
