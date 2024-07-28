import random
import Data
import time

class Geci:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def data(self):
        return f'{self.a} {self.b}'

person = Geci(2,3)

g = [0,1,2,3]

Act_map = random.choice(Data.ship_maps)

print(time.time())