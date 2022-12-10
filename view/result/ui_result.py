# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Result(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        Form.setMinimumSize(QtCore.QSize(1200, 800))
        Form.setMaximumSize(QtCore.QSize(1200, 800))
        Form.setStyleSheet("background-image: url(view/assets/Background.png)")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1202, 814))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 17, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget.setMinimumSize(QtCore.QSize(1200, 800))
        self.widget.setMaximumSize(QtCore.QSize(1200, 800))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.tvTitle = QtWidgets.QLabel(self.widget)
        self.tvTitle.setGeometry(QtCore.QRect(120, 30, 1001, 61))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(54)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tvTitle.setFont(font)
        self.tvTitle.setStyleSheet("color: #ffffff;\n"
                                   "background: transparent;")
        self.tvTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.tvTitle.setObjectName("tvTitle")
        self.btnRepeat = QtWidgets.QPushButton(self.widget)
        self.btnRepeat.setGeometry(QtCore.QRect(750, 590, 131, 51))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnRepeat.setFont(font)
        self.btnRepeat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRepeat.setStyleSheet("* {\n"
                                     "    background: #686DE0;\n"
                                     "    border-radius: 24px;\n"
                                     "    color: #FFFFFF;\n"
                                     "    padding: 12px;\n"
                                     "}\n"
                                     "\n"
                                     "*:hover {\n"
                                     "    background: #6350E8;\n"
                                     "}")
        self.btnRepeat.setObjectName("btnRepeat")
        self.tvDescription = QtWidgets.QLabel(self.widget)
        self.tvDescription.setGeometry(QtCore.QRect(740, 190, 421, 71))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tvDescription.setFont(font)
        self.tvDescription.setStyleSheet("color: #ffffff;\n"
                                         "background: transparent;")
        self.tvDescription.setObjectName("tvDescription")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(720, 290, 361, 261))
        self.listWidget.setStyleSheet("background: white;\n"
                                      "border-radius: 24px")
        self.listWidget.setObjectName("listWidget")
        self.tvIdeal = QtWidgets.QLabel(self.widget)
        self.tvIdeal.setGeometry(QtCore.QRect(740, 310, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tvIdeal.setFont(font)
        self.tvIdeal.setStyleSheet("background: white")
        self.tvIdeal.setObjectName("tvIdeal")
        self.tvBMI = QtWidgets.QLabel(self.widget)
        self.tvBMI.setGeometry(QtCore.QRect(150, 190, 331, 61))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(38)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tvBMI.setFont(font)
        self.tvBMI.setStyleSheet("color: #ffffff;\n"
                                 "background: transparent;")
        self.tvBMI.setAlignment(QtCore.Qt.AlignCenter)
        self.tvBMI.setObjectName("tvBMI")
        self.tvResult = QtWidgets.QLabel(self.widget)
        self.tvResult.setGeometry(QtCore.QRect(140, 540, 361, 51))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tvResult.setFont(font)
        self.tvResult.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tvResult.setStyleSheet("color: #ffffff;\n"
                                    "background: transparent;")
        self.tvResult.setAlignment(QtCore.Qt.AlignCenter)
        self.tvResult.setObjectName("tvResult")
        self.btnClose = QtWidgets.QPushButton(self.widget)
        self.btnClose.setGeometry(QtCore.QRect(920, 590, 131, 51))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnClose.setFont(font)
        self.btnClose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClose.setStyleSheet("* {\n"
                                    "    background: #4834D4;\n"
                                    "    border-radius: 24;\n"
                                    "    color: #FFFFFF;\n"
                                    "    padding: 12px;\n"
                                    "}\n"
                                    "\n"
                                    "*:hover {\n"
                                    "    background: #372CAE;\n"
                                    "}")
        self.btnClose.setObjectName("btnClose")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(200, 280, 231, 231))
        self.widget_2.setStyleSheet("background: white;\n"
                                    "border-radius: 110%;\n"
                                    "border: 8px solid #4834D4;")
        self.widget_2.setObjectName("widget_2")
        self.tvCount = QtWidgets.QLabel(self.widget_2)
        self.tvCount.setGeometry(QtCore.QRect(20, 90, 191, 51))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.tvCount.setFont(font)
        self.tvCount.setStyleSheet("background: white;\n"
                                   "border: none")
        self.tvCount.setAlignment(QtCore.Qt.AlignCenter)
        self.tvCount.setObjectName("tvCount")
        self.tvTips = QtWidgets.QTextBrowser(self.widget)
        self.tvTips.setGeometry(QtCore.QRect(720, 350, 361, 192))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tvTips.setFont(font)
        self.tvTips.setStyleSheet("background: white;\n"
                                  "padding: 16px;\n"
                                  "border-radius: 24px")
        self.tvTips.setObjectName("tvTips")
        self.gridLayout_2.addWidget(self.widget, 16, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bobotin - Hasil"))
        self.tvTitle.setText(_translate("Form", "HASIL"))
        self.btnRepeat.setToolTip(_translate("Form",
                                             "<html><head/><body><p><span style=\" font-weight:400;\">Ulangi Program</span></p></body></html>"))
        self.btnRepeat.setText(_translate("Form", "ULANG"))
        self.tvDescription.setText(_translate("Form", "Keterangan"))
        self.tvIdeal.setText(_translate("Form", "Lorem Ipsum"))
        self.tvBMI.setText(_translate("Form", "BMI"))
        self.tvResult.setText(_translate("Form", "Lorem Ipsum"))
        self.btnClose.setToolTip(_translate("Form", "<html><head/><body><p>Tutup Program</p></body></html>"))
        self.btnClose.setText(_translate("Form", "TUTUP"))
        self.tvCount.setText(_translate("Form", "68"))
        self.tvTips.setHtml(_translate("Form",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                       "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lorem ipsum dolor sit amet</p></body></html>"))
