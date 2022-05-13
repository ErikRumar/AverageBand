import time
from threading import Thread
from playsound import playsound
from pygame import mixer
import multiprocessing
# from Sonus import sounds, multisounds
import Sonus

global sounds
global multisounds



class Project:
    global sounds
    global multisounds


    def __init__(self, name, length, tempo, instruments, recordings):
        self.name = name
        self.length = length
        self.tempo = tempo
        self.instruments = instruments
        self.recordings = recordings

    def __str__(self):
        return f"{self.name}\nlength: {self.length}   tempo: {self.tempo}"

    def show_project(self):                             # The layout overview of the project
        string = ""

        multisound = False
        sound = False
        list_to_string = ""


        a1 = (" ") * self.length + "."
        b1 = (" ") * self.length + "."
        c1 = (" ") * self.length + "."
        d1 = (" ") * self.length + "."
        e1 = (" ") * self.length + "."
        f1 = (" ") * self.length + "."
        g1 = (" ") * self.length + "."
        a2 = (" ") * self.length + "."
        b2 = (" ") * self.length + "."
        c2 = (" ") * self.length + "."
        d2 = (" ") * self.length + "."
        e2 = (" ") * self.length + "."
        f2 = (" ") * self.length + "."
        g2 = (" ") * self.length + "."

        beat = (" ") * self.length + "."


        refined_record = ""
        count = -1
        for record in self.recordings:
            if record == [""]:
                break
            list_to_string = ""
            count += 1

            string += f"{self.instruments[count]}:\n-*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*\n"

            for w in record:
                list_to_string = list_to_string + w

            for q in list_to_string:
                multisound = False
                sound = False
                if q == ".":
                    multisound = True
                    sound = False
                    break
                else:
                    sound = True
            if multisound == True:
                for y in record:
                    if y[:2] == "a1":
                        a1 = a1[: (int(y[3:])-1) ] + "_" + a1[ (int(y[3:])) :]
                    if y[:2] == "b1":
                        b1 = b1[: (int(y[3:])-1) ] + "_" + b1[ (int(y[3:])) :]
                    if y[:2] == "c1":
                        c1 = c1[: (int(y[3:])-1) ] + "_" + c1[ (int(y[3:])) :]
                    if y[:2] == "d1":
                        d1 = d1[: (int(y[3:])-1) ] + "_" + d1[ (int(y[3:])) :]
                    if y[:2] == "e1":
                        e1 = e1[: (int(y[3:])-1) ] + "_" + e1[ (int(y[3:])) :]
                    if y[:2] == "f1":
                        f1 = f1[: (int(y[3:])-1) ] + "_" + f1[ (int(y[3:])) :]
                    if y[:2] == "g1":
                        g1 = g1[: (int(y[3:])-1) ] + "_" + g1[ (int(y[3:])) :]
                    if y[:2] == "a2":
                        a2 = a2[: (int(y[3:])-1) ] + "_" + a2[ (int(y[3:])) :]
                    if y[:2] == "b2":
                        b2 = b2[: (int(y[3:])-1) ] + "_" + b2[ (int(y[3:])) :]
                    if y[:2] == "c2":
                        c2 = c2[: (int(y[3:])-1) ] + "_" + c2[ (int(y[3:])) :]
                    if y[:2] == "d2":
                        d2 = d2[: (int(y[3:])-1) ] + "_" + d2[ (int(y[3:])) :]
                    if y[:2] == "e2":
                        e2 = e2[: (int(y[3:])-1) ] + "_" + e2[ (int(y[3:])) :]
                    if y[:2] == "f2":
                        f2 = f2[: (int(y[3:])-1) ] + "_" + f2[ (int(y[3:])) :]
                    if y[:2] == "g2":
                        g2 = g2[: (int(y[3:])-1) ] + "_" + g2[ (int(y[3:])) :]
                refined_record = f"g1{g1}\nf1{f1}\ne1{e1}\nd1{d1}\nc1{c1}\nb1{b1}\na1{a1}\ng2{g2}\nf2{f2}\ne2{e2}\nd2{d2}\nc2{c2}\nb2{b2}\na2{a2}\n\n-*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*\n"
            
            elif sound == True:
                for y in record:
                    beat = beat[: (int(y)-1) ] + "_" + beat[ (int(y)) :]
                refined_record = f"{self.instruments[count][:2]}{beat}\n\n-*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*--------*\n"
            
            string += refined_record
            a1 = (" ") * self.length + "."
            b1 = (" ") * self.length + "."
            c1 = (" ") * self.length + "."
            d1 = (" ") * self.length + "."
            e1 = (" ") * self.length + "."
            f1 = (" ") * self.length + "."
            g1 = (" ") * self.length + "."
            a2 = (" ") * self.length + "."
            b2 = (" ") * self.length + "."
            c2 = (" ") * self.length + "."
            d2 = (" ") * self.length + "."
            e2 = (" ") * self.length + "."
            f2 = (" ") * self.length + "."
            g2 = (" ") * self.length + "."

            beat = (" ") * self.length + "."
            refined_record = ""
        return string

    def play_project(self):
        global sounds
        global multisounds
        
        for bar in range(1, self.length+1):
            print("bar: ", bar)
            beats = False
            notes = []
            count = -1
            for recording in self.recordings:
                # print(recording)
                count += 1
                list_to_string = ""

                for decide_multi_or_sound in range(1):

                    for w in recording:
                        list_to_string = list_to_string + w


                    for q in list_to_string:
                        multisound = False
                        sound = False
                        if q == ".":
                            multisound = True
                            sound = False
                            break
                        else:
                            sound = True
                    

                if multisound == True:
                    for x in multisounds:
                        if self.instruments[count] == x.get_name():
                            instrument = x
                            break
                if sound == True:
                    for x in sounds:
                        if self.instruments[count] == x.get_name():
                            instrument = x
                            break

                # print("this is the instrument", instrument.get_name())


                if multisound == True:
                    for xnote in self.recordings[count]:
                        if int(xnote[3:]) == bar:
                            notes.append(xnote[:2])
                # print("these are the notes", notes)
                if sound == True:
                    for beat in recording:
                        if int(beat) == bar:
                            beats = True


                # print("beat", beat, "instrument", instrument.get_name())

                # beat_play.terminate()
                if multisound == True:
                    count2 = -1
                    for note in notes:
                        count2 += 1
                        # instrument.play(note)
                        note_play = multiprocessing.Process(instrument.play(note))
                        note_play.start()
                        note_play.join()       
                        note_play.terminate()
                    print("played")
                    # print("____________________________:_____________________________:___________________:_____________________:_________")
                if beats == True:
                    # print("playin beat:::::::::::::::::::::::::.")
                    # instrument.play()
                    print("player ", instrument.get_name())
                    beat_play = multiprocessing.Process(instrument.play())
                    beat_play.start()
                    beat_play.join()
                    print("played")
                notes = []
                beats = False
            time.sleep(Sonus.tempo_to_sec(self.tempo))
            print("\n\n")



    
    def get_name(self):
        return self.name


#    def synchronize():
#         global sounds
#         global multisounds
#         sounds = Sonus.sounds
#         multisounds = Sonus.multisounds 



