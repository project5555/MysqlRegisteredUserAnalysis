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

data2 = data.resample("D").size().to_period("D")
data_apr = data2['2018-04-01':'2018-04-30']
x_index = pd.date_range(start='20180401',periods=30)
plt.figure(figsize=(10,6),dpi=150)
plt.title("2018年4月新注册用户分析图")

plt.plot(x_index,data_apr,color='red',marker='o',mfc='w')

plt.xlabel("注册日期")
plt.ylabel("用户数量")
plt.legend()

plt.show()