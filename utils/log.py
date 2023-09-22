import os
import logging

from datetime import datetime

class TextLog:
    def __init__(self) -> None:
        logging.info("Create log file")
        
        # Create folder if not existed
        self.logFolderPath = 'log'
        os.makedirs('log', exist_ok=True)
        self.logFile = open(self.createLogFile(), 'a')
    
    def createLogFile(self):
        now = datetime.now()
        date_time = now.strftime
        return os.path.join(self.logFolderPath, str(datetime.now()))
    
    def appendToLogFile(self, line):
        self.logFile.write(line)
    
    def close(self):
        self.logFile.close()


if __name__ == "__main__":
    textlog = TextLog()
    bbox = [[0], [1], [2], [3]]
    text = '12'
    score = 0.123214
    
    r = (bbox, text, score)
    textlog.appendToLogFile(r)
    textlog.close()