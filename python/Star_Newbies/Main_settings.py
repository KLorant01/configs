import json
import keyboard
import Utility

def settings_draw(curzor, padding, height, C_autoskip, audio):
    SCREEN = 'Settings'

    if audio == 100:
        str_audio = str(audio)
    elif audio//10 == 0:
        str_audio = '  ' + str(audio)
    else:
        str_audio = ' ' + str(audio)

    print('')
    print('')
    print(f" {SCREEN} ".center(padding, "="))
    print(f" Path: /home/usr/StarNewbies/settings ")
    print('')
    print('')
    print('')
    print(f"   {curzor[0]} Audio                                    {str(str_audio) + ' %'}                                                ".center(padding))
    print(f"   {curzor[1]} Cinematic autoskip                      {'off  [ON]' if C_autoskip else '[OFF]  on'}                                              ".center(padding))
    print(f"   {curzor[2]} Window height                            {str(height) + ' line'}                                             ".center(padding))
    print(f"   {curzor[3]} Window wight                                {str(padding) + ' character'}                                     ".center(padding))
    print(f"   {curzor[4]} Apply                                                                                          ".center(padding))

    for _ in range(22):
        print('')

    for _ in range(height - 40):
        print('')

    print(' Navigate with ARROWS or WS')
    print(' Use the ARROWS or the AD keys to modify the options')
    print(' Select <Apply> and press ENTER to save changes')
    print(' Press ESC or Q to quit settings')
    print('')
    print(f" Current System:  {Utility.show_os()} ".rjust(padding))


def apply_changes(DATA, padding, height, C_autoskip, audio):
    DATA['settings'][0]['audio'] = audio
    DATA['settings'][0]['C_autoskip'] = C_autoskip
    DATA['settings'][0]['padding'] = padding
    DATA['settings'][0]['height'] = height
    with open('Data/settings.js', 'w') as fuck:
        fuck.write(json.dumps(DATA, indent=2))


def run(delta=True,):

    curzor = ['>', ' ', ' ', ' ', ' ']

    with open('Data/settings.js', 'r') as fuck:
        DATA = json.loads(fuck.read())

    audio = DATA['settings'][0]['audio']
    C_autoskip = DATA['settings'][0]['C_autoskip']
    padding = DATA['settings'][0]['padding']
    height = DATA['settings'][0]['height']

    while 1:
        if delta:
            delta = False
            Utility.clear_window()
            settings_draw(curzor, padding, height, C_autoskip, audio)

        if keyboard.is_pressed('w'):
            while True:
                if not keyboard.is_pressed('w'): break
            pos = curzor.index('>') - 1
            if pos < 0: pos = 4
            curzor, curzor[pos], delta = [' ', ' ', ' ', ' ', ' '], '>', True

        if keyboard.is_pressed('up'):
            while True:
                if not keyboard.is_pressed('up'): break
            pos = curzor.index('>') - 1
            if pos < 0: pos = 4
            curzor, curzor[pos], delta = [' ', ' ', ' ', ' ', ' '], '>', True

        if keyboard.is_pressed('s'):
            while True:
                if not keyboard.is_pressed('s'): break
            pos = curzor.index('>') + 1
            if pos > 4: pos = 0
            curzor, curzor[pos], delta = [' ', ' ', ' ', ' ', ' '], '>', True

        if keyboard.is_pressed('down'):
            while True:
                if not keyboard.is_pressed('down'): break
            pos = curzor.index('>') + 1
            if pos > 4: pos = 0
            curzor, curzor[pos], delta = [' ', ' ', ' ', ' ', ' '], '>', True

        if keyboard.is_pressed('esc'):
            while True:
                if not keyboard.is_pressed('esc'): break
            return 1

        if keyboard.is_pressed('q'):
            while True:
                if not keyboard.is_pressed('q'): break
            return 1

        if keyboard.is_pressed('d'):
            while True:
                if not keyboard.is_pressed('d'): break

            match curzor.index('>'):
                case 0:
                    if audio < 100:
                        audio += 5
                case 1:
                    C_autoskip = not C_autoskip
                case 2:
                    if height < 100:
                        height += 1
                case 3:
                    if padding < 900:
                        padding += 1
                case 4:
                    apply_changes(DATA, padding, height, C_autoskip, audio)
            delta = True

        if keyboard.is_pressed('right'):
            while True:
                if not keyboard.is_pressed('right'): break

            match curzor.index('>'):
                case 0:
                    if audio < 100:
                        audio += 5
                case 1:
                    C_autoskip = not C_autoskip
                case 2:
                    if height < 100:
                        height += 1
                case 3:
                    if padding < 900:
                        padding += 1
                case 4:
                    apply_changes(DATA, padding, height, C_autoskip, audio)
            delta = True

        if keyboard.is_pressed('a'):
            while True:
                if not keyboard.is_pressed('a'): break

            match curzor.index('>'):
                case 0:
                    if audio > 0:
                        audio = audio - 5
                case 1:
                    C_autoskip = not C_autoskip
                case 2:
                    if height > 0:
                        height = height - 1
                case 3:
                    if padding > 0:
                        padding = padding - 1
                case 4:
                    apply_changes(DATA, padding, height, C_autoskip, audio)
            delta = True

        if keyboard.is_pressed('left'):
            while True:
                if not keyboard.is_pressed('left'): break

            match curzor.index('>'):
                case 0:
                    if audio > 0:
                        audio = audio - 5
                case 1:
                    C_autoskip = not C_autoskip
                case 2:
                    if height > 0:
                        height = height - 1
                case 3:
                    if padding > 0:
                        padding = padding - 1
                case 4:
                    apply_changes(DATA, padding, height, C_autoskip, audio)
            delta = True

        if keyboard.is_pressed('enter'):
            while True:
                if not keyboard.is_pressed('enter'): break

            match curzor.index('>'):
                case 0:
                    pass
                case 1:
                    C_autoskip = not C_autoskip
                    delta = True
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    apply_changes(DATA, padding, height, C_autoskip, audio)
                    delta = True
