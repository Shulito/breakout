from abc import ABC, abstractmethod


class Updatable(ABC):
  @abstractmethod
  def update(self, delta_ms: float) -> None:
    pass
