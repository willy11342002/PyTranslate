import sys
from PIL import Image
import pyautogui
import threading
import pystray


class SysTray(object):

    def on_clicked(self, icon, item):
        self.state = not item.checked
        if self.state:
            self.activate()
        else:
            self.deactivate()

    def __init__(self, title, activate=None, deactivate=None, state:bool=True):
        self.state = state
        self.activate = activate or threading.Thread(target=pyautogui.alert, args=('activate.',)).start
        self.deactivate = deactivate or threading.Thread(target=pyautogui.alert, args=('deactivate.',)).start
        self.icon = pystray.Icon(title,
            icon=Image.open('icon.png'),
            menu=pystray.Menu(
                pystray.MenuItem(
                    '啟用',
                    self.on_clicked,
                    checked=lambda item: self.state
                ),
                pystray.MenuItem(
                    '關閉',
                    self.stop,
                ),
            )
        )

    def run(self):
        if self.state:
            self.activate()
        self.icon.run()

    def stop(self):
        self.deactivate()
        self.icon.stop()


if __name__ == '__main__':
    SysTray('測試').run()
