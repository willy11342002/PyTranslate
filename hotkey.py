import threading
import keyboard
import time


class Hotkey(threading.Thread):
    def __init__(self, hotkeys={}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.running = True
        self.hotkeys = hotkeys

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            for keys, func in self.hotkeys.items():
                if keyboard.is_pressed(keys):
                    func()
            time.sleep(.05)
