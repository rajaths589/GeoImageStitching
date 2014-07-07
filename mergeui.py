# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mergeUI.ui'
#
# Created: Tue Jul  8 01:51:29 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(673, 408)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 521, 231))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 10, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.img1 = QtGui.QLineEdit(self.frame)
        self.img1.setGeometry(QtCore.QRect(10, 80, 381, 27))
        self.img1.setObjectName(_fromUtf8("img1"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.img2 = QtGui.QLineEdit(self.frame)
        self.img2.setGeometry(QtCore.QRect(10, 170, 381, 27))
        self.img2.setObjectName(_fromUtf8("img2"))
        self.imgbtn1 = QtGui.QPushButton(self.frame)
        self.imgbtn1.setGeometry(QtCore.QRect(410, 80, 98, 27))
        self.imgbtn1.setObjectName(_fromUtf8("imgbtn1"))
        self.imgbtn2 = QtGui.QPushButton(self.frame)
        self.imgbtn2.setGeometry(QtCore.QRect(410, 170, 98, 27))
        self.imgbtn2.setObjectName(_fromUtf8("imgbtn2"))
        self.status = QtGui.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(0, 350, 541, 17))
        self.status.setObjectName(_fromUtf8("status"))
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 260, 521, 80))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(220, 10, 101, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.output = QtGui.QLineEdit(self.frame_2)
        self.output.setGeometry(QtCore.QRect(10, 40, 381, 27))
        self.output.setObjectName(_fromUtf8("output"))
        self.btnoutput = QtGui.QPushButton(self.frame_2)
        self.btnoutput.setGeometry(QtCore.QRect(410, 40, 98, 27))
        self.btnoutput.setObjectName(_fromUtf8("btnoutput"))
        self.merge = QtGui.QPushButton(Dialog)
        self.merge.setGeometry(QtCore.QRect(550, 50, 98, 27))
        self.merge.setObjectName(_fromUtf8("merge"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(550, 20, 66, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(550, 100, 66, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.selectImage = QtGui.QRadioButton(Dialog)
        self.selectImage.setGeometry(QtCore.QRect(550, 120, 116, 31))
        self.selectImage.setObjectName(_fromUtf8("selectImage"))
        self.translateX = QtGui.QSpinBox(Dialog)
        self.translateX.setGeometry(QtCore.QRect(550, 160, 60, 27))
        self.translateX.setMinimum(-10)
        self.translateX.setMaximum(10)
        self.translateX.setObjectName(_fromUtf8("translateX"))
        self.translateY = QtGui.QSpinBox(Dialog)
        self.translateY.setGeometry(QtCore.QRect(550, 200, 60, 27))
        self.translateY.setMinimum(-10)
        self.translateY.setMaximum(10)
        self.translateY.setObjectName(_fromUtf8("translateY"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(620, 164, 66, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(620, 203, 66, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.translate = QtGui.QPushButton(Dialog)
        self.translate.setGeometry(QtCore.QRect(550, 240, 98, 27))
        self.translate.setObjectName(_fromUtf8("translate"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(550, 280, 66, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.remerge = QtGui.QPushButton(Dialog)
        self.remerge.setGeometry(QtCore.QRect(550, 300, 98, 27))
        self.remerge.setObjectName(_fromUtf8("remerge"))
        self.cancel = QtGui.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(430, 370, 98, 27))
        self.cancel.setObjectName(_fromUtf8("cancel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Semi-Automatic Satellite Image Mosaicing", None))
        self.label.setText(_translate("Dialog", "Input Images", None))
        self.label_2.setText(_translate("Dialog", "Image 1", None))
        self.label_3.setText(_translate("Dialog", "Image 2", None))
        self.imgbtn1.setText(_translate("Dialog", "Select", None))
        self.imgbtn2.setText(_translate("Dialog", "Select", None))
        self.status.setText(_translate("Dialog", "Status:", None))
        self.label_5.setText(_translate("Dialog", "Output Image", None))
        self.btnoutput.setText(_translate("Dialog", "Select", None))
        self.merge.setText(_translate("Dialog", "Merge", None))
        self.label_6.setText(_translate("Dialog", "Step 1", None))
        self.label_7.setText(_translate("Dialog", "Step 2", None))
        self.selectImage.setText(_translate("Dialog", "Image1", None))
        self.label_8.setText(_translate("Dialog", "X", None))
        self.label_9.setText(_translate("Dialog", "Y", None))
        self.translate.setText(_translate("Dialog", "Translate", None))
        self.label_10.setText(_translate("Dialog", "Step 3", None))
        self.remerge.setText(_translate("Dialog", "Re-Merge", None))
        self.cancel.setText(_translate("Dialog", "Cancel", None))

