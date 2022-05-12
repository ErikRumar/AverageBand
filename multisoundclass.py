import time
from threading import Thread
from playsound import playsound
from pygame import mixer
from noteclass import Note


class MultiSound:

    def __init__(self, name, notes):
        self.name = name
        self.notes = notes

    def __str__(self):
        return f"multisound name {self.name} multisound notes {self.notes}"

    def play(self, note):

        for x in self.notes:
            if note == x.get_name()[len(x.get_name())-2:]:
                player = x
                print("player", player.get_name())
        player.play()

    def get_name(self):
        return self.name
        
    def get_type(self):
        return "multisound"
