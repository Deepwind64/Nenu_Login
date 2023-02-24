# 创建账号信息
user = input("请输入学号：")
pw = input("请输入密码：")
with open("info.txt","wt",encoding='utf-8') as f:
    f.write(user+'\n')
    f.write(pw)

# 创建开机启动文件
hide='''@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~0"" h",0)(window.close)&&exit
:begin
'''
import os
workpath=os.getcwd()
disk = workpath[:2]+'\n'
cd = "cd "+ '"' + workpath+ '"' +'\n'
start = "start"+' "" ' + '"'+'.\Scripts\pythonw.exe"' + ' ' + '"'+'.\login.py"'
with open("login.bat","wt",encoding='utf-8') as f:
    f.writelines(hide)
    f.write(disk)
    f.write(cd)
    f.write(start)