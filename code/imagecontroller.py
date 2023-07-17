import cv2
import matplotlib.pyplot as plt
import numpy as np

class ImageContronller:
    def __init__(self):
        # 左中右图片路径
        self.image_left = ''
        self.image_central = ''
        self.image_right = ''

    def setImageLeft(self, imagefile):
        self.image_left = imagefile

    def setImageCentral(self, imagefile):
        self.image_central = imagefile

    def setImageRight(self, imagefile):
        self.image_right = imagefile

    def printRoad(self):
        print(self.image_left)
        print(self.image_central)
        print(self.image_right)

    # 提取图片中的痕迹轮廓
    def extractSootPattern(self, image):
        # 读取图片
        e = cv2.imread(image)
        # 图片灰度化
        g = cv2.cvtColor(e, cv2.COLOR_BGR2GRAY)
        # 图片二值化
        r, b = cv2.threshold(g, 240, 255, cv2.THRESH_BINARY_INV)
        # 提取图片中的轮廓
        cr, t = cv2.findContours(b, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 计算出面积最大的一组轮廓
        # i: 组数
        # maxa: 最大面积
        # maxi: 面积最大的轮廓组数
        i = 0
        maxa = 0
        maxi = 0
        for cnt in cr:
            area = cv2.contourArea(cnt)
            if area > maxa:
                maxa = area
                maxi = i
            i = i + 1
        # 获取图片的长和宽
        rows, cols = e.shape[:2]

        # 筛选坐标
        tx = []
        ty = []
        for cnt in cr[maxi]:
            if cnt[0][1] > 400 and cnt[0][1] < 900:
                tx.append(cnt[0][0])
                ty.append(cnt[0][1])
        n_x = np.array(tx)
        n_y = np.array(ty)
        t_x = []
        t_y = []
        # 以x轴为准，将坐标对从小到大排队
        n = list(zip(n_x, n_y))
        n = sorted(n, key=lambda x: x[0])
        for i in n:
            if i[0] in t_x:
                continue
            y = i[1]
            for j in n:
                if i[0] == j[0] and i[1] < j[1]:
                    y = j[1]
            t_x.append(i[0])
            t_y.append(y)

        n_x = np.array(t_x)
        n_y = np.array(t_y)
        # 将x,y的图片坐标转换为实际坐标
        n_x = n_x * 5 / cols
        n_y = 4 - (n_y * 4 / rows)
        # 将的到的坐标进行二次多项式拟合
        # 得到的系数将作为特征参数返回
        paraNihe = np.polyfit(n_x, n_y, 2)
        # 获取拟合曲线的坐标
        fit = np.poly1d(paraNihe)
        f_y = fit(n_x)
        return n_x, n_y, f_y, paraNihe