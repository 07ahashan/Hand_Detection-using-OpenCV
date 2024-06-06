import cv2
import mediapipe as mp 
from google.protobuf.json_format import MessageToDict

# initializing the model
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode = False,
    model_complexity = 1,
    min_detection_confidence = 0.75,
    min_tracking_confidence = 0.75,
    max_num_hands =2)

# Start capturing video from webcam 

capture = cv2.VideoCapture(0)

while True:

    # read video frame by frame
    success, img = capture.read()

    # flip image (frame)
    img =cv2.flip(img, 1)

    # Convert BGR image to RGB image 
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the RGB image
    results = hands.process(imgRGB)

    # If hands are present in image(frame) 
    if results.multi_hand_landmarks:

        # Both Hands are present in image(frame) 
        if len(results.multi_handedness)  == 2:
             
            # Display 'Both Hands' on the image 
            cv2.putText(img, 'Both Hand Display', (250,50),cv2.FONT_HERSHEY_COMPLEX, 0.9,(0, 255, 0), 2)
        
        #if only one hand is present
        else:
           for i in results.multi_handedness:
                # Convert the proto message to a dictionary
                handedness_dict = MessageToDict(i)
    
                # Extract the label
                label = handedness_dict['classification'][0]['label']
    
                if label == 'Left':
                    # Display 'Left Hand' on the left side of the window
                    cv2.putText(img, label + ' Hand', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
                else:
                    # Display 'Right Hand' on the right side of the window (assuming this is what you want for the right hand)
                    cv2.putText(img, label + ' Hand', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 255, 0), 2)
            
    cv2.imshow('Image', img)
    if  cv2.waitKey(1) & 0xff ==ord('q'):
        break;