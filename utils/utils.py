import cv2

def draw_bounding_box(frame, rect, color=(0, 255, 0), thickness=2):
    x, y, w, h = rect
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)
