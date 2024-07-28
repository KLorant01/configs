import keyboard
import json
import Utility

a = '                       ██████████████████||||||::::::......                                                                                 '
b = '                      ██         ██                                                                                                         '
c = '                      ██         ██      ██      █████          ██   ██  █████  ██           ██  █████   ██  █████  ██████||||||::::::......'
d = '                       ██████    ██     ██ █     ██   █    █    ███  ██  █      ██     █     ██  █    █  ██  █      ██                      '
e = '                            ██   ██    ██   █    █████    █ █   ██ █ ██  █████   ██   █ █   ██   █████   ██  █████  ██████|||:::...         '
f = '                            ██   ██   ████████   ██   █    █    ██  ███  █        ██ █   █ ██    █    █  ██  █          ██|:.               '
g = '                      ███████    ██  ██       █  ██   █         ██   ██  █████     ██     ██     █████   ██  █████  ██████.                 '


def menu_draw(curzor, padding, height):

    SCREEN = ' MENU '

    print('')
    print('')
    print('')
    print( a.center(padding))
    print( b.center(padding))
    print( c.center(padding))
    print( d.center(padding))
    print( e.center(padding))
    print( f.center(padding))
    print( g.center(padding))
    print('')
    print('')
    print('')
    print(f" {SCREEN} ".center(padding, "="))
    print(f" Path: /home/usr/StarNewbies/menu ")
    print('')
    print('')
    print('')
    print(f"   {curzor[0]} New Game     ".center(padding))
    print(f"   {curzor[1]} Load Game    ".center(padding))
    print(f"   {curzor[2]} Settings     ".center(padding))
    print(f"   {curzor[3]} Achievements ".center(padding))
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')

    for _ in range(height-40):
        print('')

    print(' Navigate with ARROWS or WS')
    print(' Press ENTER or D to select an option')
    print(' Press ESC to quit the game')
    print('')
    print(f" Current System:  {Utility.show_os()} ".rjust(padding))

def run(delta=True, curzor=['>', ' ', ' ', ' ', ]):

    with open('Data/settings.js', 'r') as fuck:
        DATA = json.loads(fuck.read())

    while 1:
        if delta:

            delta = False
            Utility.clear_window()
            menu_draw(curzor, DATA['settings'][0]['padding'], DATA['settings'][0]['height'])

        if keyboard.is_pressed('w'):
            while True:
                if not keyboard.is_pressed('w'): break
            pos = curzor.index('>') - 1
            if pos < 0: pos = 3
            curzor, curzor[pos], delta = [' ', ' ', ' ', ' ', ], '>', True

        if keyboard.is_pressed('up'):
            while True:
                if not keyboard.is_pressed('up'): break
            pos = curzor.index('>') - 1
            if pos < 0: pos = 3
            curzor, curzor[pos], delta = [' ', ' ', ' ', ' ', ], '>', True


        if keyboard.is_pressed('s'):
            while True:
                if not keyboard.is_pressed('s'): break
            pos = curzor.index('>') + 1
            if pos > 3: pos = 0
            curzor, curzor[pos], delta = [' ', ' ', ' ', ' ', ], '>', True

        if keyboard.is_pressed('down'):
            while True:
                if not keyboard.is_pressed('down'): break
            pos = curzor.index('>') + 1
            if pos > 3: pos = 0
            curzor, curzor[pos], delta = [' ', ' ', ' ', ' ', ], '>', True


        if keyboard.is_pressed('esc'):
            while True:
                if not keyboard.is_pressed('esc'): break
            return 0

        if keyboard.is_pressed('q'):
            while True:
                if not keyboard.is_pressed('q'): break
            return 0


        if keyboard.is_pressed('d'):
            while True:
                if not keyboard.is_pressed('d'): break

            match curzor.index('>'):
                case 0:
                    return 2
                case 1:
                    return 3
                case 2:
                    return 4
                case 3:
                    return 5

        if keyboard.is_pressed('enter'):
            while True:
                if not keyboard.is_pressed('enter'): break

            match curzor.index('>'):
                case 0:
                    return 2
                case 1:
                    return 3
                case 2:
                    return 4
                case 3:
                    return 5

        if keyboard.is_pressed('right'):
            while True:
                if not keyboard.is_pressed('right'): break

            match curzor.index('>'):
                case 0:
                    return 2
                case 1:
                    return 3
                case 2:
                    return 4
                case 3:
                    return 5
