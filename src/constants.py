from enum import Enum
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

# Bat constants
BAT_INITIAL_COORD: Final[Tuple[float, float]] = (PLAYGROUND_WIDTH / 2 + PLAYGROUND_TOP_LEFT_COORD[X_COORD], 526)
BAT_VELOCITY: Final[float] = 400.0

MOVE_RIGHT_DIRECTION: Final[pygame.math.Vector2] = pygame.math.Vector2(1.0, 0.0)
MOVE_LEFT_DIRECTION: Final[pygame.math.Vector2] = pygame.math.Vector2(-1.0, 0.0)

KEYS_TO_DIRECTIONS_MAPPING: Final[Dict[int, pygame.math.Vector2]] = {
  pygame.K_RIGHT: MOVE_RIGHT_DIRECTION,
  pygame.K_d: MOVE_RIGHT_DIRECTION,
  pygame.K_KP6: MOVE_RIGHT_DIRECTION,
  pygame.K_LEFT: MOVE_LEFT_DIRECTION,
  pygame.K_a: MOVE_LEFT_DIRECTION,
  pygame.K_KP4: MOVE_LEFT_DIRECTION
}

KEYS_TO_NOTIFICATION_MAPPING: Final[Dict[int, NotificationType]] = {
  pygame.K_SPACE: NotificationType.BALL_RELEASED
}

# Ball constants
BALL_INITIAL_COORD: Final[Tuple[float, float]] = (BAT_INITIAL_COORD[0], 515)
VERTICAL_OFFSET_BETWEEN_BALL_AND_BAT: Final[float] = BAT_INITIAL_COORD[Y_COORD] - BALL_INITIAL_COORD[Y_COORD]

BALL_VELOCITY: Final[float] = 200.0

# File system constants
CONTENT_FOLDER_PATH: Final[str] = path.abspath(path.join(path.dirname(__file__), "..", "content"))

IMAGES_FOLDER_PATH: Final[str] = path.join(CONTENT_FOLDER_PATH, "images")
BRICK_IMAGES_FOLDER_PATH: Final[str] = path.join(IMAGES_FOLDER_PATH, "bricks")
PLAYER_IMAGES_FOLDER_PATH: Final[str] = path.join(IMAGES_FOLDER_PATH, "player")
STAGE_IMAGES_FOLDER_PATH: Final[str] = path.join(IMAGES_FOLDER_PATH, "stage")

FONTS_FOLDER_PATH: Final[str] = path.join(CONTENT_FOLDER_PATH, "fonts")
