from enum import Enum
from typing import Any, Dict, List, Tuple


class NotificationType(Enum):
    # When the ball passes by the bat
    BALL_MISSED = 1
    # When the player releases the ball when attached to the bat
    BALL_RELEASED = 2
    # When the ball hits a brick
    BRICK_DESTROYED = 3
    # All bricks destroyed
    BRICKS_DESTROYED = 4
    # When the game first starts
    INITIAL_SETUP = 5


class NotificationsSink:
    def __init__(self):
        self._notifications = list()

    def write(self, notification: NotificationType, extra_data: Dict[Any, Any] = None) -> None:
        self._notifications.append((notification, extra_data))

    def read_all(self) -> List[Tuple[NotificationType, Dict[Any, Any]]]:
        result = self._notifications.copy()
        self._notifications.clear()

        return result
