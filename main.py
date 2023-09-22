from app.checkNumInArea import checkNum
from app.controlKeyboard import keyboardWrite, keyboardPressSpace
from app.controlMouse import moveAndClick, moveMouse, leftClick, getMousePosition
from app.getScreenArea import getScreenArea

from utils.log import TextLog
import easyocr

import yaml
import time
import logging

def getConfig(path:str='config.yaml'):
    try:
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
        
        return data
    except FileNotFoundError:
        logging.exception("Khong tim thay file config.yaml")
    except:
        logging.error("Loi khac")
        

def main():
    inputData = getConfig()
    reader = easyocr.Reader(['en'])
    textlog = TextLog()
    
    
    # 1. Nhap so luong X muon giu
    # -> Nhap o file config.yaml, phan "NumToGet"
    
    num = 0
    
    while num == 0:    
    
        # 2. Di chuot den vi tri (x0,y0) va click chuot trai
        moveAndClick(inputData["FirstClickXY"])
        time.sleep(0.5)
        
        # 3. Check so man hinh
        # 3.1. Lay 1 phan man hinh
        screenArea = getScreenArea(area=inputData["ScreenPart"])
        time.sleep(0.5)
        # 3.2. Check so trong phan man hinh do, chi cho phep so '0123456789'
        bbox, text, score = checkNum(reader=reader, img=screenArea)
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    


if __name__ == '__main__':
    getConfig()
    
    