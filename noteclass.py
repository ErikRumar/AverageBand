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
        return f"note name {self.name} note path {self.sound}" 

    def play(self):
        playsound(self.sound)

    def get_name(self):
        return self.name
        
    def get_sound(self):
        return self.sound

    def get_type(self):
        return "note"

