# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\lib\modules\imagerTemplate.ui'
#
# Created: Wed Jun 05 10:43:58 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(182, 246)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 4, 177, 258))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.width = QtGui.QLabel(self.layoutWidget)
        self.width.setObjectName(_fromUtf8("width"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.width)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.height = QtGui.QLabel(self.layoutWidget)
        self.height.setObjectName(_fromUtf8("height"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.height)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.xpos = QtGui.QLabel(self.layoutWidget)
        self.xpos.setObjectName(_fromUtf8("xpos"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.xpos)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.ypos = QtGui.QLabel(self.layoutWidget)
        self.ypos.setObjectName(_fromUtf8("ypos"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.ypos)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_11)
        self.pixelSize = QtGui.QLabel(self.layoutWidget)
        self.pixelSize.setObjectName(_fromUtf8("pixelSize"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.pixelSize)
        self.snap_Button = QtGui.QPushButton(self.layoutWidget)
        self.snap_Button.setObjectName(_fromUtf8("snap_Button"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.snap_Button)
        self.video_button = QtGui.QPushButton(self.layoutWidget)
        self.video_button.setCheckable(True)
        self.video_button.setObjectName(_fromUtf8("video_button"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.video_button)
        self.run_Button = QtGui.QPushButton(self.layoutWidget)
        self.run_Button.setObjectName(_fromUtf8("run_Button"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.run_Button)
        self.record_button = QtGui.QPushButton(self.layoutWidget)
        self.record_button.setCheckable(True)
        self.record_button.setObjectName(_fromUtf8("record_button"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.record_button)
        self.stop_button = QtGui.QPushButton(self.layoutWidget)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.stop_button)
        self.cameraSnapBtn = QtGui.QPushButton(self.layoutWidget)
        self.cameraSnapBtn.setObjectName(_fromUtf8("cameraSnapBtn"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.cameraSnapBtn)
        self.hide_check = QtGui.QCheckBox(self.layoutWidget)
        self.hide_check.setObjectName(_fromUtf8("hide_check"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.hide_check)
        self.alphaSlider = QtGui.QSlider(self.layoutWidget)
        self.alphaSlider.setMaximum(100)
        self.alphaSlider.setSingleStep(2)
        self.alphaSlider.setProperty("value", 50)
        self.alphaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.alphaSlider.setInvertedControls(True)
        self.alphaSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.alphaSlider.setObjectName(_fromUtf8("alphaSlider"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.alphaSlider)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_2)
        self.restoreROI = QtGui.QPushButton(self.layoutWidget)
        self.restoreROI.setObjectName(_fromUtf8("restoreROI"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.restoreROI)
        self.saveROI = QtGui.QPushButton(self.layoutWidget)
        self.saveROI.setObjectName(_fromUtf8("saveROI"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.saveROI)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Width (um)", None, QtGui.QApplication.UnicodeUTF8))
        self.width.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Height (um)", None, QtGui.QApplication.UnicodeUTF8))
        self.height.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Xpos (um)", None, QtGui.QApplication.UnicodeUTF8))
        self.xpos.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Ypos (um)", None, QtGui.QApplication.UnicodeUTF8))
        self.ypos.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "Pixel Size (um)", None, QtGui.QApplication.UnicodeUTF8))
        self.pixelSize.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.snap_Button.setText(QtGui.QApplication.translate("Form", "Snap", None, QtGui.QApplication.UnicodeUTF8))
        self.video_button.setText(QtGui.QApplication.translate("Form", "Video", None, QtGui.QApplication.UnicodeUTF8))
        self.run_Button.setText(QtGui.QApplication.translate("Form", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.record_button.setText(QtGui.QApplication.translate("Form", "Record Stack", None, QtGui.QApplication.UnicodeUTF8))
        self.stop_button.setText(QtGui.QApplication.translate("Form", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.cameraSnapBtn.setText(QtGui.QApplication.translate("Form", "Camera Snap", None, QtGui.QApplication.UnicodeUTF8))
        self.hide_check.setText(QtGui.QApplication.translate("Form", "Hide Overlay", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreROI.setText(QtGui.QApplication.translate("Form", "Restore ROI", None, QtGui.QApplication.UnicodeUTF8))
        self.saveROI.setText(QtGui.QApplication.translate("Form", "Save ROI", None, QtGui.QApplication.UnicodeUTF8))

