import cv2
import numpy as np

class Fill_color(object):
    def start(self):
        while True:
            file = input('$ File Name: ')
            start_img = self.preprocessing(file)
            origin = cv2.imread(file,0)
            origin_color = cv2.imread(file)

            if origin is None or origin_color is None:
                print('-- Not found file --')
            else:
                bin_img = self.binarize(origin, 220)
                open_img = self.image_open(bin_img)
                reverse_img = self.reverse(open_img)
                dilate_img = self.image_dilate(reverse_img, 1, 1)
                white_img, transform = self.fill_white(reverse_img, dilate_img)
                color_img = self.fill_color(origin_color,transform,[0,0,255])
                cv2.imshow('Result',color_img)
                cv2.waitKey(0)

    # def preprocessing(self, file):
    #     origin = cv2.imread(file, 0)
    #     img = self.binarize(origin, 220)
    #     result = cv2.imread(file)
    # 
    #     index = 0
    #     for i in range(len(img)-10,-1,-1):
    #         if min(img[i]) != 255:
    #             index = i
    #             break
    #     result = result[:index+1]
    #     img = img[:index+1]
    # 
    #     index = 0
    #     for i in range(1,len(img)):
    #         if min(img[i]) != 255:
    #             index = i
    #             break
    #     result = result[index:]
    #     img = img[:index+1]
    # 
    #     cv2.imshow('1',img)
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

    def image_dilate(self, img, kernel_size, n):
        #팽창
        for i in range(n):
            kernel = np.ones((kernel_size, kernel_size), np.uint8)
            img = cv2.dilate(img, kernel, iterations=1)
        return img

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
            elif x > len(color)-1 or y > len(color[0])-1:
                pass
            elif color[x][y] == 255:
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
main.start()
