#from neural_net import net
from tokens import *
class Text2CMD:
    cmd_stream = []
    def __init__(self, txt):
        self.txt = txt
        self.lt = None
        self.li = 0
        self.lv = ''
        self.trace = 0
    def Token(self, txt):
        self.t = None
        self.i = 0
        self.ni = 0
        self.v = ''
        eq = [
            BehaviourTokenEQ.MV,
            BehaviourTokenEQ.M_BW,
            BehaviourTokenEQ.M_FW,
            BehaviourTokenEQ.MVF_BW,
            BehaviourTokenEQ.MVF_FW,
            BehaviourTokenEQ.MV_F,
            BehaviourTokenEQ.DIR,
            BehaviourTokenEQ.DIR_B,
            BehaviourTokenEQ.DIR_F,
            BehaviourTokenEQ.DIR_I,
            BehaviourTokenEQ.DIR_L,
            BehaviourTokenEQ.DIR_R,
            BehaviourTokenEQ.INT,
            BehaviourTokenEQ.M_I,
            BehaviourTokenEQ.M_NE,
            BehaviourTokenEQ.NE,
            BehaviourTokenEQ.PE,
            BehaviourTokenEQ.REF,
            BehaviourTokenEQ.RT,
            BehaviourTokenEQ.RT_BACK,
            BehaviourTokenEQ.RT_I,
            BehaviourTokenEQ.RT_R,
            BehaviourTokenEQ.RT_L,
            BehaviourTokenEQ.RT_NE,
            BehaviourTokenEQ.QR,
            BehaviourTokenEQ.QS
        ]
        bt = [
            BehaviourToken.MV,
            BehaviourToken.M_BW,
            BehaviourToken.M_FW,
            BehaviourToken.MVF_BW,
            BehaviourToken.MVF_FW,
            BehaviourToken.MV_F,
            BehaviourToken.DIR,
            BehaviourToken.DIR_B,
            BehaviourToken.DIR_F,
            BehaviourToken.DIR_N,
            BehaviourToken.DIR_L,
            BehaviourToken.DIR_R,
            BehaviourToken.INT,
            BehaviourToken.M_I,
            BehaviourToken.M_NE,
            BehaviourToken.NE,
            BehaviourToken.PE,
            BehaviourToken.REF,
            BehaviourToken.RT,
            BehaviourToken.RT_B,
            BehaviourToken.RT_I,
            BehaviourToken.RT_R,
            BehaviourToken.RT_L,
            BehaviourToken.RT_NE,
            BehaviourToken.QR,
            BehaviourToken.QS
        ]
        for x, q in enumerate(eq):
            if txt in q:
                self.t = bt[x]
                self.v = txt
                if self.t in [BehaviourToken.MV, BehaviourToken.RT, BehaviourToken.MV_F, BehaviourToken.DIR]:
                    if self.t == BehaviourToken.MV:
                        self.i = Intents.MV
                    elif self.t == BehaviourToken.RT:
                        self.i = Intents.RT
                    elif self.t == BehaviourToken.MV_F:
                        self.i = Intents.MV_F
                    elif self.t == BehaviourToken.DIR:
                        self.i = Intents.DIR
                    else:
                        self.i = Intents.NI
                    if NIntents.MV(self.t):
                        self.ni = Intents.MV
                    elif NIntents.RT(self.t):
                        self.ni = Intents.RT
                    elif NIntents.DIR(self.t):
                        self.ni = Intents.DIR
                    elif NIntents.MV_F(self.t):
                        self.ni = Intents.MV_F
                    else:
                        self.ni = Intents.NI
        return (self.t, self.i, self.ni, self.v) if self.t is not None else None

    def equat(self):
        Text2CMD.cmd_stream = []
        self.lt = None
        self.li = 0
        self.lv = ''
        self.trace = 0
        ct = None
        ci = 0
        cv = ''
        txt_stream = self.txt.split(' ')
        for x, txt in enumerate(txt_stream):
            try:
                txt = float(txt)
            except:
                pass
            t = self.Token(txt)
            nt = self.Token(txt_stream[x+1]) if x + 1 < len(txt_stream) else [[-5],[-5],[-5],[-5]]
            if t is not None:
                ct = t[0]
                ci = t[1]
                cv = t[3]
            else:
                continue
            clen = len(Text2CMD.cmd_stream)
            if self.trace > 0:
                self.trace -= 1
                continue
            if self.lt != None:
                if self.li == Intents.MV:
                    if NIntents.MV(ct):
                        Text2CMD.cmd_stream.insert(clen, (ct, ci, cv))
                    elif NIntents.MV(nt[0]):
                        Text2CMD.cmd_stream.insert(clen, (nt[0], nt[1], nt[3]))
                        Text2CMD.cmd_stream.insert(clen+1, (ct, ci, cv))
                        self.trace += 1
                elif self.li == Intents.DIR:
                    if NIntents.DIR(ct):
                        Text2CMD.cmd_stream.insert(clen, (ct, ci, cv))
                    elif NIntents.DIR(nt[0]):
                        Text2CMD.cmd_stream.insert(clen, (nt[0], nt[1], nt[3]))
                        Text2CMD.cmd_stream.insert(clen+1, (ct, ci, cv))
                        self.trace += 1
                elif self.li == Intents.RT:
                    if NIntents.RT(ct):
                        Text2CMD.cmd_stream.insert(clen, (ct, ci, cv))
                    elif NIntents.RT(nt[0]):
                        Text2CMD.cmd_stream.insert(clen, (nt[0], nt[1], nt[3]))
                        Text2CMD.cmd_stream.insert(clen+1, (ct, ci, cv))
                        self.trace += 1
                elif self.li == Intents.MV_F:
                    if NIntents.MV_F(ct):
                        Text2CMD.cmd_stream.insert(clen, (ct, ci, cv))
                    elif NIntents.MV_F(nt[0]):
                        Text2CMD.cmd_stream.insert(clen, (nt[0], nt[1], nt[3]))
                        Text2CMD.cmd_stream.insert(clen+1, (ct, ci, cv))
                        self.trace += 1
                elif (self.li == Intents.NI or self.li == 0):
                    Text2CMD.cmd_stream.insert(clen, (ct, ci, cv))
                else:
                    continue
            else:
                if ct == BehaviourToken.QS or ct == BehaviourToken.QR or ct == BehaviourToken.INT or ct == BehaviourToken.IN_HW:
                    Text2CMD.cmd_stream.append((ct, ci, ' '.join(txt_stream)))
                    break
                Text2CMD.cmd_stream.append((ct, ci, cv))
            self.lt = ct
            self.li = ci
            self.lv = cv