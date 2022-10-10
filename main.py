# +998998679679 Muhammad aka
import os
import sys
from PySide2 import *
from qt_material import *
import psutil
import PySide2extn

from multiprocessing import cpu_count

from ui_interface_pyside import *
from datetime import *
import platform


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		apply_stylesheet(app, theme='dark-cyan.xml')

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(50)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0,92,157,550))
		self.ui.centralwidget.setGraphicsEffect(self.shadow)

		self.setWindowIcon(QtGui.QIcon(":/icons/icons/outline_airplay_white_24dp.png"))
		self.setWindowTitle("UTIL Manager")
		QSizeGrip(self.ui.size_grip)


		self.ui.minimize_window_button.clicked.connect(lambda:self.showMinimized())
		self.ui.close_window_button.clicked.connect(lambda:self.close())
		self.ui.restore_window_button.clicked.connect(lambda:self.restore_or_maximize_window())


		self.ui.cpu_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.cpu_and_memory))
		self.ui.batery_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.battery))
		self.ui.system_info_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.system_information))
		self.ui.activity_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.activites))
		self.ui.storage_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.storage))
		self.ui.sensors_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.sensors))
		self.ui.networks_page_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.networks))
#Move window
		
		def moveWindow(e):
			if self.isMaximized() == False:
				if e.buttons() == Qt.LeftButton:
					#Move window
					self.move(self.pos() + e.globalPos()- self.clickPosition)
					self.clickPosition = e.globalPos()
					e.accept()

		#mouse clicked event
		self.ui.header_frame.mouseMoveEvent = moveWindow

		#left menu toggle button
		self.ui.open_close_side_bar_btn.clicked.connect(lambda:self.slideLeftMenu())



		#style clicked button
		for w in self.ui.menu_frame.findChildren(QPushButton):
			w.clicked.connect(self.applyButtonStyle)





		self.show()


		self.battery()
		self.cpu_ram()
		self.system_info()
		self.processes()



	###################################################
	# function that creates table widgets
	###################################################
	def create_table_widget(self,rowPosition,columnPosition, text, tableName):
		qtablewidgetitem = QTableWidgetItem()
		getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtablewidgetitem)
		qtablewidgetitem = getattr(self.ui, tableName).item(rowPosition, columnPosition)

		qtablewidgetitem.setText(text)
	###################################################




	###################################################
	# running processes
	###################################################
	def processes(self):
		for x in psutil.pids():
			#create new row
			rowPosition = self.ui.tableWidget.rowCount()
			self.ui.tableWidget.insertRow(rowPosition)

			try:
				process = psutil.Process(x)
				##crate widget
				# print(process)
				# rowPosition = row number
				# x = column number

				self.create_table_widget(rowPosition, 0, str(process.pid), "tableWidget")
				self.create_table_widget(rowPosition, 1, process.name(), "tableWidget")
				self.create_table_widget(rowPosition, 2, process.status(), "tableWidget")
				# self.create_table_widget(rowPosition, 3, process.status(), "tableWidget")
				# self.create_table_widget(rowPosition, 4, str(datetime.utcfromtimestamp(process.crate_time()).strftime('%Y-%m-%d  %H:%M:%S'), "tableWidget"))

				#create an cell widget
				suspend_btn = QPushButton(self.ui.tableWidget)
				suspend_btn.setText('Suspend')
				suspend_btn.setStyleSheet("color:brown")
				# self.create_table_widget(rowPosition, 2, suspend_btn)

				self.ui.tableWidget.setCellWidget(rowPosition, 3,
					suspend_btn)

				resume_btn = QPushButton(self.ui.tableWidget)
				resume_btn.setText('Resume')
				resume_btn.setStyleSheet("color:green")
				self.ui.tableWidget.setCellWidget(rowPosition, 5, 
					resume_btn)

				terminate_btn = QPushButton(self.ui.tableWidget)
				terminate_btn.setText('Terminate')
				terminate_btn.setStyleSheet("color:orange")
				self.ui.tableWidget.setCellWidget(rowPosition, 6, 
					terminate_btn)

				kill_btn = QPushButton(self.ui.tableWidget)
				kill_btn.setText('Kill')
				kill_btn.setStyleSheet("color:red")
				self.ui.tableWidget.setCellWidget(rowPosition, 7, 
					kill_btn)

			except Exception as e:
				print(e)


		# QtCore.Qt.MatchFlag.MatchRecursiv|QtCore.Qt.MatchFlag
		self.ui.activity_search.textChanged.connect(self.findName)
		###################################################
		###################################################



	###################################################
	# search activity table
	###################################################
	def findName(self):
		name = self.ui.activity_search.text().lower()
		for row in range(self.ui.tableWidget.rowCount()):
			item = self.ui.tableWidget.item(row, 1)
			self.ui.tableWidget.setRowHidden(row, name not in item.text().lower())
	###################################################





	###################################################
	# get system informtion
	###################################################
	def system_info(self):
		time = datetime.now().strftime("%I:%M:%S %p")
		self.ui.system_date.setText(str(time))
		date = datetime.now().strftime("%Y-%m-%d")
		self.ui.system_time.setText(str(date))

		self.ui.system_machine.setText(platform.machine())
		self.ui.system_version.setText(platform.version())
		self.ui.system_platform.setText(platform.platform())
		self.ui.system_sytem.setText(platform.system())
		self.ui.system_processor.setText(platform.processor())

	###################################################




	###################################################
	# cpu and ram information
	###################################################
	def cpu_ram(self):
		totalRam = 1.0
		totalRam = psutil.virtual_memory()[0] * totalRam
		totalRam = totalRam / (1024 * 1024 * 1024)
		self.ui.total_ram.setText(str("{:.4f}".format(totalRam) + ' GB'))

		availRam = 1.0
		availRam = psutil.virtual_memory()[1] * availRam
		availRam = availRam / (1024 * 1024 * 1024)
		self.ui.aviable_ram.setText(str("{:.4f}".format(availRam) + ' GB'))

		ramUsed = 1.0
		ramUsed = psutil.virtual_memory()[3] * ramUsed
		ramUsed = ramUsed / (1024 * 1024 * 1024)
		self.ui.used_ram.setText(str("{:.4f}".format(ramUsed) + ' GB'))

		ramFree = 1.0
		ramFree = psutil.virtual_memory()[4] * ramFree
		ramFree = ramFree / (1024 * 1024 * 1024)
		self.ui.free_ram.setText(str("{:.4f}".format(ramFree) + ' GB'))

		ramUsages = str(psutil.virtual_memory()[2]) + '%'
		self.ui.ram_usage.setText(str("{:.4f}".format(totalRam)+ ' GB'))

		core = cpu_count()
		self.ui.cpu_count.setText(str(core))

		cpuPer = psutil.cpu_percent()
		self.ui.cpu_per.setText(str(cpuPer)+ " %")

		cpuMainCore = psutil.cpu_count(logical = False)
		self.ui.cpu_main_core.setText(str(cpuMainCore))

		#cpu oercentage indicator 
		#// set progress bar value
		self.ui.cpu_percentage.rpb_setMaximum(100)
		#// set progress value
		self.ui.cpu_percentage.rpb_setValue(cpuPer)
		#set progress bar style
		self.ui.cpu_percentage.rpb_setBarStyle('Hybrid2')
		#set progress bar line color
		self.ui.cpu_percentage.rpb_setLineColor((255, 30, 99))
		#set progress bar line color
		self.ui.cpu_percentage.rpb_setPieColor((45, 74, 83))
		#set progress bar text color
		self.ui.cpu_percentage.rpb_setTextColor((255, 255, 255))
		#set progress bar starting position
		self.ui.cpu_percentage.rpb_setInitialPos('West')
		#set progress bar text type
		self.ui.cpu_percentage.rpb_setTextFormat('Persentage')
		#set progress bar line font
		self.ui.cpu_percentage.rpb_setTextFont('Arial')
		#set progress bar line width
		self.ui.cpu_percentage.rpb_setLineWidth(15)
		#set progress ber path width
		self.ui.cpu_percentage.rpb_setPathWidth(15)
		#set progress bar line cap
		self.ui.cpu_percentage.rpb_setLineCap('RoundCap')
		#set progress line style
		#DotLine, DashLine
		# self.ui.cpu_percentage.rpb_setLineStyle('DashLine')



		#####################################ryhyhyh##############
			# ram usage indicator using spiral progress bar
		###################################################


		# setting minumim value
		###################################################
		self.ui.ram_percantage.spb_setMinimum((0, 0, 0))
		###################################################
		###################################################

		# setting the maximum value
		###################################################
		self.ui.ram_percantage.spb_setMinimum((totalRam, totalRam, totalRam))
		###################################################
		###################################################


		# set progress  value
		###################################################
		self.ui.ram_percantage.spb_setValue((availRam, ramUsed, ramFree))
		###################################################
		###################################################


		# set progress color (r, g, b)
		###################################################
		self.ui.ram_percantage.spb_lineColor(((6, 233, 38), (6, 231, 233), (233, 6, 201)))
		###################################################
		###################################################



		# setting the initial position of the progress bar
		###################################################
		self.ui.ram_percantage.spb_setInitialPos(('West','West','West'))
		###################################################
		###################################################

		# set line width
		###################################################
		self.ui.ram_percantage.spb_lineWidth(15)
		###################################################
		###################################################

		# set gap width
		###################################################
		self.ui.ram_percantage.spb_setGap(15)
		###################################################
		###################################################

		# set line style
		###################################################
		self.ui.ram_percantage.spb_lineStyle(('SolidLine','SolidLine','SolidLine'))
		###################################################
		###################################################

		# set line cap
		###################################################
		self.ui.ram_percantage.spb_lineCap(('RoundCap','RoundCap','RoundCap'))
		###################################################
		###################################################

		# hide the path
		###################################################
		self.ui.ram_percantage.spb_setPathHidden(True)
		###################################################
		###################################################










	###################################################
	# a function to convert seconds to hours
	###################################################
	def secs2hours(self, secs):
		mm, ss = divmod(secs, 60)
		hh,mm = divmod(mm, 60)
		return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)
	###################################################




	###################################################
	#get system battery information
	###################################################

	def battery(self):
		batt = psutil.sensors_battery()

		if not hasattr(psutil, "sensors_batter" ):
			self.ui.battery_status.setText("Platform not supported")

		if batt is None:
			self.ui.battery_status.setText("No battery installed")

		if batt.power_plugged:
			self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
			self.ui.battery_time_left.setText("N/A")

			if batt.percent < 100:
				self.ui.battery_status.setText("Charging")
			else:
				self.ui.battery_status.setText("Fully Charged")

			self.ui.battery_plugged.setText("Yes")
		else:
			self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
			self.ui.battery_time_left.setText(self.secs2hours(batt.secsleft))
			if batt.percent < 100:
				self.ui.battery_status.setText("Discharging")
			else:
				self.ui.battery_status.setText("Fully Charged")
			self.ui.battery_plugged.setText("No")
			#set progress bar value
			self.ui.battery_usage.rpb_setMaximum(100)
			#set progress value
			self.ui.battery_usage.rpb_setValue(batt.percent)
			#set progress bar style
			self.ui.battery_usage.rpb_setBarStyle('Hybrid2')
			#set progress bar line color
			self.ui.battery_usage.rpb_setLineColor((255, 30, 99))
			#set progress bar line color
			self.ui.battery_usage.rpb_setPieColor((45, 74, 83))
			#set progress bar text color
			self.ui.battery_usage.rpb_setTextColor((255, 255, 255))
			#set progress bar starting position
			self.ui.battery_usage.rpb_setInitialPos('West')
			#set progress bar text type
			self.ui.battery_usage.rpb_setTextFormat('Persentage')
			#set progress bar line width
			self.ui.battery_usage.rpb_setLineWidth(15)
			#set progress ber path width
			self.ui.battery_usage.rpb_setPathWidth(15)
			#set progress bar line cap
			self.ui.battery_usage.rpb_setLineCap('RoundCap')
			#set progress line style
			#DotLine, DashLine
			# self.ui.battery_usage.rpb_setLineStyle('DotLine')








	#side menu button styling function
	def applyButtonStyle(self):
		for w in self.ui.menu_frame.findChildren(QPushButton):
			if w.objectName() != self.sender().objectName():
				#apply the deafult style
				w.setStyleSheet("border-bottom: none;")
		#apply the new style
		self.sender().setStyleSheet("border-bottom: 2px solid")
		return




	#Slide left menu function
	def slideLeftMenu(self):
		width = self.ui.left_menu_cont_frame.width()
		if width == 40:
			newWidth = 200
		else:
			newWidth = 40
		self.animation = QPropertyAnimation(self.ui.left_menu_cont_frame,b"minimumWidth")
		self.animation.setDuration(350)
		self.animation.setStartValue(width)
		self.animation.setEndValue(newWidth)
		self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
		self.animation.start()


	#Add mouse event
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()




	def restore_or_maximize_window(self):
		if self.isMaximized():
			self.showNormal()
			self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/outline_cached_white_24dp.png"))
		else:
			self.showMaximized()
			self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/outline_cached_white_24dp.png"))
			






if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())