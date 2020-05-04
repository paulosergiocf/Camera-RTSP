import rtsp

with rtsp.Client(rtsp_server_uri = 'rtsp://192.168.1.10:554/user=admin&password=123456&channel=1&stream=0') as client:
    client.preview()
