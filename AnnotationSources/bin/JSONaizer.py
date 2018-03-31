#!bin/usr/python
# -*- coding: utf-8 -*-.
# Adrian Garcia Moreno

import os
import sys
import gzip
from operator import itemgetter
from collections import defaultdict
import json

def build_defaultdict(levels):
    if levels <= 1:        
        return defaultdict(list)
    else:
        return defaultdict(lambda : build_defaultdict(levels - 1))

def set_value(defdict, row):
    if len(row) == 2:
        if row[1] not in defdict[row[0]]: 
            defdict[row[0]].append(row[1])
    else:
        defdict[row[0]] = set_value(defdict[row[0]], row[1:])
    return defdict

def input_format_reader(inputfile):
    if os.path.splitext(inputfile)[1] == ".gz":
        file_handle = gzip.open(inputfile, "r")
    else:
        file_handle = open(inputfile, "r")
    return file_handle

inputfile = sys.argv[1] 
cols = sys.argv[2].split(":")
delimiter = sys.argv[3]
outputfile = sys.argv[4]

defdict = build_defaultdict(len(cols) - 1)
cols = map(lambda x: int(x) - 1, cols)
req_cols = itemgetter(*cols)

file_handle = input_format_reader(inputfile)
for line in file_handle:
    info = line.split("\t")
    if len(info) > 1:
        info = req_cols(info)
        set_value(defdict, info)
file_handle.close()

with open("{}.json".format(outputfile), "w") as jsonHandle:
    json.dump(defdict, jsonHandle, separators = (',', ':'))
