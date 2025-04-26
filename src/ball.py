from os import path
from typing import List, Set, Tuple

import pygame

from src.blackboard import Blackboard
from src.collision import Collision, ObjectType
from src.constants import BALL_INITIAL_COORD, STAGE_IMAGES_FOLDER_PATH, CoordPosition
from src.interfaces import GameObject
from src.notifications import NotificationType
from src.utils import create_sprite_from_surface, load_image


class Ball(GameObject):
  def __init__(
      self,
      ball_group: pygame.sprite.Group,
      shadow_group: pygame.sprite.Group,
  ):
    ball_surface = load_image(file_path=path.join(STAGE_IMAGES_FOLDER_PATH, "ball.png"))

    self._ball_sprite, self._shadow_sprite = create_sprite_from_surface(
      surface=ball_surface,
      coord_position=CoordPosition.CENTER,
      coord=BALL_INITIAL_COORD,
      sprite_group=ball_group,
      shadow_group=shadow_group
    )

  def reacts_to_collisions(self) -> bool:
    return True

  def get_collisions(self) -> List[Collision]:
    return [
      Collision(
        object_type=ObjectType.BALL,
        rect=self._ball_sprite.rect
      )
    ]

  def has_collided(self, collision: Collision) -> None:
    pass

  def get_interested_notification_types(self) -> Set[NotificationType] | None:
    return None

  def emit_notifications(self) -> Set[NotificationType] | None:
    return None

  def receive_notification(self, notification: NotificationType, blackboard: Blackboard) -> None:
    pass

  def update(self, delta_ms: float) -> None:
    pass
