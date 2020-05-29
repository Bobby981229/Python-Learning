"""
新型冠状病毒 - 海外疫情数据
"""

import requests
import json
import sys
import urllib
import urllib.request


def main():
    # API接口和Key
    url = requests.get('http://api.tianapi.com/txapi/ncovabroad/index?key=830dea812bef2311c86d80c20a67b686')
    data_model2 = json.loads(url.text)

    print('COVID-19 Oversea Data: ')
    for news in data_model2['newslist']:  # 遍历Json字典
        print('Continents:', news['continents'])
        print('Country Name:', news['provinceName'])
        print('Current Confirmed Count:', news['currentConfirmedCount'])
        print('Confirmed Count:', news['confirmedCount'])
        print('Cured Count:', news['curedCount'])
        print('Dead Count:', news['deadCount'])
        print('Location Id:', news['locationId'])
        print('Country ShortCode:', news['countryShortCode'])
        print('\n*************************************\n')


if __name__ == '__main__':
    main()
