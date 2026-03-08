import requests

# ======================= 固定配置 =======================

url = "" #填入事先保存的url地址

campusNetworkWebURL = '' #填入学校校园网登录网站ip

# ======================================================


#登陆函数
def login():
    response = requests.get(url).status_code  # 直接利用 GET 方式请求这个 URL 同时获取状态码
    print("状态码{}".format(response))  # 打印状态码
