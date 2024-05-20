import requests as R
import time as T

# DDDDD中的后缀：联通写unicom，电信写aust，移动写cmcc
address = 'http://10.255.0.19/a79.htm'
send_data = {'callback': 'dr1003','DDDDD': '学号@后缀','upass': '校园网密码','0MKKey': '123456'}
request_header = {'Connection': 'keep-alive', 'Host': '10.255.0.19'}
try:
    response = R.post(address,send_data,headers=request_header).status_code
    print("Wait for 3 seconds to login secondly .")
    T.sleep(3)
    response = R.post(address,send_data,headers=request_header).status_code

    print("Login Successfully !")
    print("I Love AUST !")
except:
    print("登录异常，请检查账号、后缀、密码是否正确后重试。\n如排除以上错误，请联系QQ2033930698反馈，不胜感激！")

