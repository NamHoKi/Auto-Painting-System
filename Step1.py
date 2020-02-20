import cv2
import numpy as np

class Fill_color(object):
    def start(self, file):
        # start_img = self.preprocessing(file)
        origin = cv2.imread(file,0)
        origin_color = cv2.imread(file)

        bin_img = self.binarize(origin, 220)
        open_img = self.image_open(bin_img)
        reverse_img = self.reverse(open_img)
        dilate_img = self.image_dilate(reverse_img)
        edge_img = self.edge_detection(reverse_img, dilate_img)
        white_img, transform = self.fill_white(reverse_img, edge_img)
        color_img = self.fill_color(origin_color,transform,[0,0,255])

        cv2.imshow('Result',color_img)
        cv2.waitKey(0)

    def read_data(self):
        pass

    # def preprocessing(self, file):
    #     img = cv2.imread(file)
    #     index = 0
    #     for i in range(1,len(img)):
    #         if max(img[i]) != 0:
    #             index = i
    #             break
    #     img = img[index:]
    #     index = 0
    #     for i in range(len(img)-2,-1,-1):
    #         if max(img[i]) != 0:
    #             index = i
    #             break
    #     img = img[:i+1]
    #     index = 0
    #
    #     cv2.imshow('test',img)
    #     cv2.waitKey(0)

    def binarize(self, img, threshold):
        # 이진화
        ret, bin_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
        return bin_img

    def image_open(self, img, kernel_size=5):
        # 열기
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        return result

    def reverse(self, img):
        # 밝기 반전
        for i in range(len(img)):
            for j in range(len(img[0])):
                if img[i][j] == 0:
                    img[i][j] = 255
                else:
                    img[i][j] = 0
        return img

    def image_dilate(self, img):
        #팽창
        kernel = np.ones((3, 3), np.uint8)
        result = cv2.dilate(img, kernel, iterations=1)
        return result

    def edge_detection(self, img1, img2):
        and_result = img1[:]
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] + img2[i][j] == 255:
                    and_result[i][j] = 255
                else:
                    and_result[i][j] = 0
        return and_result

    def fill_white(self, img1, img2):
        x, y = int(len(img1) / 2), int(len(img1[0]) / 2)
        color = img2[:]
        q = [[x, y]]
        offset = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        transform = []
        while q:
            cur = q.pop(0)
            x, y = cur[0], cur[1]
            if x < 0 or y < 0:
                pass
            if x >= len(color) or y >= len(color[0]):
                pass
            if color[x][y] == 255:
                pass
            else:
                color[x][y] = 255
                transform.append([x, y])
                for i in range(4):
                    q.append([x + offset[i][0], y + offset[i][1]])
        return [color, transform]

    def fill_color(self, img, transform, color):
        for t in transform:
            img[t[0]][t[1]] = np.array(color)
        return img

main = Fill_color()
main.start('sy_ap1.png')


# import cv2
# import numpy as np

# # 이미지 읽어오기
# img = cv2.imread('sy_ap1.png',0)
# cv2.imshow('origin',img)

# # 이진화
# ret, bin_img = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)
# cv2.imshow("bin",bin_img)

# # 팽창
# kernel = np.ones((5, 5), np.uint8)
# result = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, kernel)

# cv2.imshow("open", result)

# # 밝기 뒤집기
# for i in range(len(result)):
#     for j in range(len(result[0])):
#         if result[i][j] == 0:
#             result[i][j] = 255
#         else:
#             result[i][j] = 0

# cv2.imshow('reverse',result)

# kernel = np.ones((3, 3), np.uint8)
# result2 = cv2.dilate(result, kernel, iterations = 1)

# cv2.imshow("dilate", result2)

# # and 연산 -> edge 검출 2중선
# and_result = result[:]
# for i in range(len(result)):
#     for j in range(len(result[0])):
#         if result[i][j] + result2[i][j] == 255:
#             and_result[i][j] = 255
#         else:
#             and_result[i][j] = 0

# cv2.imshow('and',and_result)

# # 색 채우기
# x, y = int(len(result)/2) , int(len(result[0])/2)
# color = and_result[:]
# q = [[x,y]]
# offset = [[1,0],[0,1],[-1,0],[0,-1]]

# transform = []
# while q:
#     cur = q.pop(0)
#     x,y = cur[0], cur[1]
#     if x < 0 or y < 0:
#         pass
#     if x >= len(color) or y >= len(color[0]):
#         pass
#     if color[x][y] == 255:
#         pass
#     else:
#         color[x][y] = 255
#         transform.append([x,y]) # 색 채운곳을 저장
#         for i in range(4):
#             q.append([x+offset[i][0],y+offset[i][1]])
# cv2.imshow('Q',color)
# cv2.waitKey(0)

# # RGB
# img = cv2.imread('sy_ap1.png')

# for t in transform:
#     img[t[0]][t[1]] = np.array([0,0,255])
# cv2.imshow('Apple',img)
# cv2.waitKey(0)
