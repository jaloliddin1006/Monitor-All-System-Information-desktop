# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_interfaceaVQCdw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.SpiralProgressBar import spiralProgressBar
from PySide2extn.RoundProgressBar import roundProgressBar

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(649, 459)
        MainWindow.setStyleSheet(u"\n"
"*{\n"
"	color: rgb(255, 255, 255);\n"
"border: none;\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(82, 88, 105);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.open_close_side_bar_btn = QPushButton(self.header_left_frame)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        font = QFont()
        font.setFamily(u"Rockwell")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.open_close_side_bar_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/outline_format_align_left_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar_btn, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setPixmap(QPixmap(u":/icons/icons/outline_airplay_white_24dp.png"))

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)

        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setStyleSheet(u"")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.header_right_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/outline_minimize_white_24dp2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)
        self.minimize_window_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/outline_cached_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/outline_close_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setStyleSheet(u"background-color: rgb(47, 47, 47);")
        self.main_body_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.left_menu_cont_frame = QFrame(self.main_body_frame)
        self.left_menu_cont_frame.setObjectName(u"left_menu_cont_frame")
        self.left_menu_cont_frame.setMinimumSize(QSize(40, 0))
        self.left_menu_cont_frame.setMaximumSize(QSize(20, 16777215))
        self.left_menu_cont_frame.setStyleSheet(u"background-color: rgb(82, 88, 105);\n"
"color: rgb(255, 255, 255);")
        self.left_menu_cont_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.left_menu_cont_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_cont_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy1)
        self.menu_frame.setMinimumSize(QSize(100, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.system_info_page_btn = QPushButton(self.menu_frame)
        self.system_info_page_btn.setObjectName(u"system_info_page_btn")
        font3 = QFont()
        font3.setPointSize(13)
        self.system_info_page_btn.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/outline_airplay_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.system_info_page_btn.setIcon(icon4)
        self.system_info_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.system_info_page_btn, 2, 1, 1, 1, Qt.AlignLeft)

        self.sensors_page_btn = QPushButton(self.menu_frame)
        self.sensors_page_btn.setObjectName(u"sensors_page_btn")
        self.sensors_page_btn.setFont(font3)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/outline_thermostat_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sensors_page_btn.setIcon(icon5)
        self.sensors_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.sensors_page_btn, 5, 1, 1, 1, Qt.AlignLeft)

        self.cpu_page_btn = QPushButton(self.menu_frame)
        self.cpu_page_btn.setObjectName(u"cpu_page_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/outline_memory_white_24dp2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_page_btn.setIcon(icon6)
        self.cpu_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.cpu_page_btn, 0, 1, 1, 1, Qt.AlignLeft)

        self.batery_page_btn = QPushButton(self.menu_frame)
        self.batery_page_btn.setObjectName(u"batery_page_btn")
        self.batery_page_btn.setFont(font3)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/outline_bolt_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.batery_page_btn.setIcon(icon7)
        self.batery_page_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.batery_page_btn, 1, 1, 1, 1, Qt.AlignLeft)

        self.storage_btn = QPushButton(self.menu_frame)
        self.storage_btn.setObjectName(u"storage_btn")
        self.storage_btn.setFont(font3)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/outline_adjust_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_btn.setIcon(icon8)
        self.storage_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.storage_btn, 4, 1, 1, 1, Qt.AlignLeft)

        self.activity_btn = QPushButton(self.menu_frame)
        self.activity_btn.setObjectName(u"activity_btn")
        self.activity_btn.setFont(font3)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/outline_auto_graph_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_btn.setIcon(icon9)
        self.activity_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.activity_btn, 3, 1, 1, 1, Qt.AlignLeft)

        self.networks_page_button = QPushButton(self.menu_frame)
        self.networks_page_button.setObjectName(u"networks_page_button")
        self.networks_page_button.setFont(font3)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/outline_wifi_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.networks_page_button.setIcon(icon10)
        self.networks_page_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.networks_page_button, 6, 1, 1, 1, Qt.AlignLeft)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setMargin(5)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1, Qt.AlignLeft)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setMargin(5)

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1, Qt.AlignLeft)

        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setMargin(5)

        self.gridLayout.addWidget(self.label_7, 3, 2, 1, 1, Qt.AlignLeft)

        self.label_8 = QLabel(self.menu_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setMargin(5)

        self.gridLayout.addWidget(self.label_8, 4, 2, 1, 1, Qt.AlignLeft)

        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setMargin(5)

        self.gridLayout.addWidget(self.label_9, 5, 2, 1, 1, Qt.AlignLeft)

        self.label_10 = QLabel(self.menu_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setMargin(5)

        self.gridLayout.addWidget(self.label_10, 6, 2, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_8.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.left_menu_cont_frame)

        self.main_body_contents = QFrame(self.main_body_frame)
        self.main_body_contents.setObjectName(u"main_body_contents")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"color: rgb(203, 203, 203);")
        self.cpu_and_memory = QWidget()
        self.cpu_and_memory.setObjectName(u"cpu_and_memory")
        self.verticalLayout_8 = QVBoxLayout(self.cpu_and_memory)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cpu_info_frame = QFrame(self.cpu_and_memory)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        font4 = QFont()
        font4.setPointSize(9)
        self.cpu_info_frame.setFont(font4)
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.cpu_info_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_15 = QLabel(self.cpu_info_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)

        self.cpu_per = QLabel(self.cpu_info_frame)
        self.cpu_per.setObjectName(u"cpu_per")
        self.cpu_per.setFont(font1)

        self.gridLayout_5.addWidget(self.cpu_per, 1, 1, 1, 1)

        self.label_34 = QLabel(self.cpu_info_frame)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)

        self.gridLayout_5.addWidget(self.label_34, 1, 0, 1, 1)

        self.cpu_main_core = QLabel(self.cpu_info_frame)
        self.cpu_main_core.setObjectName(u"cpu_main_core")
        self.cpu_main_core.setFont(font1)

        self.gridLayout_5.addWidget(self.cpu_main_core, 2, 1, 1, 1)

        self.label_36 = QLabel(self.cpu_info_frame)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font1)

        self.gridLayout_5.addWidget(self.label_36, 2, 0, 1, 1)

        self.cpu_count = QLabel(self.cpu_info_frame)
        self.cpu_count.setObjectName(u"cpu_count")
        self.cpu_count.setFont(font1)

        self.gridLayout_5.addWidget(self.cpu_count, 0, 1, 1, 1)

        self.cpu_percentage = roundProgressBar(self.cpu_info_frame)
        self.cpu_percentage.setObjectName(u"cpu_percentage")
        self.cpu_percentage.setMinimumSize(QSize(150, 150))
        self.cpu_percentage.setMaximumSize(QSize(150, 150))

        self.gridLayout_5.addWidget(self.cpu_percentage, 0, 2, 3, 1)


        self.verticalLayout_8.addWidget(self.cpu_info_frame)

        self.ram_info_frame = QFrame(self.cpu_and_memory)
        self.ram_info_frame.setObjectName(u"ram_info_frame")
        self.ram_info_frame.setFont(font1)
        self.ram_info_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.ram_info_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.used_ram = QLabel(self.ram_info_frame)
        self.used_ram.setObjectName(u"used_ram")

        self.gridLayout_6.addWidget(self.used_ram, 2, 1, 1, 1)

        self.total_ram = QLabel(self.ram_info_frame)
        self.total_ram.setObjectName(u"total_ram")

        self.gridLayout_6.addWidget(self.total_ram, 0, 1, 1, 1)

        self.label_40 = QLabel(self.ram_info_frame)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_6.addWidget(self.label_40, 1, 0, 1, 1)

        self.ram_usage = QLabel(self.ram_info_frame)
        self.ram_usage.setObjectName(u"ram_usage")

        self.gridLayout_6.addWidget(self.ram_usage, 4, 1, 1, 1)

        self.free_ram = QLabel(self.ram_info_frame)
        self.free_ram.setObjectName(u"free_ram")

        self.gridLayout_6.addWidget(self.free_ram, 3, 1, 1, 1)

        self.label_38 = QLabel(self.ram_info_frame)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_6.addWidget(self.label_38, 0, 0, 1, 1)

        self.label_44 = QLabel(self.ram_info_frame)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_6.addWidget(self.label_44, 3, 0, 1, 1)

        self.label_42 = QLabel(self.ram_info_frame)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_6.addWidget(self.label_42, 2, 0, 1, 1)

        self.aviable_ram = QLabel(self.ram_info_frame)
        self.aviable_ram.setObjectName(u"aviable_ram")

        self.gridLayout_6.addWidget(self.aviable_ram, 1, 1, 1, 1)

        self.label_46 = QLabel(self.ram_info_frame)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_6.addWidget(self.label_46, 4, 0, 1, 1)

        self.ram_percantage = spiralProgressBar(self.ram_info_frame)
        self.ram_percantage.setObjectName(u"ram_percantage")
        self.ram_percantage.setMinimumSize(QSize(150, 150))
        self.ram_percantage.setMaximumSize(QSize(150, 150))

        self.gridLayout_6.addWidget(self.ram_percantage, 0, 2, 5, 1)


        self.verticalLayout_8.addWidget(self.ram_info_frame)

        self.stackedWidget.addWidget(self.cpu_and_memory)
        self.battery = QWidget()
        self.battery.setObjectName(u"battery")
        self.battery.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"")
        self.verticalLayout_9 = QVBoxLayout(self.battery)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_48 = QLabel(self.battery)
        self.label_48.setObjectName(u"label_48")
        font5 = QFont()
        font5.setFamily(u"Mongolian Baiti")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_48.setFont(font5)

        self.verticalLayout_9.addWidget(self.label_48, 0, Qt.AlignBottom)

        self.frame_4 = QFrame(self.battery)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font1)

        self.gridLayout_7.addWidget(self.label_50, 1, 0, 1, 1)

        self.battery_status = QLabel(self.frame_4)
        self.battery_status.setObjectName(u"battery_status")
        self.battery_status.setFont(font1)

        self.gridLayout_7.addWidget(self.battery_status, 0, 1, 1, 1)

        self.battery_plugged = QLabel(self.frame_4)
        self.battery_plugged.setObjectName(u"battery_plugged")
        self.battery_plugged.setFont(font1)

        self.gridLayout_7.addWidget(self.battery_plugged, 3, 1, 1, 1)

        self.label_51 = QLabel(self.frame_4)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font1)

        self.gridLayout_7.addWidget(self.label_51, 2, 0, 1, 1)

        self.battery_charge = QLabel(self.frame_4)
        self.battery_charge.setObjectName(u"battery_charge")
        self.battery_charge.setFont(font1)

        self.gridLayout_7.addWidget(self.battery_charge, 1, 1, 1, 1)

        self.label_49 = QLabel(self.frame_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font1)

        self.gridLayout_7.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_52 = QLabel(self.frame_4)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font1)

        self.gridLayout_7.addWidget(self.label_52, 3, 0, 1, 1)

        self.battery_time_left = QLabel(self.frame_4)
        self.battery_time_left.setObjectName(u"battery_time_left")
        self.battery_time_left.setFont(font1)

        self.gridLayout_7.addWidget(self.battery_time_left, 2, 1, 1, 1)

        self.battery_usage = roundProgressBar(self.frame_4)
        self.battery_usage.setObjectName(u"battery_usage")
        self.battery_usage.setMinimumSize(QSize(150, 150))
        self.battery_usage.setMaximumSize(QSize(150, 150))

        self.gridLayout_7.addWidget(self.battery_usage, 0, 2, 4, 1)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.battery)
        self.system_information = QWidget()
        self.system_information.setObjectName(u"system_information")
        self.verticalLayout_10 = QVBoxLayout(self.system_information)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame = QFrame(self.system_information)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_60 = QLabel(self.frame)
        self.label_60.setObjectName(u"label_60")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_60.setFont(font6)

        self.gridLayout_8.addWidget(self.label_60, 3, 0, 1, 1)

        self.system_platform = QLabel(self.frame)
        self.system_platform.setObjectName(u"system_platform")
        self.system_platform.setFont(font1)

        self.gridLayout_8.addWidget(self.system_platform, 2, 1, 1, 1)

        self.system_sytem = QLabel(self.frame)
        self.system_sytem.setObjectName(u"system_sytem")
        self.system_sytem.setFont(font6)

        self.gridLayout_8.addWidget(self.system_sytem, 1, 0, 1, 1, Qt.AlignTop)

        self.label_61 = QLabel(self.frame)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font6)

        self.gridLayout_8.addWidget(self.label_61, 4, 0, 1, 1)

        self.system_date = QLabel(self.frame)
        self.system_date.setObjectName(u"system_date")
        self.system_date.setFont(font1)

        self.gridLayout_8.addWidget(self.system_date, 4, 1, 1, 1)

        self.label_67 = QLabel(self.frame)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font6)

        self.gridLayout_8.addWidget(self.label_67, 4, 2, 1, 1)

        self.label_65 = QLabel(self.frame)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font6)

        self.gridLayout_8.addWidget(self.label_65, 2, 2, 1, 1)

        self.label_57 = QLabel(self.frame)
        self.label_57.setObjectName(u"label_57")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_57.setFont(font7)

        self.gridLayout_8.addWidget(self.label_57, 0, 0, 1, 1, Qt.AlignTop)

        self.label_66 = QLabel(self.frame)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font6)

        self.gridLayout_8.addWidget(self.label_66, 3, 2, 1, 1)

        self.system_version = QLabel(self.frame)
        self.system_version.setObjectName(u"system_version")
        self.system_version.setFont(font1)

        self.gridLayout_8.addWidget(self.system_version, 3, 1, 1, 1)

        self.label_59 = QLabel(self.frame)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font6)

        self.gridLayout_8.addWidget(self.label_59, 2, 0, 1, 1)

        self.system_processor = QLabel(self.frame)
        self.system_processor.setObjectName(u"system_processor")
        self.system_processor.setFont(font1)

        self.gridLayout_8.addWidget(self.system_processor, 2, 3, 1, 1)

        self.system_machine = QLabel(self.frame)
        self.system_machine.setObjectName(u"system_machine")
        self.system_machine.setFont(font1)

        self.gridLayout_8.addWidget(self.system_machine, 3, 3, 1, 1)

        self.system_time = QLabel(self.frame)
        self.system_time.setObjectName(u"system_time")
        self.system_time.setFont(font1)

        self.gridLayout_8.addWidget(self.system_time, 4, 3, 1, 1)


        self.verticalLayout_10.addWidget(self.frame, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.system_information)
        self.activites = QWidget()
        self.activites.setObjectName(u"activites")
        self.verticalLayout_11 = QVBoxLayout(self.activites)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_2 = QFrame(self.activites)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFont(font1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_71 = QLabel(self.frame_2)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font6)

        self.horizontalLayout_9.addWidget(self.label_71)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.activity_search = QLineEdit(self.frame_6)
        self.activity_search.setObjectName(u"activity_search")
        self.activity_search.setFont(font1)

        self.horizontalLayout_10.addWidget(self.activity_search)

        self.pushButton_6 = QPushButton(self.frame_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/outline_search_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon11)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.pushButton_6)


        self.horizontalLayout_9.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.activites)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFont(font1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"background-color: rgb(48, 48, 48);")

        self.verticalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_11.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.activites)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFont(font1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font1)

        self.horizontalLayout_11.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font1)

        self.horizontalLayout_11.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font1)

        self.horizontalLayout_11.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font1)

        self.horizontalLayout_11.addWidget(self.pushButton_10)


        self.verticalLayout_11.addWidget(self.frame_5, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.activites)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.verticalLayout_13 = QVBoxLayout(self.storage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_72 = QLabel(self.storage)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font7)

        self.verticalLayout_13.addWidget(self.label_72)

        self.tableWidget_2 = QTableWidget(self.storage)
        if (self.tableWidget_2.columnCount() < 9):
            self.tableWidget_2.setColumnCount(9)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"color: rgb(0, 255, 30);")

        self.verticalLayout_13.addWidget(self.tableWidget_2)

        self.stackedWidget.addWidget(self.storage)
        self.sensors = QWidget()
        self.sensors.setObjectName(u"sensors")
        self.verticalLayout_14 = QVBoxLayout(self.sensors)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_73 = QLabel(self.sensors)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font7)

        self.verticalLayout_14.addWidget(self.label_73)

        self.tableWidget_3 = QTableWidget(self.sensors)
        if (self.tableWidget_3.columnCount() < 6):
            self.tableWidget_3.setColumnCount(6)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setFont(font1)
        self.tableWidget_3.setStyleSheet(u"color: rgb(0, 255, 0);")

        self.verticalLayout_14.addWidget(self.tableWidget_3)

        self.stackedWidget.addWidget(self.sensors)
        self.networks = QWidget()
        self.networks.setObjectName(u"networks")
        self.verticalLayout_7 = QVBoxLayout(self.networks)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea = QScrollArea(self.networks)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 192, 448))
        font8 = QFont()
        font8.setPointSize(8)
        self.scrollAreaWidgetContents.setFont(font8)
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_74 = QLabel(self.frame_7)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font7)

        self.verticalLayout_16.addWidget(self.label_74)

        self.tableWidget_4 = QTableWidget(self.frame_7)
        if (self.tableWidget_4.columnCount() < 5):
            self.tableWidget_4.setColumnCount(5)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setStyleSheet(u"color: rgb(0, 255, 0);")

        self.verticalLayout_16.addWidget(self.tableWidget_4)


        self.verticalLayout_15.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_75 = QLabel(self.frame_8)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font7)

        self.verticalLayout_17.addWidget(self.label_75)

        self.tableWidget_5 = QTableWidget(self.frame_8)
        if (self.tableWidget_5.columnCount() < 9):
            self.tableWidget_5.setColumnCount(9)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, __qtablewidgetitem36)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setStyleSheet(u"color: rgb(0, 255, 0);")

        self.verticalLayout_17.addWidget(self.tableWidget_5)


        self.verticalLayout_15.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_76 = QLabel(self.frame_9)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font7)

        self.verticalLayout_18.addWidget(self.label_76)

        self.tableWidget_6 = QTableWidget(self.frame_9)
        if (self.tableWidget_6.columnCount() < 6):
            self.tableWidget_6.setColumnCount(6)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem42)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setStyleSheet(u"color: rgb(0, 255, 0);")

        self.verticalLayout_18.addWidget(self.tableWidget_6)


        self.verticalLayout_15.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_77 = QLabel(self.frame_10)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font7)

        self.verticalLayout_19.addWidget(self.label_77)

        self.tableWidget_7 = QTableWidget(self.frame_10)
        if (self.tableWidget_7.columnCount() < 6):
            self.tableWidget_7.setColumnCount(6)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, __qtablewidgetitem48)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setStyleSheet(u"color: rgb(0, 255, 0);")

        self.verticalLayout_19.addWidget(self.tableWidget_7)


        self.verticalLayout_15.addWidget(self.frame_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.networks)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_7.addWidget(self.main_body_contents)

        self.right_frame = QFrame(self.main_body_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setStyleSheet(u"background-color: rgb(82, 88, 105);")
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.right_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.about_frame = QFrame(self.right_frame)
        self.about_frame.setObjectName(u"about_frame")
        self.about_frame.setFrameShape(QFrame.StyledPanel)
        self.about_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.about_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 0)
        self.about_top_frame = QFrame(self.about_frame)
        self.about_top_frame.setObjectName(u"about_top_frame")
        self.about_top_frame.setFrameShape(QFrame.StyledPanel)
        self.about_top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.about_top_frame)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 30, 0)
        self.label_11 = QLabel(self.about_top_frame)
        self.label_11.setObjectName(u"label_11")
        font9 = QFont()
        font9.setFamily(u"Mongolian Baiti")
        font9.setPointSize(16)
        self.label_11.setFont(font9)

        self.verticalLayout_5.addWidget(self.label_11, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_13 = QLabel(self.about_top_frame)
        self.label_13.setObjectName(u"label_13")
        font10 = QFont()
        font10.setFamily(u"Mongolian Baiti")
        font10.setPointSize(14)
        self.label_13.setFont(font10)
        self.label_13.setStyleSheet(u"color: rgb(204, 204, 204);")

        self.verticalLayout_5.addWidget(self.label_13, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.about_top_frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.about_main_frame = QFrame(self.about_frame)
        self.about_main_frame.setObjectName(u"about_main_frame")
        self.about_main_frame.setFrameShape(QFrame.StyledPanel)
        self.about_main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.about_main_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(50)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(20, 0, 50, 0)
        self.label_16 = QLabel(self.about_main_frame)
        self.label_16.setObjectName(u"label_16")
        font11 = QFont()
        font11.setFamily(u"Sakkal Majalla")
        font11.setPointSize(14)
        font11.setBold(True)
        font11.setUnderline(True)
        font11.setWeight(75)
        self.label_16.setFont(font11)

        self.gridLayout_2.addWidget(self.label_16, 2, 1, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.label_12 = QLabel(self.about_main_frame)
        self.label_12.setObjectName(u"label_12")
        font12 = QFont()
        font12.setFamily(u"Sakkal Majalla")
        font12.setPointSize(14)
        font12.setBold(True)
        font12.setItalic(False)
        font12.setUnderline(True)
        font12.setWeight(75)
        self.label_12.setFont(font12)

        self.gridLayout_2.addWidget(self.label_12, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.label_14 = QLabel(self.about_main_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font11)

        self.gridLayout_2.addWidget(self.label_14, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.pushButton_3 = QPushButton(self.about_main_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font13 = QFont()
        font13.setPointSize(12)
        self.pushButton_3.setFont(font13)
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/outline_subscriptions_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon12)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.pushButton_4 = QPushButton(self.about_main_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font13)
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/outline_local_cafe_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon13)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.pushButton_5 = QPushButton(self.about_main_frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font13)
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/outline_payment_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon14)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.pushButton_5, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.about_main_frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.about_grid = QFrame(self.about_frame)
        self.about_grid.setObjectName(u"about_grid")
        self.about_grid.setFrameShape(QFrame.StyledPanel)
        self.about_grid.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.about_grid, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.about_frame, 0, Qt.AlignLeft)


        self.horizontalLayout_7.addWidget(self.right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background-color: rgb(47, 47, 47);")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.footer_left_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.footer_right_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(self.footer_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setSizeIncrement(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)

        self.footer_right_frame.raise_()
        self.size_grip.raise_()
        self.footer_left_frame.raise_()

        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PSUTIL MANAGER", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.system_info_page_btn.setText("")
        self.sensors_page_btn.setText("")
        self.cpu_page_btn.setText("")
        self.batery_page_btn.setText("")
        self.storage_btn.setText("")
        self.activity_btn.setText("")
        self.networks_page_button.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CPU Count", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"CPU Per", None))
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Aviable RAM", None))
        self.ram_usage.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Total RAM", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Free RAM", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Used RAM", None))
        self.aviable_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"RAM Usage", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Plugget In", None))
        self.battery_time_left.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.system_platform.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_sytem.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"System Date", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.system_version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.system_processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_machine.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Activites", None))
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Processes", None))
        self.pushButton_6.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Process Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Process Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Suspend", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Resume", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kill", None));
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Disk Partition", None))
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Mount Point", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Max File", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Max Path", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Free Strorage", None));
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Sensor", None));
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Current", None));
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Critical", None));
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Duplex", None));
        ___qtablewidgetitem23 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem24 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Network IO Counter", None))
        ___qtablewidgetitem25 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"IO", None));
        ___qtablewidgetitem26 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Bytes Sent", None));
        ___qtablewidgetitem27 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Bytes Recevied", None));
        ___qtablewidgetitem28 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Packets Sent", None));
        ___qtablewidgetitem29 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Packets Recevied", None));
        ___qtablewidgetitem30 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"ERR In", None));
        ___qtablewidgetitem31 = self.tableWidget_5.horizontalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ERR Out", None));
        ___qtablewidgetitem32 = self.tableWidget_5.horizontalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Drop In", None));
        ___qtablewidgetitem33 = self.tableWidget_5.horizontalHeaderItem(8)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None));
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Network Addresses", None))
        ___qtablewidgetitem34 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem35 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem36 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Netmask", None));
        ___qtablewidgetitem37 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Broadcast", None));
        ___qtablewidgetitem38 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Network Connections", None))
        ___qtablewidgetitem39 = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"FD", None));
        ___qtablewidgetitem40 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem41 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem42 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"LADDR", None));
        ___qtablewidgetitem43 = self.tableWidget_7.horizontalHeaderItem(4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem44 = self.tableWidget_7.horizontalHeaderItem(5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"App Designed And\n"
"Developed By ICT \n"
"Academy.", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"PayPal", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"YouTube/", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Patreon/", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Copyright", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

