import pytest
from unittest.mock import patch, MagicMock
from src.entities.device import Device  
from PIL import Image
import cv2
# Testando o método validate_str_connection
@patch('cv2.VideoCapture')
def test_validate_str_connection(mock_videocapture):
    # Configurando o mock para retornar um VideoCapture "aberto"
    mock_videocapture_instance = MagicMock()
    mock_videocapture.return_value = mock_videocapture_instance
    mock_videocapture_instance.isOpened.return_value = True

    # Criando uma instância de Device
    device = Device(name="Camera1", ip="192.168.1.100", port=554, user="admin", password="admin123")

    # Verificando se a string de conexão foi montada corretamente
    expected_str = 'rtsp://192.168.1.100:554/user=admin&password=admin123&channel=1&stream=0'
    assert device.string_connection == expected_str

    # Verificando se o VideoCapture foi aberto corretamente
    mock_videocapture.assert_called_once_with(expected_str)
    mock_videocapture_instance.isOpened.assert_called_once()

# Testando exceção no método validate_str_connection
@patch('cv2.VideoCapture')
def test_validate_str_connection_failure(mock_videocapture):
    # Configurando o mock para retornar um VideoCapture "não aberto"
    mock_videocapture_instance = MagicMock()
    mock_videocapture.return_value = mock_videocapture_instance
    mock_videocapture_instance.isOpened.return_value = False

    # Testando se a exceção é lançada corretamente
    with pytest.raises(Exception, match="Error, is not possible connect in device Camera1"):
        Device(name="Camera1", ip="192.168.1.100", port=554, user="admin", password="admin123")

# Testando o método update_frame
@patch('cv2.VideoCapture')
@patch('cv2.cvtColor')
@patch('PIL.Image.fromarray')
def test_update_frame(mock_fromarray, mock_cvtcolor, mock_videocapture):
    # Configurando o mock para o VideoCapture
    mock_videocapture_instance = MagicMock()
    mock_videocapture.return_value = mock_videocapture_instance
    mock_videocapture_instance.read.return_value = (True, "frame_data")

    # Criando mocks para os outros métodos
    mock_cvtcolor.return_value = "converted_frame"
    mock_image_instance = MagicMock()
    mock_fromarray.return_value = mock_image_instance

    # Criando uma instância de Device
    device = Device(name="Camera1", ip="192.168.1.100", port=554, user="admin", password="admin123")

    # Chamando o método update_frame
    device.update_frame(frame_width=640, frame_height=480)

    # Verificando se o frame foi atualizado corretamente
    mock_videocapture_instance.read.assert_called_once()
    mock_cvtcolor.assert_called_once_with("frame_data", cv2.COLOR_BGR2RGB)
    mock_fromarray.assert_called_once_with("converted_frame")
    mock_image_instance.resize.assert_called_once_with((640, 480), Image.LANCZOS)
    assert device.resized_frame == mock_image_instance.resize.return_value
