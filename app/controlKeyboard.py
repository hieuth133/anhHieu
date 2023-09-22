import pyautogui

def keyboardWrite(num:str):
    '''
    num must be string
    '''
    pyautogui.typewrite(message=num)
    return

def keyboardPress(key):
    pyautogui.press(key)
    
def keyboardPressSpace():
    keyboardPress("space")
    