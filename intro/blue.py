#!/usr/bin/env python


# import modules
import yaml


# read story metadata

with open("solar.yml", 'r') as stream:
    try:
        work_meta = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
# print(work_meta)

# create story html

import unisworks
work = unisworks.unisworks(work_meta)
#print(work)

with open("pub/index.html", "w") as work_file:
    work_file.write(work)
    
# publish using surge.sh
# (make sure surge is installed using npm install -g surge)
cmd = "surge --domain " + work_meta['url'] + " ./pub/"

import os
os.system(cmd)