import os
import shutil
import webbrowser
import atexit
from tkinter import *

root = Tk()


# Moves and renames OG Park_P to CustomMaps folder called Park_P_Temp
def move_park_p():
    park_source = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CookedPCConsole/Park_P.upk'
    park_dest = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CookedPCConsole/Park_P_Temp.upk'

    park_cooked = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CookedPCConsole/Park_P_Temp.upk'
    park_custom = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps'

    os.rename(park_source, park_dest)
    shutil.move(park_cooked, park_custom)

    load_map_button.configure(state=DISABLED)

    atexit.register(return_park_p)
    move_custom_map()

# Disables button to load default map when it's already loaded.
    if "Park_P_Temp.upk" in os.listdir('/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps'):
        load_default_button.config(state=NORMAL)
    else:
        load_default_button.config(state=DISABLED)


# Names Park_P_Temp back to normal and moves it back to CookedPCConsole
def return_park_p():
    park_source = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CookedPCConsole/Park_P.upk'
    park_dest = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CookedPCConsole/Park_P_Temp.upk'

    park_cooked = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CookedPCConsole'
    park_custom = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps/Park_P_Temp.upk'

    shutil.move(park_custom, park_cooked)
    os.rename(park_dest, park_source)


def return_park_p_error():
    park_source = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CookedPCConsole/Park_P.upk'
    park_dest = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CookedPCConsole/Park_P_Temp.upk'

    park_custom = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps/Park_P.upk'

    print("Fix if you can... :(")

    os.rename(park_custom, map_source)
    os.rename(park_dest, park_source)


# Moves and renames custom map to CookedPCConsole
def move_custom_map():
    map_name_ = maps.get('active')
    maps_path_ = ('/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps/', map_name_)
    map_source_ = ''.join(maps_path_)

    map_dest = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps/Park_P.upk'
    map_cooked = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CookedPCConsole'

    os.rename(map_source_, map_dest)
    shutil.move('/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps/Park_P.upk', map_cooked)

# Updates Current Map text
    map_name_ = maps.get('active')

    if map_name_ != "Park_P_Temp.upk":
        current_map_combo = ("Current Map:", map_name_)
        current_map = Label(bottom_frame, text=current_map_combo, bd='8', width='25')
        current_map.grid_remove()
        current_map.grid(column=0, row=0, columnspan=2)


# Returns custom map to CustomMaps and renames it back to normal
def return_custom_map():
    map_name__ = maps.get('active')
    maps_path__ = ('/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps/', map_name__)
    map_source__ = ''.join(maps_path__)

    park_source = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CookedPCConsole/Park_P.upk'
    park_source_og = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CookedPCConsole/Park_P_Temp.upk'
    park_custom = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps/Park_P_Temp.upk'
    park_dest = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps'
    park_cooked = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CookedPCConsole'
    park_p_custom = '/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps/Park_P.upk'

    try:
        shutil.move(park_custom, park_cooked)
        shutil.move(park_source, park_dest)
        os.rename(park_p_custom, map_source__)
        os.rename(park_source_og, park_source)
    except WindowsError:
        return_park_p_error()

    # Updates Current Map Text
    default = "Default"
    current_map_combo = ("Current Map:", default)
    current_map_combo_join = ''.join(current_map_combo)
    current_map = Label(bottom_frame, text=current_map_combo, bd='8', width='25')
    current_map.grid_remove()
    current_map.grid(column=0, row=0, columnspan=2)

    # Disables button to load default map when it's already loaded.
    if "Park_P_Temp.upk" in os.listdir('/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps'):
        load_default_button.config(state=NORMAL)
    else:
        load_default_button.config(state=DISABLED)

    # Disables button to load ANY map when a non-default one is loaded.
    if "Park_P_Temp.upk" not in os.listdir('/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps'):
        load_map_button.config(state=NORMAL)
    else:
        load_default_button.config(state=DISABLED)


def open_maps_folder():
    webbrowser.open('C:/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps')


main_frame = Frame(root, bd='5')
main_frame.pack()

bottom_frame = Frame(root, bd='5', width='30')
bottom_frame.pack()

title_maps = Label(main_frame, bd='5', text="Available Maps:",)
title_maps.grid(column=0, row=0, sticky=W)

# List box and scroll bar to display map choices
maps_scroll_bar = Scrollbar(main_frame)
maps_scroll_bar.grid(column=1, row=1, sticky=N+S)

maps = Listbox(main_frame, font=('default_font', '10'), yscrollcommand = maps_scroll_bar.set, selectmode=SINGLE, width='25', )

maps_in_directory = os.listdir('/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps')
y=1
for x in range(0, len(maps_in_directory)):
        maps.insert(END, "".join(maps_in_directory[x:y]))
        y += 1

maps.grid(column=0, row=1)
maps_scroll_bar.config(command=maps.yview)

map_name = maps.get('active')
maps_path = ('/Program Files (x86)/Steam/steamapps/common/rocketleague/TAGame/CustomMaps', map_name)
map_source = ''.join(maps_path)

# Buttons at bottom
load_map_button = Button(main_frame, text = "Load Map", width='8', command=move_park_p, relief=RAISED)
load_map_button.grid(column=0, columnspan=2, row=0, sticky=E)

maps_folder_button = Button(bottom_frame, text="Maps Folder", width='10', command=open_maps_folder, relief=GROOVE)
maps_folder_button.grid(column=0, row=1, sticky=E)

load_default_button = Button(bottom_frame, text="Load Default", width='10', command=return_custom_map, relief=GROOVE, state=DISABLED)
load_default_button.grid(column=1, row=1, sticky=E)

default = "Default"
current_map_combo = ("Current Map: ", default)
current_map_combo_join = ''.join(current_map_combo)
current_map = Label(bottom_frame, text=current_map_combo_join, bd='8', width='25')
current_map.grid(column=0, row=0, columnspan=2)

root.title("Rocket League Map Loader")
root.geometry('250x300')
root.mainloop()