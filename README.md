# Network auto login CSU

开机自动登录铁道学院的校园网

### 前言

- 没什么项目经验，代码写的不好，请见谅
- 第一次写README，写的不好，如果觉得啰嗦请见谅
- 模仿了其他大佬的项目，可能会有东施效颦的违和感
- 所学知识不足，无法评估本项目的安全性，请注意

### 环境

- `Python`
- 第三方库：`requests` 安装依赖：`pip install requests`

### 食用方法

1. 下载源码
2. 在config.py设置需要的变量
3. 完成批处理文件启动`main.py`
4. 把批处理文件添加为开机自启动

### 快速上手

##### 1. 环境安装

电脑已有`python`环境的可以跳过这一步

<details>
    <summary>👉详细步骤</summary>


1. 下载`Python`安装包[👉点此下载](https://www.python.org/downloads/)

2. 进入页面后，下载最新版，按提示安装即可

   <img src="http://i0.hdslb.com/bfs/album/7ec22c2867497b6ae11f06df5b8b5b246c10bd2c.png" alt="Download Python" style="zoom: 67%;" />

3. 检查环境是否安装成功：

   1. 按下<kbd>win</kbd> + <kbd>R</kbd>，在弹出的窗口输入`cmd`，回车

      <img src="http://i0.hdslb.com/bfs/album/7bab6d374401f75f1e51c5e6d6df632b54bb81b5.png" alt="cmd" style="zoom: 67%;" />

   2. 在命令指示行内输入：`python -V`

      👉成功：则会显示你的python版本
      
      👉失败：自行百度python 环境变量配置

      ​	参考：[Python环境变量配置](https://www.runoob.com/python/python-install.html)

</details>

##### 2. 项目配置

1. 下载本项目，尽量放在一个不包含中文路径、后续自己还能找到的地方

2. 准备配置信息：

   - 你的账号和密码，运营商

   - 你电脑的IP和Mac地址

     <details>
         <summary>👉查看你的IP和Mac地址</summary>

     1. 按下<kbd>win</kbd> + <kbd>R</kbd>，在弹出的窗口输入`cmd`，回车

     2. 在命令行输入：`ipconfig/all`
     
     3. 找到”以太网适配器：以太网“这一栏：
     
        👉找到物理地址，复制备用
     
        👉找到IPv4地址，复制备用
     
      </details>
   
3. 将以上信息填入config/config.py内

   注意：Mac地址填进去后需要把分隔符<kbd>-</kbd>删除，只保留字符

4. 右键编辑`startup.bat`文件，把`main.py`文件的绝对路径填入到双引号里面

   <details>
       <summary>👉小技巧</summary>

   👉右键`main.py`，创建快捷方式，右键快捷方式 -- > 属性，复制图中的路径即可：

   <img src="http://i0.hdslb.com/bfs/album/4bf193e0f858abfdc92c0dfcee6474d3e80dd843.png" alt="image-20210925163022540" style="zoom: 67%;" />

5. 添加开机启动项

   1. 按下<kbd>win</kbd> + <kbd>R</kbd>，在弹出的窗口输入`shell:startup`，回车
   2. 把刚刚配置好的`startup.bat`文件复制到打开的文件夹，就成功添加了开机启动项
   3. 在任务管理器的启动栏，可以方便的设置是否开机自启动
   4. 配置完成，快去试试效果吧 👍

##### 3. 一些吐槽

<details>
    <summary>碎碎念</summary>

​		开学后发现，学校的校园网登入更换了UI，原先保存的密码也没了，行吧，我手动输入后点记住密码就好了，手动输入×1，但是它也记不住密码呀，而且chrome也不会提示保存我的密码。F12一看，好家伙，账号密码表单输入属性全是`text`，能记住就有鬼了。再后来：手动输入×2，手动输入×3……所以这个项目诞生了。

不过，咱的项目会有人来使用吗…？

</details>

### 声明和警告

- 在配置批处理文件时，杀毒软件可能会警告，请信任，批处理文件只是快捷启动程序，不含病毒
- 在使用本项目过程中造成的严重后果，须自己承担。包括但不限于：自己断网、IP被ban、学校不放假

