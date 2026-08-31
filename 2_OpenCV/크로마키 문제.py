import cv2
import sys

sea_cap = cv2.VideoCapture("./movies/sea.mp4")
woman_cap = cv2.VideoCapture("./movies/woman.mp4")

if not sea_cap.isOpened or not woman_cap.isOpened():
    print('입력 동영상 중 하나 이상을 열 수 없습니다.')
    sys.exit()

width1 = int(sea_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
width2 = int(woman_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height1 = int(sea_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
height2 = int(woman_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps1 = sea_cap.get(cv2.CAP_PROP_FPS)
fps2 = woman_cap.get(cv2.CAP_PROP_FPS)

lower_green = (50, 180, 0)
upper_green = (70, 255, 255)



print('너비1: ', width1)
print('너비2: ', width2)
print('높이1: ', height1)
print('높이2: ', height2)
print('FPS1: ', fps1)
print('FPS2: ', fps2)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("sum.avi", fourcc, fps1, (width1, height1))



if not out.isOpened():
    sea_cap.release()
    woman_cap.release()
    raise RuntimeError('출력 동영상 파일을 생성할 수 없습니다.')

delay = max(1, round(1000 / fps1))
stop = False

while True:
    ret1, frame1 = woman_cap.read()
    ret2, frame2 = sea_cap.read()
    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    composite = frame1.copy()
    cv2.copyTo(frame2, mask, composite)
    if not ret1:
        break
    if composite.shape[1] != width1 or composite.shape[0] != height1:
        composite = cv2.resize(composite, (width1, height1))
    out.write(composite)
    cv2.imshow('output', composite)
    if cv2.waitKey(delay) == 27:
        stop = True
        break
    if stop:
        break

sea_cap.release()
woman_cap.release()
out.release()
cv2.destroyAllWindows()