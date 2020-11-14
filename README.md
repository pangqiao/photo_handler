# 照片备份工具
经常有很多照片会通过微信保存。照片文件信息中的“修改时间”会记录从微信存到手机的时间，”创建时间“记录从手机转存到电脑的时间，所以在电脑中看到的”创建时间“比”修改时间“还要晚。如果照片不能当天从微信存到手机，而且新的文件名也不能显示拍照的时间信息(mmexport1605017364829.jpg)，真正的拍照时间会丢失。由于不能从文件名得到创建时间，只能文件属性查找，时间一长，按照时间归类就成了耗时耗力的工作。下面这张照片的拍照时间是2020年10月7日，从微信存到手机的日期是10月24日，拍照时间丢失。  
![UI](https://github.com/pangqiao/photo_handler/blob/main/images/wechat.jpg)  

本软件会扫描该目录及子目录，自动读取文件头中该文件的“修改时间”，根据修改时间建立目录，然后将该文件拷贝到目录中去，完成自动归类。软件支持扫描jpg、png、jpeg、mp4、heic和mov等格式的照片和视频文件。  

# 使用方法
界面很简单，两个单选框，加一个按钮和进度条：  
![UI](https://github.com/pangqiao/photo_handler/blob/main/images/main.jpg)  
20201030 - 表示文件夹格式为年月日。  
202010   - 表示文件夹格式为年月。  
选文件夹  - 选中需要归类的文件夹，其目录及子目录下的文件都会被分类。  
 
选中默认的20201030，并点击“选文件夹”:  
![选文件夹](https://github.com/pangqiao/photo_handler/blob/main/images/select_the_folder.jpg)  
选中文件夹“testfolder”并确认，会在选中文件夹同级目录创建一个output目录，归类好的文件都会被拷贝到这个output目录中去，原来的目录结构不会改变，文件也不会丢失，支持文件夹和文件中带空格。  
 
这是之前的目录结构：  
![before](https://github.com/pangqiao/photo_handler/blob/main/images/folder_before.jpg)  
  
这是归类之后的目录结构，多出一个output目录，已经按照格式归类:    
![after](https://github.com/pangqiao/photo_handler/blob/main/images/folder_after.jpg)

# 版本
2020/10/25 - v1.0 
- First release.

2010/11/06 - v1.1
- Use "shutil" instead of "os.system".

2010/11/08 - v2.0  
- Add UI.

2010/11/13 - v2.1  
- Add progress bar.

