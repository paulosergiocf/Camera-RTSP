import cv2
from PIL import Image

class Device:
    def __init__(self: object, name: str, ip:str , port: int, user: str, password: str):
        self.name = name
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password

        self.string_connection = None
        self.resized_frame = None
        self.videpcapture = None
        self.validate_str_connection()

        

    def validate_str_connection(self):
        """
        Valida possibilidade de conexão

        Raises:
            Exception: Erro lançado ao não conseguir abrir o video.
        """
        self.string_connection = f'rtsp://{self.ip}:{self.port}/user={self.user}&password={self.password}&channel=1&stream=0'
        self.videpcapture = cv2.VideoCapture(self.string_connection)

        if not self.videpcapture.isOpened():
            raise Exception(f"Error, is not possible connect in device {self.name}")

    def update_frame(self, frame_width: int, frame_height: int):
        if not self.videpcapture:
            self.videpcapture = cv2.VideoCapture(self.string_connection)

        ret, frame =self.videpcapture.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)

            self.resized_frame = frame.resize((frame_width, frame_height), Image.LANCZOS)

  


        
        