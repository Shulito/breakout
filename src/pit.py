from typing import List, Set

import pygame

from src.blackboard import Blackboard
from src.collision import Collision, ObjectType
from src.interfaces import GameObject
from src.notifications import NotificationType


class Pit(GameObject):
  def __init__(self):
    self._emit_notification = False

  def reacts_to_collisions(self) -> bool:
    return True

  def get_collision_rects(self) -> List[Collision]:
    return [
      Collision(
        object_type=ObjectType.PIT,
        rect=pygame.FRect((0, 600), (800, 200))
      )
    ]

  def has_collided(self, collision: Collision) -> None:
    match collision.object_type:
      case ObjectType.BALL:
        self._emit_notification = True

  def get_interested_notification_types(self) -> Set[NotificationType] | None:
    return None

  def emit_notification(self) -> NotificationType | None:
    if self._emit_notification:
      self._emit_notification = False
      return NotificationType.BALL_MISSED

    return None

  def receive_notification(self, notification_type: NotificationType, blackboard: Blackboard) -> None:
    return None

  def update(self, delta_ms: float) -> None:
    return
