from abc import ABC, abstractmethod
from typing import List

from src.collision import Collision


class Updatable(ABC):
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
  def update(self, delta_ms: float) -> None:
    pass
