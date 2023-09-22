from app.checkNumInArea import checkNum
from app.controlKeyboard import keyboardWrite, keyboardPressSpace
from app.controlMouse import moveAndClick, moveMouse, leftClick, getMousePosition
from app.getScreenArea import getScreenArea

from utils.log import TextLog
import easyocr

import yaml
import time
from datetime import datetime
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
        # 3.2. Check so trong phan man hinh do, chi cho phep so '0-9'
        bbox, text, score = checkNum(reader=reader, img=screenArea)
        
        now = datetime.now()
        date_time = now.strftime("%d%m%Y - %H%M%S")
        # save to log file
        textlog.appendToLogFile((bbox, text, score, date_time))
        time.sleep(0.5)
        
        try:
            num = int(text)
        except:
            logging.warning('ocr cannot detect text or wrong format')
            continue
        
        if num == 0:
            #4. Bam space
            keyboardPressSpace()
        else:
            num = abs(num)
            break
        
    
    # 5. Di chuot den vi tri x1,y2, click chuot trai
    moveAndClick(inputData["SecondClickXY"])
    
    # 6. Nhap X
    if inputData["NumToGet"] >= num:
        keyboardWrite(num)
    else:
        keyboardWrite(inputData["NumToGet"])
        
    # 7. Bam enter hoac j do
        
        
        
        
        
        
        
    
    
    
    
    


# if __name__ == '__main__':
#     getConfig()
    

if __name__ == "__main__":
    textlog = TextLog()
    bbox = [[0], [1], [2], [3]]
    text = '12'
    score = 0.123214
    
    r = (bbox, text, score)
    textlog.appendToLogFile(r)
    textlog.close()

    
    
    