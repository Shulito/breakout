from dataclasses import dataclass
from enum import Enum

import pygame


class ObjectType(Enum):
  BALL = 1
  BAT = 2
  BRICK = 3
  SIDE_WALL = 4
  TOP_WALL = 5


@dataclass
class Collision:
  object_type: ObjectType
  rect: pygame.FRect
