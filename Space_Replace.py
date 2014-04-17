#!/usr/bin/env python

from sys import argv
import os

path = os.getcwd()

filenames = os.listdir(path)

for filename in filenames:
    os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ','_')))

