#! /usr/bin/env bash
#http://wiki.gridcoin.us/Linux_Downloads_(pre-compiled)
notify-send 'Downloading GridCoin'
gksudo add-apt-repository ppa:gridcoin/gridcoin-stable
gksudo apt-get update
gksudo apt-get upgrade
gksudo ufw allow 32749/tcp
gksudo apt-get install -y gridcoinresearch-qt
gksudo apt-get install -y gridcoinresearchd
gksudo apt-get install -y unzip
gksudo apt-get autoremove
gksudo apt-get clean
cd ~/Downloads
wget http://download.gridcoin.us/download/downloadstake/signed/snapshot.zip
unzip -o snapshot.zip -d ~/.GridcoinResearch
rm snapshot.zip
notify-send 'Done Installing GridCoin'
