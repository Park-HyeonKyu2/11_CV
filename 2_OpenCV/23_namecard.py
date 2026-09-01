import cv2
import numpy as np

img = cv2.imread("./images/namecard.jpg")

w, h = img.shape[:2]
print(w, h)

src_quad = np.array([
    [50, 50],
    [50, w - 50],
    [h - 50, w - 50],
    [h - 50, 50],
], dtype=np.float32)


preview = img.copy()
for pt in src_quad.astype(int):
    cv2.circle(preview, tuple(pt), 8, (0, 0, 255), -1)

cv2.polylines(preview, [src_quad.astype(np.int32)], True, (0, 255, 0), 3)

cv2.imshow("preview", preview)

cv2.waitKey(0)
cv2.destroyAllWindows()







