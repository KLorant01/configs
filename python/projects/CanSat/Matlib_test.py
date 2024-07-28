from typing import List, Any

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

DATA = []
fonal = ''
TIME = []

try:
    with open("file path", 'rb') as File:
        for i in File:
            a = File.readline(i)
            DATA.append(a)
except FileNotFoundError:
    print("no file?")
except Exception as e:
    print("Error -> ", e)

for f in DATA:
    coma = 0
    for caracter in f:
        if caracter == ',':

            match coma:
                case 0:
                    TIME.append(fonal)
                case 1:
                    pass
                case 2:
                    pass
                case _:
                    pass
            fonal = ''
            coma += 1

        else:
            fonal = fonal + caracter





plt.show()