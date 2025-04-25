from dataclasses import dataclass
from enum import Enum

import pygame


class ObjectType(Enum):
  WALL = 1
  BAT = 2
  BALL = 3
  BRICK = 4


@dataclass
class Collision:
  object_type: ObjectType
  rect: pygame.FRect
