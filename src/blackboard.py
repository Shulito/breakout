from dataclasses import dataclass

import pygame


@dataclass
class Blackboard:
  score: int
  lives: int
  bat_frect: pygame.FRect
