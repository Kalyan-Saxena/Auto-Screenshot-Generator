import pyscreenshot as ImageGrab
import schedule
import time
import os

def take_screenshot():
    print("Taking screenshot now........")
    imageName = f'screenshot-{str(round(time.time()))}.png'
    filePath = os.path.join(os.getcwd(), 'Screenshots', imageName)
    if not os.path.exists(os.path.join(os.getcwd(), 'Screenshots')):
        os.mkdir('Screenshots')
    screenshot = ImageGrab.grab()
    screenshot.save(filePath)
    print("Screenshot taken")

def main():
    schedule.every().minute.do(take_screenshot)

    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__ == "__main__":
    main()