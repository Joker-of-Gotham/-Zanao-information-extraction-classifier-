import requests
import urllib3

# 禁用InsecureRequestWarning警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

'''首先获取每个帖子的内容'''
# 定义cookies和headers
cookies = {
    'user_token': 'bFdkbllabVhZMnlZbTRSejJteUllcldzeTR5YnJwYXZkb0E9',
    'Hm_lvt_44d055a19f3943caa808501f424e662e': '1724378807,1724432557,1724435805,1724467591',
    'HMACCOUNT': 'D96A3B88EC57C3E4',
    'Hm_lpvt_44d055a19f3943caa808501f424e662e': '1724469079',
    'SERVERID':'d029130b9062872e906b6e5e55765858|1724479647|1724478855',
}

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
    'Referer': 'https://c.zanoa.cn/l/11111111',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
params = {
    "id": "1T21NHsn", #获取不同的内容，改id
    "isIOS":"false",
    "url":"https://c.zanoa.cn/l/11111111",
    "from":""
}

response_post = requests.post('https://c.zanao.com/sc-api/thread/info',params = params, cookies=cookies, headers=headers_post, verify=False)

if response_post.status_code == 200:
    data = response_post.json()
    print("———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    # 提取想要的字段
    filtered_data = {
        'title': data['data']['detail']['title'],
        'content': data['data']['detail']['content'],
        'cate_name': data['data']['detail']['cate_name']
    }
    # 按指定顺序输出
    print(f"title: {filtered_data['title']}")
    print(f"content: {filtered_data['content']}")
    print(f"cate_name: {filtered_data['cate_name']}")
else:
    print("Info页面请求失败")

'''再获取每个帖子的评论'''
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
    'Referer': 'https://c.zanoa.cn/l/11111111',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

#获取不同的comment，改get的url
response = requests.get('https://c.zanao.com/sc-api/comment/list?id=1858887123&rcid=0&vuid=0&sign=cUdDcGl2VjU0eG1zVEswdUp0ZVRrcDFDRm4rR3c5M2laWmdPQkNERjdlQm51c0RGTEJ1ZkxFNmI3TXNuYStyQWRWZU9FLzI3M2ZPNERPeHNhVmlkdnRyRkRTdWN5dHc0bGRVTzR4bjd1K289&url=https:%2F%2Fc.zanao.com%2Fl%2F1T21NHsn&isIOS=false', cookies=cookies, headers=headers, verify=False)

if response.status_code == 200:
    data = response.json()
    print("———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    # 遍历评论列表，按顺序编号并打印内容
    for i, item in enumerate(data['data']['list'], 1):
        print(f"{i}. 内容: {item['content']}, 时间: {item['post_time_text']}")
        if 'reply_list' in item and item['reply_list']:
            for j, reply in enumerate(item['reply_list'], 1):
                print(f"   {i}.{j} 回复: {reply['content']}, 时间: {reply['post_time_text']}")
else:
    print("Request failed")

'''再获取本校部分热帖'''
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
    'Referer': 'https://c.zanoa.cn/l/11111111',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = {
    'count': '10',
    'type': '1',
    'isIOS': 'false',
}

response = requests.get('https://c.zanao.com/sc-api/thread/hot', params=params, cookies=cookies, headers=headers, verify=False)

if response.status_code == 200:
    data = response.json()
    print("———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    # 提取并组合所需字段
    # 将数据提取并格式化输出
    for item in data['data']['list']:
        title = item['title']
        view_count = item['view_count']
        hot_val = item['hot_val']
        hot_rank = item['hot_rank']
        print(f"标题: {title}, 浏览数: {view_count}, 排名: {hot_rank}")
else:
    print("Request failed")

'''再获取跨校部分热帖'''
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
    'Referer': 'https://c.zanoa.cn/l/11111111',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = {
    'isIOS': 'false',
}

response = requests.get('https://c.zanao.com/sc-api/mx/tag/hot', params=params, cookies=cookies, headers=headers, verify=False)

if response.status_code == 200:
    data = response.json()
    print("———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    print(data)  # 打印整个响应数据
else:
    print("Request failed")