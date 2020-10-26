#!/usr/bin/python
#endcoding: utf-8

import os
import time

support_list = ['.jpg', '.JPG', '.png','.mp4','.mov']

try:
    RootDir = os.getcwd()

    for root, dir, files in os.walk(RootDir):
        for file in files:
            file_with_path = os.path.join(root, file)
            name, ext = os.path.splitext(file_with_path)
            if ext in support_list:
                mtime = os.stat(file_with_path).st_mtime
                mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
                #print(mtime)  #2020-10-21 20:32:32
                dirname = mtime[0:10]

                if not (os.path.isdir(dirname)):
                    os.mkdir(dirname)
                cmd = "copy " + file_with_path + " " + dirname
                os.system(cmd)
    print("Done!")				
except PermissionError as err:
    print('PermissionError:', err)