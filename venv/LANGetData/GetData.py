#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import json
import conndb

# 第一部分
def main():
    TOKEN = '246063d5e3484005a6f10d8f5deb0d10' #经常变化
    Pollu = "O3"
    DataName = "datao3"
    header = {  # 头文件
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Connection': 'keep-alive',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'referer': 'https://106.37.208.244:50009/Track/SamplingIndex'
    }

    url = 'http://api.airsensor.top/airapi/chart/historyRankingBar?_TOKEN_=' + TOKEN  # 链接路径，外的GetTrackList.json文件
    # html = requests.get(url,headers=header,verify=False)

    # payload的响应参数
    datacs = {
        "pollu": Pollu,
        "startTime": 1582617600000,
        "endTime": 1585210588333,
        "sort": "positive",
        "orgCode": "HBPURUN",
        "staOrDev": "sta"
    }

    try:
        # 不能确定正确执行的代码
        res = requests.post(url, json=datacs, headers=header).json()
    except:
        print('Cookie已过期请在txt中更换')
    datas = res  # 研究json中结构进行赋值

    allData = []
    for data in datas:  # 用json中的load方法，将json串转换成字典
        print(data)
        sta = conndb.exe_update(cur,
                                "insert into "+DataName+"(staName, color, rank1, value) "
                                "values('%s','%s','%s','%s')" % (data["staName"], data["color"], data["rank"], data["value"]))
        if sta == 1:
            print('插入成功')
        else:
            print('插入失败')


conn, cur = conndb.conn_db()
main()
conndb.exe_commit(cur)    # 注意！！ 一定要记得commit，否则操作成功了，但是并没有添加到数据库中
print("添加到数据库中")
conndb.conn_close(conn, cur)