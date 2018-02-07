#! /usr/bin/env python3

import csv
import subprocess
import sys
import shutil

command = ['wget', '--continue', '--quiet', '--show-progress']
base = 'https://raw.githubusercontent.com/textcreationpartnership/'
baseDir = '/master/'
baseExt = '.xml'
errCount = 0

# get terminal size
columns, rows = shutil.get_terminal_size((80, 20))

# open catalogue file and create csv object
with open('TCP.csv', 'r') as f:
    csvreader = csv.reader(f)
    next(csvreader)  # skip header

    # iterate over each line in the csv
    for entry in csvreader:

        # download message
        message = 'Downloading ' + entry[0] + ': ' + entry[7]
        if len(message) > columns:
            print(message[:columns - 3] + '...')
        else:
            print(message)

        # only attempt to download free texts
        if entry[4] == 'Free':
            address = [base + entry[0] + baseDir + entry[0] + baseExt]
            # begin wget download and wait for its exit
            p = subprocess.Popen(command + address)
            p.wait()

            # successful download
            if int(p.returncode) == 0:
                print('Downloaded ' + entry[0])
            # collect errors
            elif int(p.returncode) > 0 and errCount < 5:
                print('\033[1;31;40mDownload failed\033[00m')
                errCount += 1
            # quit after 5 errors
            elif errCount == 5:
                print('There seems to be a problem.')
                print('Please check your network connection and try again.')
                sys.exit()
        else:
            print(entry[0] + ' is not available.')
            pass
