import time
from threading import Thread
from playsound import playsound
from pygame import mixer


class Sound:

    def __init__(self, name, category, sound):                  # This is the 'single' sound class with only one type of sound, like drums have
        self.name = name
        self.category = category
        self.sound = sound

    def __str__(self):
        return f"sound name {self.name} sound category {self.category} sound path {self.sound}"

    def play(self):
        playsound(self.sound)
        
    def get_name(self):
        return self.name

    def get_type(self):
        return "sound"