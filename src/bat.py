from typing import List

from pygame import BLEND_RGBA_MULT

from src.collision import Collision, ObjectType
from src.constants import *
from src.interfaces import Updatable
from src.utils import load_image, get_direction_from_pressed_keys
from os import path


class Bat(Updatable):
  def __init__(
      self,
      bat_group: pygame.sprite.Group,
      shadow_group: pygame.sprite.Group
  ):
    bat_surface = load_image(file_path=path.join(PLAYER_IMAGES_FOLDER_PATH, "bat.png"))

    shadow_surface = bat_surface.copy()
    shadow_surface.fill(SHADOW_COLOR, None, BLEND_RGBA_MULT)

    self._bat_sprite = pygame.sprite.Sprite(bat_group)
    self._bat_sprite.image = bat_surface
    self._bat_sprite.rect = self._bat_sprite.image.get_frect(center=BAT_INITIAL_COORD)

    self._shadow_sprite = pygame.sprite.Sprite(shadow_group)
    self._shadow_sprite.image = shadow_surface
    self._shadow_sprite.rect = self._shadow_sprite.image.get_frect(center=BAT_INITIAL_COORD)
    self._shadow_sprite.rect.center += SHADOW_OFFSET

  def reacts_to_collisions(self) -> bool:
    return True

  def get_collisions(self) -> List[Collision]:
    return [
      Collision(
        object_type=ObjectType.BAT,
        rect=self._bat_sprite.rect
      )
    ]

  def _follow_shadow(self) -> None:
    self._shadow_sprite.rect.center = self._bat_sprite.rect.center + SHADOW_OFFSET

  def has_collided(self, collision: Collision) -> None:
    if collision.object_type == ObjectType.WALL:
      if collision.rect.center[0] < self._bat_sprite.rect.center[0]:
        # Colliding to the left
        self._bat_sprite.rect.topleft = (collision.rect.topright[0], self._bat_sprite.rect.topleft[1])
      else:
        # Colliding to the right
        self._bat_sprite.rect.topright = (collision.rect.topleft[0], self._bat_sprite.rect.topleft[1])

      self._follow_shadow()

  def update(self, delta_ms: float) -> None:
    direction = get_direction_from_pressed_keys()
    self._bat_sprite.rect.center += direction * BAT_VELOCITY * delta_ms

    self._follow_shadow()
