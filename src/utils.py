from typing import Tuple

import pygame
from pygame.typing import SequenceLike


def load_image(file_path: str, has_transparency: bool = True) -> pygame.Surface:
  surface = pygame.image.load(file_path)

  if has_transparency:
    return surface.convert_alpha()
  return surface


def render_text(
    text: str,
    font: pygame.font.Font,
    color: pygame.Color | SequenceLike[int] | str | int,
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
