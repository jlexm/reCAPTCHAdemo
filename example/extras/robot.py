import time
import pyautogui
print(pyautogui.size())

time.sleep(3)

namex = 837
namey = 654

emailx = 831
emaily = 747

submitx = 982
submity = 816

time.sleep(0.5)
pyautogui.click(namex, namey)
pyautogui.typewrite("alexmrvstest")

time.sleep(0.5)
pyautogui.click(emailx, emaily)
pyautogui.typewrite("lex@example.com")

time.sleep(0.5)
pyautogui.click(submitx, submity)

