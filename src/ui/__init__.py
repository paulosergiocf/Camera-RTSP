import tkinter as tk
import tkinter.font as font
from .personalization import Colors, Fonts
from .labels import Labels
from PIL import ImageTk
import os
from src.entities.device import Device

from dotenv import load_dotenv
load_dotenv()


class App(tk.Tk):   
    def __init__(self, ):
        super().__init__()
        self.__config()
        self.inicio()
        self.selected_device = None
    
    def __config(self):
        """
        Descrição
            Configurações da interface.
        """ 
        self.geometry("1024x768")
        self.title(f"Gerenciador de Cameras RTSP - {Labels.VERSION.value}")
        self.configure(bg=Colors.CINZA_ESCURO_AZULADO.value, padx=5, pady=5)
    

    def inicio(self):
        """
        Descrição:
            Tela inicial da aplicação.
        """

        # mock
        devices_mock = list()
        device1 = Device(name="garagem",ip=os.environ['IP'],port=os.environ['PORT'],user=os.environ['USERDEVICE'], password=os.environ['PASSWORDDEVICE'])
        device2 = Device(name="garagem",ip=os.environ['IP'],port=os.environ['PORT'],user=os.environ['USERDEVICE'], password=os.environ['PASSWORDDEVICE'])
        devices_mock.append(device1)
        devices_mock.append(device2)

        self.interface = Title(self)
        self.interface.pack()

        self.interface = Interface(self)
        self.interface.pack(fill="both", expand=True)

        self.controls = PtzConstrol(self.interface.left)
        self.controls.pack()

        self.grid = DevicesGrid(self.interface.right, devices=devices_mock)
        self.grid.pack()

        self.grid.update_devices()

                
class Interface(tk.Frame):
    def __init__(self, frame):
        super().__init__(frame, bg=frame.cget('bg'))
 
        self.left = tk.Frame(self, bg=self.cget('bg'))
        self.left.place(relx=0.0, rely=0.15, relwidth=0.3, relheight=0.7)

        self.right = tk.Frame(self, bg=self.cget('bg'), border=2)
        self.right.place(relx=0.3, rely=0.15, relwidth=0.7, relheight=0.7)

class Title(tk.Frame):
    def __init__(self, frame):
        super().__init__(frame, bg=frame.cget('bg'))

        title = tk.Label(self, font=font.Font(family=Fonts.FONT_ROBOTO.value, size=14), text=F'{Labels.TITLE.value}', bg=frame.cget('bg'), fg=Colors.CINZA_CLARO.value)
        title.pack()

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

class DevicesGrid(tk.Frame):
    def __init__(self, frame: object, devices: list):
        super().__init__(frame, bg=frame.cget('bg'))
        self.devices = devices

    def __create_grid(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.grid = tk.Frame(self)
        self.grid.pack()

    def update_devices(self):
        self.__create_grid()

        frame_width = 200 if len(self.devices) > 1 else 600
        frame_height = 200 if len(self.devices) > 1 else 600

        for device in self.devices:
            video_button = tk.Button(self.grid, bg=self.cget('bg'), fg=Colors.CINZA_CLARO.value, 
                                     command=lambda d=device: self.device_maximize(d))
            video_button.pack()

            def update_frame(device=device, button=video_button):
                device.update_frame(frame_width, frame_height)

                if device.resized_frame is not None:
                    imgtk = ImageTk.PhotoImage(image=device.resized_frame)
                    
                    button.imgtk = imgtk
                    button.configure(image=imgtk)
                
                button.after(100, update_frame)

            update_frame()

    def device_maximize(self, device: Device):
        pass

