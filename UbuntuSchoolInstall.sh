#! /usr/bin/env bash
notify-send 'Downloading School Software'
gksudo add-apt-repository -y ppa:webupd8team/java
gksudo add-apt-repository -y ppa:team-xbmc/ppa
gksudo add-apt-repository -y ppa:webupd8team/y-ppa-manager
gksudo add-apt-repository -y ppa:freecad-maintainers/freecad-stable
gksudo add-apt-repository -y ppa:otto-kesselgulasch/gimp
gksudo apt-get update
gksudo apt-get -y upgrade
gksudo apt-get install -y wine
gksudo apt-get install -y oracle-java8-installer
wget 'https://notepad-plus-plus.org/repository/7.x/7.2.2/npp.7.2.2.Installer.x64.exe'
wine npp.7.2.2.Installer.x64.exe
rm npp.7.2.2.Installer.x64.exe
gksudo apt-get install -y vlc
gksudo apt-get install -y audacity
gksudo apt-get install -y python-software-properties
gksudo apt-get install -y synaptic
gksudo apt-get install -y libreoffice
gksudo apt-get install -y flashplugin-installer
gksudo apt-get install -y filezilla 
gksudo apt-get install -y virtualbox
gksudo apt-get install -y virtualbox-guest-additions-iso
gksudo apt-get install -y virtualbox-guest-utils
gksudo apt-get install -y exfat-fuse 
gksudo apt-get install -y exfat-utils
gksudo apt-get install -y freecad
gksudo apt-get install -y git
gksudo apt-get install -y libtext-csv-perl
gksudo apt-get install -y python3-pip
gksudo apt-get install -y python3-pyqt4 
gksudo apt-get install -y pyqt4-dev-tools
gksudo apt-get install -y inkscape 
gksudo apt-get install -y qt4-designer
gksudo apt-get install -y gimp
gksudo apt-get install -y arduino
gksudo apt-get install -y blender
notify-send 'Done Installing School Software'
