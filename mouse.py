import cv2
import mediapipe as mp
import pyautogui
import math

# Initialize MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Initialize video capture
cap = cv2.VideoCapture(0)

# Get screen size
screen_width, screen_height = pyautogui.size()

drag = False

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Get the position of the index finger and thumb
            x1, y1 = int(handLms.landmark[8].x * img.shape[1]), int(handLms.landmark[8].y * img.shape[0])
            x2, y2 = int(handLms.landmark[4].x * img.shape[1]), int(handLms.landmark[4].y * img.shape[0])
            # Calculate the distance between the tips of the index finger and thumb
            distance = math.hypot(x2 - x1, y2 - y1)
            # If the distance is above a certain threshold, move the mouse
            if distance > 40:
                # Map the camera resolution to the screen resolution and flip the x coordinate
                screen_x = screen_width - int(x1 * screen_width / img.shape[1])  # Flip the x coordinate
                screen_y = int(y1 * screen_height / img.shape[0])
                pyautogui.moveTo(screen_x, screen_y)
                if drag:
                    pyautogui.mouseUp()
                    drag = False
            # If the distance is below a certain threshold, left click the mouse
            elif distance < 20:
                if not drag:
                    pyautogui.mouseDown()
                    drag = True

            # Get the position of the middle finger and thumb
            x3, y3 = int(handLms.landmark[12].x * img.shape[1]), int(handLms.landmark[12].y * img.shape[0])
            # Calculate the distance between the tips of the middle finger and thumb
            distance2 = math.hypot(x3 - x2, y3 - y2)
            # If the distance is below a certain threshold, right click the mouse
            if distance2 < 20:
                pyautogui.rightClick()

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
