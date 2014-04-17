#!/usr/bin/env python

from sys import argv
from sys import exit
import os

if len(argv) < 2:
    exit('Not enough args')

script, root_dir = argv

path = root_dir

filenames = os.listdir(path)

for filename in filenames:
    os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ','_')))

