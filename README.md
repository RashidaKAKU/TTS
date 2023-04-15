# Rashida TTS

## ！TXT编码格式需为UTF8

基于PYTTSX3的文本转语音工具  
UI为 tkinter  
测试 43000 字符没有问题  

![界面展示](https://github.com/RashidaKAKU/TTS/blob/main/Snipaste_2023-04-15_15-39-20.png "界面展示")

B站视频展示
<https://reurl.cc/AdakoY>

# 常见问题

## .py 文件无法正常运行
一般是由于缺少运行库，可以尝试使用 `pip install -r requirements.txt` 解决

## Linux 系统缺少 espeak

ArchLinux 以及基于此系统的发行版 Linux 用户可以通过 yay 安装 AUR 包 `espeak` 解决这个问题

Ubuntu 系统可以通过安装 `espeak` 解决

如果尚未解决，可以尝试重新安装 `espeak` 模块
