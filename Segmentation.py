import cv2
import copy

class Segmentation(object):
    def start(self):
        pass

    def test(self):
        file_name = input('$ File name : ')
        img = cv2.imread(file_name,0)
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

    def segmentation_image_show(self,origin_img, segmentation_img, count):
        color_img = copy.deepcopy(origin_img)
        
        # 영역 개수
        if count <= 5:
            color = [0,0,255]
        else:
            color = [200,0,0]

        for i in range(len(segmentation_img)):
            for j in range(len(segmentation_img[0])):
                if segmentation_img[i][j] != 0 and segmentation_img[i][j] != 255 and segmentation_img[i][j] != 1:
                    color_img[i][j] = color
        return color_img

sg = Segmentation()
sg.test()
