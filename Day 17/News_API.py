"""
国内新闻头条 - 标题
"""

import requests
import json


def main():
    # 调用API接口和Key
    resp = requests.get('http://api.tianapi.com/guonei/index?key=830dea812bef2311c86d80c20a67b686')
    data_model = json.loads(resp.text)

    print('国内新闻:')
    for news in data_model['newslist']:  # 遍历Json字典
        print(news['title'])  # 选择需要的键值对进行打印


if __name__ == '__main__':
    main()

