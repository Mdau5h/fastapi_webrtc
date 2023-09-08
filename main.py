import cv2

vid = cv2.VideoCapture(0)

vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = vid.read()

    if ret:
        cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
