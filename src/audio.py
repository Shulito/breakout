from enum import Enum
from os import path
from typing import Dict

import pygame

from src.constants import AUDIO_FOLDER_PATH


class SoundName(Enum):
  BALL_HITS_BAT = "ball_hits_bat.ogg"
  BALL_HITS_BRICK = "ball_hits_brick.ogg"


class Mixer:
  def __init__(self):
    pygame.mixer.init()

    self._sounds: Dict[SoundName, pygame.mixer.Sound] = {
      sound_name: pygame.mixer.Sound(path.join(AUDIO_FOLDER_PATH, sound_name.value)) for sound_name in SoundName
    }

  def __del__(self):
    pygame.mixer.quit()

  def play_sound(self, sound_name: SoundName) -> None:
    self._sounds[sound_name].play()
