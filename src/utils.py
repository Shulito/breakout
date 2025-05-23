from typing import Set, Tuple

import pygame
from pygame import BLEND_RGBA_MULT

from src.constants import (
  KEYS_TO_DIRECTIONS_MAPPING,
  KEYS_TO_NOTIFICATION_MAPPING,
  SHADOW_COLOR,
  SHADOW_OFFSET,
)
from src.coord import CoordPosition
from src.notifications import NotificationType


def rect_to_hashable_value(rect: pygame.FRect) -> str:
  return f"{rect.x}:{rect.y}:{rect.width}:{rect.height}"


def get_direction_from_pressed_keys() -> pygame.math.Vector2:
  pressed_keys = pygame.key.get_pressed()
  final_direction = pygame.math.Vector2(0.0, 0.0)

  for key in KEYS_TO_DIRECTIONS_MAPPING.keys():
    if pressed_keys[key]:
      final_direction += KEYS_TO_DIRECTIONS_MAPPING[key]

  return final_direction.normalize() if final_direction else final_direction


def get_notifications_from_pressed_keys() -> Set[NotificationType]:
  pressed_keys = pygame.key.get_pressed()
  notifications = set()

  for key in KEYS_TO_NOTIFICATION_MAPPING.keys():
    if pressed_keys[key]:
      notifications.add(KEYS_TO_NOTIFICATION_MAPPING[key])

  return notifications


def load_image(file_path: str, has_transparency: bool = True) -> pygame.Surface:
  surface = pygame.image.load(file_path)

  if has_transparency:
    return surface.convert_alpha()
  return surface


def get_rect_from_sprite(
    sprite: pygame.sprite.Sprite,
    coord: Tuple[int | float, int | float],
    coord_position: CoordPosition
) -> pygame.FRect:
  match coord_position:
    case CoordPosition.TOP_LEFT:
      return sprite.image.get_frect(topleft=coord)
    case CoordPosition.CENTER:
      return sprite.image.get_frect(center=coord)
    case _:
      raise ValueError("Unexpected coord position")


def create_sprite_from_surface(
    surface: pygame.Surface,
    coord_position: CoordPosition,
    coord: Tuple[int | float, int | float],
    sprite_group: pygame.sprite.Group,
    shadow_group: pygame.sprite.Group | None = None
) -> Tuple[pygame.sprite.Sprite, pygame.sprite.Sprite | None]:
  sprite = pygame.sprite.Sprite(sprite_group)
  sprite.image = surface
  sprite.rect = get_rect_from_sprite(
    sprite=sprite,
    coord=coord,
    coord_position=coord_position
  )

  shadow_sprite = None
  if shadow_group:
    shadow_surface = surface.copy()
    shadow_surface.fill(SHADOW_COLOR, None, BLEND_RGBA_MULT)

    shadow_sprite = pygame.sprite.Sprite(shadow_group)
    shadow_sprite.image = shadow_surface
    shadow_sprite.rect = get_rect_from_sprite(
      sprite=shadow_sprite,
      coord=coord,
      coord_position=coord_position
    )

    shadow_sprite.rect.center += SHADOW_OFFSET

  return sprite, shadow_sprite


def follow_shadow(
    sprite: pygame.sprite.Sprite,
    shadow: pygame.sprite.Sprite
) -> None:
  shadow.rect.center = sprite.rect.center + SHADOW_OFFSET


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
