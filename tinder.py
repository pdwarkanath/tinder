import pyautogui
# x = pyautogui.position()
x = (930, 597)
import time
try:
	while True:
		time.sleep(0.2)
		pyautogui.click(x)
except KeyboardInterrupt:
	pass