import time
from threading import Thread
from playsound import playsound
from pygame import mixer


class Sound:

    def __init__(self, name, category, sound):
        self.name = name
        self.category = category
        self.sound = sound

    def __str__(self):
        print(self.name)
        print(self.category)

    def play(self):
        mixer.music.load(self.sound)
        mixer.music.play()