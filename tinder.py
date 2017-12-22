import pyautogui
import time
# x = pyautogui.position()
x = (930, 597)

for i in range(100):
	time.sleep(0.2)
	pyautogui.click(x)
