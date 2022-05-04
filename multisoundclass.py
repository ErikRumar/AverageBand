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
            if note == x:
                player = x
        x.play()
