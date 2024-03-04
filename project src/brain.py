from nano import board
from tokens import *
from time import sleep
from random import random
from response import response
DO1 = board.get_pin('d:12:o')
DO2 = board.get_pin('d:11:o')
DO3 = board.get_pin('d:10:o')
DO4 = board.get_pin('d:8:o')
IRF = board.get_pin('d:6:i')
IRB = board.get_pin('d:7:i')
ECHO = board.get_pin('d:3:i')
TRIG = board.get_pin('d:4:o')
def DO(_1, _2, _3, _4):
    sleep(.1)
    DO1.write(_1)
    DO2.write(_2)
    DO3.write(_3)
    DO4.write(_4)
class Brain:
    def cmd2pw(self, cmd_s):
        _lt = None
        lt = None
        for x, cmd_ in enumerate(cmd_s):
            cmd = cmd_[2]
            if lt != None:
                if lt == BehaviourToken.DIR:
                    if _lt == BehaviourToken.MV or _lt == BehaviourToken.RT:
                        lt, _lt = _lt, None
                    else:
                        _lt, lt = None, None
                if lt == BehaviourToken.MV:
                    if cmd in BehaviourTokenEQ.M_FW:
                        DO(1, 0, 1, 0)
                    if cmd in BehaviourTokenEQ.M_BW:
                        DO(0, 1, 0, 1)
                    if cmd in BehaviourTokenEQ.M_I:
                        DO(0, 0, 0, 0)
                if lt == BehaviourToken.RT:
                    if cmd in BehaviourTokenEQ.RT_L:
                        DO(0, 1, 1, 0)
                        sleep(.55)
                        DO(0, 0, 0, 0)
                    if cmd in BehaviourTokenEQ.RT_R:
                        DO(1, 0, 0, 1)
                        sleep(.5)
                        DO(0, 0, 0, 0)
                    if cmd in BehaviourTokenEQ.RT_I:
                        DO(0, 0, 0, 0)
                    if cmd in BehaviourTokenEQ.RT_NE:
                        DO(0, 0, 0, 0)
                    if cmd in BehaviourTokenEQ.RT_BACK:
                        DO(0, 1, 1, 0)
                        sleep(random()*1.5+.35)
                        DO(0, 0, 0, 0)
                if lt == BehaviourToken.NE:
                    continue
                if lt == BehaviourToken.PE:
                    continue
                if lt == BehaviourToken.INT or lt == BehaviourToken.QS or lt == BehaviourToken.QR or ' ' in cmd:
                    response(cmd)
                    break
            _lt = lt
            if cmd in BehaviourTokenEQ.MV:
                lt = BehaviourToken.MV
            elif cmd in BehaviourTokenEQ.RT:
                lt = BehaviourToken.RT
            elif cmd in BehaviourTokenEQ.DIR:
                lt = BehaviourToken.DIR
            elif cmd in BehaviourTokenEQ.MV_F:
                lt = BehaviourToken.MV
            elif cmd in BehaviourTokenEQ.QR:
                lt = BehaviourToken.QR
            elif cmd in BehaviourTokenEQ.QS:
                lt = BehaviourToken.QS
            elif cmd in BehaviourTokenEQ.INT:
                lt = BehaviourToken.INT
            elif cmd in BehaviourTokenEQ.NE:
                lt = BehaviourToken.NE
            elif cmd in BehaviourTokenEQ.PE:
                lt = BehaviourToken.PE
            elif cmd in BehaviourTokenEQ.DIR_F:
                DO(1, 0, 1, 0)
            elif cmd in BehaviourTokenEQ.DIR_B:
                DO(0, 1, 0, 1)
            elif cmd in BehaviourTokenEQ.DIR_L:
                DO(0, 1, 1, 0)
                sleep(.55)
                DO(0, 0, 0, 0)
            elif cmd in BehaviourTokenEQ.DIR_R:
                DO(1, 0, 0, 1)
                sleep(.55)
                DO(0, 0, 0, 0)
            elif ' ' in cmd:
                response(cmd)
                break
            else:
                lt = None