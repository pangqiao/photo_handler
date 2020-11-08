# 照片备份工具
经常有很多照片通过微信等应用保存到手机，这种照片会丢失文件名中的时间信息，通常我们要等很久才会备份照片到电脑，按照时间归类就成了耗时耗力的工作。本软件会扫描该目录及子目录，自动读取每个文件的创建时间，根据创建时间查询并建立目录，然后将该文件拷贝到目录中去，完成自动归类。软件支持扫描jpg、png、jpeg、mp4、heic和mov等格式的照片和视频文件。

# 使用方法
界面很简单，两个单选框，加一个选文件夹的按钮。  
![UI](https://github.com/pangqiao/photo_handler/blob/main/images/main.jpg)  
20201030 - 表示文件夹格式为年月日。  
202010   - 表示文件夹格式为年月。  
选文件夹  - 选中需要归类的文件夹，其目录及子目录下的文件都会被分类。  
 
选中默认的20201030，并点击“选文件夹”  
![选文件夹](https://github.com/pangqiao/photo_handler/blob/main/images/select_the_folder.jpg)  
选中文件夹并确认，会在选中文件夹同级目录创建一个output目录，归类好的文件都会被拷贝到这个output目录中去，原来的目录结构不会改变，文件也不会丢失。  
 
这是之前的目录结构：  
![before](https://github.com/pangqiao/photo_handler/blob/main/images/folder_before.jpg)  
这是归类之后的目录结构:  
![after](https://github.com/pangqiao/photo_handler/blob/main/images/folder_after.jpg)

# 版本
2020/10/25 - v1.0 
- First release

2010/11/06 - v1.1
- Support folder name with space.  
- support the file name with space.

2010/11/08 - v2.0  
- Add UI.
