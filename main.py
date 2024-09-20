import cv2
from detector.detector import MotionDetector, FaceDetector
from utils.utils import draw_bounding_box


def run_detection():
    cap = cv2.VideoCapture(0) 

    face_detector = FaceDetector()
    motion_detector = MotionDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = face_detector.detect_faces(frame)

        motion_contours = motion_detector.detect_motion(frame)

        for (x, y, w, h) in faces:
            draw_bounding_box(frame, (x, y, w, h), color=(0, 0, 255)) 

        for contour in motion_contours:
            x, y, w, h = cv2.boundingRect(contour)
            draw_bounding_box(frame, (x, y, w, h), color=(0, 0, 255)) 

        cv2.imshow('Face and Motion Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run_detection()
