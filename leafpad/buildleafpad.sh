#!/bin/sh

function echo_bold {
	echo -e "\e[1m$@\e[0m"
}

# get the source...
if [ -f leafpad-0.8.17.tar.gz ]; then
	echo_bold We already have the source...
else
	echo_bold Downloading the source...
	wget http://savannah.nongnu.org/download/leafpad/leafpad-0.8.17.tar.gz
fi

# Build the src rpms
rm -rf SRPMS
mkdir SRPMS
mock --buildsrpm --sources=leafpad-0.8.17.tar.gz --spec=leafpad.spec --resultdir=SRPMS

# Build the all rpms
rm -rf RPMS
mkdir RPMS
mock SRPMS/*.src.rpm --resultdir=RPMS
