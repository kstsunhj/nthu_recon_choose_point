import sys
import cv2
import numpy as np


""" # if len(sys.argv) == 1:
#     print("Empty input!")
#     sys.exit(1) """






def choose_point(image_path):
    pos = []
    def on_EVENT_LBUTTONDOWN (event, x, y, flags, param):
    
        if event == cv2.EVENT_LBUTTONDOWN:
            xy = "%d, %d" %(x, y)
            #print(xy)
            pos.append([x,y])
            cv2.circle(img, (x, y), 1, (255, 0, 0), thickness = -1)
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,0,0), thickness = 1)
            cv2.imshow( "image", img)
        if len(pos) == 7:
            # Transpose the list
            transposed_point_set = list(map(list, zip(*pos)))

            # Convert the transposed list to a string
            # point_set_str = '\n'
            point_set_str = ''
            point_set_str+=str(transposed_point_set[0]).replace('[','').replace(']','')+'\n'
            point_set_str+=str(transposed_point_set[1]).replace('[','').replace(']','')+'\n'
            with open(image_path.split('.')[-2] + '.txt','a') as file:
                file.write(point_set_str)
            cv2.destroyAllWindows()
            #sys.exit(0)
    img = cv2.imread (image_path)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    #print(img)
    cv2.imshow("image", img)
    '''
    while(True):
        try:
            cv2.waitKey(100)
        except Exception:
            cv2.destroyWindow ("image")
            break
    '''
    cv2.waitKey(0)
    cv2.destroyAllWindows()

choose_point(r'path/to/image')
