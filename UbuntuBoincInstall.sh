#! /usr/bin/env bash
notify-send 'Downloading Boinc'
gksudo apt-get update
gksudo apt-get upgrade
gksudo apt-get install -y boinc-client
gksudo apt-get install -y boinc-manager
gksudo apt-get install -y virtualbox
gksudo apt-get autoremove
gksudo apt-get clean
notify-send 'Done Installing Boinc'
