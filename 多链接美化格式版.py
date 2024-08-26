import pandas as pd
import requests
import urllib3
import json

# 禁用InsecureRequestWarning警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 读取Excel文件
excel_path = 'D:/大学文件/大学学习/集市爬虫相关/保存结果/2024年08月26日_集市爬虫ID.xlsx'
df = pd.read_excel(excel_path)

# 初始URL，ID部分会在后续代码中动态替换
url_1 = "https://c.zanao.com/sc-api/comment/list?id=1858887123"

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

# 遍历Excel文件中的ID列
for index, row in df.iterrows():
    id = row.iloc[1]  # 假设第二列的索引是1，根据实际情况调整索引

    params = {
        "id": id,
        "isIOS": "false",
        "url": "https://c.zanoa.cn/l/" + str(id),  # 假设帖子ID可以直接附加到URL
        "from": ""
    }

    response_post = requests.post('https://c.zanao.com/sc-api/thread/info', 
                                   params=params, 
                                   cookies=cookies, 
                                   headers=headers_post, 
                                   verify=False)

    # 检查响应状态码
    if response_post.status_code == 200:
        data = response_post.json()
        # 检查数据结构
        if 'data' in data and 'detail' in data['data']:
            detail = data['data']['detail']
            # 使用 get() 方法避免 KeyError
            title = detail.get('title', 'No title')
            content = detail.get('content', 'No content')
            cate_name = detail.get('cate_name', 'No category')

            print("———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
            print(f"title: {title}")
            print(f"content: {content}")
            print(f"cate_name: {cate_name}")

            # 提取thread_id并更新URL
            thread_id = detail.get('thread_id', 'No thread_id')
            if thread_id != 'No thread_id':
                url_1 = f"https://c.zanao.com/sc-api/comment/list?id={thread_id}"
            else:
                print("未能提取到 thread_id")

    '''获取每个帖子的评论'''
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

    # 获取评论内容
    response = requests.get(url_1, cookies=cookies, headers=headers, verify=False)

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
        print("评论请求失败，状态码：", response.status_code)

# 获取本校部分热帖
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
    for item in data['data']['list']:
        title = item['title']
        response