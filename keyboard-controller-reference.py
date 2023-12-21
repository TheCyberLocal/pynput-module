"""
This Python script serves as a refernce sheet for the pynput.keyboard module, showcases key press simulation,
hotkey binding, event recording and playback, text replacement abbreviations, and state checking.
"""

from pynput.keyboard import Controller  # Importing the Controller submodule from pynput.keyboard

keyboard = Controller()  # Create a keyboard controller object.

# Simulate pressing and releasing 'shift+s' and then a space.
keyboard.press_and_release('shift+s, space')

# Type a string 'Here comes the BOOM'.
keyboard.write('Here comes the BOOM')

# Press and hold 'a' key.
keyboard.press('a')

# Release 'a' key.
keyboard.release('a')

# Define a hotkey 'ctrl+shift+a' that triggers a print function.
keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Define another hotkey for 'page up, page down' to type 'foobar'.
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# Wait until 'esc' key is pressed.
keyboard.wait('esc')

# Record all keyboard events until 'esc' is pressed.
recorded = keyboard.record(until='esc')

# Replay recorded events at three times the speed.
keyboard.play(recorded, speed_factor=3)

# Replace '@@' with an email address when typed followed by a space.
keyboard.add_abbreviation('@@', 'long.email@example.com')

# Wait indefinitely until a keyboard interrupt or another stop condition.
keyboard.wait()

# Check if 'ctrl' is currently pressed.
if keyboard.is_pressed('ctrl'):
    print('ctrl was pressed')
