import pyautogui, time
time.sleep(3)
while True:
    pyautogui.hotkey("fn","f5")
    time.sleep(3)
    pyautogui.moveTo(200,350)
    pyautogui.click()
    time.sleep(10)