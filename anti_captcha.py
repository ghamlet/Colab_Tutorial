import cv2
import numpy as np
import pyautogui
import time


def find_captcha():
    find = True

    while True:
        
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
        gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY) 

        _, threshold = cv2.threshold(gray, 20, 260, cv2.THRESH_BINARY) 
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
        
        for contour in contours: 
            area = cv2.contourArea(contour)

            if  22000 < area < 24000 and find:
                x,y,w,h = cv2.boundingRect(contour)
                if w < 1500:

                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.imwrite("ver.jpg", frame)
                    
                    pyautogui.moveTo(x+25, y+33,3)
                    pyautogui.click()
        
                    find = False
                    time.sleep(5)
                
            else: find = True
                
         
if __name__ == "__main__":
    find_captcha()