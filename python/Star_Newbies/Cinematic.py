import json
import time
import Utility

FRAME_RATE = 0.07


def frame(img, rate, padding, height):
    Utility.clear_window()
    with open(f'Cin/{img}', 'r') as fuck:
        for line in fuck:
            line = line.strip()
            line = line.replace('$', '')
            print(line.center(padding))

        for _ in range(height - 39):
            print('')
        time.sleep(rate)


def Cinematic_run():
    with open('settings.js', 'r') as fuck:
        DATA = json.loads(fuck.read())
        height = DATA['settings'][0]['height']
        padding = DATA['settings'][0]['padding']

    frame('C0001', 0.65, padding, height)  # | IDLE
    frame('C0000', 0.65, padding, height)  # |
    frame('C0001', 0.65, padding, height)  # |
    frame('C0000', 0.65, padding, height)  # |
    frame('C0001', 0.65, padding, height)  # |

    frame('C0002', 0.5, padding, height)  # | CYCLE 377 spelling
    frame('C0003', 0.35, padding, height)  # |
    frame('C0004', 0.25, padding, height)  # |
    frame('C0005', 0.13, padding, height)  # |
    frame('C0006', 0.13, padding, height)  # |
    frame('C0007', 0.45, padding, height)  # |
    frame('C0008', 0.13, padding, height)  # |
    frame('C0009', 0.13, padding, height)  # |
    frame('C0010', 0.13, padding, height)  # |
    frame('C0011', 0.35, padding, height)  # |
    frame('C0012', 0.65, padding, height)  # |
    frame('C0011', 0.65, padding, height)  # |
    frame('C0012', 0.65, padding, height)  # |
    frame('C0011', 0.45, padding, height)  # |
    frame('C0013', 0.125, padding, height)  # |
    frame('C0014', 0.125, padding, height)  # |
    frame('C0015', 0.65, padding, height)  # |
    frame('C0016', 0.65, padding, height)  # |
    frame('C0015', 0.33, padding, height)  # |

    frame('C0017', 0.25, padding, height)  # | STELLARSYSTEM: 54a00 spelling
    frame('C0018', 0.13, padding, height)  # |
    frame('C0019', 0.13, padding, height)  # |
    frame('C0020', 0.13, padding, height)  # |
    frame('C0021', 0.13, padding, height)  # |
    frame('C0022', 0.13, padding, height)  # |
    frame('C0023', 0.13, padding, height)  # |
    frame('C0024', 0.13, padding, height)  # |
    frame('C0025', 0.13, padding, height)  # |
    frame('C0026', 0.13, padding, height)  # |
    frame('C0027', 0.13, padding, height)  # |
    frame('C0028', 0.13, padding, height)  # |
    frame('C0029', 0.13, padding, height)  # |
    frame('C0030', 0.35, padding, height)  # |
    frame('C0031', 0.13, padding, height)  # |
    frame('C0032', 0.13, padding, height)  # |
    frame('C0033', 0.13, padding, height)  # |
    frame('C0034', 0.13, padding, height)  # |
    frame('C0035', 0.25, padding, height)  # |
    frame('C0036', 0.65, padding, height)  # |

    frame('C0037', 0.65, padding, height)  # | IDlE
    frame('C0036', 0.65, padding, height)  # |
    frame('C0037', 0.65, padding, height)  # |
    frame('C0036', 0.65, padding, height)  # |
    frame('C0037', 0.65, padding, height)  # |
    frame('C0036', 0.65, padding, height)  # |

    frame('C0036', 0.02, padding, height)  # | RECAP
    frame('C0035', 0.02, padding, height)  # |
    frame('C0034', 0.02, padding, height)  # |
    frame('C0033', 0.02, padding, height)  # |
    frame('C0032', 0.02, padding, height)  # |
    frame('C0031', 0.02, padding, height)  # |
    frame('C0030', 0.02, padding, height)  # |
    frame('C0029', 0.02, padding, height)  # |
    frame('C0028', 0.02, padding, height)  # |
    frame('C0027', 0.02, padding, height)  # |
    frame('C0026', 0.02, padding, height)  # |
    frame('C0025', 0.02, padding, height)  # |
    frame('C0024', 0.02, padding, height)  # |
    frame('C0023', 0.02, padding, height)  # |
    frame('C0022', 0.02, padding, height)  # |
    frame('C0021', 0.02, padding, height)  # |
    frame('C0020', 0.02, padding, height)  # |
    frame('C0019', 0.02, padding, height)  # |
    frame('C0018', 0.02, padding, height)  # |
    frame('C0017', 0.02, padding, height)  # |
    frame('C0016', 0.02, padding, height)  # |
    frame('C0015', 0.02, padding, height)  # |
    frame('C0014', 0.02, padding, height)  # |
    frame('C0013', 0.02, padding, height)  # |
    frame('C0012', 0.02, padding, height)  # |
    frame('C0011', 0.02, padding, height)  # |
    frame('C0010', 0.02, padding, height)  # |
    frame('C0009', 0.02, padding, height)  # |
    frame('C0008', 0.02, padding, height)  # |
    frame('C0007', 0.02, padding, height)  # |
    frame('C0006', 0.02, padding, height)  # |
    frame('C0005', 0.02, padding, height)  # |
    frame('C0004', 0.02, padding, height)  # |
    frame('C0003', 0.02, padding, height)  # |
    frame('C0002', 0.02, padding, height)  # |
    frame('C0001', 0.65, padding, height)  # |
    frame('C0000', 0.65, padding, height)  # |


Cinematic_run()

# TODO make a coooool cutsceen!
