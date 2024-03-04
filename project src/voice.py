from pyfirmata import Arduino
import speech_recognition as sr
import threading
from utils import main, error
from txt2cmd import Text2CMD
rec = sr.Recognizer()

def process_speech():
    try:
        main.print('>>\t[Listening...]')
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic, 0.5)
            aud = rec.listen(mic, 3.25, 1)
            main.print('>>\t[Recognizing...]')
            speech = rec.recognize_google(aud)
            main.print('>> '+speech)
            cmd = Text2CMD(speech)
            cmd.equat()
    except Exception as E:
        Text2CMD.cmd_stream = []
        error.print('>> '+('...' if len(str(E)+'...') == 3 else str(E)))
        main.print('>>\t[Failed to recognize...]')
        main.print('>>\t[Trying again...]')

record = lambda: threading.Thread(target=process_speech, daemon=True).start()