import tkinter as tk
from PIL import ImageTk
import threading


class DevicesGrid(tk.Frame):
    def __init__(self, frame: object, devices: list):
        super().__init__(frame, bg=frame.cget('bg'))
        self.devices = devices


    def __create_grid(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)

    def update_devices(self):
        self.__create_grid()

        frame_width = 200 if len(self.devices) > 1 else 600
        frame_height = 200 if len(self.devices) > 1 else 600

        for idx, device in enumerate(self.devices):
            button = tk.Button(self.grid_frame, bg=self.cget('bg'),
                                     fg="white", command=lambda d=device: self.device_maximize(d))
            button.pack()

        def update_frame():
            try:
                if device.videpcapture is None or not device.videpcapture.isOpened():
                    return

                while True:
                    device.update_frame(frame_width, frame_height)

                    if device.resized_frame is not None:
                        imgtk = ImageTk.PhotoImage(image=device.resized_frame)
                        button.imgtk = imgtk
                        button.configure(image=imgtk)

                    button.after(10, update_frame)  # Atualiza o frame no botão
                    break

            except Exception as e:
                print(f"Error updating frame for device {device.name}: {e}")

        update_frame()
           


        

    def device_maximize(self, device: object):
        pass

