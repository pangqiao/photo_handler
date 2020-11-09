#!/usr/bin/python
# -*- coding:utf-8 -*-

# Script Name   : photo_handler.py
# Author        : QiaoWei(qiaowei1976@qq.com)
# Created       : 07th November 2020
# Version       : 2.0
#
# Description   : This is a software which sorting the photos/videos
#                 according to the created time.
#

from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import platform
import os
import time
import shutil

class dir_format():
    MONTH_DAY = 1.0       #20201030
    MONTH = 2.0           #202010

class Color():
    bg = "tan"
    fg = 'Black'

class Panel(object):
    def __init__(self, master):
        self.root = master
        self.root.title("照片分类")

        self.dim_str = str(260) + 'x' + str(60)
        self.root.geometry(self.dim_str)
        self.root.resizable(0, 0)
        self.root.attributes("-alpha", 0.9)
        self.create_panel()

        self.MONTH_DAY = (float)(dir_format.MONTH_DAY)
        self.MONTH = (float)(dir_format.MONTH)
        self.selected = (float)(dir_format.MONTH_DAY)

    def create_panel(self):

        # The background of the panel.
        label = Label(self.root, bg = Color().bg, fg = Color().fg)
        label.place(x = 0, y = 0, width = 260, height = 60)

        # The button to select the folder.
        self.Select_button = Button(self.root, text = '选文件夹', font = ('华文楷体', 10, 'normal'),
            bg = Color().bg, fg = Color().fg, command = lambda:self.cmd_select_dir())
        self.Select_button.place(x = 165, y = 5, width = 90, height = 50)

        # The radio button to select the folder type: year + month, or year + month + day.
        radio_info = [('20201030',  (float)(dir_format.MONTH_DAY), 0, 0),
            ('202010  ', (float)(dir_format.MONTH), 0, 30)]

        self.value = IntVar()
        self.value.set((float)(dir_format.MONTH_DAY))

        for dir_string, num, pos_x, pos_y in radio_info:
            radio = Radiobutton(self.root, text = dir_string, value = num,
                bg = Color().bg, fg = Color().fg, command = self.cmd_radio_clicked,
                font = ('Kailti', 9, 'normal'), variable = self.value)
            radio.place(x = pos_x, y = pos_y, width = 160, height = 30)

    def cmd_radio_clicked(self):
        self.selected = (float)(self.value.get())

    def cmd_select_dir(self):
        try:
            folder = tkinter.filedialog.askdirectory()
            if folder == '': return

            if(platform.system()=='Windows'):
                folder = '\\'.join(folder.split('/'))

            handle = photo_handler(folder, self.selected)
            handle.run()

        except PermissionError:
            tkinter.messagebox.showinfo('提示', '有文件在处理, 请关闭文件夹或文件！')

class photo_handler(object):

    supportList = ['.jpg', '.JPG', '.png', '.mp4', '.mov', '.bmp', '.heic']

    def __init__(self, dir, selected):
        self.path = dir
        self.selected = selected

    def run(self):
        self.grep_file(self.path)
        print("归类完成！\n")

    def grep_file(self, dir):

        prev_dir = os.getcwd()
        os.chdir(dir)

        for root, subdirs, files in os.walk("."):
            for file in files:
                name, ext = os.path.splitext(file)
                if ext in self.supportList:
                    self.copy_file(root, file)

        os.chdir(prev_dir)

    def copy_file(self, root, file):
        prev_dir = os.getcwd()
        os.chdir(root)
        dir = os.getcwd()

        mtime = os.stat(file).st_mtime
        mtime = time.strftime('%Y%m%d %H:%M:%S', time.localtime(mtime))
        #print(mtime)  #2020-10-21 20:32:32

        value = (float)(dir_format().MONTH_DAY)
        if (self.selected == value):
            dirname = mtime[0:8]
        else:
            dirname = mtime[0:6]

        self.dest_path = self.path + "\\.." + "\\output"
        if not (os.path.isdir(self.dest_path)):
            os.mkdir(self.dest_path)

        dest_dir = os.path.join(self.dest_path, dirname)
        if not (os.path.isdir(dest_dir)):
            os.mkdir(dest_dir)

        shutil.copy(os.path.join(dir, file), dest_dir)

        os.chdir(prev_dir)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if __name__ == '__main__':
    root = Tk()
    root.title("照片分类")
    Panel(root)
    root.mainloop()