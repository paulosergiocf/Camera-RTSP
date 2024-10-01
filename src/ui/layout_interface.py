import tkinter as tk
import tkinter.font as font
from .personalization import Colors, Fonts
from .labels import Labels

class Interface(tk.Frame):
    def __init__(self, frame):
        super().__init__(frame, bg=frame.cget('bg'))
 
        self.left = tk.Frame(self, bg=self.cget('bg'))
        self.left.place(relx=0.0, rely=0.15, relwidth=0.3, relheight=0.7)

        self.right = tk.Frame(self, bg=Colors.CINZA_ESCURO.value, border=2)
        self.right.place(relx=0.3, rely=0.15, relwidth=0.7, relheight=0.7)

class Title(tk.Frame):
    def __init__(self, frame):
        super().__init__(frame, bg=frame.cget('bg'))

        title = tk.Label(self, font=font.Font(family=Fonts.FONT_ROBOTO.value, size=14), text=F'{Labels.TITLE.value}', bg=frame.cget('bg'), fg=Colors.CINZA_CLARO.value)
        title.pack()