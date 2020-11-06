#!/usr/bin/python
# This Python file uses the following encoding: utf-8
# Author: qiaowei1976@qq.com

import os
import time

class photo_handler(object):

    supportList = ['.jpg', '.JPG', '.png','.mp4','.mov']

    def __init__(self):
        self.path = os.getcwd()

    def run(self):
        self.move_dir_space(self.path)
        self.handle_photo(self.path)

    def move_dir_space(self, dir):
        prev_dir = os.getcwd()
        os.chdir(dir)

        for root, subdirs, files in os.walk("."):
            for dir in subdirs:
                #substitue the space of the directory
                if dir.find(" ") != -1:
                    dir_no_space = dir.replace(' ', '_')
                    new_path = os.path.join(root, dir_no_space)

                    if not (os.path.isdir(new_path)):
                        os.rename(os.path.join(root, dir) , new_path)

        os.chdir(prev_dir)

    def handle_photo(self, dir):

        prev_dir = os.getcwd()
        os.chdir(dir)

        for root, subdirs, files in os.walk("."):
            for file in files:
                name, ext = os.path.splitext(file)
                if ext in self.supportList:
                    self.move_file(root, file)

        os.chdir(prev_dir)

    def move_file(self, root, file):
        prev_dir = os.getcwd()
        os.chdir(root)
        dir = os.getcwd()

        file_no_space = file.replace(' ', '_')
        os.rename(os.path.join(dir, file) , os.path.join(dir, file_no_space))

        mtime = os.stat(file_no_space).st_mtime
        mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        #print(mtime)  #2020-10-21 20:32:32
        dirname = mtime[0:10]

        self.dest_path = self.path + "\\output"
        if not (os.path.isdir(self.dest_path)):
            os.mkdir(self.dest_path)

        dest_dir = os.path.join(self.dest_path, dirname)
        if not (os.path.isdir(dest_dir)):
            os.mkdir(dest_dir)

        cmd = "copy " +  os.path.join(dir, file) + " " + dest_dir
        os.system(cmd)

        os.chdir(prev_dir)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
if __name__ == "__main__":
    try:
        handler = photo_handler()
        handler.run()
    except PermissionError:
        print("Please close the file!")