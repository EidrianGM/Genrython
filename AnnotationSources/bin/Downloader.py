#!bin/usr/python
# -*- coding: utf-8 -*-.
# Adrian Garcia Moreno

import os
import sys
import time
import urllib
import json

path_script_annotations = "{}/../".format(os.path.dirname(sys.argv[0]))
os.chdir(path_script_annotations)

def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

def save(url, filename):
    urllib.urlretrieve(url, filename, reporthook)
    sys.stdout.write("\nDone!\n")

def urlsgetter(download):
    if download in AnnotUrls:
        urls = [AnnotUrls[download]]
    elif download == "all":
        urls = AnnotUrls.values()
    else:
        sys.stdout.write("Sorry but you must have misspelled something.\nTry again please")
        sys.exit()
    return urls

with open("AnnotUrls.json", "r") as jsonHandle:
    AnnotUrls = json.load(jsonHandle)    
    
sys.stdout.write("\n".join(AnnotUrls.keys()))

download = raw_input("\nWhat do you need to download?\n(write 'all' to download everything):\n")
urls = urlsgetter(download)

for url in urls:
    fileName = "AnnotationFiles/{}".format(url.split('/')[-1])
    sys.stdout.write("Downloading {}:\n".format(fileName))
    ## Need to implement a hash analysis to avoid downloading
    ## the exactly same existing files unless they have been changed 
    ## which will be asummed as if they were updated with new info 
    ## relevant to any research line.
    save(url, fileName)
