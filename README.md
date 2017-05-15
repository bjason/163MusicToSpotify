# 163MusicToSpotify
This tiny program enable you to convert your favorite 163 music playlist to Spotify
To convert, following the steps as follow:
1. go get the id of your 163 playlist, to get it open the page of the playlist in a browser then copy the numbers behind "music.163.com/#/playlist?id=" in address bar. 
2. download t.py to your computer and make sure there are python installed.
3. right click the file and edit it. **paste the playlist id to playlistId vairable so that it can convert the playlist.**
4. double click to run it.
5. open the txt file right next to the t.py and select all then copy.
6. open [this site](http://spotlistr.herokuapp.com/#/search/textbox) and paste the text. Following steps are all proceeded on that site. 

Note: the API 163 provided only enable me to retrive 1000 songs in your playlist. 

## 如何将spotify歌单导入网易云音乐？
关于这一点，虽然网上已经有不少方法，但是大多还需要自己手动更改不少东西，总体来说十分麻烦。但原理一般都是利用网易提供的导入酷狗歌单（.KGL）文件进行导入，依葫芦画瓢，写了个很小的程序，具体的操作如下：

###### 步骤

1. 进入[这个页面](https://rawgit.com/watsonbox/exportify/master/exportify.html)，以.csv格式导出你需要导入到网易云音乐的歌单。
2. 从[这里](https://github.com/bjason/Convert-.CSV-to-.kgl)下载[csvToKgl.py](https://github.com/bjason/Convert-.CSV-to-.kgl/blob/master/csvToKgl.py)文件，请确保电脑上已经正确安装Python。随后，将文件中的*directory*变量改为你存放.csv的目录。
3. 运行csvToKgl.py，得到所有的.kgl文件。
4. 进入[导入酷狗歌单页面](http://music.163.com/#/import/kugou)依次上传.kgl文件。

###### 优点

* 可以同时转换多个歌单

###### 可能遇到的问题

* 当歌单中存在过多网易未收录的歌曲，可能会导致上传失败。

## 如何将网易云音乐歌单导入spotify？
网上似乎没有太多关于这个需求的解决方法啊，我找到的[唯一一个](https://sspai.com/post/36542)是利用网易提供的 API 得到歌单列表的JSON文件，再使用 workflow + IFTTT 曲线救国的方法，不仅不直观，而且要在手机上多次下载软件、多次授权之后才能进行操作，我跟着原文的方式尝试了一遍之后，依然没有在spotify中看到导入的歌单……所以被逼无奈才又写了几行代码实现的。

###### 步骤

1. 得到歌单ID：从浏览器进入到你的歌单，复制地址栏中"music.163.com/#/playlist?id="后面的数字。
2. 进入到[这个页面](https://github.com/bjason/163MusicToSpotify)下载[t.py](https://github.com/bjason/163MusicToSpotify/blob/master/t.py)文件，请确保电脑上已经正确安装Python。随后，将文件中的*playlistId*变量改为你刚刚获得的歌单ID。
3. 运行t.py得到一个.txt文件。
4. 打开 [这个网站](http://spotlistr.herokuapp.com/#/search/textbox)并粘贴.txt中的全部内容，等待其自动识别并创建歌单。

###### 优点
* 相比[这个方法](https://sspai.com/post/36542)简单、成功率高

###### 可能遇到的问题

* 网易云API只返回歌单中最多1000首歌曲的信息。
* 由于版权原因，部分歌曲spotify不能添加。
