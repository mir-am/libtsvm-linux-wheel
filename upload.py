# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:36:35 2019

@author: Mir
"""


import ftplib
import glob
import os
import sys

sev_addr = 'ftp.mirblog.ir'
usr = 'libtsvm@mirblog.ir'
pwd = '$@!7324Hm'
whl_path = sys.argv[1]
time_out = 300

session = ftplib.FTP(sev_addr, usr, pwd, timeout=time_out)
session.set_pasv(True)

os.chdir(whl_path)
for whl_file in glob.glob('*.whl'):
    
    file = open(whl_file, 'rb')
    session.storbinary('STOR %s' % whl_file, file)

file.close()
session.quit()