#! /usr/bin/env python3
import urllib3
import subprocess
import os
import sys
import zipfile
import EducationGridGUI as gui


def downloadFile(url):
	http = urllib3.PoolManager()
	r = http.request('GET',url)
	file_name=url.split('/')[-1]
	print("gettin")


	if r.status == 404:
		print("NOT FOUND")
		return 0

	name=file_name.split('.')
	n=len(name)-1
	file_name=''
	for index, i in enumerate(name):
		if index != n:
			file_name=str(file_name+'_'+i)
	else:
		file_name=str(file_name+'.'+i)

	if r.status == 200:
		file = open(file_name,'wb')
		file.write(r.data)
		file.close()

	exec(file_name)
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
		downloadFile('http://download.gridcoin.us/download/downloadstake/signed/snapshot.zip')
		zip_file=zipfile.ZipFile('snapshot.zip')
		#zip_file.extractall('windows grid coin directory')
		zip_file.close()
	elif os.name == 'posix':	#Ubuntu
        	print('Using Ubuntu System')
        	print('Downloading GridCoin')
        	subprocess.call('./UbuntuGridCoinInstall.sh')

def SchoolInstall():
	if os.name == 'nt':    #WINDOWS system
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
