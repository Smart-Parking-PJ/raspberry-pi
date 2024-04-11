import time
import requests
from picamera import PiCamera
import os

camera = PiCamera()

api_endpoint = "https://00c7-223-194-160-130.ngrok-free.app/photo/1"


def take_and_send_photo():
    file_name = f"photo_{int(time.time())}.jpg"
    camera.capture(file_name)

    try:
        with open(file_name, "rb") as photo_file:
            files = {"file": (file_name, photo_file)}
            response = requests.post(api_endpoint, files=files)
            if response.status_code == 200:
                print("사진 전송 성공!")
            else:
                print(f"사진 전송 실패. 응답 코드: {response.status_code}")
    except Exception as e:
        print(f"에러 발생: {e}")
    finally:
        os.remove(file_name)


while True:
    print("Code Running...")
    take_and_send_photo()
    time.sleep(3)
