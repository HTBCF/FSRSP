# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'firelocation.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_FirelocationPredict(object):
    def setupUi(self, FirelocationPredict):
        if not FirelocationPredict.objectName():
            FirelocationPredict.setObjectName(u"FirelocationPredict")
        FirelocationPredict.resize(1608, 870)
        self.verticalLayout_4 = QVBoxLayout(FirelocationPredict)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.imageinput = QGroupBox(FirelocationPredict)
        self.imageinput.setObjectName(u"imageinput")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageinput.sizePolicy().hasHeightForWidth())
        self.imageinput.setSizePolicy(sizePolicy)
        self.imageinput.setMinimumSize(QSize(0, 0))
        self.imageinput.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.imageinput)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_left = QVBoxLayout()
        self.verticalLayout_left.setObjectName(u"verticalLayout_left")
        self.verticalLayout_left.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.leftimage = QLabel(self.imageinput)
        self.leftimage.setObjectName(u"leftimage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftimage.sizePolicy().hasHeightForWidth())
        self.leftimage.setSizePolicy(sizePolicy1)
        self.leftimage.setMinimumSize(QSize(400, 300))
        self.leftimage.setMaximumSize(QSize(400, 300))
        self.leftimage.setStyleSheet(u"background-color: rgb(199, 199, 199)")
        self.leftimage.setScaledContents(False)
        self.leftimage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.leftimage)


        self.verticalLayout_left.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_left_button = QHBoxLayout()
        self.horizontalLayout_left_button.setObjectName(u"horizontalLayout_left_button")
        self.leftselect = QPushButton(self.imageinput)
        self.leftselect.setObjectName(u"leftselect")
        sizePolicy1.setHeightForWidth(self.leftselect.sizePolicy().hasHeightForWidth())
        self.leftselect.setSizePolicy(sizePolicy1)
        self.leftselect.setMinimumSize(QSize(150, 23))

        self.horizontalLayout_left_button.addWidget(self.leftselect)

        self.leftcancel = QPushButton(self.imageinput)
        self.leftcancel.setObjectName(u"leftcancel")
        sizePolicy1.setHeightForWidth(self.leftcancel.sizePolicy().hasHeightForWidth())
        self.leftcancel.setSizePolicy(sizePolicy1)
        self.leftcancel.setMinimumSize(QSize(150, 23))

        self.horizontalLayout_left_button.addWidget(self.leftcancel)


        self.verticalLayout_left.addLayout(self.horizontalLayout_left_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_left)

        self.verticalLayout_central = QVBoxLayout()
        self.verticalLayout_central.setObjectName(u"verticalLayout_central")
        self.verticalLayout_central.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.centralimage = QLabel(self.imageinput)
        self.centralimage.setObjectName(u"centralimage")
        sizePolicy1.setHeightForWidth(self.centralimage.sizePolicy().hasHeightForWidth())
        self.centralimage.setSizePolicy(sizePolicy1)
        self.centralimage.setMinimumSize(QSize(400, 300))
        self.centralimage.setMaximumSize(QSize(400, 300))
        self.centralimage.setStyleSheet(u"background-color: rgb(199, 199, 199)")
        self.centralimage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.centralimage)


        self.verticalLayout_central.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_central_button = QHBoxLayout()
        self.horizontalLayout_central_button.setObjectName(u"horizontalLayout_central_button")
        self.centralselect = QPushButton(self.imageinput)
        self.centralselect.setObjectName(u"centralselect")
        sizePolicy1.setHeightForWidth(self.centralselect.sizePolicy().hasHeightForWidth())
        self.centralselect.setSizePolicy(sizePolicy1)
        self.centralselect.setMinimumSize(QSize(150, 23))

        self.horizontalLayout_central_button.addWidget(self.centralselect)

        self.centralcancel = QPushButton(self.imageinput)
        self.centralcancel.setObjectName(u"centralcancel")
        sizePolicy1.setHeightForWidth(self.centralcancel.sizePolicy().hasHeightForWidth())
        self.centralcancel.setSizePolicy(sizePolicy1)
        self.centralcancel.setMinimumSize(QSize(150, 23))

        self.horizontalLayout_central_button.addWidget(self.centralcancel)


        self.verticalLayout_central.addLayout(self.horizontalLayout_central_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_central)

        self.verticalLayout_right = QVBoxLayout()
        self.verticalLayout_right.setObjectName(u"verticalLayout_right")
        self.verticalLayout_right.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.rightimage = QLabel(self.imageinput)
        self.rightimage.setObjectName(u"rightimage")
        sizePolicy1.setHeightForWidth(self.rightimage.sizePolicy().hasHeightForWidth())
        self.rightimage.setSizePolicy(sizePolicy1)
        self.rightimage.setMinimumSize(QSize(400, 300))
        self.rightimage.setMaximumSize(QSize(400, 300))
        self.rightimage.setStyleSheet(u"background-color: rgb(199, 199, 199)")
        self.rightimage.setTextFormat(Qt.AutoText)
        self.rightimage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.rightimage)


        self.verticalLayout_right.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rightselect = QPushButton(self.imageinput)
        self.rightselect.setObjectName(u"rightselect")
        sizePolicy1.setHeightForWidth(self.rightselect.sizePolicy().hasHeightForWidth())
        self.rightselect.setSizePolicy(sizePolicy1)
        self.rightselect.setMinimumSize(QSize(150, 23))

        self.horizontalLayout.addWidget(self.rightselect)

        self.rightcancel = QPushButton(self.imageinput)
        self.rightcancel.setObjectName(u"rightcancel")
        sizePolicy1.setHeightForWidth(self.rightcancel.sizePolicy().hasHeightForWidth())
        self.rightcancel.setSizePolicy(sizePolicy1)
        self.rightcancel.setMinimumSize(QSize(150, 23))

        self.horizontalLayout.addWidget(self.rightcancel)


        self.verticalLayout_right.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_right)


        self.horizontalLayout_6.addWidget(self.imageinput)

        self.verticalLayout_operatelog = QGroupBox(FirelocationPredict)
        self.verticalLayout_operatelog.setObjectName(u"verticalLayout_operatelog")
        self.verticalLayout_operatelog.setMaximumSize(QSize(600, 10000))
        self.verticalLayout = QVBoxLayout(self.verticalLayout_operatelog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.operatelog = QTextBrowser(self.verticalLayout_operatelog)
        self.operatelog.setObjectName(u"operatelog")

        self.verticalLayout.addWidget(self.operatelog)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.cleanlog_btn = QPushButton(self.verticalLayout_operatelog)
        self.cleanlog_btn.setObjectName(u"cleanlog_btn")
        sizePolicy1.setHeightForWidth(self.cleanlog_btn.sizePolicy().hasHeightForWidth())
        self.cleanlog_btn.setSizePolicy(sizePolicy1)
        self.cleanlog_btn.setMinimumSize(QSize(150, 23))

        self.horizontalLayout_7.addWidget(self.cleanlog_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_6.addWidget(self.verticalLayout_operatelog)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_output = QHBoxLayout()
        self.horizontalLayout_output.setObjectName(u"horizontalLayout_output")
        self.horizontalLayout_output.setSizeConstraint(QLayout.SetNoConstraint)
        self.sootpatternextract = QGroupBox(FirelocationPredict)
        self.sootpatternextract.setObjectName(u"sootpatternextract")
        self.verticalLayout_2 = QVBoxLayout(self.sootpatternextract)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_extractimage = QHBoxLayout()
        self.horizontalLayout_extractimage.setObjectName(u"horizontalLayout_extractimage")
        self.leftextractimage = PlotWidget(self.sootpatternextract)
        self.leftextractimage.setObjectName(u"leftextractimage")
        self.leftextractimage.setMinimumSize(QSize(400, 300))
        self.leftextractimage.setMaximumSize(QSize(400, 300))

        self.horizontalLayout_extractimage.addWidget(self.leftextractimage)

        self.centralextractimage = PlotWidget(self.sootpatternextract)
        self.centralextractimage.setObjectName(u"centralextractimage")
        self.centralextractimage.setMinimumSize(QSize(400, 300))
        self.centralextractimage.setMaximumSize(QSize(400, 300))

        self.horizontalLayout_extractimage.addWidget(self.centralextractimage)

        self.rightextractimage = PlotWidget(self.sootpatternextract)
        self.rightextractimage.setObjectName(u"rightextractimage")
        self.rightextractimage.setMinimumSize(QSize(400, 300))
        self.rightextractimage.setMaximumSize(QSize(400, 300))

        self.horizontalLayout_extractimage.addWidget(self.rightextractimage)


        self.verticalLayout_2.addLayout(self.horizontalLayout_extractimage)

        self.horizontalLayout_extractbutton = QHBoxLayout()
        self.horizontalLayout_extractbutton.setObjectName(u"horizontalLayout_extractbutton")
        self.extract_btn = QPushButton(self.sootpatternextract)
        self.extract_btn.setObjectName(u"extract_btn")
        self.extract_btn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_extractbutton.addWidget(self.extract_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_extractbutton)


        self.horizontalLayout_output.addWidget(self.sootpatternextract)

        self.firelocationpredict = QGroupBox(FirelocationPredict)
        self.firelocationpredict.setObjectName(u"firelocationpredict")
        self.firelocationpredict.setMaximumSize(QSize(600, 10000))
        self.verticalLayout_3 = QVBoxLayout(self.firelocationpredict)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_firelocationimage = QHBoxLayout()
        self.horizontalLayout_firelocationimage.setObjectName(u"horizontalLayout_firelocationimage")
        self.firelocationimage = PlotWidget(self.firelocationpredict)
        self.firelocationimage.setObjectName(u"firelocationimage")
        self.firelocationimage.setMaximumSize(QSize(500, 500))

        self.horizontalLayout_firelocationimage.addWidget(self.firelocationimage)


        self.verticalLayout_3.addLayout(self.horizontalLayout_firelocationimage)

        self.horizontalLayout_labellocation = QHBoxLayout()
        self.horizontalLayout_labellocation.setObjectName(u"horizontalLayout_labellocation")
        self.label_location = QLabel(self.firelocationpredict)
        self.label_location.setObjectName(u"label_location")
        self.label_location.setMaximumSize(QSize(300, 200))

        self.horizontalLayout_labellocation.addWidget(self.label_location)


        self.verticalLayout_3.addLayout(self.horizontalLayout_labellocation)

        self.horizontalLayout_predict = QHBoxLayout()
        self.horizontalLayout_predict.setObjectName(u"horizontalLayout_predict")
        self.predict_btn = QPushButton(self.firelocationpredict)
        self.predict_btn.setObjectName(u"predict_btn")
        self.predict_btn.setMaximumSize(QSize(150, 16777215))
        self.predict_btn.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_predict.addWidget(self.predict_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_predict)


        self.horizontalLayout_output.addWidget(self.firelocationpredict)


        self.verticalLayout_4.addLayout(self.horizontalLayout_output)


        self.retranslateUi(FirelocationPredict)

        QMetaObject.connectSlotsByName(FirelocationPredict)
    # setupUi

    def retranslateUi(self, FirelocationPredict):
        FirelocationPredict.setWindowTitle(QCoreApplication.translate("FirelocationPredict", u"\u57fa\u4e8e\u4eba\u5de5\u795e\u7ecf\u7f51\u7edc\u7684\u706b\u6e90\u5b9a\u4f4d\u8f6f\u4ef6", None))
        self.imageinput.setTitle(QCoreApplication.translate("FirelocationPredict", u"\u56fe\u7247\u8f93\u5165", None))
        self.leftimage.setText(QCoreApplication.translate("FirelocationPredict", u"\u8bf7\u9009\u62e9\u56fe\u7247", None))
        self.leftselect.setText(QCoreApplication.translate("FirelocationPredict", u"\u9009\u62e9\u5de6\u5899\u56fe\u7247", None))
        self.leftcancel.setText(QCoreApplication.translate("FirelocationPredict", u"\u6e05\u7a7a", None))
        self.centralimage.setText(QCoreApplication.translate("FirelocationPredict", u"\u8bf7\u9009\u62e9\u56fe\u7247", None))
        self.centralselect.setText(QCoreApplication.translate("FirelocationPredict", u"\u9009\u62e9\u4e2d\u5899\u56fe\u7247", None))
        self.centralcancel.setText(QCoreApplication.translate("FirelocationPredict", u"\u6e05\u7a7a", None))
        self.rightimage.setText(QCoreApplication.translate("FirelocationPredict", u"\u8bf7\u9009\u62e9\u56fe\u7247", None))
        self.rightselect.setText(QCoreApplication.translate("FirelocationPredict", u"\u9009\u62e9\u53f3\u5899\u56fe\u7247", None))
        self.rightcancel.setText(QCoreApplication.translate("FirelocationPredict", u"\u6e05\u7a7a", None))
        self.verticalLayout_operatelog.setTitle(QCoreApplication.translate("FirelocationPredict", u"\u64cd\u4f5c\u8bb0\u5f55", None))
        self.cleanlog_btn.setText(QCoreApplication.translate("FirelocationPredict", u"\u6e05\u7a7a", None))
        self.sootpatternextract.setTitle(QCoreApplication.translate("FirelocationPredict", u"\u70df\u96fe\u8f6e\u5ed3\u63d0\u53d6", None))
        self.extract_btn.setText(QCoreApplication.translate("FirelocationPredict", u"\u63d0\u53d6", None))
        self.firelocationpredict.setTitle(QCoreApplication.translate("FirelocationPredict", u"\u706b\u6e90\u4f4d\u7f6e\u9884\u6d4b", None))
        self.label_location.setText(QCoreApplication.translate("FirelocationPredict", u"\u5750\u6807\uff1a", None))
        self.predict_btn.setText(QCoreApplication.translate("FirelocationPredict", u"\u9884\u6d4b", None))
    # retranslateUi

