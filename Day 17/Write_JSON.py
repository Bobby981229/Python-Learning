"""
读写JSON文件
使用Python中的json模块就可以将字典或列表以JSON格式保存到文件中
"""
# json模块四个重要的函数
# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象

import json


def main():
    # 创建JSON数据文件
    info = {
        "My Name": "LSY",
        "My WeChat": "Bobby981229",
        "Friends Information": [
            {"Friend Name": "Fiamma", "WeChat Number": "197076658", "Gender": "Male", "Age": "22"},
            {"Friend Name": "Jessica", "WeChat Number": "197076675", "Gender": "Female", "Age": "20"},
            {"Friend Name": "Angle", "WeChat Number": "197075695", "Gender": "Male", "Age": "18"}],

        "Groups Information": [
            {"Group Name": "Football Team", "Population": "50",
             "Member": [{"Name": "Messi"}, {"Name": "Faze"}, {"Name": "Simple"}]},

            {"Group Name": "Basketball Team", "Population": "99",
             "Member": [{"Name": "Jack"}, {"Name": "Jesscia"}, {"Name": "Angle"}]}
        ]
    }
    try:
        with open('Json_Info.json', 'w', encoding='utf-8') as files:
            json.dump(info, files)
    except IOError as ex:
        print('Error: ', ex)

    print('数据保存成功 ！')


if __name__ == '__main__':
    main()
