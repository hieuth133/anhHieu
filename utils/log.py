import os
import logging
import csv

from datetime import datetime

class TextLog:
    def __init__(self) -> None:
        logging.info("Create log file")
        
        # Create folder if not existed
        self.logFolderPath = 'log'
        os.makedirs('log', exist_ok=True)
        self.logFile = open(self.createLogFile(), 'w')
        self.writer = csv.writer(self.logFile)
    
    def createLogFile(self):
        now = datetime.now()
        date_time = now.strftime("%d%m%Y - %H%M%S")
        return os.path.join(self.logFolderPath, date_time + '.csv')
    
    def appendToLogFile(self, line):
        self.writer.writerow(line)
    
    def close(self):
        self.logFile.close()


