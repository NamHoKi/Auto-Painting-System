import cv2
import numpy as np

# 이미지 읽어오기
img = cv2.imread('sy_ap1.png',0)
cv2.imshow('origin',img)

# 이진화
ret, bin_img = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)
cv2.imshow("bin",bin_img)

# 팽창
kernel = np.ones((5, 5), np.uint8)
result = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, kernel)

cv2.imshow("open", result)

# 밝기 뒤집기
for i in range(len(result)):
    for j in range(len(result[0])):
        if result[i][j] == 0:
            result[i][j] = 255
        else:
            result[i][j] = 0

cv2.imshow('reverse',result)

kernel = np.ones((3, 3), np.uint8)
result2 = cv2.dilate(result, kernel, iterations = 1)

cv2.imshow("dilate", result2)

# and 연산 -> edge 검출 2중선
and_result = result[:]
for i in range(len(result)):
    for j in range(len(result[0])):
        if result[i][j] + result2[i][j] == 255:
            and_result[i][j] = 255
        else:
            and_result[i][j] = 0

cv2.imshow('and',and_result)

# 색 채우기
x, y = int(len(result)/2) , int(len(result[0])/2)
color = and_result[:]
q = [[x,y]]
offset = [[1,0],[0,1],[-1,0],[0,-1]]

transform = []
while q:
    cur = q.pop(0)
    x,y = cur[0], cur[1]
    if x < 0 or y < 0:
        pass
    if x >= len(color) or y >= len(color[0]):
        pass
    if color[x][y] == 255:
        pass
    else:
        color[x][y] = 255
        transform.append([x,y]) # 색 채운곳을 저장
        for i in range(4):
            q.append([x+offset[i][0],y+offset[i][1]])
cv2.imshow('Q',color)
cv2.waitKey(0)

# RGB
img = cv2.imread('sy_ap1.png')

for t in transform:
    img[t[0]][t[1]] = np.array([0,0,255])
cv2.imshow('Apple',img)
cv2.waitKey(0)
