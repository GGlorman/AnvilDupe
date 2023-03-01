import pyautogui
from pynput import keyboard
from time import sleep as s

print("Program is running!")

COMBINATIONS = [
    {keyboard.KeyCode(char=']')}
]

current = set()


def execute():
    print("Bot is on!")
    # Add space
    pyautogui.moveTo(748, 432)
    s(0.002)
    pyautogui.click()
    s(0.002)
    pyautogui.press("space")
    s(0.002)
    pyautogui.moveTo(1178, 432)
    s(0.002)
    pyautogui.click()
    s(0.002)
    # Delete space
    pyautogui.moveTo(748, 432)
    s(0.002)
    pyautogui.click()
    s(0.002)
    pyautogui.press("backspace")
    s(0.002)
    pyautogui.moveTo(1178, 432)
    s(0.002)
    pyautogui.click()
    s(0.002)


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO)for COMBO in COMBINATIONS):
            execute()


def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
