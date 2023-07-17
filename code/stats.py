from PySide2.QtWidgets import QApplication, QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtCore
from PySide2.QtGui import QPixmap, Qt
import imagecontroller as ic
import os
import pyqtgraph as pg
import prediction
from qt_material import apply_stylesheet
import numpy as np

class Stats:
    def __init__(self):
        # 将画布背景颜色设置为白色
        pg.setConfigOption('background', '#FFFFFF')
        pg.setConfigOption('foreground', 'k')
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        QUiLoader().registerCustomWidget(pg.PlotWidget)
        self.ui = QUiLoader().load('..\\ui\\firelocation.ui')

        # 设置画布
        # 左墙轮廓提取画布
        self.ui.leftextractimage.showGrid(x=True,y=True)
        self.ui.leftextractimage.showAxes((True, True, True, True), showValues=True, size=False)
        # 中墙轮廓提取画布
        self.ui.centralextractimage.showGrid(x=True, y=True)
        self.ui.centralextractimage.showAxes((True, True, True, True), showValues=True, size=False)
        # 右墙轮廓提取画布
        self.ui.rightextractimage.showGrid(x=True, y=True)
        self.ui.rightextractimage.showAxes((True, True, True, True), showValues=True, size=False)
        # 位置预测画布
        self.ui.firelocationimage.showGrid(x=True, y=True)
        self.ui.firelocationimage.showAxes((True, True, True, True), showValues=True, size=False)

        # 图片控制器，用于处理图片
        self.imgc = ic.ImageContronller()

        # 选择图片
        # 左墙图片选择
        self.ui.leftselect.clicked.connect(lambda: self.selectImage(self.ui.leftimage, 1))
        # 中墙图片选择
        self.ui.centralselect.clicked.connect(lambda: self.selectImage(self.ui.centralimage, 2))
        # 右墙图片选择
        self.ui.rightselect.clicked.connect(lambda: self.selectImage(self.ui.rightimage, 3))

        # 清空图片
        self.ui.leftcancel.clicked.connect(lambda: self.cancelImage(self.ui.leftimage, 1))
        self.ui.centralcancel.clicked.connect(lambda: self.cancelImage(self.ui.centralimage, 2))
        self.ui.rightcancel.clicked.connect(lambda: self.cancelImage(self.ui.rightimage, 3))

        # 提取轮廓和特征值
        self.ui.extract_btn.clicked.connect(self.drawSootPattern)

        # 预测火源位置
        self.ui.predict_btn.clicked.connect(self.predict)

        # 清空操作记录
        self.ui.cleanlog_btn.clicked.connect(self.cleanLog)


    # 选择图片
    def selectImage(self, image, order):
        # 选择图片窗口
        fileDialog = QFileDialog(self.ui)
        # 图片地址存入fileDirectory
        fileDirectory,_ = fileDialog.getOpenFileNames(self.ui, '选择图片')
        # 设置图片尺寸
        pixmap = QPixmap(fileDirectory[0]).scaled(self.ui.leftimage.size(), aspectMode=Qt.KeepAspectRatio)
        # 将图片显示到label中
        image.setScaledContents(True)
        image.setPixmap(pixmap)

        # 将图片路径传入图片控制器中
        if order == 1:
            self.imgc.setImageLeft(fileDirectory[0])
            self.ui.operatelog.append('Select left wall image: '+fileDirectory[0])
        elif order == 2:
            self.imgc.setImageCentral(fileDirectory[0])
            self.ui.operatelog.append('Select central wall image: ' + fileDirectory[0])
        elif order == 3:
            self.imgc.setImageRight(fileDirectory[0])
            self.ui.operatelog.append('Select right wall image: ' + fileDirectory[0])

    # 清空图片
    def cancelImage(self, image, order):
        image.setPixmap('')
        image.setText('Please select a image')
        if order == 1:
            self.ui.operatelog.append('Clean left wall image')
        elif order == 2:
            self.ui.operatelog.append('Clean left wall image')
        elif order == 3:
            self.ui.operatelog.append('Clean left wall image')

    # 绘制图片
    def drawSootPattern(self):
        self.ui.operatelog.append('Soot Pattern Extraction')
        # 从图片控制器中获取提取到的轮廓坐标
        # x,y为轮廓原坐标，fy为拟合曲线的y轴坐标
        lx, ly, lfy, _ = self.imgc.extractSootPattern(self.imgc.image_left)
        cx, cy, cfy, _ = self.imgc.extractSootPattern(self.imgc.image_central)
        rx, ry, rfy, _ = self.imgc.extractSootPattern(self.imgc.image_right)

        # 绘制左墙曲线
        # 设置画布的坐标轴范围
        self.ui.leftextractimage.setYRange(0, 4)
        self.ui.leftextractimage.setXRange(0, 5)
        # 绘制左墙的轮廓以及拟合曲线
        self.ui.leftextractimage.plot(lx, ly, pen=pg.mkPen(width=2, color='b'))
        self.ui.leftextractimage.plot(lx, lfy, pen=pg.mkPen(width=2, color='r'))

        # 绘制中墙曲线
        # 设置画布的坐标轴范围
        self.ui.centralextractimage.setYRange(0, 4)
        self.ui.centralextractimage.setXRange(0, 5)
        # 绘制左墙的轮廓以及拟合曲线
        self.ui.centralextractimage.plot(cx, cy, pen=pg.mkPen(width=2, color='b'))
        self.ui.centralextractimage.plot(cx, cfy, pen=pg.mkPen(width=2, color='r'))

        # 绘制右墙曲线
        # 设置画布的坐标轴范围
        self.ui.rightextractimage.setYRange(0, 4)
        self.ui.rightextractimage.setXRange(0, 5)
        # 绘制左墙的轮廓以及拟合曲线
        self.ui.rightextractimage.plot(rx, ry, pen=pg.mkPen(width=2, color='b'))
        self.ui.rightextractimage.plot(rx, rfy, pen=pg.mkPen(width=2, color='r'))
        return

    # 预测火源坐标
    def predict(self):
        # 获取三面墙轮廓的特征值，左墙特征值为lf，中墙特征值为cf，右墙特征值为rf
        _, _, _, lf = self.imgc.extractSootPattern(self.imgc.image_left)
        _, _, _, cf = self.imgc.extractSootPattern(self.imgc.image_central)
        _, _, _, rf = self.imgc.extractSootPattern(self.imgc.image_right)

        # 将三面墙的特征值合并到列表feature中
        feature = []
        feature.extend(cf)
        feature.extend(lf)
        feature.extend(rf)

        # 调用prediction模块进行位置预测
        pc = prediction.Prediction(feature)
        # 预测结果转换成numpy便于绘制在画布中
        fl = pc.getPrediction().cpu().detach().numpy()

        x = [fl[0]]
        y = [fl[1]]
        # 调整预测模块的画布坐标
        self.ui.firelocationimage.setYRange(0, 5)
        self.ui.firelocationimage.setXRange(0, 5)
        # 绘制预测坐标于画布中
        self.ui.firelocationimage.plot(x, y, symbol='x', symbolPen=pg.mkPen(width=3, color='r'))
        # 显示预测坐标
        self.ui.label_location.setText('coordinates: ('+str(fl[0])+' , '+str(fl[1])+' )')
        self.ui.operatelog.append('The extracted features: '+ str(feature))
        self.ui.operatelog.append('Predicted: ( '+str(fl[0])+' , '+str(fl[1])+' )')

    def cleanLog(self):
        self.ui.operatelog.clear()

# QImageReader.supportedImageFormats()
app = QApplication([])
app.addLibraryPath(os.path.join(os.path.dirname(QtCore.__file__), "plugins"))
apply_stylesheet(app, theme='light_blue.xml', invert_secondary=True)
stats = Stats()
stats.ui.show()
app.exec_()