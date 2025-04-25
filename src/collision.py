from dataclasses import dataclass
from enum import Enum

import pygame


class CollisionType(Enum):
  WALL = 1
  BAT = 2
  BALL = 3
  BRICK = 4


@dataclass
class Collision:
  type: CollisionType
  rect: pygame.Rect | pygame.FRect
