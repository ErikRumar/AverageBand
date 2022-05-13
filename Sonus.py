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
global projects

sounds = []
multisounds = []
instruments = []
notes = []
projects = []



def tempo_to_sec(tempo):
    tempo = int(tempo)
    return 1 / (float(tempo/ 60))

def load_files():
    global sounds
    global multisounds
    global projects

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
    
    project_list = []
    with open("projects.txt", "r", encoding= "utf8") as projects_file:
        index = ""
        for x in projects_file.read():
            if x == "/":
                project_list.append(index)
                index = ""
                x = ""
            index += x
    
    for p in project_list:
        project_name, project_length, project_tempo, project_instruments, project_recordings = load_project(p)
        projects.append(projectclass.Project(project_name, project_length, project_tempo, project_instruments, project_recordings))


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


    string = (f"""n-{project_name}
l-{project_length}
t-{project_tempo}
i-{project_instruments}
""")

    records = ""

    for record in project_recordings:
        count = 0
        for x in record:
            count = 0
            for y in record:                                                               # looking for duplicates
                if y == x:
                    count += 1
                    if count >= 2:
                        record.remove(x)
        if record == "":
            new_recording = "/"
        new_recording = ""
        for element in record:
            new_recording = new_recording + element + "/"
        records = records + f"r-{new_recording}\n"

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
    global projects

    list1 = []
    for project in projects:
        list1.append(project)

    list2 = []

    with open("projects.txt", "r", encoding= "utf8") as file:
        string = file.read()
        list2 = string.split("/")

    if "" in list2:
        list2.remove("")

    return list2, list1

def open_project(project):                              # shows project
    print("\nopen", project)
    print(project.show_project())

def edit_menu(project, project_index):
    global multisounds
    global sounds
    print("Overlook Menu\n")
    menu = 0

    choice = "nwsfek"
    while True:

        while menu == 0:
            while choice.lower() != "n" and choice.lower() != "t" and choice.lower() != "l" and choice.lower() != "i" and choice.lower() != "":
                choice = input("(n)ame or (t)empo or (l)ength or (i)nstruments (nothing to return): ")

            project_name = project.name
            project_length =project.length
            project_tempo =project.tempo
            project_instruments =project.instruments
            project_recordings =project.recordings
            

            if choice.lower() == "n":
                project_name = input("name: ")

            if choice.lower() == "t":
                tempo = ""
                while check_int(tempo) != True:
                    tempo = input("tempo: ")
                    if tempo <= 0:
                        name = ""
                project_tempo = int(tempo)
                
            if choice.lower() == "l":
                length = ""
                while check_int(length) != True:
                    tempo = input("length: ")
                    if length <= 0:
                        length = ""
                project_length = int(length)
            
            if choice.lower() == "i":
                menu = 1
            if choice.lower() == "":
                main_menu()

            save_project(project_index, project_name, project_length, project_tempo, project_instruments, project_recordings)
            project.name = project_name
            project.length = project_length
            project.tempo = project_tempo
            project.instruments = project_instruments
            project.recordings = project_recordings

        while menu == 1:
            open_project(project)
            choice = input("(p)lay or (e)dit, (nothing to return): ")
            if choice == "p":
                project.play_project()
            elif choice.lower() == "e":
                menu = 2
                print("Edit Menu\n")
            elif choice == "":
                menu = 0
            else:
                print("error")
                time.sleep(0.5)

        while menu == 2:
            open_project(project)
            choice = input("choose instrument, (n)ew (nothing to return): ")
            if choice == "":
                menu = 1
                print("Overlook Menu\n")
            elif choice.lower() == "n":
                menu = 3
                print("Instrument Menu\n")
            else:
                for instrument in project.instruments:
                    sound1 = False
                    multisound = False
                    if choice.lower() == instrument.lower():
                        edit = ""
                        replace = ""
                        new_note = ""
                        while check_int(edit) != True or (int(edit) <= 0 and int(edit) >= int(project.length)):
                            edit = input("place: ")
                        edit = int(edit)
                        while not (replace == " " or replace == "_"):
                            replace = input("replacement: ")
                        for x in multisounds:                                                                                               # note is only necessary for multisounds
                            sound1 = True
                            multisound1 = False
                            if instrument == x.get_name():
                                multisound1 = True
                                break
                        if multisound1 == True:
                            while  (new_note.lower() != "a1" and new_note.lower() != "b1" and new_note.lower() != "c1" and new_note.lower() != "d1" and new_note.lower() != "e1" and new_note.lower() != "f1" and new_note.lower() != "g1" and new_note.lower() != "a2" and new_note.lower() != "b2" and new_note.lower() != "c2" and new_note.lower() != "d2" and new_note.lower() != "e2" and new_note.lower() != "f2" and new_note.lower() != "g2"):
                                new_note = input("note: ")
                            new_note = new_note.lower()


                with open(f"{project_index}.txt", "r", encoding = "utf8") as project_txt:
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
                                    project_instruments = string_to_list(string[1:])

                                if mode == "r":
                                    project_recordings.append(string[2:].split("/"))

                            string += char

                    new_project_recordings = []

                    for record in project_recordings:                                               # removing '' that usually becomes included
                        new_project_record = []
                        for element in record:
                            if element == "":
                                pass
                            else:
                                new_project_record.append(element)
                        new_project_recordings.append(new_project_record)

                    

                    project_recordings = new_project_recordings
                    
                    
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


                        for x in multisounds:                                                                                               # check if record is multisound or not
                            sound = True
                            multisound = False
                            if project.instruments[count3] == x.get_name():
                                multisound = True
                                sound = False
                                break

                        if instrument_index == count3:
                            count4 = -1
                            for element in record:
                                count4 += 1

                                if replace == " ":
                                    print(element)
                                    if multisound == True:
                                        if int(element[3:]) == edit and element[:2] == new_note:
                                            pass
                                        else:
                                            new_project_record.append(element)
                                    elif sound == True:
                                        if int(element) == edit :
                                            pass
                                        else:
                                            new_project_record.append(element)
                                    print(new_project_record)

                                elif replace == "_":
                                    new_project_record.append(element)
                            if multisound == True and replace != " ":
                                new_project_record.append(f"{new_note}.{edit}")
                            elif sound == True and replace != " ":
                                new_project_record.append(f"{edit}")
                            new_project_recordings.append(new_project_record)
                        else:
                            new_project_recordings.append(record)

                    project_recordings = new_project_recordings


                    print("edit done")
                    save_project(project_index, project_name, project_length, project_tempo, project_instruments, new_project_recordings)
                    load_project(project_index)

        while menu == 3:
            
            names = []
            instruments = []
            for instrument in multisounds:                          # list of sounds
                print(instrument.get_name())
                instruments.append(instrument)
                names.append(instrument.get_name().lower())
            
            for instrument in sounds:
                print(instrument.get_name())
                instruments.append(instrument)
                names.append(instrument.get_name().lower())

            new_instrument = ""

            while new_instrument.lower() not in names:
                new_instrument = input("choice: ")
            for instrument in instruments:
                if new_instrument.lower() == instrument.get_name().lower():
                    project_name, project_length, project_tempo, project_instruments, project_recordings = load_project(project_index)
                    project_instruments.append(instrument.get_name())
                    project_recordings.append([""])
            
            save_project(project_index, project_name, project_length, project_tempo, project_instruments, project_recordings)
            project.name = project_name
            project.length = project_length
            project.tempo = project_tempo
            project.instruments = project_instruments
            project.recordings = project_recordings
            with open(f"projects.txt", "r", encoding= "utf8") as file:
                list = file.read()
            list = list + project_index + "/"
            
            with open(f"projects.txt", "w", encoding= "utf8") as file:
                file.write(list)
            menu = 2






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
        project_list, printlist = list_of_projects()
        new_project_index = "project" + str((int(project_list[len(project_list)-1][7:8])+1))
        save_project(new_project_index, "Untitled", 64, 120, [], [])
        project_name, project_length, project_tempo, project_instruments, project_recordings = load_project(new_project_index)
        projects.append(projectclass.Project(project_name, project_length, project_tempo, project_instruments, project_recordings))
        open_project(projects[len(projects)-1])
        edit_menu(projects[len(projects)-1], new_project_index)
    if int(choice) ==2:

        project_list, printlist = list_of_projects()
        count = -1
        for x in printlist:
            count += 1
            print(f"project{count}: {x}\n")

        project_index = " "
        while project_index.lower() not in project_list:
            project_index = input("project: ")
        project_name, project_length, project_tempo, project_instruments, project_recordings = load_project(project_index)
        project = projectclass.Project(project_name, project_length, project_tempo, project_instruments, project_recordings)
        edit_menu(project, project_index)

def main():
    global multisounds
    global sounds

    load_files()
    projectclass.multisounds = multisounds
    projectclass.sounds = sounds
    main_menu()




if __name__ == "__main__":
    main()

