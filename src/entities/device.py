import cv2
import os
from PIL import Image, ImageTk

from dotenv import load_dotenv
load_dotenv()
class Device:
    def __init__(self: object, name: str, ip:str , port: int, user: str, password: str):
        self.name = name
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password

        self.string_connection = None

        self.videpcapture = None
        self.validate_str_connection()
        self.frame = None
        self.ret = None
        self.resized_frame = None

    def validate_str_connection(self):

        self.string_connection = f'rtsp://{self.ip}:{self.port}/user={self.user}&password={self.password}&channel=1&stream=0'
        self.videpcapture = cv2.VideoCapture(self.string_connection)

        if not self.videpcapture.isOpened():
            raise Exception(f"Error, is not possible connect in device {self.name}")

    def update_frame(self, frame_width: int, frame_height: int):
        if not self.videpcapture:
            self.videpcapture = cv2.VideoCapture(self.string_connection)

        self.ret, self.frame =self.videpcapture.read()

        if self.ret:
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            self.frame = Image.fromarray(self.frame)

            self.resized_frame = self.frame.resize((frame_width, frame_height), Image.LANCZOS)

  


        
        