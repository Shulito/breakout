from os import path
from typing import List, Set

import pygame

from src.blackboard import Blackboard
from src.collision import Collision, ObjectType
from src.constants import (
  BALL_INITIAL_COORD,
  BALL_VELOCITY,
  STAGE_IMAGES_FOLDER_PATH,
  VERTICAL_OFFSET_BETWEEN_BALL_AND_BAT,
  X_COORD,
  X_LEFT,
  X_RIGHT,
  Y_COORD,
  Y_DOWN,
  Y_UP,
  CoordPosition,
)
from src.interfaces import GameObject
from src.notifications import NotificationType
from src.utils import create_sprite_from_surface, follow_shadow, load_image


class Ball(GameObject):
  def __init__(
      self,
      ball_group: pygame.sprite.Group,
      shadow_group: pygame.sprite.Group,
  ):
    ball_surface = load_image(file_path=path.join(STAGE_IMAGES_FOLDER_PATH, "ball.png"))

    self._ball_sprite, self._shadow_sprite = create_sprite_from_surface(
      surface=ball_surface,
      coord_position=CoordPosition.CENTER,
      coord=BALL_INITIAL_COORD,
      sprite_group=ball_group,
      shadow_group=shadow_group
    )

    self._follow_bat = False
    self._bat_frect = None
    self._direction = None

  def reacts_to_collisions(self) -> bool:
    return True

  def get_collisions(self) -> List[Collision]:
    return [
      Collision(
        object_type=ObjectType.BALL,
        rect=self._ball_sprite.rect
      )
    ]

  def has_collided(self, collision: Collision) -> None:
    match collision.object_type:
      case ObjectType.SIDE_WALL:
        if collision.rect.center[X_COORD] < self._ball_sprite.rect.center[X_COORD]:
          # Colliding to the left
          self._ball_sprite.rect.topleft = (
            collision.rect.topright[X_COORD],
            self._ball_sprite.rect.topleft[Y_COORD]
          )

          y = Y_DOWN if self._direction[Y_COORD] > 0 else Y_UP
          self._direction = pygame.Vector2(X_RIGHT, y).normalize()
        else:
          # Colliding to the right
          self._ball_sprite.rect.topright = (
            collision.rect.topleft[X_COORD],
            self._ball_sprite.rect.topleft[Y_COORD]
          )

          y = Y_DOWN if self._direction[Y_COORD] > 0 else Y_UP
          self._direction = pygame.Vector2(X_LEFT, y).normalize()
      case ObjectType.TOP_WALL:
        self._ball_sprite.rect.topleft = (
          self._ball_sprite.rect.topleft[X_COORD],
          collision.rect.bottomleft[Y_COORD]
        )

        x = X_RIGHT if self._direction[X_COORD] > 0 else X_LEFT
        self._direction = pygame.Vector2(x, Y_DOWN).normalize()
      case ObjectType.BAT:
        self._ball_sprite.rect.center = (
          self._ball_sprite.rect.center[X_COORD],
          collision.rect.center[Y_COORD] - VERTICAL_OFFSET_BETWEEN_BALL_AND_BAT
        )

        x = X_RIGHT if self._ball_sprite.rect.center[X_COORD] > collision.rect.center[X_COORD] else X_LEFT
        self._direction = pygame.Vector2(x, Y_UP).normalize()

  def get_interested_notification_types(self) -> Set[NotificationType] | None:
    return {
      NotificationType.BALL_RELEASED
    }

  def emit_notification(self) -> NotificationType | None:
    return None

  def receive_notification(self, notification_type: NotificationType, blackboard: Blackboard) -> None:
    match notification_type:
      case NotificationType.INITIAL_SETUP | NotificationType.BALL_MISSED:
        self._follow_bat = True
        self._bat_frect = blackboard.bat_frect
      case NotificationType.BALL_RELEASED:
        if self._follow_bat:
          self._follow_bat = False
          self._bat_frect = None

          self._direction = pygame.Vector2(X_RIGHT, Y_UP).normalize()

  def update(self, delta_ms: float) -> None:
    if self._follow_bat:
      pos = self._bat_frect.center

      self._ball_sprite.rect.center = (
        pos[X_COORD],
        pos[Y_COORD] - VERTICAL_OFFSET_BETWEEN_BALL_AND_BAT
      )
    else:
      self._ball_sprite.rect.center += self._direction * BALL_VELOCITY * delta_ms

    follow_shadow(self._ball_sprite, self._shadow_sprite)
