import requests
import telegram_send
import imgkit

IP="140.123.5.6"

def getImage():
    imgkit.from_url('https://netflow.dorm.ccu.edu.tw/flows/' + IP, 'out.jpg')                                                                                                                                                             .jpg')
    with open("out.jpg", "rb") as f:
        telegram_send.send(images=[f])

if __name__ == "__main__":
    getImage()
