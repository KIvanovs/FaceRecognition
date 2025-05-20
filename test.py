import cv2
import face_recognition
import os

#distance between camera and person
distance_threshold = 0.50 


image = "owner.png" 
ref_image = face_recognition.load_image_file(image) #photo placi in numpy array
ref_encodings = face_recognition.face_encodings(ref_image) # bild face uniqless as a vector of 128 numbers
known_face = ref_encodings[0]

# Haar cascade for face detection
cascade_path = "haarcascade_frontalface_default.xml"
if not os.path.exists(cascade_path):
    print("Cascade file not found.")
    exit()
face_detector = cv2.CascadeClassifier(cascade_path)

# open the camera , if it doesn't open then give the usb port
camera = cv2.VideoCapture(0)
print(f"Starting. Distance threshold = {distance_threshold}")

while True:
    got_frame, frame = camera.read()
    if not got_frame:continue
    unlocked = False

    #BRG to RGB
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_frame = small_frame[:, :, ::-1].copy()

    # Detect face encodings
    encodings = face_recognition.face_encodings(rgb_frame)
    print("Faces detected:", len(encodings))

    if len(encodings) == 1:
        dist = face_recognition.face_distance([known_face], encodings[0])[0]
        print(f"Distance: {dist:.3f}")
        if dist < distance_threshold:
            unlocked = True

    # BRG to gray and draw box green = unlocked , red = locked
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    for x, y, w, h in faces:
        color = (0, 255, 0) if unlocked else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    # Display lock status text
    status = "UNLOCKED" if unlocked else "LOCKED"
    status_color = (0, 255, 0) if unlocked else (0, 0, 255)
    cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)

    # close press q 
    cv2.imshow("Face Unlock", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
