from src.constants import *
from typing import Tuple

import pygame


def get_direction_from_pressed_keys() -> pygame.math.Vector2:
  pressed_keys = pygame.key.get_pressed()
  final_direction = pygame.math.Vector2(0.0, 0.0)

  for key in KEYS_TO_DIRECTIONS_MAPPING.keys():
    if pressed_keys[key]:
      final_direction += KEYS_TO_DIRECTIONS_MAPPING[key]

  return final_direction.normalize() if final_direction else final_direction


def load_image(file_path: str, has_transparency: bool = True) -> pygame.Surface:
  surface = pygame.image.load(file_path)

  if has_transparency:
    return surface.convert_alpha()
  return surface


def render_text(
    text: str,
    font: pygame.font.Font,
    color: pygame.Color | pygame.typing.SequenceLike[int] | str | int,
    group_to_add: pygame.sprite.Group,
    coordinates: Tuple[int, int],
) -> pygame.sprite.Sprite:
  surface = font.render(
    text=text,
    antialias=True,
    color=color,
  )

  sprite = pygame.sprite.Sprite(group_to_add)
  sprite.image = surface
  sprite.rect = sprite.image.get_frect(topleft=coordinates)

  return sprite
