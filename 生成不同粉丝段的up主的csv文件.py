import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_rows',None)

#-*- coding: utf-8 -*-
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

Df_c = pd.read_csv("B站数据.csv")
#Df_c[Df_c["充电总人数"]>0].sort_values(by=["粉丝数","充电总人数"]).to_excel("data.xlsx",index=False)
#输出10粉以上up主数据
Df_c[Df_c["粉丝数"]>=10].to_csv("B站十粉以上up主数据.csv",index=False)
#输出50粉以上up主数据
Df_c[Df_c["粉丝数"]>=50].to_csv("B站五十粉以上up主数据.csv",index=False)
#输出100粉以上up主数据
Df_c[Df_c["粉丝数"]>=100].to_csv("B站百粉以上up主数据.csv",index=False)
#输出200粉以上up主数据
Df_c[Df_c["粉丝数"]>=200].to_csv("B站二百粉以上up主数据.csv",index=False)
#输出500粉以上up主数据
Df_c[Df_c["粉丝数"]>=500].to_csv("B站五百粉以上up主数据.csv",index=False)
#输出1000粉以上up主数据
Df_c[Df_c["粉丝数"]>=1000].to_csv("B站千粉以上up主数据.csv",index=False)
#输出2000粉以上up主数据
Df_c[Df_c["粉丝数"]>=2000].to_csv("B站两千粉以上up主数据.csv",index=False)
#输出5000粉以上up主数据
Df_c[Df_c["粉丝数"]>=5000].to_csv("B站五千粉以上up主数据.csv",index=False)
#输出10000粉以上up主数据
Df_c[Df_c["粉丝数"]>=10000].to_csv("B站万粉以上up主数据.csv",index=False)
#输出20000粉以上up主数据
Df_c[Df_c["粉丝数"]>=20000].to_csv("B站两万粉以上up主数据.csv",index=False)
#输出50000粉以上up主数据
Df_c[Df_c["粉丝数"]>=50000].to_csv("B站五万粉以上up主数据.csv",index=False)
#输出100000粉以上up主数据
Df_c[Df_c["粉丝数"]>=100000].to_csv("B站十万粉以上up主数据.csv",index=False)
#输出200000粉以上up主数据
Df_c[Df_c["粉丝数"]>=200000].to_csv("B站二十万粉以上up主数据.csv",index=False)
#输出300000粉以上up主数据
Df_c[Df_c["粉丝数"]>=300000].to_csv("B站三十万粉以上up主数据.csv",index=False)
#输出400000粉以上up主数据
Df_c[Df_c["粉丝数"]>=400000].to_csv("B站四十万粉以上up主数据.csv",index=False)
#输出500000粉以上up主数据
Df_c[Df_c["粉丝数"]>=500000].to_csv("B站五十万粉以上up主数据.csv",index=False)
#输出600000粉以上up主数据
Df_c[Df_c["粉丝数"]>=500000].to_csv("B站六十万粉以上up主数据.csv",index=False)
#输出700000粉以上up主数据
Df_c[Df_c["粉丝数"]>=500000].to_csv("B站七十万粉以上up主数据.csv",index=False)
