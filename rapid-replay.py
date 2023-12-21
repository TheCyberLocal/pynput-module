"""
The script uses the 's' key to toggle recording of keystrokes and the 'p' key to play them back at double speed.
The recording starts when 's' is pressed for the first time and stops with the next press of 's'.
The recorded keystrokes are stored and can be played back multiple times by pressing 'p'.
The script demonstrates practical usage of pynput for custom keyboard interactions.
"""

from pynput import keyboard  # Import the keyboard module from pynput for controlling and monitoring the keyboard.
import time  # Import the time module for handling time-related tasks like delays.

recorded = []  # Initialize an empty list to store the recorded keystroke events.
is_recording = False  # A boolean flag to keep track of whether the script is currently recording keystrokes.

def on_activate_start():
    global is_recording  # Declare 'is_recording' as a global variable to modify its value.
    is_recording = True  # Set the recording flag to True, indicating the start of recording.
    print("Recording started")  # Output a message to the console indicating that recording has started.

def on_activate_stop():
    global is_recording, recorded  # Declare 'is_recording' and 'recorded' as global variables.
    is_recording = False  # Set the recording flag to False, indicating the end of recording.
    recorded = keyboard_listener.record(stop_recording)  # Start recording keyboard events and store them in 'recorded'.
    print("Recording stopped")  # Output a message to the console indicating that recording has stopped.

def stop_recording():
    return False  # When called, this function stops the recording.

def on_playback():
    print("Playing back")  # Output a message to the console indicating that playback is starting.
    for event in recorded:  # Iterate through each recorded keystroke event.
        keyboard_listener.play([event], speed_factor=2)  # Play each event at double the speed.
        time.sleep(0.01)  # Add a brief pause (10ms) between each event to prevent overlap.

def on_press(key):
    if key == keyboard.KeyCode(char='s'):  # Check if the pressed key is 's'.
        if not is_recording:
            on_activate_start()  # If 's' is pressed and not currently recording, start recording.
        else:
            on_activate_stop()  # If 's' is pressed and currently recording, stop recording.
    elif key == keyboard.KeyCode(char='p') and not is_recording:  # Check if the pressed key is 'p' and not currently recording.
        on_playback()  # If 'p' is pressed, start playback of recorded keystrokes.

with keyboard.Listener(on_press=on_press) as listener:
    keyboard_listener = keyboard.Controller()  # Create a keyboard controller instance for simulating key presses.
    listener.join()  # Start the keyboard listener to monitor keystroke events.
