import tkinter as tk
from .personalization import Colors
from .labels import Labels
import os

from src.entities.device import Device
from src.ui.grid_devices import DevicesGrid
from src.ui.layout_interface import Interface, Title
from src.ui.ptz_controls import PtzConstrol
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
        # device2 = Device(name="garagem",ip=os.environ['IP'],port=os.environ['PORT'],user=os.environ['USERDEVICE'], password=os.environ['PASSWORDDEVICE'])
        # device3 = Device(name="garagem",ip=os.environ['IP'],port=os.environ['PORT'],user=os.environ['USERDEVICE'], password=os.environ['PASSWORDDEVICE'])

        # devices_mock.append(device1)
        # devices_mock.append(device2)
        devices_mock.append(device1)

        self.interface = Title(self)
        self.interface.pack()

        self.interface = Interface(self)
        self.interface.pack(fill="both", expand=True)

        self.controls = PtzConstrol(self.interface.left)
        self.controls.pack()

        self.grid = DevicesGrid(self.interface.right, devices=devices_mock)
        self.grid.pack()

        self.grid.update_devices()

       