import pandas as pd
import pymysql
import matplotlib.pyplot as plt
# matplotlib配置


# 图片中文显示
plt.rcParams["font.sans-serif"] = "SimHei"

# 图片中显示负号
plt.rcParams["axes.unicode_minus"] = False


conn = pymysql.connect(host='localhost',port=3306,user='root',
                     password='root',charset='utf8',database='useranalysis')
sql_query = 'select * from user'
data = pd.read_sql(sql_query,con=conn)
conn.close()
# print(data.head())
#
# print(data.info())
# print(data.describe())
# print(data.isnull().sum())

data = data[['addtime','username']]
data.rename(columns = {'addtime':'注册日期','username':'用户数量'},inplace=True)
data['注册日期'] = pd.to_datetime(data['注册日期'])
data = data.set_index('注册日期')
index = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']

data1 = data.resample("M").size().to_period("M")
# print(data1)
data_17 = data1['2017-01':'2017-12']
data_17.index = index
data_18 = data1['2018-01':'2018-12']
data_18.index = index
data_19 = data1['2019-01':'2019-12']
data_19.index = index
plt.figure(figsize=(10,6),dpi=150)
plt.title("年度注册用户分析图")

plt.plot(data_17.index,data_17,color='b',marker='*',label='2017年')
plt.plot(data_18.index,data_18,color='orange',marker='o',label='2018年')
plt.plot(data_19.index,data_19,color='red',marker='o',mfc='w',label='2019年')

plt.xlabel("注册日期")
plt.ylabel("用户数量")
plt.legend()

plt.show()

