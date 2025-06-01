import keyboard

def register_hotkeys(autopaster):
    keyboard.add_hotkey('f8', autopaster.toggle_start_stop)