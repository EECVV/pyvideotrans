# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'videoandsrt.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import (QMetaObject, Qt)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QHBoxLayout, QLabel)

from videotrans.configure import config


class Ui_videoandsrt(object):
    def setupUi(self, videoandsrt):
        if not videoandsrt.objectName():
            videoandsrt.setObjectName(u"videoandsrt")
        videoandsrt.resize(700, 400)
        videoandsrt.setWindowModality(QtCore.Qt.NonModal)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(videoandsrt.sizePolicy().hasHeightForWidth())
        videoandsrt.setSizePolicy(sizePolicy)

        self.horizontalLayout_3 = QHBoxLayout(videoandsrt)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        # start
        self.v3 = QtWidgets.QVBoxLayout()
        self.v3.setObjectName("v3")

        # h3
        self.h3 = QtWidgets.QHBoxLayout()
        self.h3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(100, 40))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.h3.addWidget(self.label_4, 0, QtCore.Qt.AlignTop)

        self.folder = QtWidgets.QLineEdit()
        self.folder.setMinimumSize(QtCore.QSize(0, 40))
        self.folder.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.folder.setReadOnly(True)
        self.folder.setObjectName("folder")
        self.h3.addWidget(self.folder, 0, QtCore.Qt.AlignTop)

        self.folder_btn = QtWidgets.QPushButton()
        self.folder_btn.setMinimumSize(QtCore.QSize(150, 40))
        self.folder_btn.setObjectName("folder_btn")
        self.h3.addWidget(self.folder_btn, 0, QtCore.Qt.AlignTop)

        # v3 add h3
        self.v3.addLayout(self.h3)

        self.labeltips = QLabel()
        self.v3.addWidget(self.labeltips)

        # h6
        self.h7 = QtWidgets.QHBoxLayout()
        self.h7.setObjectName("h7")

        self.maxlenlabel = QtWidgets.QLabel()
        self.maxlenlabel.setText("硬字幕单行字符数")
        self.maxlen = QtWidgets.QLineEdit()
        self.maxlen.setText('30')

        self.layout_form0 = QtWidgets.QFormLayout()
        self.layout_form0.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.maxlenlabel)
        self.layout_form0.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.maxlen)

        self.issoft = QtWidgets.QCheckBox()
        self.issoft.setObjectName("issoft")
        self.issoft.setChecked(False)
        self.issoft.setText('嵌入软字幕' if config.defaulelang == 'zh' else 'Embedded Soft Subtitles')

        self.layout_form = QtWidgets.QFormLayout()

        self.languagelabel = QtWidgets.QLabel()
        self.languagelabel.setText('软字幕语言' if config.defaulelang == 'zh' else 'soft subtitle language')
        self.languagelabel.setStyleSheet('color:#777')
        self.language = QtWidgets.QComboBox()
        self.language.setMinimumSize(QtCore.QSize(0, 30))
        self.language.setObjectName("language")
        self.language.addItems(config.langnamelist)
        self.language.setDisabled(True)
        self.issoft.toggled.connect(self.update_language)

        self.layout_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.languagelabel)
        self.layout_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.language)

        self.h7.addLayout(self.layout_form0)
        self.h7.addStretch()
        self.h7.addWidget(self.issoft)
        self.h7.addLayout(self.layout_form)

        self.v3.addLayout(self.h7)

        self.startbtn = QtWidgets.QPushButton()
        self.startbtn.setMinimumSize(QtCore.QSize(250, 40))
        self.startbtn.setObjectName("startbtn")
        self.startbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.v3.addWidget(self.startbtn)

        self.loglabel = QLabel()
        self.v3.addWidget(self.loglabel)
        self.v3.addStretch()

        self.h8 = QtWidgets.QHBoxLayout()
        self.h8.setObjectName("horizontalLayout_20")
        self.opendir = QtWidgets.QPushButton()
        self.opendir.setMinimumSize(QtCore.QSize(0, 30))
        self.opendir.setStyleSheet("""background-color:transparent""")
        self.opendir.setObjectName("opendir")
        self.opendir.setCursor(QCursor(Qt.PointingHandCursor))
        self.h8.addWidget(self.opendir)
        self.v3.addLayout(self.h8)

        # end
        self.horizontalLayout_3.addLayout(self.v3)

        self.retranslateUi(videoandsrt)

        QMetaObject.connectSlotsByName(videoandsrt)

    def update_language(self, state):
        self.languagelabel.setStyleSheet(f"""color:#f1f1f1""" if state else 'color:#777777')
        self.language.setDisabled(False if state else True)

    def retranslateUi(self, videoandsrt):
        videoandsrt.setWindowTitle("批量视频和srt字幕合并" if config.defaulelang == 'zh' else 'Batch video subtitle merger')

        self.labeltips.setText(
            "将把所选文件夹内同名的视频和srt字幕进行合并，例如 1.mp4 和 1.srt" if config.defaulelang == 'zh' else 'Will merge video and srt subtitles with the same name in that folder, e.g. 1.mp4 and 1.srt')

        self.label_4.setText('视频和字幕文件夹' if config.defaulelang == 'zh' else 'Video and subtitle folders')
        self.folder_btn.setText('选择文件夹' if config.defaulelang == 'zh' else 'Select folder')
        self.folder.setPlaceholderText(
            '选择同名视频和字幕所在文件夹' if config.defaulelang == 'zh' else 'Select the folder where the video and subtitles of the same name are located')
        self.startbtn.setText('开始执行' if config.defaulelang == 'zh' else 'Start operating')
        self.opendir.setText('打开结果目录' if config.defaulelang == 'zh' else 'Open the results catalog')
