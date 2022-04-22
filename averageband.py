from soundclass import Sound
import time
from threading import Thread
from threading import *
from playsound import playsound
import multiprocessing

tempo_set = 120
tempo = 1 / (float(tempo_set / 60))


def load_files():
    two_of_them = 0
    path = ""
    sound_name = ""
    note_name = ""

    add = ""

    sound = False
    multisound = False

    with open("files.txt", "r", encoding= "utf8") as files:
        for line in files.readlines():

                for x in line:

                    if x == "-":
                        sound = True
                        multisound = False
                    elif x == ";":
                        multisound = True
                        sound = False

                    if x == "\n":
                        sound = False
                        multisound = False
                    if line == "=":
                        pass
                        if line == '"':
                            two_of_them += 1
                        if two_of_them >= 2:
                            two_of_them = 0
                            if sound == True:
                                sound_name = add - " "
                            elif multisound == True:
                                note_name = add - " "
                            continue
                    if line == ";":
                        pass
                    if line == "_":
                        pass
                    add += x
            
            sound = False
            multisound = False

def check_int(string):
    string = str(string)
    if string == "":
        bool = False
        return bool
    for x in string:
        if x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9":
            continue
        else:
            bool = False
            return bool
    bool = True
    return bool

def load_project(project):
    pass

def list_of_projects():
    pass

def edit_menu(new):
    if new == False:
        project = list_of_projects()
        load_project(project)
    else:
        load_project(False)
    



def main_menu():
    choice = -1
    print("""

                Main Menu

        1. Create new project
        2. Open project
    
    
    """)
    while check_int(choice) == True and choice != 2 and choice != 1:
        choice = input("")
    
    if choice == 1:
        edit_menu(True)
    if choice ==2:
        edit_menu(False)

def main():
    load_files()
    main_menu()
    
    snare1_o = Sound("snare1", "Snare", "C:/Users/erik.rumarvaleskog/AverageBandLibrary/Drums/snare1.wav")
    bassdrum1_o = Sound("bassdrum1", "BassDrum", "C:/Users/erik.rumarvaleskog/AverageBandLibrary/Drums/bassdrum1.wav")

    

    secs = -tempo
    while True:
        bassdrum1 = multiprocessing.Process(target=playsound, args=(bassdrum1_o, tempo))
        snare1 = multiprocessing.Process(target=playsound, args=(snare1_o, tempo))
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



if __name__ == "__main__":
    main()

