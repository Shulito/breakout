from enum import Enum


class NotificationType(Enum):
    BALL_MISSED = 1
    BRICK_DESTROYED = 2
    PLAYER_DIED = 3
