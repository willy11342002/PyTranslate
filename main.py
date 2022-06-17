from hotkey import Hotkey
from tray import SysTray
import pyautogui
pyautogui.FAILSAFE = False


class App(object):
    def __init__(self) -> None:
        self.state = True
        self.dic_hotkey = {
            'win + alt': pyautogui.middleClick
        }
        self.tray = SysTray(
            title='中鍵快速鍵小工具',
            state=self.state,
            activate=self.activate,
            deactivate=self.deactivate
        )

    def activate(self):
        '''開始監聽程式'''
        self.hotkey = Hotkey(self.dic_hotkey)
        self.hotkey.start()

    def deactivate(self):
        '''暫停監聽程式'''
        self.hotkey.stop()

    def run(self):
        '''主要進入點'''
        self.tray.run()


if __name__ == '__main__':
    app = App()
    app.run()
