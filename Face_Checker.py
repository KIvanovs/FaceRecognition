import cv2
import face_recognition
import os

class FaceChecker:
    def __init__(self, ref_image_path, cascade_path, distance_threshold=0.50, camera_id= 1,):

        # Validate paths
        if not os.path.exists(ref_image_path):
            raise FileNotFoundError(f"Reference image not found: {ref_image_path}")
        if not os.path.exists(cascade_path):
            raise FileNotFoundError(f"Cascade file not found: {cascade_path}")

        self.distance_threshold = distance_threshold
        self.camera_id = camera_id
        self.face_detector = cv2.CascadeClassifier(cascade_path)
        
        # Load the reference image and compute its encoding
        reference_image = face_recognition.load_image_file(ref_image_path)
        ref_encodings = face_recognition.face_encodings(reference_image)

        if not ref_encodings:
            raise ValueError("No face found in reference image.")
        self.known_face = ref_encodings[0]

    def authentificate(self):
        cap = cv2.VideoCapture(self.camera_id)
        print(f"Starting. Distance threshold = {self.distance_threshold}")

        while True:
            ret, frame = cap.read()

            if not ret:
                continue

            # Resize the frame for faster processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_frame = small_frame[:, :, ::-1].copy()

            # Find all face locations and encodings in the current frame
            encodings = face_recognition.face_encodings(rgb_frame)
            print("Faces detected:", len(encodings))

            # If exactly one face is detected, compare it with the known face
            if len(encodings) == 1:
                dist = face_recognition.face_distance([self.known_face], encodings[0])[0]
                print(f"Distance: {dist:.3f}")
                if dist < self.distance_threshold:
                    print("Owner recognized.")

                    cap.release()
                    cv2.destroyAllWindows()
                    return True
                else:
                    print("Face did not match.")
            else:
                print("Incorrect number of faces detected.")

            # Draw rectangles around detected faces
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
                
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Display the frame with rectangles
            cv2.putText(frame, "Locked", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("Face Recognition", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        return False
