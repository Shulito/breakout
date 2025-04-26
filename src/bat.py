from os import path
from typing import List, Set

import pygame

from src.blackboard import Blackboard
from src.collision import Collision, ObjectType
from src.constants import (
  BAT_INITIAL_COORD,
  BAT_VELOCITY,
  PLAYER_IMAGES_FOLDER_PATH,
  X_COORD,
  Y_COORD,
)
from src.coord import CoordPosition
from src.interfaces import GameObject
from src.notifications import NotificationType
from src.utils import (
  create_sprite_from_surface,
  follow_shadow,
  get_direction_from_pressed_keys,
  load_image,
)


class Bat(GameObject):
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

  def get_frect(self) -> pygame.FRect:
    return self._bat_sprite.rect

  def reacts_to_collisions(self) -> bool:
    return True

  def get_collision_rects(self) -> List[Collision]:
    return [
      Collision(
        object_type=ObjectType.BAT,
        rect=self._bat_sprite.rect
      )
    ]

  def has_collided(self, collision: Collision) -> None:
    match collision.object_type:
      case ObjectType.SIDE_WALL:
        if collision.rect.center[X_COORD] < self._bat_sprite.rect.center[X_COORD]:
          # Colliding to the left
          self._bat_sprite.rect.topleft = (
            collision.rect.topright[X_COORD],
            self._bat_sprite.rect.topleft[Y_COORD]
          )
        else:
          # Colliding to the right
          self._bat_sprite.rect.topright = (
            collision.rect.topleft[X_COORD],
            self._bat_sprite.rect.topleft[Y_COORD]
          )

        follow_shadow(self._bat_sprite, self._shadow_sprite)

  def get_interested_notification_types(self) -> Set[NotificationType] | None:
    return None

  def emit_notification(self) -> NotificationType | None:
    return None

  def receive_notification(self, notification_type: NotificationType, blackboard: Blackboard) -> None:
    pass

  def update(self, delta_ms: float) -> None:
    direction = get_direction_from_pressed_keys()
    self._bat_sprite.rect.center += direction * BAT_VELOCITY * delta_ms

    follow_shadow(self._bat_sprite, self._shadow_sprite)
