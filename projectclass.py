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

        count = -1
        for instrument in self.instruments:
            count += 1
            string += f"{instrument}:\n"

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


            refined_record = ""
            for x in self.recordings:
                for y in x:
                    if y[:2] == "a1":
                        a1 = a1[ (int(y[3:])-1) :] + "_" + a1[: (int(y[3:])) ]
                        print(a1)
                    if y[:2] == "b1":
                        b1[int(y[3:])].replace("_")
                    if y[:2] == "c1":
                        c1[int(y[3:])].replace("_")
                    if y[:2] == "d1":
                        d1[int(y[3:])].replace("_")
                    if y[:2] == "e1":
                        e1[int(y[3:])].replace("_")
                    if y[:2] == "f1":
                        f1[int(y[3:])].replace("_")
                    if y[:2] == "g1":
                        g1[int(y[3:])].replace("_")
                    if y[:2] == "a2":
                        a2[int(y[3:])].replace("_")
                    if y[:2] == "b2":
                        b2[int(y[3:])].replace("_")
                    if y[:2] == "c2":
                        c2[int(y[3:])].replace("_")
                    if y[:2] == "d2":
                        d2[int(y[3:])].replace("_")
                    if y[:2] == "e2":
                        e2[int(y[3:])].replace("_")
                    if y[:2] == "f2":
                        f2[int(y[3:])].replace("_")
                    if y[:2] == "g2":
                        g2[int(y[3:])].replace("_")
                refined_record = f"{a1}\n{b1}\n{c1}\n{d1}\n{e1}\n{f1}\n{g1}\n{a2}\n{b2}\n{c2}\n{d2}\n{e2}\n{f2}\n{g2}\n"
                string += refined_record
        print(string)




    



    def xshow_project(self):

    #     refined_recording = ""
    #     recordings_refined = []
    #     recordings = []

    #     count1 = -1
    #     for recording in self.recordings:
    #         record = []

    #         beat = []

    #         a1 = []
    #         b1 = []
    #         c1 = []
    #         d1 = []
    #         e1 = []
    #         f1 = []
    #         g1 = []
    #         a2 = []
    #         b2 = []
    #         c2 = []
    #         d2 = []
    #         e2 = []
    #         f2 = []
    #         g2 = []

    #         for note in recording:

    #             for char in note:
    #                 multisound = False
    #                 sound = True
    #                 if char == ".":
    #                     multisound = True
    #                     sound = False
    #                     break
    #                 else:
    #                     pass
            
    #             if multisound == True:

    #                 for _ in 1:
    #                     if note[:1] == "a1":
    #                         a1.append(note[2:])
    #                     if note[:1] == "b1":
    #                         b1.append(note[2:])
    #                     if note[:1] == "c1":
    #                         c1.append(note[2:])
    #                     if note[:1] == "d1":
    #                         d1.append(note[2:])
    #                     if note[:1] == "e1":
    #                         e1.append(note[2:])
    #                     if note[:1] == "f1":
    #                         f1.append(note[2:])
    #                     if note[:1] == "g1":
    #                         g1.append(note[2:])
    #                     if note[:1] == "a2":
    #                         a2.append(note[2:])
    #                     if note[:1] == "b2":
    #                         b2.append(note[2:])
    #                     if note[:1] == "c2":
    #                         c2.append(note[2:])
    #                     if note[:1] == "d2":
    #                         d2.append(note[2:])
    #                     if note[:1] == "e2":
    #                         e2.append(note[2:])
    #                     if note[:1] == "f2":
    #                         f2.append(note[2:])
    #                     if note[:1] == "g2":
    #                         g2.append(note[2:])

    #             elif sound == True:
    #                 beat.append(note)
            
    #         if multisound == True:
    #             record.append(a1)
    #             record.append(b1)
    #             record.append(c1)
    #             record.append(d1)
    #             record.append(e1)
    #             record.append(f1)
    #             record.append(g1)
    #             record.append(a2)
    #             record.append(b2)
    #             record.append(c2)
    #             record.append(d2)
    #             record.append(e2)
    #             record.append(f2)
    #             record.append(g2)
    #         elif sound == True:
    #             record.append(beat)
    #         recordings.append(record)

    #     count2 = -1
    #     refined_recording = ""

    #     for x in recordings:
    #         count2 += 1
    #         for y in x:
    #             refined_recording = f"{refined_recording}\n"





    #     count3 = -1
    #     for x in self.instruments:
    #         count3 += 1
    #         instrument_and_recording = x + (20-len(x))*" " + recordings_refined[count3]
        
        
    #     string = f"""
        
    #     {}
        
        
        
        
    #     """

    #     return string
        pass
