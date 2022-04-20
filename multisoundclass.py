import time
from threading import Thread
from playsound import playsound
from pygame import mixer
from noteclass import Note


class MultiSound:

    def __init__(self, name, category, notes):
        self.name = name
        self.category = category
        self.notes = notes

    def __str__(self):
        print(self.name)
        print(self.category)

    def play(self, note):

        for x in self.notes:
            if note == x:
                pass
        x = Note("a1", "C:/Users/erik.rumarvaleskog/AverageBandLibrary/EPiano/a1.wav")
        x.play(x)
        

x = Note("a1", "C:/Users/erik.rumarvaleskog/AverageBandLibrary/EPiano/a1.wav")
mixer.init()
x.play()