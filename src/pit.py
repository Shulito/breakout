from typing import Any, Dict, List, Set

import pygame

from src.blackboard import Blackboard
from src.collision import Collision, ObjectType
from src.interfaces import GameObject
from src.notifications import NotificationsSink, NotificationType


class Pit(GameObject):
  def __init__(
      self,
      notifications_sink: NotificationsSink
  ):
    self._notifications_sink = notifications_sink

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
        self._notifications_sink.write(NotificationType.BALL_MISSED)

  def get_interested_notification_types(self) -> Set[NotificationType] | None:
    return None

  def receive_notification(
      self,
      notification_type: NotificationType,
      blackboard: Blackboard,
      extra_data: Dict[Any, Any] = None
  ) -> None:
    return

  def update(self, delta_ms: float) -> None:
    return
