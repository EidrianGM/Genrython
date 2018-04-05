#!bin/usr/python
# -*- coding: utf-8 -*-.
# Adrian Garcia Moreno

import os
import gzip
from operator import itemgetter
import argparse
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

parser = argparse.ArgumentParser(  
    prog='JSONaizer',
    prefix_chars='-',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='''Create JSON (of nested dictionaries)
    from tsv-like file just indicating the number of the columns in 
    the categorical order and the delimiter if it is not tabs. 
    For example, imagine that the cols that interest you are 5:3:9, 
    this way the JSON will have the following structure {5:{3:[9, ...]}}''',
    )

parser.add_argument('inputfile', 
help='csv-like file, it can be in format .txt or compress in .gz')

parser.add_argument('cols', 
help='Number of the columns in the categorical order separated by ":"')

parser.add_argument('-d', '--delimiter', default='\t',
help='Delimiter of your columns the default is \\t',
nargs = 1)

parser.add_argument('-skip', '--skiplines', type=int,
help='Number of initial lines to skip before creating the dictionary')

parser.add_argument('outputfile', 
help='The name of the folder where your results will be dumped')

args = parser.parse_args()

inputfile = args.inputfile 
cols = args.cols.split(":")
delimiter = args.delimiter
outputfile = args.outputfile
skiplines = args.skiplines

defdict = build_defaultdict(len(cols) - 1)
cols = map(lambda x: int(x) - 1, cols)
req_cols = itemgetter(*cols)

file_handle = input_format_reader(inputfile)
for line in file_handle:
    if skiplines != 0:
        skiplines -= 1
        continue
    info = line.split("\t")
    if len(info) > 1:
        info = req_cols(info)
        set_value(defdict, info)
file_handle.close()

with open("{}.json".format(outputfile), "w") as jsonHandle:
    json.dump(defdict, jsonHandle, separators = (',', ':'))
