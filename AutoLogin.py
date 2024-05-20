import requests as R
address = 'http://10.255.0.19/a79.htm'

# DDDDD一项为'学号@后缀'形式
# 后缀：联通写unicom，电信写aust，移动写cmcc
send_data = {
'callback': 'dr1003',
'DDDDD': '学号@后缀',
'upass': '校园网密码',
'0MKKey': '123456',
'R1': 0,
'R3': 0,
'R6': 0,
'para': 00,
  # 电信6774，移动8487
'v': 8843
}
request_header = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': 'PHPSESSID=7oq2647ceba04rmiotvvlu1347',
'Host': '10.255.0.19',
'Referer': 'http://10.255.0.19/a79.htm',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
response = R.post(address,send_data,headers=request_header).status_code

# 一般接受返回信息应该是200
print("返回信息 : {}".format(response))
