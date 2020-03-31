# -*- cording : utf-8 -*-
# Cut_blank 후, 배경이 각각 따로 세그먼트가 되는데 수정 필요
# 배경을 흰색으로 단정지을지 고민


import cv2
import copy

class Segmentation(object):
    def start(self, file_name):
        img = cv2.imread(file_name,0)
        if img is None:
            print('Not found',file_name)
        else:
            img = self.binarize(img,220)
            sg = self.segmentation(img)
            origin = cv2.imread(file_name)
            test = self.segmentation_image_show(origin,sg[0],sg[1])
            cv2.imshow('Origign',origin)
            cv2.imshow('Color',test)
            cv2.waitKey(0)

    def binarize(self, img, threshold):
        # 이진화
        ret, bin_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
        return bin_img

    def segmentation(self, img):
        # 모든 픽셀을 돌아보고 그루핑
        segmentation_img = copy.deepcopy(img)
        offset = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        count = 0
        start_point = []

        for i in range(len(img)):
            for j in range(len(img[0])):
                if segmentation_img[i][j] == 255:
                    start_point.append([i,j])
                    count += 1
                    q = [[i,j]]
                    while q:
                        cur = q.pop(0)
                        x, y = cur[0], cur[1]
                        if x < 0 or y < 0:
                            pass
                        elif x > len(img) - 1 or y > len(img[0]) - 1:
                            pass
                        elif segmentation_img[x][y] != 255:
                            pass
                        else:
                            segmentation_img[x][y] = count
                            for i in range(4):
                                q.append([x + offset[i][0], y + offset[i][1]])
        return [segmentation_img, count]

    ## 영역 개수로 판단하기
#     def segmentation_image_show(self,origin_img, segmentation_img, count):
#         color_img = copy.deepcopy(origin_img)
        
#         # 영역 개수
#         if count <= 5:
#             color = [0,0,255]
#         else:
#             color = [200,0,0]

#         for i in range(len(segmentation_img)):
#             for j in range(len(segmentation_img[0])):
#                 if segmentation_img[i][j] != 0 and segmentation_img[i][j] != 255 and segmentation_img[i][j] != 1:
#                     color_img[i][j] = color
#         return color_img


    ## 영역 넓이로 찾기 (제일 큰 값)
    def segmentation_image_show(self,origin_img, segmentation_img, count):
        color_img = copy.deepcopy(origin_img)
        print(count)
        red_count = self.return_size(copy.deepcopy(segmentation_img),count)

        for i in range(len(segmentation_img)):
            for j in range(len(segmentation_img[0])):
                if segmentation_img[i][j] != 0 and segmentation_img[i][j] != 255 and segmentation_img[i][j] == red_count:
                    color_img[i][j] = [0,0,255]
        return color_img

    def return_size(self,img, count):
        count_list = [0] * (count + 5)
        for i in range(len(img)):
            for j in range(len(img[0])):
                if img[i][j] != 255 and img[i][j] != 0 and img[i][j] != 1:
                    count_list[img[i][j]] += 1
        return count_list.index(max(count_list))
    
#########################################################################
# GUI_Pygame 에서 쓰는 코드
# 1차 구현 3/27

import cv2
import copy

class Segmentation(object):
    def start(self, file_name, color, xy):
        img = cv2.imread(file_name,0)
        if img is None:
            print('Not found',file_name)
        else:
            img = self.binarize(img,250)
            sg = self.segmentation(img)
            origin = cv2.imread(file_name)
            color_img = self.segmentation_image_show(origin, sg, color, xy)
            return color_img
            # test = self.segmentation_image_show(origin,sg[0],sg[1], color)
            # cv2.imshow('Origign',origin)
            # cv2.imshow('Color',test)
            # cv2.waitKey(0)

    def binarize(self, img, threshold):
        # 이진화
        ret, bin_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
        return bin_img

    def segmentation(self, img):
        segmentation_img = copy.deepcopy(img)
        offset = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        count = 0
        start_point = []

        for i in range(len(img)):
            for j in range(len(img[0])):
                if segmentation_img[i][j] == 255:
                    start_point.append([i, j])
                    count += 1
                    q = [[i, j]]
                    while q:
                        cur = q.pop(0)
                        x, y = cur[0], cur[1]
                        if x < 0 or y < 0:
                            pass
                        elif x > len(img) - 1 or y > len(img[0]) - 1:
                            pass
                        elif segmentation_img[x][y] != 255:
                            pass
                        else:
                            segmentation_img[x][y] = count
                            for i in range(4):
                                q.append([x + offset[i][0], y + offset[i][1]])
        return segmentation_img

    def segmentation_image_show(self, origin_img, segmentation_img, color, xy):
        color_img = copy.deepcopy(origin_img)
        color_count = segmentation_img[xy[0]][xy[1]]

        for i in range(len(segmentation_img)):
            for j in range(len(segmentation_img[0])):
                if segmentation_img[i][j] != 0 and segmentation_img[i][j] != 255 and segmentation_img[i][j] == color_count:
                    color_img[i][j] = color
        return color_img

    # def segmentation(self, img):
    #     segmentation_img = copy.deepcopy(img)
    #     offset = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    #     count = 0
    #     start_point = []
    #
    #     for i in range(len(img)):
    #         for j in range(len(img[0])):
    #             if segmentation_img[i][j] == 255:
    #                 start_point.append([i,j])
    #                 count += 1
    #                 q = [[i,j]]
    #                 while q:
    #                     cur = q.pop(0)
    #                     x, y = cur[0], cur[1]
    #                     if x < 0 or y < 0:
    #                         pass
    #                     elif x > len(img) - 1 or y > len(img[0]) - 1:
    #                         pass
    #                     elif segmentation_img[x][y] != 255:
    #                         pass
    #                     else:
    #                         segmentation_img[x][y] = count
    #                         for i in range(4):
    #                             q.append([x + offset[i][0], y + offset[i][1]])
    #     return [segmentation_img, count]
    #
    # def segmentation_image_show(self,origin_img, segmentation_img, count , color):
    #     color_img = copy.deepcopy(origin_img)
    #     # print(count) # 세그먼트 개수 출력
    #     # [4,2,173] # 체리색
    #
    #     color_count = self.return_size(copy.deepcopy(segmentation_img),count)
    #
    #     for i in range(len(segmentation_img)):
    #         for j in range(len(segmentation_img[0])):
    #             if segmentation_img[i][j] != 0 and segmentation_img[i][j] != 255 and segmentation_img[i][j] == color_count:
    #                 color_img[i][j] = color
    #     return color_img
    #
    # def return_size(self,img, count):
    #     count_list = [0] * 255
    #     for i in range(len(img)):
    #         for j in range(len(img[0])):
    #             if img[i][j] != 255 and img[i][j] != 0 and img[i][j] != 1:
    #                 count_list[img[i][j]] += 1
    #     return count_list.index(max(count_list))
