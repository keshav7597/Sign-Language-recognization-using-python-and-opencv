#     SIGN LANGUAGE RECOGNIZATION USING PYTHON AND OPENCV ( MACHINE LEARNING )
#     GROUP 2     ( BARDEEN )
#     ADVANCED ELECTRONICS LAB 2
#  -----------------------------------------------------------------------

from locale import LC_MONETARY
import cv2          # IMPORT OPENCV
import mediapipe as mp      # IMPORTING MEDIAPIPE LIBRARY
from playsound import playsound
import os  # IMPORTING OPERATING SYSTEM

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips = [8 ,12 ,16, 20]
thumb_tip =4

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    results = hands.process(img)
    
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            lm_list=[]
            for id,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)
            finger_fold_status=[]   
            for tip in finger_tips:
                x, y= int(lm_list[tip].x *w),int(lm_list[tip].y *h)
                #print(id,":", x, y)
                cv2.circle(img,(x,y),15,(255, 0, 0), cv2.FILLED)
                
                if lm_list[tip].x < lm_list[tip -3].x:
                    cv2.circle(img,(x,y),15,(0, 255, 0), cv2.FILLED)
                    finger_fold_status.append(True)
                else:
                    finger_fold_status.append(False)
                    
            #print(finger_fold_status)
            
            if all(finger_fold_status):    
                
    #   LIKE    
                
                if lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y \
                    and lm_list[4].y < lm_list[6].y and \
                    lm_list[5].y <lm_list[9].y <lm_list[13].y <lm_list[17].y :
                   # print("LIKE")
                    cv2.putText(img,  "LIKE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                
                
    #   DISLIKE
                
                if lm_list[thumb_tip].y > lm_list[thumb_tip - 1].y > lm_list[thumb_tip - 2].y \
                        and lm_list[4].y > lm_list[6].y and lm_list[17].y <lm_list[5].y :
                    cv2.putText(img, "DISLIKE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    #print("DISLIKE")
                    
                    
    #   SORRY
                if lm_list[3].y < lm_list[4].y and \
                    lm_list[5].y <lm_list[9].y <lm_list[13].y <lm_list[17].y :
                    cv2.putText(img, "Sorry", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                    #print("Sorry")
                
                    
    #   HELLO
                
                if lm_list[4].y<lm_list[2].y and lm_list[8].y<lm_list[6].y and lm_list[12].y<lm_list[10].y and \
                    lm_list[16].y<lm_list[14].y and lm_list[20].y<lm_list[18].y \
                    and lm_list[4].x>lm_list[8].x> lm_list[12].x> lm_list[16].x > lm_list[20].x:
                    cv2.putText(img, "HELLO", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                    #playsound
                    
    #   THANKYOU
                
                if lm_list[20].y>lm_list[16].y> lm_list[12].y> lm_list[8].y and lm_list[4].y<lm_list[2].y\
                    and lm_list[4].x< lm_list[20].x\
                    and lm_list[12].x>lm_list[10].x and lm_list[8].x> lm_list[6].x and lm_list[14].x<lm_list[16].x\
                    and lm_list[20].x>lm_list[18].x:
                    cv2.putText(img, "THANKYOU", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
        
    #   DOWN
                
                if lm_list[3].x > lm_list[4].x and lm_list[3].y < lm_list[4].y and lm_list[6].y < lm_list[8].y and \
                    lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y:
                    #and lm_list[17].x> lm_list[13].x> lm_list[9].x > lm_list[5].x:
                    cv2.putText(img, "DOWN", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)   
                    
                    
    #   VICTORY
                
                if lm_list[3].x > lm_list[4].x and lm_list[8].y<lm_list[6].y and lm_list[12].y<lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y>lm_list[18].y \
                    and lm_list[8].x> lm_list[12].x:
                    cv2.putText(img, "VICTORY", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3) 
                
                
    #   FANTASTIC
                
                if lm_list[3].x > lm_list[4].x and lm_list[8].y<lm_list[6].y and lm_list[12].y>lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y<lm_list[18].y:
                    cv2.putText(img, "FANTASTIC ", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            
    #   ROCK
                
                if lm_list[3].x < lm_list[4].x and lm_list[8].y<lm_list[6].y and lm_list[12].y>lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y<lm_list[18].y:
                    cv2.putText(img, "ROCK", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0,  0), 3)
            
        
    #   I AM FINE
                
                if lm_list[12].x > lm_list[16].x > lm_list[20].x and lm_list[8].y< lm_list[4].y \
                    and lm_list[12].y<lm_list[10].y and lm_list[16].y< lm_list[14].y\
                    and lm_list[20].y< lm_list[18].y and lm_list[6].y< lm_list[8].y \
                    and lm_list[4].y< lm_list[2].y:
                    cv2.putText(img, "I AM FINE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                    #playsound('C:/Users/lenovo/Downloads/Sound/IAMFINE.mp4')
                
    #   TAKE A CHILL
                
                if lm_list[8].y>lm_list[6].y and lm_list[12].y>lm_list[10].y and lm_list[4].y<lm_list[2].y \
                    and lm_list[4].x>lm_list[20].x and lm_list[16].y>lm_list[14].y and lm_list[20].y<lm_list[18].y:
                    cv2.putText(img, "TAKE A CHILL", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            
    #   HOW
                
                if lm_list[2].x > lm_list[4].x and lm_list[8].y < lm_list[5].y and lm_list[12].y > lm_list[10].y and \
                        lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y\
                        and lm_list[4].x<lm_list[5].x<lm_list[9].x<lm_list[17].x:
                        cv2.putText(img, "HOW ARE YOU", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            
    #   UP
                
                if lm_list[0].x < lm_list[4].x and lm_list[8].y < lm_list[5].y and lm_list[12].y > lm_list[10].y and \
                        lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y and lm_list[4].x> lm_list[2].x:
                    cv2.putText(img, "UP", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                
    #   RIGHT
                
                if lm_list[4].x > lm_list[0].x and lm_list[8].y > lm_list[5].y and lm_list[12].y > lm_list[9].y and \
                        lm_list[16].y > lm_list[13].y and lm_list[20].y > lm_list[17].y\
                        and lm_list[6].y<lm_list[4].y and lm_list[5].x>lm_list[13].x>lm_list[17].x:
                        cv2.putText(img, "TAKE RIGHT", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
                
    #   LEFT
                
                if lm_list[4].x < lm_list[0].x and lm_list[8].y > lm_list[5].y and lm_list[12].y > lm_list[9].y and \
                        lm_list[16].y > lm_list[13].y and lm_list[20].y > lm_list[17].y:
                        cv2.putText(img, "TAKE LEFT", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
                
    #   STAY AWAY
                
                if lm_list[4].y > lm_list[8].y > lm_list[12].y> lm_list[16].y>lm_list[20].y \
                    and lm_list[4].x > lm_list[20].x:
                    cv2.putText(img, "STAY AWAY", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    
            
            mp_draw.draw_landmarks(img,hand_landmark,
                                    mp_hands.HAND_CONNECTIONS,
                                    mp_draw.DrawingSpec((0,0,255),2,2),
                                    mp_draw.DrawingSpec((0,255,0),4,2)
                                  )
                                  
    cv2.imshow("Hand Tracking",img)
    cv2.waitKey(1)
    
                                                      