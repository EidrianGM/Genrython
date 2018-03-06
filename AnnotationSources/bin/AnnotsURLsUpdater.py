#!bin/usr/python
# -*- coding: utf-8 -*-.
# Adrian Garcia Moreno

import json
import sys
import os

path_script_annotations = "{}/../".format(os.path.dirname(sys.argv[0]))
os.chdir(path_script_annotations)

# Crete an empty JSON if it is the first time
#AnnotUrls = {}
#with open("{}/../AnnotUrls.json".format(script_path), "w") as jsonHandle:
#    json.dump(AnnotUrls, jsonHandle, separators = (',', ':'))

with open("AnnotUrls.json", "r") as jsonHandle:
    AnnotUrls = json.load(jsonHandle)

sys.stdout.write("#Name\t\t\tURL\n")
for key in AnnotUrls:
    sys.stdout.write("{}\t{}\n".format(key, AnnotUrls[key]))

while True:
    sys.stdout.write("Write 'exit' to end and save updating\n")
    annot = raw_input("Name of new annotation:\n")
    if annot == "exit":
        break
    url = raw_input("Url:\n")
    if url == "exit":
        break
    AnnotUrls[annot] = url
    
with open("AnnotUrls.json", "w") as jsonHandle:
    json.dump(AnnotUrls, jsonHandle, separators = (',', ':'))
