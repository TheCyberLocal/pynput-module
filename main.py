from pynput.keyboard import Controller

keyboard = Controller()
# import keyboard

keyboard.press_and_release('shift+s, space')

keyboard.write('Here comes the BOOM')

keyboard.press('a')

keyboard.release('a')

keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Press page up then page down to type "foobar"
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# Blocks until you press esc.
keyboard.wait('esc')

# record events until esc is pressed
recorded = keyboard.record(until='esc')

# Then replay back at three times the speed.
keyboard.play(recorded, speed_factor=3)

# Type @@ then press space to replace with abbreviation.
keyboard.add_abbreviation('@@', 'long.email@example.com')

# Blocks keyboard like while true.
keyboard.wait()

if keyboard.is_pressed('ctrl'):
    print('ctrl was pressed')
