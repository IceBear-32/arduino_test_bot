from voice import record
import threading
from const import *
from txt2cmd import Text2CMD as TXT
from multi_instance_terminal import terminal
from brain import *
from time import sleep
from random import random, randint
def exc():
    while True:
        record()
        br = threading.Thread(target=lambda: Brain().cmd2pw(TXT.cmd_stream))
        br.start()
        for i in range(1, randint(2,6)):
            d = randint(1,5)
            if d == 1:
                DO(1, 0, 1, 0)
                sleep(random()*3)
            if d == 2:
                DO(1, 0, 1, 0)
                sleep(random()*3)
            if d == 3:
                DO(0, 1, 1, 0)
                sleep(random()*.5+.35)
            if d == 4:
                DO(1, 0, 0, 1)
                sleep(random()*.5+.35)
            if d == 5:
                DO(0, 1, 1, 0)
                sleep(random()*.75+.25)
            DO(0, 0, 0, 0)
            sleep(random()*2+.25)
        sleep(.75)
ex = threading.Thread(target=exc)
ex.start()
terminal.execute()
ex.join()