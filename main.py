import keyboard
import win32api
import win32con


def clickLeftCur():
    win32api.mouse_event( win32con.MOUSEEVENTF_MIDDLEDOWN|win32con.MOUSEEVENTF_MIDDLEUP, 0, 0)


def main():
    keyboard.add_hotkey('windows + alt', clickLeftCur)
    keyboard.wait()


if __name__ == '__main__':
    main()
