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
