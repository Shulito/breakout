from os import path
from typing import List, Set

import pygame

from src.audio import Mixer, SoundName
from src.blackboard import Blackboard
from src.collision import Collision, ObjectType
from src.constants import (
  BALL_INITIAL_COORD,
  BALL_RADIUS,
  BALL_SPEED_INCREMENT,
  BALL_SPEED_INITIAL,
  BALL_SPEED_MAX,
  BAT_HALF_WIDTH,
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

    self._follow_bat = False
    self._bat_frect = None
    self._direction = None
    self._velocity = BALL_SPEED_INITIAL

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
        if collision.rect.center[X_COORD] < self._ball_sprite.rect.center[X_COORD]:
          # Colliding to the left
          self._ball_sprite.rect.topleft = (
            collision.rect.topright[X_COORD],
            self._ball_sprite.rect.topleft[Y_COORD]
          )
        else:
          # Colliding to the right
          self._ball_sprite.rect.topright = (
            collision.rect.topleft[X_COORD],
            self._ball_sprite.rect.topleft[Y_COORD]
          )

        self._direction = pygame.Vector2(-self._direction[X_COORD], self._direction[Y_COORD])
      case ObjectType.TOP_WALL:
        self._ball_sprite.rect.topleft = (
          self._ball_sprite.rect.topleft[X_COORD],
          collision.rect.bottomleft[Y_COORD]
        )

        self._direction = pygame.Vector2(self._direction[X_COORD], -self._direction[Y_COORD])
      case ObjectType.BAT:
        if self._ball_sprite.rect.center[Y_COORD] < collision.rect.center[Y_COORD]:
          # Player reached the ball
          self._ball_sprite.rect.center = (
            self._ball_sprite.rect.center[X_COORD],
            collision.rect.topleft[Y_COORD] - BALL_RADIUS
          )

          if self._ball_sprite.rect.center[X_COORD] < collision.rect.center[X_COORD]:
            if self._ball_sprite.rect.center[X_COORD] < collision.rect.center[X_COORD] - BAT_HALF_WIDTH:
              self._direction = VECTOR_20_DEGREES_LEFT_UP
            else:
              self._direction = VECTOR_45_DEGREES_LEFT_UP
          else:
            if self._ball_sprite.rect.center[X_COORD] > collision.rect.center[X_COORD] + BAT_HALF_WIDTH:
              self._direction = VECTOR_20_DEGREES_RIGHT_UP
            else:
              self._direction = VECTOR_45_DEGREES_RIGHT_UP
        else:
          # Too far bellow the top of the bat, player missed the ball
          if self._ball_sprite.rect.center[X_COORD] < collision.rect.center[X_COORD]:
            # Colliding to the left
            self._ball_sprite.rect.topright = (
              collision.rect.topleft[X_COORD] - BALL_RADIUS,
              self._ball_sprite.rect.topright[Y_COORD]
            )
          else:
            # Colliding to the right
            self._ball_sprite.rect.topleft = (
              collision.rect.topright[X_COORD] + BALL_RADIUS,
              self._ball_sprite.rect.topleft[Y_COORD]
            )

          self._direction = pygame.Vector2(-self._direction[X_COORD], self._direction[Y_COORD])

        self._mixer.play_sound(SoundName.BALL_HITS_BAT)

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

          self._direction = VECTOR_45_DEGREES_RIGHT_UP
          self._velocity = BALL_SPEED_INITIAL

          self._mixer.play_sound(SoundName.BALL_HITS_BAT)

  def update(self, delta_ms: float) -> None:
    if self._follow_bat:
      self._ball_sprite.rect.center = (
        self._bat_frect.center[X_COORD],
        self._bat_frect.topleft[Y_COORD] - BALL_RADIUS
      )
    else:
      self._velocity = min(BALL_SPEED_MAX, self._velocity + BALL_SPEED_INCREMENT * delta_ms)
      self._ball_sprite.rect.center += self._direction * self._velocity * delta_ms

    follow_shadow(self._ball_sprite, self._shadow_sprite)
