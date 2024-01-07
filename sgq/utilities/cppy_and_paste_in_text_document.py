# il codice creato con l'aiuto di chatgpt recupera il testo selezionato e lo copia ed incolla
# direttamente nella directory definita
# alla data del 25 giugno 2023 non si riesce a far avviare il programma direttamente dalla 
# combinazione di tasti
import subprocess
import tkinter as tk
from pynput import keyboard

file_path = '/home/mauro/Scrivania/django_general_template2/sgq/utilities/storage/selected_text.txt'
ctrl_pressed = False

def copy_selected_text():
    try:
        # Copy the selected text using xclip
        subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)
        selected_text = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True, check=True).stdout.strip()

        # Append the selected text to the file
        with open(file_path, 'a') as file:
            file.write('\n' + '_' * 40 + 'OOOOOOOOOO' + '-' * 40 + '\n')  # Line of underscores before the text
            file.write(selected_text + '\n')
            file.write('_' * 20 + '\n')  # Line of underscores after the text

        message_var.set("Text copied and appended!")  # Update message variable
    except Exception as e:
        message_var.set("Error: " + str(e))  # Update message variable

def on_key_press(key):
    global ctrl_pressed

    if key == keyboard.Key.ctrl_l:
        ctrl_pressed = True

    if key == keyboard.KeyCode.from_char('c'):
        if ctrl_pressed:
            copy_selected_text()

def on_key_release(key):
    global ctrl_pressed

    if key == keyboard.Key.ctrl_l:
        ctrl_pressed = False

# Create GUI window
window = tk.Tk()
window.title("Copy and Paste Text")
window.geometry("500x400")  # Set the size of the window (width x height)
window.configure(bg="#002300")  # Set the background color of the window

# Create message variable
message_var = tk.StringVar()
message_var.set("Press Ctrl+C to copy and append selected text.")

# Create label
label = tk.Label(window, textvariable=message_var)
label.pack()

# Start listener for key presses and releases
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    try:
        # Start the GUI event loop
        window.mainloop()
    except KeyboardInterrupt:
        # Stop the listener when Ctrl+C is pressed
        listener.stop()
