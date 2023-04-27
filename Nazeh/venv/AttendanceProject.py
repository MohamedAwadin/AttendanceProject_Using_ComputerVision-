import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import Model_one as Model
# from PIL import ImageGrab

def markAttendance(name):
    with open('venv/Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString},Done')


path = 'ImagesAttendance'
#encodeListKnown = Model.LoadDatabase(path)
Model.LoadDatabase(path)

#encodeListKnown = Model.findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    S = Model.Recognize(cap)
    markAttendance(S)
    
    
