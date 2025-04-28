from dataclasses import dataclass
from enum import Enum

import pygame


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
