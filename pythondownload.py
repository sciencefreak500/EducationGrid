#! /usr/bin/env python3
import urllib3
import subprocess
import os
import sys
import EducationGridGUI as gui


def downloadFile(url):
	http = urllib3.PoolManager()
	r = http.request('GET',url)
	print("gettin")

	if r.status == 404:
		print("NOT FOUND")
		return 0

	if r.status == 200:
		file = open(url.split('/')[-1],'wb')
		file.write(r.data)
		file.close()
def Install():
	print('checks which programs the user has chosen to install')
	if ui.BoincCheck.isChecked():
		BoincInstall()
	if ui.GridCoinCheck.isChecked():
		GridCoinInstall()
	if ui.SchoolCheck.isChecked():
		SchoolInstall()
	if ui.BoincCheck.isChecked() or ui.GridCoinCheck.isChecked() or ui.SchoolCheck.isChecked():
		EndProgram()
		

def BoincInstall():
	if os.name == 'nt':    #WINDOWS system
		print('Using Windows System')
		print('Downloading BOINC + Virtualbox')
		downloadFile('https://boinc.berkeley.edu/dl/boinc_7.6.22_windows_x86_64_vbox.exe')
	elif os.name == 'posix':	#Ubuntu
		print('Using Ubuntu System')
		print('Downloading BOINC + Virtualbox')
		subprocess.call('./UbuntuBoincInstall.sh')

def GridCoinInstall():
	if os.name == 'nt':    #WINDOWS system
		print('Using Windows System')
		print('Downloading GridCoin')
		downloadFile('https://download.gridcoin.us/download/downloadstake/GridcoinResearch.msi')
	elif os.name == 'posix':	#Ubuntu
        	print('Using Ubuntu System')
        	print('Downloading GridCoin')
        	subprocess.call('./UbuntuGridCoinInstall.sh')

def SchoolInstall():
	if os.name == 'nt':    #WINDOWS system
		print('Using Windows System')
		print('Downloading School Software')
		#downloadFile('https://download.gridcoin.us/download/downloadstake/GridcoinResearch.msi')
	elif os.name == 'posix':	#Ubuntu
        	print('Using Ubuntu System')
        	print('Downloading School Software')
        	subprocess.call('./UbuntuSchoolInstall.sh')


def EndProgram():
	sys.exit(app.exec_())

def FunctionGuiMap():
       
	'''GuiButtons'''
	#MainWindow
	ui.OkButton.clicked.connect(Install)
	ui.CancelButton.clicked.connect(EndProgram)

class InstallGui(gui.QtGui.QWidget):
	def __init__(self, parent=None):
		gui.QtGui.QWidget.__init__(self,parent)

	def closeEvent(self,event):
		event.accept()

#the main program
if __name__ == "__main__":
	app = gui.QtGui.QApplication(sys.argv)
	window = InstallGui()
	ui = gui.Ui_EducationGridGUIInstaller()
	ui.setupUi(window)
	FunctionGuiMap()
	window.show()
	sys.exit(app.exec_())
