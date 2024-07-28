import json
import random

import Data
import Utility
import Creation as Cr

def draw_gen(curzor, padding, height, Mapp):

    S1 = Mapp[0][2]
    S2 = Mapp[1][2]
    S3 = Mapp[2][2]
    S4 = Mapp[3][2]
    S5 = Mapp[4][2]
    S6 = Mapp[5][2]
    S7 = Mapp[6][2]
    S8 = Mapp[7][2]



    print(f" Path: /home/usr/StarNewbies/menu ")
    print('')
    print(f'                                                                                                                           '.center(padding))
    print(f'                                                    +-----------------+                                                    '.center(padding))
    print(f'                                                    |                 |                                                    '.center(padding))
    print(f'                                                    |{S1             }|                                                    '.center(padding))
    print(f'                                                    |                 |                                                    '.center(padding))
    print(f'                               +-----------------+  |-----]     [-----|  +-----------------+                               '.center(padding))
    print(f'                               |                 |__|                 |__|                 |                               '.center(padding))
    print(f'                               |{S2             }    {S3             }    {S4             }|                               '.center(padding))
    print(f'                               |                 |¯¯|                 |¯¯|                 |                               '.center(padding))
    print(f'                               |-----]     [-----|  |-----]     [-----|  |-----]     [-----|                               '.center(padding))
    print(f'                               |                 |  |                 |  |                 |                               '.center(padding))
    print(f'                               |{S5             }|  |{S6             }|  |{S7             }|                               '.center(padding))
    print(f'                               |                 |  |                 |  |                 |                               '.center(padding))
    print(f'                               +-----------------+  |-----]     [-----|  +-----------------+                               '.center(padding))
    print(f'                                                    |                 |                                                    '.center(padding))
    print(f'                                                    |{S8             }|                                                    '.center(padding))
    print(f'                                                    |                 |                                                    '.center(padding))
    print(f'                                                    +-----------------+                                                    '.center(padding))
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
    print('')
    print('')
    print('')
    print('')
    print('')

    for _ in range(height - 40):
        print('')

    print(f" Current System:  {Utility.show_os()} ".rjust(padding))

def run(val = False, delta = True, curzor = []):
    with open('Data/settings.js', 'r') as fuck:
        DATA = json.loads(fuck.read())

    curzor = 0
    padding = DATA['settings'][0]['padding']
    height = DATA['settings'][0]['height']

    Ship = Cr.ship()
    Cr.ship.make(Ship, [])

    Crew_A = Cr.crew_Member()
    Crew_B = Cr.crew_Member()
    Crew_C = Cr.crew_Member()

    Cr.crew_Member.make(Crew_A, 'commander', 10, 4)
    Cr.crew_Member.make(Crew_B, 'engineer' , 10, 4)
    Cr.crew_Member.make(Crew_C, 'biologist', 10, 4)

    Act_map = random.choice(Data.ship_maps)     # Random mapp chose

    while not val:
        if delta:
            Utility.clear_window()
            draw_gen(curzor, padding, height, Act_map)

    while 1:
        pass