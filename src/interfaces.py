from abc import ABC, abstractmethod
from typing import List, Set

from src.blackboard import Blackboard
from src.collision import Collision
from src.notifications import NotificationType


class GameObject(ABC):
  @abstractmethod
  def reacts_to_collisions(self) -> bool:
    pass

  @abstractmethod
  def get_collisions(self) -> List[Collision]:
    pass

  @abstractmethod
  def has_collided(self, collision: Collision) -> None:
    pass

  @abstractmethod
  def get_interested_notification_types(self) -> Set[NotificationType] | None:
    pass

  @abstractmethod
  def emit_notification(self) -> NotificationType | None:
    pass

  @abstractmethod
  def receive_notification(self, notification_type: NotificationType, blackboard: Blackboard) -> None:
    pass

  @abstractmethod
  def update(self, delta_ms: float) -> None:
    pass
