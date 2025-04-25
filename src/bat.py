from os import path
from typing import List

import pygame

from src.collision import Collision, ObjectType
from src.constants import (
  BAT_INITIAL_COORD,
  BAT_VELOCITY,
  PLAYER_IMAGES_FOLDER_PATH,
  CoordPosition,
)
from src.interfaces import Updatable
from src.utils import (
  create_sprite_from_surface,
  follow_shadow,
  get_direction_from_pressed_keys,
  load_image,
)


class Bat(Updatable):
  def __init__(
      self,
      bat_group: pygame.sprite.Group,
      shadow_group: pygame.sprite.Group
  ):
    bat_surface = load_image(file_path=path.join(PLAYER_IMAGES_FOLDER_PATH, "bat.png"))

    self._bat_sprite, self._shadow_sprite = create_sprite_from_surface(
      surface=bat_surface,
      coord_position=CoordPosition.CENTER,
      coord=BAT_INITIAL_COORD,
      sprite_group=bat_group,
      shadow_group=shadow_group
    )

  def reacts_to_collisions(self) -> bool:
    return True

  def get_collisions(self) -> List[Collision]:
    return [
      Collision(
        object_type=ObjectType.BAT,
        rect=self._bat_sprite.rect
      )
    ]

  def has_collided(self, collision: Collision) -> None:
    if collision.object_type == ObjectType.WALL:
      if collision.rect.center[0] < self._bat_sprite.rect.center[0]:
        # Colliding to the left
        self._bat_sprite.rect.topleft = (collision.rect.topright[0], self._bat_sprite.rect.topleft[1])
      else:
        # Colliding to the right
        self._bat_sprite.rect.topright = (collision.rect.topleft[0], self._bat_sprite.rect.topleft[1])

      follow_shadow(self._bat_sprite, self._shadow_sprite)

  def update(self, delta_ms: float) -> None:
    direction = get_direction_from_pressed_keys()
    self._bat_sprite.rect.center += direction * BAT_VELOCITY * delta_ms

    follow_shadow(self._bat_sprite, self._shadow_sprite)
