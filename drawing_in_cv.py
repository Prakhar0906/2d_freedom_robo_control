import cv2 as cv
import numpy as np
import math
import serial


L1 = 200
L2 = 200
#ser = serial.Serial('COM9',9600)

def inv_kin(a1,a2,end_x,end_y):
    q2_val = (pow(a1,2)+pow(a2,2)-pow(end_x,2)-pow(end_y,2))/(2*a1*a2)
    #print("The q1 val is:",q2_val)
    q2 = math.pi - math.acos(q2_val)
    q1 = math.atan(end_y/end_x)+math.atan((a2*math.sin(q2))/(a1+a2*math.cos(q2)))
    return (q1,q2)    

def print_coords(event,x,y,falgs,params):
    if event == cv.EVENT_LBUTTONDOWN:
        img.fill(255)
        cv.circle(img,(0,500),400,(0,0,255),3)
        print(x,",",y)
        angles = inv_kin(L1,L2,x,(500-y))
        end_1_y = int(L1*math.sin(angles[0]))
        end_1_x = int(L1*math.cos(angles[0]))
        #print(int(math.sqrt(pow(end_1_x,2)+pow(end_1_y,2))))        
        cv.line(img,(0,500),(end_1_x,500-end_1_y),(0,0,0),2)
        cv.line(img,(end_1_x,500-end_1_y),(x,y),(0,0,0),2)
        data_1 = str(int(math.degrees(angles[1])))+'\n'
        data_2 = str(int(math.degrees(angles[0])))+'\n'
        print(data_1)
        print(data_2)
        #ser.write(bytes(data_1,'utf-8'))
        #print(ser.readline())
        #ser.write(bytes(data_2,'utf-8'))
        #print(ser.readline())

        
        

img = np.zeros((500,500,3),np.uint8)
img.fill(255)
cv.circle(img,(0,500),400,(0,0,255),3)


cv.namedWindow('image')
cv.setMouseCallback('image',print_coords)

while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break

ser.close()
cv.destroyAllWindows()
