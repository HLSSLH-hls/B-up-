import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)

#-*- coding: utf-8 -*-

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

up_db = pd.read_csv("B站数据.csv")
up_db = up_db[(up_db["uid"] > 1000) & (up_db["粉丝数"]>=10) & ((up_db["总播放量"]>0) | (up_db["总阅读量"]>0))]
compute_length = 20
list_of_compute = [10*(2**i) for i in range(compute_length)]
print(list_of_compute)
number_remain = [len(up_db[up_db["粉丝数"]>=list_of_compute[j]]) for j in range(compute_length)]
print(number_remain)
percentage_rate = []
for i in range(1,compute_length):
    percentage_rate.append((number_remain[i]/number_remain[i-1])*100)
print(percentage_rate)
ax1 = plt.subplot()
#ax2 = ax1.twinx()
ax1.semilogx(list_of_compute[1:],percentage_rate,marker = "d")
#ax2.semilogy(list_of_compute[1:],number_remain[1:],marker = "*")
#for fn,pr in zip(number_remain,percentage_rate):
def plotText(offsetlist):
    for i in range(len(offsetlist)):
        plt.text(list_of_compute[i+1],percentage_rate[i]+offsetlist[i],(number_remain[i],f"{format(percentage_rate[i],'.2f')}%"),color = "black")
offsetlist = [0,-2,-1,1,-3,1,0,0,-2,0,-2,0,-1,0,0,0,0,-1,0]
plotText(offsetlist)
ax1 = plt.subplot()
plt.yticks(np.arange(20,82,2))
plt.ylabel("晋级人数占比(%)")
plt.xlabel("粉丝数量(对数尺度)")
plt.title("不同粉丝数量晋级比例")
plt.show()


'''
x = [i for i in range(len(Df_c))]
y = Df_c["uid"].to_list()

plt.plot(y,x)
plt.show()'''