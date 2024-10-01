import tkinter as tk
from .personalization import Colors


class PtzConstrol(tk.Frame):
    def __init__(self, frame):
        super().__init__(frame, bg=frame.cget('bg'))
        self.buttons()
        self.buttons_disable()

    def buttons_enable(self):
        self.up.config(state=tk.ACTIVE)
        self.down.config(state=tk.ACTIVE)
        self.left.config(state=tk.ACTIVE)
        self.rigth.config(state=tk.ACTIVE)
        self.zoom_up.config(state=tk.ACTIVE)
        self.zoom_down.config(state=tk.ACTIVE)

    def buttons_disable(self):
        self.up.config(state=tk.DISABLED)
        self.down.config(state=tk.DISABLED)
        self.left.config(state=tk.DISABLED)
        self.rigth.config(state=tk.DISABLED)
        self.zoom_up.config(state=tk.DISABLED)
        self.zoom_down.config(state=tk.DISABLED)
    
    def buttons(self):
        self.buttom_top = tk.Frame(self, bg=self.cget('bg'), pady=1)
        self.buttom_top.pack()
        self.up = tk.Button(self.buttom_top, text='up', bg=self.cget('bg'), fg=Colors.CINZA_CLARO.value)
        self.up.pack()

        self.buttons_mid = tk.Frame(self, bg=self.cget('bg'), pady=1)
        self.buttons_mid.pack()
        

        buttons_left = tk.Frame(self.buttons_mid, bg=self.cget('bg'), padx=2)
        buttons_left.pack(side='right')
        self.left = tk.Button(buttons_left, text='left', bg=self.cget('bg'), fg=Colors.CINZA_CLARO.value)
        self.left.pack()

        buttons_right = tk.Frame(self.buttons_mid, bg=self.cget('bg'), padx=2)
        buttons_right.pack(side='left')
        self.rigth = tk.Button(buttons_right, text='right', bg=self.cget('bg'), fg=Colors.CINZA_CLARO.value)
        self.rigth.pack()

        self.buttom_down = tk.Frame(self, bg=self.cget('bg'), pady=2)
        self.buttom_down.pack()
        self.down = tk.Button(self.buttom_down, text='down', bg=self.cget('bg'), fg=Colors.CINZA_CLARO.value)
        self.down.pack()

        self.buttom_zoom = tk.Frame(self, bg=self.cget('bg'), pady=2)
        self.buttom_zoom.pack()
        buttons_left = tk.Frame(self.buttom_zoom, bg=self.cget('bg'), padx=2)
        buttons_left.pack(side='right')
        buttons_right = tk.Frame(self.buttom_zoom, bg=self.cget('bg'), padx=2)
        buttons_right.pack(side='left')

        self.zoom_down = tk.Button(buttons_left, text='Zoom -', bg=self.cget('bg'), fg=Colors.CINZA_CLARO.value)
        self.zoom_down.pack()

        self.zoom_up = tk.Button(buttons_right, text='Zoom +', bg=self.cget('bg'), fg=Colors.CINZA_CLARO.value)
        self.zoom_up.pack()

        self.buttom_exit = tk.Frame(self, bg=self.cget('bg'), pady=2)
        self.buttom_exit.pack()
        quit_button = tk.Button(self.buttom_exit, text='Sair', bg=self.cget('bg'), fg=Colors.CINZA_CLARO.value, command=quit)
        quit_button.pack()
