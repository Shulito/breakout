from typing import Dict, Set

import pygame

from src.ball import Ball
from src.bat import Bat
from src.blackboard import Blackboard
from src.collision import Collision
from src.constants import (
  FPS,
  GAME_TITLE,
  INITIAL_LIVES,
  INITIAL_SCORE,
  SCREEN_COLOR,
  SCREEN_HEIGHT,
  SCREEN_WIDTH,
)
from src.interfaces import GameObject
from src.notifications import NotificationType
from src.playground import Playground
from src.utils import get_notifications_from_pressed_keys


class Breakout:
  def __init__(self):
    pygame.init()

    pygame.display.set_caption(GAME_TITLE)
    self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self._clock = pygame.time.Clock()

    self._background_group = pygame.sprite.Group()
    self._middleground_group = pygame.sprite.Group()
    self._foreground_group = pygame.sprite.Group()

    # Create game objects
    self._blackboard = Blackboard(
      score=INITIAL_SCORE,
      lives=INITIAL_LIVES,
      bat_frect=None
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

    self._blackboard.bat_frect = bat.get_frect()

    ball = Ball(
      ball_group=self._middleground_group,
      shadow_group=self._background_group
    )

    self._game_objects = [
      playground,
      bat,
      ball
    ]

    # Wire up notifications
    self._notification_mapping: Dict[NotificationType, Set[GameObject]] = {
      notification_type: set() for notification_type in NotificationType
    }

    for game_object in self._game_objects:
      notification_types = game_object.get_interested_notification_types()
      if notification_types:
        for notification_type in notification_types:
          self._notification_mapping[notification_type].add(game_object)

      game_object.receive_notification(
        notification_type=NotificationType.INITIAL_SETUP,
        blackboard=self._blackboard
      )

  def __del__(self):
    pygame.quit()

  def _find_collision(self, object_to_check_collision: GameObject) -> Collision | None:
    collisions_to_check = object_to_check_collision.get_collision_rects()
    if not collisions_to_check:
      return None

    for game_object in self._game_objects:
      if object_to_check_collision == game_object:
        continue

      for collision1 in collisions_to_check:
        for collision2 in game_object.get_collision_rects():
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

      player_notifications = get_notifications_from_pressed_keys()

      for game_object in self._game_objects:
        # Update objects
        game_object.update(delta_ms)

        # Check collisions
        if game_object.reacts_to_collisions():
          collision = self._find_collision(game_object)
          if collision:
            game_object.has_collided(collision)

        # Check notifications
        notification = game_object.emit_notification()
        if notification:
          for game_object_to_notify in self._notification_mapping[notification]:
            game_object_to_notify.receive_notification(
              notification_type=notification,
              blackboard=self._blackboard
            )

        for player_notification in player_notifications:
          game_object.receive_notification(
            notification_type=player_notification,
            blackboard=self._blackboard
          )

      self._screen.fill(SCREEN_COLOR)
      self._background_group.draw(self._screen)
      self._middleground_group.draw(self._screen)
      self._foreground_group.draw(self._screen)

      pygame.display.update()
