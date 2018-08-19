#!/bin/bash

# go to applications/ubuntu software center first and search for skype, then add the respective repository by clicking the respective button 

# first off all: become root

sudo su

  apt-get install -y gnome-session-fallback
  apt-get update
  apt-get upgrade
  apt-get install -y vim
  apt-get install -y kile    
  apt-get install -y gnome-tweak-tool 
  apt-get install -y vim-gnome
# sets window buttons to the right side
  gconftool-2 --set /apps/metacity/general/button_layout --type string "menu:minimize,maximize,close"

# apt-get install synaptic

  apt-get install -y ubuntu-restricted-extras
  apt-get install -y libdvdread4
  /usr/share/doc/libdvdread4/install-css.sh 

  apt-get install -y skype
  apt-get install -y checkgmail

  # apt-get install cheese

  apt-get install -y chromium-browser
  apt-get install -y chromium-codecs-ffmpeg-extra

  apt-get install -y vlc

  apt-get install -y jabref

  apt-get install -y gnuplot-x11

  apt-get install -y git-core

  apt-get install -y devtodo

  apt-get install -y xfig
  apt-get install -y grace
  apt-get install -y gimp

  apt-get install -y ps2eps

# attempts to get utility eps2pdf

  apt-get install -y texlive-extra-utils
  apt-get install -y texlive-base-bin dvidvi
# this one seems to be the one doing the job:
  apt-get install texlive-latex-recommended

# more packages for latex
  apt-get install -y  texlive-latex-extra
  apt-get install -y  texlive-latex-extra
  apt-get install -y  texlive-publishers
  apt-get install -y  texlive-fonts-extra
  apt-get install -y  texlive-math-extra
  apt-get install -y  texlive-latex3

# vim latex
  apt-get install -y  vim-latexsuite
  # and making it available (?)
  vim-addons -w install -y latex-suite

  apt-get install -y xpdf
  apt-get install -y xournal

# packages for tunneling project
  apt-get install -y qiv
  apt-get install -y ffmpeg
  apt-get install -y mplayer
 
# python packages
#
  #apt-get install python-numpy
# apt-get install python-matplotlib
# apt-get install python-argparse
# apt-get install ipython
# apt-get install python-scipy

# package for plotting in 3d
  apt-get install -y paraview

# vpn client
  apt-get install -y vpnc
  
# octave
  apt-get install -y octave3.2

# pdftk in order to split and rearrange pdfs
  pdftk

# caliber
 python -c "import sys; py3 = sys.version_info[0] > 2; u = __import__('urllib.request' if py3 else 'urllib', fromlist=1); exec(u.urlopen('http://status.calibre-ebook.com/linux_installer').read()); main(install_dir='/opt')"

# install R
# install R:
  apt-get install r-base
# install the R GUI:
  apt-get install rwkward # does not work, but installation through software center possible
# install RStudio:
# then go to software center
  # go to https://www.rstudio.com/products/rstudio/download/ and select version of ubuntu to download
  # download 

# curl (needed for oclient):
  apt-get install curl

# needed for geopandas (for fiona):
  apt-get install libgdal-dev
