#! /usr/bin/env python3
import urllib3
import subprocess
import os


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



if os.name == 'nt':    #WINDOWS system
	print('Using Windows System')
	print('Downloading BOINC + Virtualbox')
	downloadFile('https://boinc.berkeley.edu/dl/boinc_7.6.22_windows_x86_64_vbox.exe')
	#download.gridcoin.us/download/downloadstake/GridcoinResearch.msi
elif os.name == 'posix':
        print('Using Ubuntu System')
        print('Downloading BOINC + Virtualbox')
        subprocess.call('./UbuntuBoincInstall.sh')
        
