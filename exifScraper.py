#!/usr/bin/env python3
import exiftool
import os


for file in os.listdir("test"):
    with exiftool.ExifTool() as et:
        print(et.get_tag("CreateDate", file))
