import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe Hand model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Recognize gestures function
def recognize_gesture(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    if thumb_tip.y < thumb_ip.y and thumb_ip.y < index_finger_tip.y and index_finger_tip.y < middle_finger_tip.y and middle_finger_tip.y < ring_finger_tip.y and ring_finger_tip.y < pinky_tip.y:
        return "thumbs_up"
    if index_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and middle_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and ring_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and pinky_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y:
        return "palm_open"
    if index_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and middle_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and ring_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and pinky_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y:
        return "fist"
    if index_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and middle_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and ring_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and pinky_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y:
        return "peace"
    if index_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and middle_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and ring_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and pinky_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y:
        return "one_finger_up"
    return None

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks)
            if gesture:
                print(f'Gesture: {gesture}')
                if gesture == "thumbs_up":
                    pyautogui.press('volumeup')
                elif gesture == "palm_open":
                    pyautogui.press('playpause')
                elif gesture == "fist":
                    pyautogui.press('volumedown')
                elif gesture == "peace":
                    pyautogui.press('nexttrack')
                elif gesture == "one_finger_up":
                    pyautogui.press('prevtrack')

    cv2.imshow('Hand Gesture Recognition', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
