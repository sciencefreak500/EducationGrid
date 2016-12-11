#! /usr/bin/env bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y boinc-client
sudo apt-get install -y boinc-manager
sudo apt-get install -y virtualbox
sudo apt-get autoremove
sudo apt-get clean
