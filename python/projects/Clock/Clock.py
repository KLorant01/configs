import time
import os
import datetime
import Clock_graphic as Cg

def delta_time(function):
    def wrapper(*args, **kwargs):
        act_time = time.time()
        function(*args, **kwargs)
        delta_time = time.time() - act_time
        print(f"{function} :: {delta_time}")
    return wrapper

@delta_time
def valami(num):
    for _ in range(num):
        pass

#    valami(300_000_000)
    print(os.environ)
    print(datetime.datetime.now())

def Init():
    setup = input("Cloc >> ")

    if setup == "":                 return 1
    if setup == "default":          return 1

    if setup == "exit":             return 0





def main():
    state = Init()
    while 1:


        match state:
            case 1:
                Cg.draw_def()
            case 0:
                break

if __name__ == "__main__":
    main()