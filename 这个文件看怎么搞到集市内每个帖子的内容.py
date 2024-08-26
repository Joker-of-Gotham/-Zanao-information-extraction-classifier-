import requests
import urllib3

# 禁用InsecureRequestWarning警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 定义cookies和headers
cookies = {
    'user_token': 'bFdkbllabVhZMnlZbTRSejJteUllcldzeTR5YnJwYXZkb0E9',
    'Hm_lvt_44d055a19f3943caa808501f424e662e': '1724378807,1724432557,1724435805,1724467591',
    'HMACCOUNT': 'D96A3B88EC57C3E4',
    'Hm_lpvt_44d055a19f3943caa808501f424e662e': '1724469079',
    'SERVERID': '7104c712046e7b9d0b698b157a020fee|1724475858|1724475857',
}

# 第一步：GET 请求访问初始页面
initial_url = 'https://c.zanao.com/l/1T21NDCu'

headers_post = {
    'Host': 'c.zanao.com',
    'Connection': 'keep-alive',
    'X-Sc-Version': '2.7.0',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Sc-Platform': 'android',
    'X-Sc-Alias': 'sysu',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090b19) XWEB/11205 Flue',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryr2raXeKAyBGdISUt',
    'Origin': 'https://c.zanao.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://c.zanao.com/l/1T21NDCu',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
params = {
    "id": "1T21NDCu",
    "isIOS":"false",
    "url":"https://c.zanao.com/l/1T21NDCu",
    "from":""
}

response_post = requests.post('https://c.zanao.com/sc-api/thread/info',params = params, cookies=cookies, headers=headers_post, verify=False)

if response_post.status_code == 200:
    data = response_post.json()
    print(data)  # 打印整个响应数据
    title = data.get('title', 'Default Title')  # 如果'title'不存在，使用'Default Title'
    content = data.get('content', 'Default Content')  # 如果'content'不存在，使用'Default Content'
    print(f"title: {title}")
    print(f"content: {content}")
else:
    print("Info页面请求失败")