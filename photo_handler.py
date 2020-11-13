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

import tkinter as tk
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

supportList = ['.jpg', '.JPG', '.png', '.mp4', '.mov', '.bmp', '.heic']

class photo_handler(object):
    def __init__(self, master):
        self.root = master
        self.root.title("照片分类")
        bg = self.root.cget("background") 

        self.dim_str = str(260) + 'x' + str(80)
        self.root.geometry(self.dim_str)
        self.root.resizable(0, 0)
        self.root.attributes("-alpha", 0.9)
        self.create_panel()

        self.MONTH_DAY = (float)(dir_format.MONTH_DAY)
        self.MONTH = (float)(dir_format.MONTH)
        self.selected = (float)(dir_format.MONTH_DAY)
        self.num = 0

    def create_panel(self):
        # The background of the panel.
        label = tk.Label(self.root, bg = Color().bg, fg = Color().fg)
        label.place(x = 0, y = 0, width = 260, height = 80)

        # The radio button to select the folder type: year + month, or year + month + day.
        radio_info = [('20201030',  (float)(dir_format.MONTH_DAY), 0, 3),
            ('202010  ', (float)(dir_format.MONTH), 0, 28)]

        self.value = tk.IntVar()
        self.value.set((float)(dir_format.MONTH_DAY))

        for dir_string, num, pos_x, pos_y in radio_info:
            radio = tk.Radiobutton(self.root, text = dir_string, value = num,
                bg = Color().bg, fg = Color().fg, command = self.cmd_radio_clicked,
                font = ('Kailti', 9, 'normal'), variable = self.value)
            radio.place(x = pos_x, y = pos_y, width = 160, height = 25)

        # The button to select the folder.
        self.btn = tk.Button(self.root, text = '选文件夹', font = ('华文楷体', 10, 'normal'),
            bg = Color().bg, fg = Color().fg, command = lambda:self.cmd_select_dir())
        self.btn.place(x = 160, y = 8, width = 80, height = 40)

        label = tk.Label(self.root, text = '进度：', font = ('Kailti', 8, 'normal'),
            bg = Color().bg, fg = Color().fg).place(x = 2, y = 58, width = 75, height = 20)

        # Create the backgound of progress bar
        self.progress_width = 180;
        self.progress_high = 10;
        self.cv = tk.Canvas(self.root, bg = 'white')
        self.cv.place(x = 64, y = 62, width = self.progress_width, height = self.progress_high)
        self.fill = self.cv.create_rectangle(0, 0, 0, self.progress_high, fill = "green")

    def Draw_progress(self, total, num):
        print(total, num)
        n = (self.progress_width / total) * num
        self.cv.coords(self.fill, (0, 0, n, self.progress_high))
        self.root.update()
        if total < 20:
            time.sleep(0.02)

    def cmd_radio_clicked(self):
        self.selected = (float)(self.value.get())

    def cmd_select_dir(self):
        try:
            folder = tkinter.filedialog.askdirectory()
            if folder == '': return
            if(platform.system()=='Windows'):
                folder = '\\'.join(folder.split('/'))

            self.btn['state'] = 'disable'
            self.grep_file(folder)
            print("归类完成！\n")
            self.btn['state'] = 'normal'

        except PermissionError:
            tkinter.messagebox.showinfo('提示', '有文件在处理, 请关闭文件夹或文件！')

    def grep_file(self, dir):
        self.path = dir
        self.total = 0;
        prev_dir = os.getcwd()
        os.chdir(dir)

        for root, subdirs, files in os.walk("."):
            for file in files:
                name, ext = os.path.splitext(file)
                if ext in supportList:
                    self.total += 1;

        self.num = 0
        for root, subdirs, files in os.walk("."):
            for file in files:
                name, ext = os.path.splitext(file)
                if ext in supportList:
                    try:
                        self.copy_file(root, file)
                    except shutil.SameFileError:
                        pass
                    self.num += 1
                    self.Draw_progress(self.total, self.num)

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
    #root = Tk()
    root = tk.Tk()
    root.title("照片分类")
    photo_handler(root)
    root.mainloop()