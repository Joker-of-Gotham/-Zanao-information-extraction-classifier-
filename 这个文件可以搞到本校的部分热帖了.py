import requests
import urllib3
import logging

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED')

cookies = {
    'user_token': 'bFdkbllabVhZMnlZbTRSMG5ZK0lpTFYzdVorTHJuU21ybWs9',
    'Hm_lvt_44d055a19f3943caa808501f424e662e': '1724298113,1724378807,1724432557,1724435805',
    'HMACCOUNT': '667D17138C24F3D7',
    'Hm_lpvt_44d055a19f3943caa808501f424e662e': '1724435819',
    'SERVERID': '0224bacc402dad574a17bae94740104f|1724435820|1724435805',
}

headers = {
    'Host': 'c.zanao.com',
    'Connection': 'keep-alive',
    'X-Sc-Version': '2.7.0',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Sc-Platform': 'android',
    'X-Sc-Alias': 'sysu',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090b19) XWEB/11205 Flue',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://c.zanao.com/l/1T21NcR9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': 'user_token=bFdkbllabVhZMnlZbTRSMG5ZK0lpTFYzdVorTHJuU21ybWs9; Hm_lvt_44d055a19f3943caa808501f424e662e=1724298113,1724378807,1724432557,1724435805; HMACCOUNT=667D17138C24F3D7; Hm_lpvt_44d055a19f3943caa808501f424e662e=1724435819; SERVERID=0224bacc402dad574a17bae94740104f|1724435820|1724435805',
}

params = {
    'count': '3',
    'type': '1',
    'isIOS': 'false',
}

response = requests.get('https://c.zanao.com/sc-api/thread/hot', params=params, cookies=cookies, headers=headers, verify=False)

if response.status_code == 200:
    data = response.json()
    print(data)  # 打印整个响应数据
    title = data.get('title', 'Default Title')  # 如果'title'不存在，使用'Default Title'
    content = data.get('content', 'Default Content')  # 如果'content'不存在，使用'Default Content'
    print(f"Title: {title}")
    print(f"Content: {content}")
else:
    print("Request failed")