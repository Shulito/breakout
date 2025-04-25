from typing import List

from src.blackboard import Blackboard
from src.collision import Collision, CollisionType
from src.constants import *
from src.interfaces import Updatable
from src.utils import load_image, render_text
from os import path


class Playground(Updatable):
  def __init__(
      self,
      blackboard: Blackboard,
      pattern_group: pygame.sprite.Group,
      boundaries_group: pygame.sprite.Group,
      text_group: pygame.sprite.Group
  ):
    self._blackboard = blackboard
    self._previous_blackboard = None
    self._score_title_sprite = None
    self._score_value_sprite = None
    self._lives_title_sprite = None
    self._lives_value_sprite = None

    # fonts
    self._text_group = text_group

    self._title_font = pygame.font.Font(
      filename=path.join(FONTS_FOLDER_PATH, "Arcade.ttf"),
      size=TITLE_FONT_SIZE
    )
    self._content_font = pygame.font.Font(
      filename=path.join(FONTS_FOLDER_PATH, "Arcade.ttf"),
      size=CONTENT_FONT_SIZE
    )

    # background pattern
    pattern_surface = load_image(
      file_path=path.join(STAGE_IMAGES_FOLDER_PATH, "pattern.png"),
      has_transparency=False
    )

    pattern_surface_tiled = pygame.Surface((PLAYGROUND_WIDTH, PLAYGROUND_HEIGHT))
    for x in range(0, PLAYGROUND_WIDTH, pattern_surface.get_width()):
      for y in range(0, PLAYGROUND_HEIGHT, pattern_surface.get_height()):
        pattern_surface_tiled.blit(pattern_surface, (x, y))

    pattern_sprite = pygame.sprite.Sprite(pattern_group)
    pattern_sprite.image = pattern_surface_tiled
    pattern_sprite.rect = pattern_sprite.image.get_frect(topleft=PLAYGROUND_TOP_LEFT_COORD)

    # boundaries
    boundaries_surface = load_image(path.join(STAGE_IMAGES_FOLDER_PATH, "boundaries.png"))

    boundaries_sprite = pygame.sprite.Sprite(boundaries_group)
    boundaries_sprite.image = boundaries_surface
    boundaries_sprite.rect = boundaries_sprite.image.get_frect(topleft=(0, 0))

    # Collision rects
    self._collision_rects = [
      Collision(
        type=CollisionType.WALL,
        rect=pygame.FRect((0, 32), (80, 567))
      ),
      Collision(
        type=CollisionType.WALL,
        rect=pygame.FRect((580, 32), (80, 567))
      ),
      Collision(
        type=CollisionType.WALL,
        rect=pygame.FRect((0, 0), (595, 31))
      ),
    ]

  def get_collisions(self, delta_ms: float) -> List[Collision]:
    return self._collision_rects

  def update(self, delta_ms: float, colliding_with: Collision | None) -> None:
    if self._previous_blackboard == self._blackboard:
      # Same values as before, no need to update the textures
      return

    self._previous_blackboard = self._blackboard.clone()

    # remove old values from sprite group
    if self._score_title_sprite:
      self._score_title_sprite.kill()
    if self._score_value_sprite:
      self._score_value_sprite.kill()
    if self._lives_title_sprite:
      self._lives_title_sprite.kill()
    if self._lives_value_sprite:
      self._lives_value_sprite.kill()

    # create new sprites with new values
    self._score_title_sprite = render_text(
      text=PLAYGROUND_SCORE_TITLE,
      font=self._title_font,
      color=TITLE_FONT_COLOR,
      group_to_add=self._text_group,
      coordinates=PLAYGROUND_SCORE_TITLE_COORD
    )

    self._score_value_sprite = render_text(
      text=str(self._blackboard.score),
      font=self._content_font,
      color=CONTENT_FONT_COLOR,
      group_to_add=self._text_group,
      coordinates=PLAYGROUND_SCORE_VALUE_COORD
    )

    self._lives_title_sprite = render_text(
      text=PLAYGROUND_LIVES_TITLE,
      font=self._title_font,
      color=TITLE_FONT_COLOR,
      group_to_add=self._text_group,
      coordinates=PLAYGROUND_LIVES_TITLE_COORD
    )

    self._lives_value_sprite = render_text(
      text=str(self._blackboard.lives),
      font=self._content_font,
      color=CONTENT_FONT_COLOR,
      group_to_add=self._text_group,
      coordinates=PLAYGROUND_LIVES_VALUE_COORD
    )
