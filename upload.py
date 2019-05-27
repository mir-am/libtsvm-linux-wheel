# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:36:35 2019

@author: Mir
"""


import dropbox
import glob
import os
import sys

acc_token = 'Aq4crTcY2oAAAAAAAAAAC9i5oxSy7n-Hy9wUBADbeg7oNxOHKsyO8C1tx_H21dPn'
file_to = '/wheels/'
whl_path = sys.argv[1]

dbx = dropbox.Dropbox(acc_token)

os.chdir(whl_path)
for whl_file in glob.glob('*.whl'):
    
    with open(whl_file, 'rb') as f:
        dbx.files_upload(f.read(), file_to + whl_file)
