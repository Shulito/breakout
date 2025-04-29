from os import path
from typing import List, Set

import pygame

from src.audio import Mixer, SoundName
from src.bat import Bat
from src.blackboard import Blackboard
from src.collision import (
  Collision,
  ObjectType,
  resolve_collision_by_direction,
  resolve_collision_by_trajectory,
)
from src.constants import (
  BALL_INITIAL_COORD,
  BALL_RADIUS,
  BALL_SPEED_INCREMENT,
  BALL_SPEED_INITIAL,
  BALL_SPEED_MAX,
  BAT_QUARTER_WIDTH,
  STAGE_IMAGES_FOLDER_PATH,
  VECTOR_20_DEGREES_LEFT_UP,
  VECTOR_20_DEGREES_RIGHT_UP,
  VECTOR_45_DEGREES_LEFT_UP,
  VECTOR_45_DEGREES_RIGHT_UP,
  X_COORD,
  Y_COORD,
)
from src.coord import CoordPosition
from src.interfaces import GameObject
from src.notifications import NotificationType
from src.utils import create_sprite_from_surface, follow_shadow, load_image


class Ball(GameObject):
  def __init__(
      self,
      ball_group: pygame.sprite.Group,
      shadow_group: pygame.sprite.Group,
      bat: Bat,
      mixer: Mixer
  ):
    ball_surface = load_image(file_path=path.join(STAGE_IMAGES_FOLDER_PATH, "ball.png"))

    self._ball_sprite, self._shadow_sprite = create_sprite_from_surface(
      surface=ball_surface,
      coord_position=CoordPosition.CENTER,
      coord=BALL_INITIAL_COORD,
      sprite_group=ball_group,
      shadow_group=shadow_group
    )

    self._mixer = mixer

    self._bat = bat
    self._follow_bat = False
    self._direction = None
    self._speed = BALL_SPEED_INITIAL
    self._previous_rect = self._ball_sprite.rect.copy()

  def reacts_to_collisions(self) -> bool:
    return True

  def get_collision_rects(self) -> List[Collision]:
    return [
      Collision(
        object_type=ObjectType.BALL,
        rect=self._ball_sprite.rect
      )
    ]

  def has_collided(self, collision: Collision) -> None:
    match collision.object_type:
      case ObjectType.SIDE_WALL:
        self._direction.x *= -1

        resolve_collision_by_trajectory(
          previous_rect=self._previous_rect,
          rect=self._ball_sprite.rect,
          colliding_rect=collision.rect
        )
      case ObjectType.TOP_WALL:
        self._direction.y *= -1

        resolve_collision_by_trajectory(
          previous_rect=self._previous_rect,
          rect=self._ball_sprite.rect,
          colliding_rect=collision.rect
        )
      case ObjectType.BAT:
        if self._ball_sprite.rect.center[Y_COORD] < collision.rect.center[Y_COORD]:
          # Hitting with upper part of the bat
          if self._ball_sprite.rect.center[X_COORD] < collision.rect.center[X_COORD]:
            if self._ball_sprite.rect.center[X_COORD] < collision.rect.center[X_COORD] - BAT_QUARTER_WIDTH:
              self._direction = VECTOR_20_DEGREES_LEFT_UP.copy()
            else:
              self._direction = VECTOR_45_DEGREES_LEFT_UP.copy()
          else:
            if self._ball_sprite.rect.center[X_COORD] > collision.rect.center[X_COORD] + BAT_QUARTER_WIDTH:
              self._direction = VECTOR_20_DEGREES_RIGHT_UP.copy()
            else:
              self._direction = VECTOR_45_DEGREES_RIGHT_UP.copy()

          resolve_collision_by_direction(
            direction=self._direction,
            rect=self._ball_sprite.rect,
            colliding_rect=collision.rect
          )
        else:
          # Hitting with lower part of the bat
          self._direction.x *= -1

          resolve_collision_by_trajectory(
            previous_rect=self._previous_rect,
            rect=self._ball_sprite.rect,
            colliding_rect=collision.rect
          )

        self._mixer.play_sound(SoundName.BALL_HITS_BAT)

  def get_interested_notification_types(self) -> Set[NotificationType] | None:
    return {
      NotificationType.BALL_RELEASED,
      NotificationType.BALL_MISSED
    }

  def emit_notification(self) -> NotificationType | None:
    return None

  def receive_notification(self, notification_type: NotificationType, blackboard: Blackboard) -> None:
    match notification_type:
      case NotificationType.INITIAL_SETUP | NotificationType.BALL_MISSED:
        self._follow_bat = True
      case NotificationType.BALL_RELEASED:
        if self._follow_bat:
          self._follow_bat = False

          self._direction = VECTOR_45_DEGREES_RIGHT_UP.copy()
          self._speed = BALL_SPEED_INITIAL

          self._mixer.play_sound(SoundName.BALL_HITS_BAT)

  def update(self, delta_ms: float) -> None:
    self._previous_rect = self._ball_sprite.rect.copy()

    if self._follow_bat:
      self._ball_sprite.rect.center = (
        self._bat.get_rect().center[X_COORD] + 4 * BALL_RADIUS,
        self._bat.get_rect().topleft[Y_COORD] - BALL_RADIUS
      )
    else:
      self._speed = min(BALL_SPEED_MAX, self._speed + BALL_SPEED_INCREMENT * delta_ms)
      self._ball_sprite.rect.center += self._direction * self._speed * delta_ms

    follow_shadow(self._ball_sprite, self._shadow_sprite)
