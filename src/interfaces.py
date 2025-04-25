from abc import ABC, abstractmethod
from typing import List
from src.collision import Collision


class Updatable(ABC):
  @abstractmethod
  def get_collisions(self) -> List[Collision]:
    pass

  @abstractmethod
  def has_collided(self, colliding_with: Collision) -> None:
    pass

  @abstractmethod
  def update(self, delta_ms: float) -> None:
    pass
