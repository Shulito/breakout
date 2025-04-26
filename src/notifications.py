from enum import Enum


class NotificationType(Enum):
    # When the ball passes by the bat
    BALL_MISSED = 1
    # When the player releases the ball when attached to the bat
    BALL_RELEASED = 2
    # When the ball hits a brick
    BRICK_DESTROYED = 3
    # When the game first starts
    INITIAL_SETUP = 4
    # When the number of lives of the player has reached zero
    PLAYER_DIED = 5
