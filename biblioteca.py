import pyautogui, time

# Abrir site
pyautogui.press("win")
pyautogui.write("Google")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://www.sp.senai.br/unidade/jundiai/")
pyautogui.press('enter')        
time.sleep(2)

cursos = pyautogui.locateOnScreen('cursos.png')
posi_cursos = pyautogui.center(cursos)
pyautogui.cick(posi_cursos.x, posi_cursos.y)
