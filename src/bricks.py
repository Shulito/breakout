from os import path
from typing import Any, Dict, List, Set, Tuple

import pygame

from src.blackboard import Blackboard
from src.collision import Collision, ObjectType
from src.constants import (
  BRICK_HEIGHT,
  BRICK_IMAGES_FOLDER_PATH,
  BRICK_WIDTH,
  BRICKS_HORIZONTAL_COUNT,
  BRICKS_TOP_COORD,
  BRICKS_VERTICAL_COUNT,
  EXTRA_DATA_BRICK_RECT,
  X_COORD,
  Y_COORD,
)
from src.coord import CoordPosition
from src.interfaces import GameObject
from src.notifications import NotificationType
from src.utils import create_sprite_from_surface, load_image, rect_to_hashable_value


class Brick:
  def __init__(
      self,
      surface: pygame.Surface,
      coord: Tuple[float, float],
      coord_position: CoordPosition,
      brick_group: pygame.sprite.Group,
      shadow_group: pygame.sprite.Group
  ):
    self._brick_sprite, self._shadow_sprite = create_sprite_from_surface(
      surface=surface,
      coord_position=coord_position,
      coord=coord,
      sprite_group=brick_group,
      shadow_group=shadow_group
    )

  def __del__(self):
    self._brick_sprite.kill()
    self._shadow_sprite.kill()

  def get_rect(self) -> pygame.FRect:
    return self._brick_sprite.rect


class BrickLayer(GameObject):
  def __init__(
      self,
      bricks_group: pygame.sprite.Group,
      shadow_group: pygame.sprite.Group
  ):
    self._bricks_group = bricks_group
    self._shadow_group = shadow_group

    self._brick_surfaces: List[pygame.Surface] = [
      load_image(file_path=path.join(BRICK_IMAGES_FOLDER_PATH, "red.png"), has_transparency=False),
      load_image(file_path=path.join(BRICK_IMAGES_FOLDER_PATH, "yellow.png"), has_transparency=False),
      load_image(file_path=path.join(BRICK_IMAGES_FOLDER_PATH, "blue.png"), has_transparency=False),
      load_image(file_path=path.join(BRICK_IMAGES_FOLDER_PATH, "purple.png"), has_transparency=False),
      load_image(file_path=path.join(BRICK_IMAGES_FOLDER_PATH, "green.png"), has_transparency=False)
    ]

    self._bricks: Dict[str, Brick] = {}

  def _lay_bricks(self) -> None:
    self._bricks.clear()

    for i in range(BRICKS_HORIZONTAL_COUNT):
      for j in range(BRICKS_VERTICAL_COUNT):
        brick_coord = (
          BRICKS_TOP_COORD[X_COORD] + i * BRICK_WIDTH,
          BRICKS_TOP_COORD[Y_COORD] + j * BRICK_HEIGHT
        )

        brick = Brick(
          surface=self._brick_surfaces[j],
          coord=brick_coord,
          coord_position=CoordPosition.TOP_LEFT,
          brick_group=self._bricks_group,
          shadow_group=self._shadow_group
        )

        self._bricks[rect_to_hashable_value(brick.get_rect())] = brick

  def reacts_to_collisions(self) -> bool:
    return True

  def get_collision_rects(self) -> List[Collision]:
    return [
      Collision(
        object_type=ObjectType.BRICK,
        rect=brick.get_rect()
      )
      for brick in self._bricks.values()
    ]

  def has_collided(self, collision: Collision) -> None:
    return

  def get_interested_notification_types(self) -> Set[NotificationType] | None:
    return {
      NotificationType.BRICK_DESTROYED,
      NotificationType.BRICKS_DESTROYED
    }

  def receive_notification(
      self,
      notification_type: NotificationType,
      blackboard: Blackboard,
      extra_data: Dict[Any, Any] = None
  ) -> None:
    match notification_type:
      case NotificationType.INITIAL_SETUP | NotificationType.BRICKS_DESTROYED:
        self._lay_bricks()
      case NotificationType.BRICK_DESTROYED:
        self._bricks.pop(rect_to_hashable_value(extra_data[EXTRA_DATA_BRICK_RECT]))

  def update(self, delta_ms: float) -> None:
    return
