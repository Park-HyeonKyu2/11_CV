import cv2
import sys

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("recoding.avi", fourcc, fps, (width, height))

if not out.isOpened():
    cap.release()
    raise RuntimeError('출력 동영상 파일을 생성할 수 없습니다.')

print('카메라 연결 성공!')

delay = max(1, round(1000 / fps))
stop = False

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if not ret:
        break
    if frame.shape[1] != width or frame.shape[0] != height:
        frame = cv2.resize(frame, (width, height))
    out.write(frame)
    cv2.imshow('output', frame)
    if cv2.waitKey(delay) == 27:
        stop = True
        break

cap.release()
out.release()
cv2.destroyAllWindows()