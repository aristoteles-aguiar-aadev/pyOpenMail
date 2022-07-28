
from copy import copy
import pyautogui
import time
import pyperclip
import numpy as np
import pandas as pd
import plotly.express as px



pyautogui.PAUSE = 1
#abrir navegar 

pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")

#acessar o email Gmail/
link_gmail = "mail.google.com/mail/u/0/"
pyperclip.copy(link_gmail)
pyautogui.hotkey("Ctrl", "v")
pyautogui.press("enter")
time.sleep(1)
#abrir nova aba
pyautogui.hotkey("ctrl", "shift", "n")
link_Ink = "https://www.linkedin.com/in/aristoteles-aguiar/"
pyperclip.copy(link_Ink)
pyautogui.hotkey("Ctrl", "v")
pyautogui.press("enter")
time.sleep(1)




#credenciais
#pyautogui.click(838, 368)

time.sleep(10)
pyautogui.press("F5")










