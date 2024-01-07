import subprocess
from pynput import keyboard

def on_activate():
    print("Hello, World!")

# Define the hotkey combination
hotkey = keyboard.HotKey(keyboard.HotKey.parse("<ctrl>+<alt>+H"), on_activate)

# Create a listener that monitors hotkey presses
with keyboard.Listener(on_press=hotkey.press, on_release=hotkey.release) as listener:
    listener.join()