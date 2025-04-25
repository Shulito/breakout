from src.bat import Bat
from src.blackboard import Blackboard
from src.collision import Collision
from src.constants import *
from src.interfaces import Updatable
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
      lives=INITIAL_LIVES
    )

    playground = Playground(
      blackboard=self._blackboard,
      pattern_group=self._background_group,
      boundaries_group=self._foreground_group,
      text_group=self._foreground_group
    )

    bat = Bat(
      bat_group=self._middleground_group,
      shadow_group=self._background_group
    )

    self._updatable_objects = [
      playground,
      bat
    ]

  def __del__(self):
    pygame.quit()

  def _find_collision(self, delta_ms: float, object_to_check_collision: Updatable) -> Collision | None:
    collisions_to_check = object_to_check_collision.get_collisions(delta_ms)
    if not collisions_to_check:
      return None

    for game_object in self._updatable_objects:
      if object_to_check_collision == game_object:
        continue

      for collision1 in collisions_to_check:
        for collision2 in game_object.get_collisions(delta_ms):
          if pygame.FRect.colliderect(collision1.rect, collision2.rect):
            return collision2

    return None

  def run(self) -> None:
    running = True

    while running:
      delta_ms = self._clock.tick(FPS) / 1000

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      if not running:
        break

      for game_object in self._updatable_objects:
        collision = self._find_collision(delta_ms, game_object)

        game_object.update(
          delta_ms=delta_ms,
          colliding_with=collision
        )

      self._screen.fill(SCREEN_COLOR)
      self._background_group.draw(self._screen)
      self._middleground_group.draw(self._screen)
      self._foreground_group.draw(self._screen)

      pygame.display.update()
