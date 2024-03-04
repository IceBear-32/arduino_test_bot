from tkinter import *
from tkinter import scrolledtext
from threading import Thread
class TerminalWindow(Toplevel):
    def __init__(self, master, title):
        super().__init__(master)
        self.config(bg="black")
        title_bar = Frame(self, bg='black', relief='raised', bd=1)
        title_bar.pack(expand=1, fill='x', side=TOP, ipady=5)
        self.text_area = scrolledtext.ScrolledText(self, wrap=WORD, state=DISABLED,
                                                   bg="black", fg="white", bd=0, insertbackground='white')
        self.text_area.pack(expand=True, fill='both')
        self.text_area.see(END)
        def move_window(event):
            self.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
        self.overrideredirect(1)
        self.geometry('500x500+200+200')
        title = Label(title_bar, text=title, fg='white', bg='black')
        title.pack()
        title_bar.config(cursor='hand2')
        title_bar.bind('<B1-Motion>', move_window)
    def print(self, msg):
        self.text_area.config(state=NORMAL)
        self.text_area.insert(END, str(msg) + "\n")
        self.text_area.config(state=DISABLED)
        self.text_area.see(END)

class Terminal:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("470x20+0+0")
        self.root.text_area = scrolledtext.ScrolledText(self.root, wrap=WORD, state=NORMAL, bg='black', fg='white', bd=0)
        self.root.text_area.pack(expand=False, fill='both')
        self.root.text_area.insert(END, 'Managing terminal instances. Close to kill the program.')
        self.root.text_area.config(state=DISABLED)
        self.root.resizable(width=False, height=False)
        self.root.title("Terminal Manager (MTIM) - Main")
        self.root.config(bg="black")

    def create_terminal(self, terminal_name):
        terminal = TerminalWindow(self.root, terminal_name)
        return terminal
    
    def execute(self):
        self.root.mainloop()

terminal = Terminal()