import pyautogui

def moveMouse(x,y):
    pyautogui.moveTo(x=x,
                     y=y
                     )
    return


def leftClick():
    pyautogui.click(button='LEFT')
    return

def getMousePosition():
    print(pyautogui.displayMousePosition())


def moveAndClick(x,y):
    pyautogui.click(x=x,
                    y=y,
                    button='LEFT')
    
    