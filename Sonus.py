import projectclass
from soundclass import Sound
from multisoundclass import MultiSound
from noteclass import Note
import time
from threading import Thread
from threading import *
from playsound import playsound
import multiprocessing

global sounds
global multisounds

sounds = []
multisounds = []
instruments = []
notes = []



def tempo_to_sec(tempo):
    tempo = int(tempo)
    return 1 / (float(tempo/ 60))

def load_files():
    global sounds
    global multisounds

    sounds = []
    multisounds = []


    two_of_them = 0
    path = ""
    sound_name = ""
    multisound_name = ""
    note_name = ""
    note_list = []
    category = ""

    string = ""

    sound = False
    multisound = False

    with open("files.txt", "r", encoding= "utf8") as files:
        for line in files.readlines():
            for x in line:

                if x == "-":
                    sound = True
                    multisound = False
                    naming = True
                elif x == ";":
                    multisound = True
                    sound = False
                    naming = True

                if x == "=":
                    if sound == True:
                        sound_name = string[1:]
                    elif multisound == True:
                        note_name = string[1:]
                    string = ""

                if x == '"':
                    two_of_them += 1
                if two_of_them >= 2:
                    string.replace("=", "")
                    string.replace(" ", "")
                    string.replace('"', "")
                    path = string[2:]

                if x == "\n" and naming == True:
                    if multisound == True:
                        multisound_name = string[2:]
                    elif sound == True:
                        category = string[1:]
                if x == "\n" and naming == False and note_name != "":
                    if multisound == True:
                        note = Note(multisound_name + "," + note_name, path)
                        note_list.append(note)
                        string = ""
                if x == "\n" and naming == False:
                    if sound == True:
                        s = Sound(sound_name, category, path)
                        sounds.append(s)
                if x == "_":

                    if multisound == True:
                        multisounds.append(MultiSound(multisound_name, note_list))
                    note_list = []
                    two_of_them = 0
                    path = ""
                    sound_name = ""
                    multisound_name = ""
                    note_name = ""
                    category = ""
                    string = ""


                    sound = False
                    multisound = False

                if naming == True and x == "\n":
                    naming = False
                    string = ""
                    string += x
                else:
                    string += x

                if two_of_them >= 2:
                    string = ""
                    two_of_them = 0


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

def string_to_list(string):
    element = ""
    list = []
    two_of_them = 0
    init = False
    for char in string:

        if char == "'":
            two_of_them += 1
            if two_of_them == 2:
                list.append(element[1:])
                init = False
                two_of_them = 0
                element = ""
            else:
                init = True
        if init == True:
            element += char

    return list

def save_project(project_index, project_name, project_length, project_tempo, project_instruments, project_recordings):


    string = (f"""n- {project_name}
    l- {project_length}
    t- {project_tempo}
    i- {project_instruments}
    """)

    records = ""

    for record in project_recordings:
        new_recording = ""
        for element in record:
            new_recording = new_recording + element + "/"
        records = records + f"r- {new_recording}\n"

    string = string + records

    with open(f"{project_index}.txt", "w", encoding="utf8") as file:
        file.write(string)


def load_project(project_index):
    
    with open(f"{project_index}.txt", "r") as file:
        project_name = ""
        project_length = 0
        project_tempo = 0
        project_instruments = []
        project_recordings = []
        count = 0
        for line in file.readlines():
            string = ""
            for char in line:

                if string == "":
                    if char == "n":
                        mode = "n"

                    if char == "l":
                        mode = "l"

                    if char == "t":
                        mode = "t"
                    
                    if char == "i":
                        mode = "i"

                    if char == "r":
                        mode = "r"

                    mode_init = True

                if mode_init == True:
                    count += 1
                    if count >= 3:
                        mode_init = False
                    string += char
                    continue
                    
                if char == "\n":
                    
                    if mode == "n":
                        project_name = string[2:]

                    if mode == "l":
                        project_length = int(string[2:])

                    if mode == "t":
                        project_tempo = int(string[2:])

                    if mode == "i":
                        project_instruments = string_to_list(string[2:])

                    if mode == "r":
                        project_recordings.append(string[2:].split("/"))

                    new_project_recordings = []

                    for record in project_recordings:                       # removing '' that usually becomes included
                        new_project_record = []
                        for element in record:
                            if element == "":
                                pass
                            else:
                                new_project_record.append(element)
                        new_project_recordings.append(new_project_record)

                    project_recordings = new_project_recordings

                string += char

    return project_name, project_length, project_tempo, project_instruments, project_recordings

def list_of_projects():
    pass

def open_project(project):
    print("\nopen", project)
    print(project.show_project())

def edit_menu(project, project_index):
    menu = 1
    print("Overlook Menu\n")

    while True:
        while menu == 1:
            choice = input("(p)lay or (e)dit, (nothing to return): ")
            if choice == "p":
                project.play_project()
            elif choice.lower() == "e":
                menu = 2
                print("Edit Menu\n")
            elif choice == "":
                main_menu()
            else:
                print("error")
                time.sleep(0.5)
        
        while menu == 2:
            choice = input("choose instrument(nothing to return): ")
            if choice == "":
                menu = 1
                print("Overlook Menu\n")
            else:
                for instrument in project.instruments:
                    if choice.lower() == instrument.lower():
                        edit = ""
                        replace = ""
                        new_note = ""
                        while check_int(edit) != True or (int(edit) <= 0 and int(edit) >= int(project.length)):
                            edit = input("place: ")
                        edit = int(edit)
                        while not (replace == " " or replace == "_"):
                            replace = input("replacement: ")
                        while not  (replace.lower() != "a1" or replace.lower() != "b1" or replace.lower() != "c1" or replace.lower() != "d1" or replace.lower() != "e1" or replace.lower() != "f1" or replace.lower() != "g1" or replace.lower() != "a2" or replace.lower() != "b2" or replace.lower() != "c2" or replace.lower() != "d2" or replace.lower() != "e2" or replace.lower() != "f2" or replace.lower() != "g2"):
                            new_note = input("note: ")
                        new_note = new_note.lower()


                with open(f"{project_index}.txt", "r", encoding = "utf8") as project_txt:
                    print("edit done")
                    project_name = ""
                    project_length = 0
                    project_tempo = 0
                    project_instruments = []
                    project_recordings = []
                    count = 0
                    for line in project_txt.readlines():
                        string = ""
                        for char in line:

                            if string == "":
                                if char == "n":
                                    mode = "n"

                                if char == "l":
                                    mode = "l"

                                if char == "t":
                                    mode = "t"
                                
                                if char == "i":
                                    mode = "i"

                                if char == "r":
                                    mode = "r"

                                mode_init = True

                            if mode_init == True:
                                count += 1
                                if count >= 3:
                                    mode_init = False
                                string += char
                                continue
                                
                            if char == "\n":
                                
                                if mode == "n":
                                    project_name = string[2:]

                                if mode == "l":
                                    project_length = int(string[2:])

                                if mode == "t":
                                    project_tempo = int(string[2:])

                                if mode == "i":
                                    project_instruments = string_to_list(string[2:])

                                if mode == "r":
                                    project_recordings.append(string[2:].split("/"))

                            string += char
                    
                    count2 = -1
                    for instrument in project_instruments:
                        count2 += 1
                        if instrument.lower() == choice.lower():
                            instrument_index = count2
                            break
                    
                    new_project_record = []
                    new_project_recordings = []

                    count3 = -1
                    for record in project_recordings:
                        count3 += 1
                        if instrument_index == count3:
                            count4 = -1
                            for element in record:
                                count4 += 1
                                print("element", element)
                                if int(element[4:]) == edit and element[:2] == new_note:
                                    if replace == "_":
                                        new_project_record.append(f"{new_note}.{edit}")
                                    elif replace == " ":
                                        pass
                                    else:
                                        new_project_record.append(element)
                            new_project_recordings.append(new_project_record)
                    save_project(project_index, project_name, project_length, project_tempo, project_instruments, new_project_recordings)
                    load_project(project_index)





def main_menu():
    global sounds
    global multisounds

    choice = 9999
    print("""

                Main Menu

        1. Create new project
        2. Open project
    
    
    """)
    while not (check_int(choice) == True and (choice == 2 or choice == 1)):
        if check_int(choice) == True:
            if int(choice) <= 2 and int(choice) >= 1:
                break
            else:
                choice = input("")
        else:
            choice = input("")
    
    if int(choice) == 1:
        edit_menu(True)
    if int(choice) ==2:
        project_index = input("project: ")
        project_name, project_length, project_tempo, project_instruments, project_recordings = load_project(project_index)
        project = projectclass.Project(project_name, project_length, project_tempo, project_instruments, project_recordings)
        open_project(project)
        edit_menu(project, project_index)

def main():
    global multisounds
    global sounds

    load_files()
    projectclass.multisounds = multisounds
    projectclass.sounds = sounds
    # for y in sounds:
    #     print(y, ":::")
    # print("\n")
    # for x in multisounds:
    #     print(x, ":::")
    main_menu()




if __name__ == "__main__":
    main()

