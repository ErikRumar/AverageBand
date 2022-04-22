import time
from threading import Thread
from playsound import playsound
from pygame import mixer
import multiprocessing


class Note:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def __str__(self):
        print(self.name)

    def play(self):
        playsound(self.sound)
