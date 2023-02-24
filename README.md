# Nenu_Login
A Windows campus network automatic login tool for Nenuers.

**Version**: v1.0

The following introduction is in Chinese:
# The sence-free authentcation is a lie! / 无感知登录是个谎言

东师的校园网存在一些顽固的登录问题，即使使用了固定的MAC地址也无法保证每次都能正常登录，这些问题包括但不限于：
- 在更换登录地点时出现登录失效
- 在一段时间的登录后自动失效
- 在5G和2.4G网络间更换会导致登录失效

所以我上课摸鱼写了一个 Python+Selenium 的脚本用于代替手动登录，由于最近时间比较赶，代码肯定是不Pythonic了（笑哭）

模拟浏览器登录方式的平均的登录时间在5~10秒，由于硬件情况和网络质量的不同可能还会有所变大

目前有JS逆向来直接发申请以获得用网资格的计划，但限于时间和技术力的限制，更新时间随缘

## How to Use / 使用教程
1. 下载并配置好环境，选择合适的位置放置Nenu_Login文件夹
2. 点击"安装.bat"，输入账户密码完成初始账号设置，并会自动设置开机自启.注意：如果此时再修改Nenu_Login文件夹的路径则需要重新安装
3. 如果已经联网，在点击后会出现"网络已连接"的提示。未联网将自动连接，并弹出"连接成功"的提示
4. 如果有报错，请根据错误信息执行操作
5. 如果想要卸载该程序，点击"卸载.bat"再删除整个文件夹即可
