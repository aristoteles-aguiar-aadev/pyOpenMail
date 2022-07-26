
import py
import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1
#abrir navegar 

pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
#pyautogui.alert(" Gmail ")
pyautogui.hotkey("ctrl", "t")

#acessar o email Gmail/

link = "mail.google.com/mail/u/0/"

pyperclip.copy(link)
pyautogui.hotkey("Ctrl", "v")
pyautogui.press("enter")
time.sleep(1)

#credenciais
#pyautogui.click(838, 368)

time.sleep(10)
pyautogui.press("F5")










