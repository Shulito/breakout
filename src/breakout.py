import pygame

from src.blackboard import Blackboard
from src.constants import *
from src.playground import Playground


class Breakout:
  def __init__(self):
    pygame.init()

    pygame.display.set_caption(GAME_TITLE)
    self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self._clock = pygame.time.Clock()

    self._background_group = pygame.sprite.Group()
    self._middleground_group = pygame.sprite.Group()
    self._foreground_group = pygame.sprite.Group()

    self._blackboard = Blackboard(
      score=INITIAL_SCORE,
      lives=INITIAL_LIVES,
    )

    self._game_objects = [
      Playground(
        blackboard=self._blackboard,
        pattern_group=self._background_group,
        boundaries_group=self._foreground_group,
        text_group=self._foreground_group,
      )
    ]

  def __del__(self):
    pygame.quit()

  def run(self) -> None:
    running = True

    while running:
      delta_ms = self._clock.tick(FPS) / 1000

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      for game_object in self._game_objects:
        game_object.update(delta_ms)

      self._screen.fill(SCREEN_COLOR)
      self._background_group.draw(self._screen)
      self._middleground_group.draw(self._screen)
      self._foreground_group.draw(self._screen)

      pygame.display.update()
