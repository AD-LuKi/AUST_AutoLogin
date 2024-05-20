import requests as R

address = 'http://10.255.0.19/a79.htm'

send_data = {
'callback': 'dr1003',
'DDDDD': '2022304240@unicom',
'upass': 'lhh0211',
'0MKKey': '123456',
'R1': 0,
'R3': 0,
'R6': 0,
'para': 00,
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

print("回应代码{}".format(response))
