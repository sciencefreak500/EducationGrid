#! /usr/bin/env python3
#This file contains the functions to the gui in order to install any and all components of the EducationGrid for Windows and Ubuntu systems.
import subprocess
import sys
import EducationGridGUI as gui
import urllib.request

def downloadFile(url):
	response = urllib.request.urlopen(url)
	
	original_name = url.split('/')[-1]
	name=original_name.split('.')
	n=len(name)-1
	file_name=''
	for index, i in enumerate(name):
		if index != n:
			file_name=str(file_name+'_'+i)
		else:
			file_name=str(file_name+'.'+i)
	
	with open(file_name, 'wb') as file:
		file.write(response.read())
	
	subprocess.call(file_name)
	

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
	if sys.platform == 'win32':    #WINDOWS system
		print('Using Windows System')
		print('Downloading BOINC + Virtualbox')
		downloadFile('https://boinc.berkeley.edu/dl/boinc_7.6.22_windows_x86_64_vbox.exe')
	elif sys.platform == 'linux':	#Ubuntu
		print('Using Ubuntu System')
		print('Downloading BOINC + Virtualbox')
		subprocess.call('./UbuntuBoincInstall.sh')
	elif sys.platform == 'darwin':	#Mac
		print('Using Mac System')
		print('Downloading BOINC + Virtualbox')
		downloadFile('https://boinc.berkeley.edu/dl/boinc_7.6.33_macOSX_x86_64.zip')

def GridCoinInstall():
	if sys.platform == 'win32':    #WINDOWS system
		print('Using Windows System')
		print('Downloading GridCoin')
		downloadFile('https://download.gridcoin.us/download/downloadstake/GridcoinResearch.msi')
	elif sys.platform == 'linux':	#Ubuntu
        	print('Using Ubuntu System')
        	print('Downloading GridCoin')
        	subprocess.call('./UbuntuGridCoinInstall.sh')
	elif sys.platform == 'darwin':	#Mac
		print('Using Mac System')
		print('Downloading GridCoin')

def SchoolInstall():
	if sys.platform == 'win32':    #WINDOWS system
		print('Using Windows System')
		print('Downloading School Software')
		downloadFile('https://www.fosshub.com/Audacity.html/audacity-win-2.1.2.exe')
		downloadFile('https://download.filezilla-project.org/client/FileZilla_3.23.0.2_win64-setup_bundled.exe')
		downloadFile('https://github.com/FreeCAD/FreeCAD/releases/download/0.16/FreeCAD-0.16.6706.f86a4e4-WIN-x64_Installer-1.exe')
		downloadFile('https://github.com/git-for-windows/git/releases/download/v2.11.0.windows.1/Git-2.11.0-64-bit.exe')
		downloadFile('https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe')
		downloadFile('https://inkscape.org/en/gallery/item/3956/inkscape-0.91-x64.msi')
		downloadFile('https://download.gimp.org/mirror/pub/gimp/v2.8/windows/gimp-2.8.18-setup.exe')
		downloadFile('https://notepad-plus-plus.org/repository/7.x/7.2.2/npp.7.2.2.Installer.x64.exe')
		downloadFile('downloads.sourceforge.net/project/pyqt/PyQt4/PyQt-4.11.4/PyQt4-4.11.4-gpl-Py3.4-Qt4.8.7-x64.exe?r=&ts=1481742484&use_mirror=pilotfiber')
		downloadFile('download.arduino.org/IDE/1.7.11/arduino-1.7.11.org-windows.exe')
		downloadFile('mirror.cs.umn.edu/blender.org/release/Blender2.78/blender-2.78a-windows64.msi')
		downloadFile('download.virtualbox.org/virtualbox/5.0.30/VirtualBox-5.0.30-112061-Win.exe')
		#downloadFile('https://bootstrap.pypa.io/get-pip.py')
	elif sys.platform == 'linux':	#Ubuntu
        	print('Using Ubuntu System')
        	print('Downloading School Software')
        	subprocess.call('./UbuntuSchoolInstall.sh')
	elif sys.platform == 'darwin':	#Mac
		print('Using Mac System')
		print('DOwnloading School Software')


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
