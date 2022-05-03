from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key
from itertools import groupby
from pathlib import Path
import tkinter as tk
import googletrans
import traceback
import pyperclip
import threading
import time


config = dict(
    line.split('=', 1)
    for line in Path('.env').read_text().split('\n')
    if line
)


class MouseTracker(threading.Thread):
    """設定物件永遠跟隨滑鼠位置"""
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mouse = MouseController()
        self.root = root
        self.flag = True

    def move_to_mouse(self):
        try:
            # 計算當前視窗位置
            x, y = self.mouse.position
            x -= self.root.winfo_screenwidth()
            x += self.root.winfo_width()
            x += 30
            # 視窗定位
            position = f'{"+" if x >= 0 else ""}{x}{"+" if y >= 0 else ""}{y}'
            self.root.geometry(position)
            return True
        except:
            return False

    def run(self):
        while self.flag:
            self.flag = self.move_to_mouse()
            time.sleep(.05)


class Translator(tk.Toplevel):
    """翻譯機"""
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.keyboard = KeyboardController()
        self.tr = googletrans.Translator()
        # 永遠顯示於最頂層
        self.attributes('-topmost',True)
        # 去除標頭
        self.wm_overrideredirect(True)
        # 添加文字顯示框
        self.text = tk.Label(self)
        self.text.pack(padx=5, pady=3)
        # 跟隨滑鼠
        MouseTracker(self).start()
        # 綁定翻譯功能
        KeyboardListener(on_press=self.on_press).start()

    def on_press(self, key):
        """定義各快速鍵功能"""
        # F8 綁定為翻譯功能
        if key == Key.f8:
            self.trans()
        # F9 顯示/隱藏畫面
        elif key == Key.f9:
            self.switch_status()
        # F10 完全關閉程式
        elif key == Key.f10:
            self.quit()

    def switch_status(self):
        """切換畫面顯示/隱藏"""
        if self.winfo_viewable():
            self.withdraw()
        else:
            self.deiconify()

    def trans(self):
        """翻譯反白的文字顯示於畫面上"""
        try:
            # 複製當前反白的文字
            time.sleep(0.2)
            with self.keyboard.pressed(Key.ctrl):
                self.keyboard.press('c')
            time.sleep(0.2)
            # 將複製的文字進行翻譯
            origin_text = pyperclip.paste()
            translated_text = self.tr.translate(origin_text, dest='zh-tw')
            translated_text = groupby(enumerate(translated_text.text), key=lambda x: x[0]//30)
            translated_text = '\n'.join([
                ''.join([c[1] for c in chars]).strip()
                for k, chars in translated_text
            ])
            # 顯示於畫面上
            self.text.config(text=translated_text)
            self.deiconify()
        except Exception as e:
            e = traceback.format_exc()
            self.text.config(text=e)
            self.deiconify()


def main():
    # 設定 Tk 不顯示
    root = tk.Tk()
    root.title(f'翻譯機 V{config["VERSION"]}')
    root.withdraw()
    # 主視窗
    page = Translator(root)
    root.mainloop()


if __name__ == '__main__':
    main()
