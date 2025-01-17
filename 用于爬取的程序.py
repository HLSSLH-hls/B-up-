from bs4 import BeautifulSoup as bf
import json
import requests
import time
#记录uid，名称，粉丝数，总播放量，总阅读量，总点赞量，充电总人数，爬取日期
import csv
import datetime

'''下面这些url是B站上搜到的一个大佬提供的一些查询接口，如果感兴趣可以直接去搜一些'''



def execute(start,number)->int:
  #仿造一个请求的用户，让浏览器通过。
  headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"#Ss,
  ,
  "cookie": "buvid3=1B52E98E-119D-1126-80B8-69260FEA20A579244infoc; i-wanna-go-back=-1; _uuid=DE8A10B3D-D61E-1817-15CC-21A99D104D4B577984infoc; buvid4=DAE62528-31A6-9112-1C11-E46D9D03648D80889-022030912-a4vcJ0YF2lRwByI6pRVuSQ%3D%3D; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; nostalgia_conf=-1; blackside_state=0; fingerprint3=8648a8d2a3f6b9428cfae7f02c7754d2; LIVE_BUVID=AUTO6916496618083562; hit-dyn-v2=1; b_ut=5; DedeUserID=470259749; DedeUserID__ckMd5=c93152db31206f76; b_nut=100; is-2022-channel=1; hit-new-style-dyn=0; CURRENT_FNVAL=4048; SESSDATA=2f2cda25%2C1684110499%2Cfdeaa%2Ab1; bili_jct=cc722f3ef2d5de1ad28041a800aa3607; sid=6tyeiya0; rpdid=|(ku|RR)YlYu0J'uYY)Y)kkJ~; CURRENT_QUALITY=80; PVID=4; fingerprint=9f4e5e4fd6cc00fa65242fdb347ab8ff; bsource=search_bing; bp_video_offset_470259749=732286125939359700; buvid_fp=9f4e5e4fd6cc00fa65242fdb347ab8ff; innersign=1; b_lsid=10A841436_184AD1A34BB"
  }
  end = start+number
  To_write_list = []
  for uid in range(start,end):
    dict_data = {"uid":-1,"爬取日期":None,"名称":None,"粉丝数":-1,"总播放量":-1,"总阅读量":-1,"总点赞量":-1,"充电总人数":-1}
    #url2包含粉丝数
    while True:
      result2 = requests.get(f"https://api.bilibili.com/x/relation/stat?vmid={uid}",headers = headers)
      tx2 = json.loads(result2.text.encode("utf-8"))
      if tx2["code"] == -412:
        print("请求被拦截")
        time.sleep(60)
        continue
      break
    try:
      dict_data["粉丝数"] = tx2["data"]["follower"]
    except Exception as e:
      with open("error.log","a") as fe:
        fe.write(repr(e))
      continue
    #如果粉丝数触发规则【具体见readme】,则从下一个uid开始
    if dict_data["粉丝数"] < 10:
      continue

    #url1包含uid和名称
    result1 = requests.get(f"https://api.bilibili.com/x/web-interface/card?mid={uid}",headers = headers)
    #如果该uid不存在，则跳过
    tx1= json.loads(result1.text.encode("utf-8"))
    if tx1["code"] != 0:
      continue
    dict_data["uid"] = tx1["data"]["card"]["mid"]
    dict_data["名称"] = tx1["data"]["card"]["name"]
    
    #url3包含总播放量，总阅读量，总点赞量
    result3 = requests.get(f"https://api.bilibili.com/x/space/upstat?mid={uid}",headers = headers)
    #print(result3.text)
    tx3 = json.loads(result3.text.encode("utf-8"))
    #print(tx3)
    dict_data["总播放量"] = tx3["data"]["archive"]["view"]
    dict_data["总阅读量"] = tx3["data"]["article"]["view"]
    dict_data["总点赞量"] = tx3["data"]["likes"]
    
    #url4包含充电总人数
    result4 =  requests.get(f"https://api.bilibili.com/x/ugcpay-rank/elec/month/up?up_mid={uid}",headers = headers)
    tx4 = json.loads(result4.text.encode("utf-8"))
    if tx4["code"] != 88214:
      dict_data["充电总人数"] = tx4["data"]["total_count"]
    #载入该条数据爬取日期
    dict_data["爬取日期"] = datetime.datetime.now()
    To_write_list.append(dict_data)

  
  #写入csv文件
  f = open("B站数据.csv","a",encoding="utf-8",newline="")
  writer = csv.DictWriter(f,fieldnames=["uid","爬取日期","名称","粉丝数","总播放量","总阅读量","总点赞量","充电总人数"])
  #writer.writeheader()

  for line in To_write_list:
    writer.writerow(line)

  f.close()

def main():
  #从the_start的这个uid开始
  the_start = 704401
  #这次读取多少条
  number_to_read = 50
  for i in range(2000):
    t0 = time.time()
    execute(the_start,number_to_read)
    the_start += number_to_read
    t = time.time()-t0
    print(f"读取和解析{number_to_read}条数据耗时{t}s,当前读取进度为UID是{the_start}的up主")
    time.sleep(1.5)

main()