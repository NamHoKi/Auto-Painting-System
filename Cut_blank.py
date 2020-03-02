# -*- cording : utf-8 -*-

import cv2

class Cut_blank(object):
    def main(self):
        while True:
            command = input('$ file_name')
            if command == 'exit':
                return
            self.cut_blank(command)

    def cut_blank(self, file_name):
        origin = cv2.imread(file_name, 0)
        if origin is None:
            print('Not found '+file_name)
            return
        img = self.binarize(origin, 220)
        result = cv2.imread(file_name)

        x1, x2, y1, y2 = 0, 0, 0, 0

        for i in range(len(img) - 1, -1, -1):
            if min(img[i]) != 255:
                x2 = i
                break

        for i in range(0, len(img)):
            if min(img[i]) != 255:
                x1 = i
                break

        check = False
        for i in range(0, len(img[0])):
            for j in range(0, len(img)):
                if img[j][i] != 255:
                    y1 = i
                    check = True
                    break
            if check:
                break

        check = False
        for i in range(len(img[0]) - 1, -1, -1):
            for j in range(0, len(img)):
                if img[j][i] != 255:
                    y2 = i
                    check = True
                    break
            if check:
                break

        img = img[x1:x2, y1:y2]
        cv2.imshow('after', img)
        cv2.waitKey(0)

    def binarize(self, img, threshold):
        # 이진화
        ret, bin_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
        return bin_img
