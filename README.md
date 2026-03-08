# 个人学习项目

# CampusNetworkAutoLogin 校园网自动登录
连接校园网后自动登录，程序常驻后台，每小时自动检测，支持系统托盘手动登录

## 简要说明
使用Python语言，使用前需要自行抓包获取数据，通过向校园网服务器发送http请求，模拟登录过程，从而可实现自动登录校园网连接服务

本仓库作为个人学习使用，同时也为备份

## 可用场景
基于广州热点软件科技股份有限公司的哆点校园网登陆平台进行编写

理论上使用该平台的校园网均可使用此脚本

**其余平台未测试**

## 需要使用到的软件包
requests pystray pillow

``` Terminal
pip install requests pystray pillow
```

## 使用方法
### P.S. 首先请确保校园网为下线状态

以Microsoft Edge进行操作
* 连接校园网并进入登录网页

![](/image/Login.png)

* 填入账号密码并选择运营商后不要点击登录，按F12打开调试工具，并切换到网络(Network)选项卡后再点击登录

![](/image/NetworkDebug.png)

选择左侧第一项，保存右侧的请求URL

* 进入`CampusNeworkAuoLoin`文件夹，编辑`main.py`文件，在`固定配置`中按照注释填入内容，保存后运行即可


# 另含简化版脚本
### P.S. 该简化版本启动后仅会自动登陆校园网，不包含其他功能，一次性使用，登录成功后即可关闭
通过同样抓包方法获得url后编辑`CampusNeworkAuoLoin`文件夹中的`Simplified Edtion.py`文件,按照注释填写，填写后启动即可
