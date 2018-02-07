#! /usr/bin/env python3

import csv
import subprocess
import shutil

command = ['git', 'clone', '--quiet']
base = 'https://github.com/textcreationpartnership/'
baseExt = '.git'

# get terminal size
columns, rows = shutil.get_terminal_size((80, 20))

# open catalogue file and create csv object
with open('TCP.csv', 'r') as f:
    csvreader = csv.reader(f)
    next(csvreader)  # skip header

    # iterate over each line in the csv
    for entry in csvreader:

        # download message
        message = 'Cloning ' + entry[0] + ': ' + entry[7]
        if len(message) > columns:
            print(message[:columns - 3] + '...')
        else:
            print(message)

        # only attempt to download free texts
        if entry[4] == 'Free':
            address = [base + entry[0] + baseExt]
            # begin git clone and wait for its exit
            p = subprocess.Popen(command + address)
            p.wait()
        else:
            print(entry[0] + ' is not available.')
            pass
