from abc import ABC, abstractmethod
from typing import List
from src.collision import Collision


class Updatable(ABC):
  @abstractmethod
  def get_collisions(self, delta_ms: float) -> List[Collision]:
    pass

  @abstractmethod
  def update(self, delta_ms: float, colliding_with: Collision | None) -> None:
    pass
