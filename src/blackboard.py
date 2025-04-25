from dataclasses import dataclass


@dataclass
class Blackboard:
  score: int
  lives: int

  def copy(self) -> "Blackboard":
    return Blackboard(
      score=self.score,
      lives=self.lives
    )
