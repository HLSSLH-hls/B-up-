import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)

#-*- coding: utf-8 -*-

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

up_db = pd.read_csv("B站数据.csv")
up_db = up_db[(up_db["uid"] > 1000) & (up_db["粉丝数"]>=10) & ((up_db["总播放量"]>0) | (up_db["总阅读量"]>0)) & (up_db["充电总人数"] >= 0)]

compute_length = 20
list_of_compute = [10*(2**i) for i in range(compute_length)]
print(list_of_compute)
number= []
up_dbx = 0
for j in range(compute_length):
    if j == compute_length - 1:
        up_dbx =up_db[(up_db["粉丝数"]>=list_of_compute[j])] 
    else:
        up_dbx =up_db[(up_db["粉丝数"]>=list_of_compute[j]) & (up_db["粉丝数"]<list_of_compute[j+1])] 
        print(list_of_compute[j],list_of_compute[j+1])
    print(-1 in up_dbx["充电总人数"].to_list())
    print(len(up_dbx))
    number.append(int(np.mean(up_dbx["充电总人数"].to_list())))
    print(number)

ax1 = plt.subplot()
#ax2 = ax1.twinx()
ax1.semilogx(list_of_compute,number,marker = "d")
#ax2.semilogy(list_of_compute[1:],number_remain[1:],marker = "*")
#for fn,pr in zip(number_remain,percentage_rate):
ax1.semilogy()
def plotText(offsetlist):
    for i in range(len(offsetlist)):
        if i == len(offsetlist)-1:
            plt.text(list_of_compute[i],number[i],("/",f"{number[i]}人充电"),color = "black")
        else:
            plt.text(list_of_compute[i],number[i],("/",f"{number[i]}人充电"),color = "black")

offsetlist = [i for i in range(20)]
offsetlist = [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,1,-2,3,1,-2,1,1]
plotText(offsetlist)
ax1 = plt.subplot()
#plt.yticks(np.arange(0,100,4))
plt.ylabel("充电人数")
plt.xlabel("粉丝数量(对数尺度)")
plt.title("不同粉丝量级下平均充电人数")
plt.show()


'''
x = [i for i in range(len(Df_c))]
y = Df_c["uid"].to_list()

plt.plot(y,x)
plt.show()'''