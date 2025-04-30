from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict

import pygame

from src.constants import X_COORD, Y_COORD


class ObjectType(Enum):
  BALL = 1
  BAT = 2
  BRICK = 3
  PIT = 4
  SIDE_WALL = 5
  TOP_WALL = 6


@dataclass
class Collision:
  object_type: ObjectType
  rect: pygame.FRect


def resolve_collision_by_trajectory(
    previous_rect: pygame.FRect,
    rect: pygame.FRect,
    colliding_rect: pygame.FRect
) -> None:
  slope = rect.center[Y_COORD] - previous_rect.center[Y_COORD]
  slope /= rect.center[X_COORD] - previous_rect.center[X_COORD]
  x_value_to_move = -1 if rect.center[X_COORD] > previous_rect.center[X_COORD] else 1

  new_x = x_value_to_move + rect.center[X_COORD]
  new_y = slope * rect.center[X_COORD] - slope * previous_rect.center[X_COORD] + previous_rect.center[Y_COORD]
  rect.center = (new_x, new_y)

  while pygame.FRect.colliderect(rect, colliding_rect):
    new_x = x_value_to_move + rect.center[X_COORD]
    new_y = slope * rect.center[X_COORD] - slope * previous_rect.center[X_COORD] + previous_rect.center[Y_COORD]
    rect.center = (new_x, new_y)


def resolve_collision_by_direction(
    direction: pygame.Vector2,
    rect: pygame.FRect,
    colliding_rect: pygame.FRect
) -> None:
  rect.center += direction
  while pygame.FRect.colliderect(rect, colliding_rect):
    rect.center += direction
