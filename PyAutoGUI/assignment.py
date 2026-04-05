import pyautogui
import time
import os

time.sleep(3)

# 1. Open Chrome
os.system("open -a 'Google Chrome'")
time.sleep(3)

# 2. FORCE focus Chrome (VERY IMPORTANT)
pyautogui.click(100, 100)
time.sleep(1)

# 3. Open NEW window
pyautogui.hotkey('command', 'n')
time.sleep(2)

# 4. Open YouTube
pyautogui.hotkey('command', 'l')
time.sleep(1)

pyautogui.write('https://www.youtube.com', interval=0.05)
pyautogui.press('enter')
time.sleep(6)

# 5. Search
pyautogui.press('/')
time.sleep(1)

pyautogui.write('Danku rituku rituku dum dum', interval=0.05)
pyautogui.press('enter')

time.sleep(1)
x,y = pyautogui.position() 
print(f"Current mouse position: ({x}, {y})")

pyautogui.click(376, 432)  # click first video (adjust as needed)

