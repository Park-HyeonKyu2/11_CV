import cv2
img = cv2.imread("./images/keyboard.bmp", cv2.IMREAD_GRAYSCALE)

_, img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

count, labels, stats, centroids = cv2.connectedComponentsWithStats(img_bin, connectivity=8)
print("라벨 개수(배경 포함): ", count)
print("라벨 개수(배경 제외): ", count - 1)

print("labels shape: ", labels.shape)
print("labels 일부: \n", labels[:10, :10])

print("stats: ")
print(stats)

print("centroids: ")
print(centroids)

for i in range(1, count):
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]
    area = stats[i, cv2.CC_STAT_AREA]

    if area < 30:
        continue

    cx, cy = centroids[i]

    cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.circle(dst, (int(cx), int(cy)), 3, (0, 0, 255), -1)

cv2.imshow("img", img)
cv2.imshow()















