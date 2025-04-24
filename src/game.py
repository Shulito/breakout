from abc import abstractmethod


class GameObject:
  @abstractmethod
  def update(self, delta_ms: float) -> None:
    pass
