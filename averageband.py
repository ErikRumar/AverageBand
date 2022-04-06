from soundclass import Sound
import time
from threading import Thread
from threading import *
from playsound import playsound

tempo_set = 120
tempo = 1 / (float(tempo_set / 60))
 
snare1_o = Sound("snare1", "Snare", "C:/Users/erik.rumarvaleskog/AverageBandLibrary/Drums/snare1.wav")
bassdrum1_o = Sound("bassdrum1", "BassDrum", "C:/Users/erik.rumarvaleskog/AverageBandLibrary/Drums/bassdrum1.wav")

bassdrum1 = Thread(target=Sound.play, args=(bassdrum1_o, tempo))
snare1 = Thread(target=Sound.play, args=(snare1_o, tempo))

secs = -tempo
while True:
    secs += tempo
    if secs % 2 == 0:
        bassdrum1.start()
        bassdrum1.join()
    else:
        snare1.start()
        snare1.join()

    time.sleep(tempo)
    bassdrum1.terminate()
    snare1.terminate()





