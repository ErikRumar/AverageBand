import time
from threading import Thread
from playsound import playsound
from pygame import mixer
import multiprocessing


class Project:

    def __init__(self, name, length, tempo, instruments, recordings):
        self.name = name
        self.length = length
        self.tempo = tempo
        self.instruments = instruments
        self.recordings = recordings

    def __str__(self):
        return f"{self.name}\nlength: {self.length}   tempo: {self.tempo}"

    def show_project(self):
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
        for x in self.recordings:
            list_to_string = ""
            count += 1

            string += f"{self.instruments[count]}:\n-------------------------------------------------------------------------------\n"

            for w in x:
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
                for y in x:
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
                refined_record = f"{g1}\n{f1}\n{e1}\n{d1}\n{c1}\n{b1}\n{a1}\n{g2}\n{f2}\n{e2}\n{d2}\n{c2}\n{b2}\n{a2}\n-------------------------------------------------------------------------------\n"
            
            elif sound == True:
                for y in x:
                    beat = beat[: (int(y)-1) ] + "_" + beat[ (int(y)) :]
                refined_record = f"{beat}\n-------------------------------------------------------------------------------\n"
            
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
        print(string)

