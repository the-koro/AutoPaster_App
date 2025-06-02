import keyboard

def register_hotkeys(autopaster):
    keyboard.add_hotkey('f1', autopaster.show_help)
    keyboard.add_hotkey('f4', autopaster.reset)
    keyboard.add_hotkey('f8', autopaster.toggle_start_stop)