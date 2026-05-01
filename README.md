# 用户注册行为分析项目

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-green)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.6%2B-red)

## 📋 项目概述

本项目通过分析用户注册数据，洞察用户增长趋势和注册行为模式。使用Python进行数据提取、清洗、分析和可视化，为产品运营决策提供数据支持。

**分析目标**:

- 了解年度用户注册趋势
- 分析月度注册波动规律
- 识别注册高峰期和低谷期
- 为运营策略提供数据支撑

## 🎯 业务价值

### 关键发现

1. **年度增长趋势**: 分析2017-2019年用户注册量变化
2. **季节性规律**: 识别注册量的月度波动模式
3. **日度精细分析**: 深入分析特定月份的日注册分布
4. **运营决策支持**: 为注册活动安排提供数据依据

### 应用场景

- 📊 用户增长趋势监控
- 📅 运营活动时间规划
- 🎯 注册转化率优化
- 💡 用户获取策略制定

## 🛠️ 技术栈

- **Python 3.8+**: 核心编程语言
- **Pandas**: 数据处理和分析
- **PyMySQL**: 数据库连接和数据提取
- **Matplotlib**: 数据可视化
- **MySQL 8.0**: 数据存储

## 📁 项目结构

```
user-registration-analysis/
│
├── README.md                          # 项目说明文档
├── requirements.txt                   # Python依赖包
├── .gitignore                        # Git忽略文件
│
├── data/                             # 数据文件
│   └── user.sql                      # 数据库结构和示例数据
│
├── src/                              # 源代码
│   ├── RegisteredUserAnalysis.py     # 年度注册趋势分析
│   ├── NewRegisteredUserAnalysis.py  # 月度注册分析
│   └── utils.py                      # 工具函数（可选）
│
├── notebooks/                        # Jupyter Notebook（可选）
│   └── analysis.ipynb
│
├── reports/                          # 分析报告和图表
│   ├── 年度注册用户分析图.png
│   └── 2018年4月新注册用户分析图.png
│
└── docs/                             # 文档
    └── 数据字典.md
```

## 📊 数据下载

由于数据文件较大，未包含在GitHub仓库中，请从以下链接下载：

### 数据集下载
- **百度网盘**: [点击下载](https://pan.baidu.com/s/你的链接)  提取码: xxxx

### 数据说明
- **文件名**: user.sql, user1111.xlsx
- **文件大小**: 约 30MB
- **下载后**: 将文件放在 `data/` 目录下

### 数据结构
```csv
username,last_login_time,login_count,addtime
mr000001,2017/01/01 1:57,0,2017/01/01 1:57
mr000002,2017/01/01 7:33,0,2017/01/01 7:33
...
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- MySQL 8.0+
- 必要的Python包

### 安装依赖

```bash
# 克隆项目
git clone https://github.com/yourusername/user-registration-analysis.git
cd user-registration-analysis

# 创建虚拟环境（推荐）
python -m venv venv

# Windows激活虚拟环境
venv\Scripts\activate

# Mac/Linux激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 配置数据库

1. **创建数据库**

```sql
-- 使用MySQL客户端执行
CREATE DATABASE useranalysis CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. **导入数据**

```bash
# 导入SQL文件
mysql -u root -p useranalysis < data/user.sql
```

3. **修改数据库配置**
   在代码文件中修改数据库连接信息：

```python
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='your_username',      # 修改为你的用户名
    password='your_password',  # 修改为你的密码
    charset='utf8',
    database='useranalysis'
)
```

### 运行分析

```bash
# 运行年度注册趋势分析
python src/RegisteredUserAnalysis.py

# 运行月度注册分析
python src/NewRegisteredUserAnalysis.py
```

## 📊 分析模块说明

### 模块1: 年度注册用户趋势分析

**文件**: `src/RegisteredUserAnalysis.py`

**功能**:

- 连接MySQL数据库提取用户注册数据
- 按年度和月度进行数据重采样
- 对比2017、2018、2019年注册趋势
- 生成年度对比趋势图

**核心代码逻辑**:

```python
# 数据时间序列重采样
data1 = data.resample("M").size().to_period("M")

# 按年份筛选数据
data_17 = data1['2017-01':'2017-12']
data_18 = data1['2018-01':'2018-12']
data_19 = data1['2019-01':'2019-12']

# 可视化对比
plt.plot(data_17.index, data_17, color='b', marker='*', label='2017年')
plt.plot(data_18.index, data_18, color='orange', marker='o', label='2018年')
plt.plot(data_19.index, data_19, color='red', marker='o', mfc='w', label='2019年')
```

**输出结果**:

- 📈 年度注册用户趋势对比图
- 📊 各年度月度注册量统计

### 模块2: 月度新注册用户分析

**文件**: `src/NewRegisteredUserAnalysis.py`

**功能**:

- 分析特定月份的日注册分布
- 识别月度内的注册高峰期
- 生成日度注册趋势图

**核心代码逻辑**:

```python
# 按日重采样
data2 = data.resample("D").size().to_period("D")

# 筛选特定月份
data_apr = data2['2018-04-01':'2018-04-30']

# 日度趋势可视化
plt.plot(x_index, data_apr, color='red', marker='o', mfc='w')
```

**输出结果**:

- 📅 月度日注册量趋势图
- 📈 识别注册高峰日和低谷日

## 📈 数据说明

### 数据表结构

**表名**: `user`

| 字段名          | 类型         | 说明         |
| --------------- | ------------ | ------------ |
| username        | varchar(255) | 用户名       |
| last_login_time | varchar(255) | 最后登录时间 |
| login_count     | varchar(255) | 登录次数     |
| addtime         | varchar(255) | 注册时间     |

### 数据样例

```
username | last_login_time    | login_count | addtime
----------+--------------------+-------------+-------------------
mr000001 | 2017/01/01 1:57   | 0           | 2017/01/01 1:57
mr000002 | 2017/01/01 7:33   | 0           | 2017/01/01 7:33
mr000003 | 2017/01/01 7:50   | 0           | 2017/01/01 7:50
```

### 数据时间范围

- **起始时间**: 2017年1月
- **结束时间**: 2019年12月
- **数据量**: 约3年用户注册记录

## 🎯 分析结果示例

### 年度趋势发现

- **2017年**: 用户注册基础期，建立用户增长基线
- **2018年**: 用户增长期，分析增长驱动因素
- **2019年**: 用户成熟期，关注用户质量而非数量

### 月度规律发现

- **高峰期**: 通常出现在月初或月末
- **低谷期**: 节假日前后注册量可能下降
- **季节性**: 特定月份可能有季节性波动

### 日度精细发现

- **工作日 vs 周末**: 注册行为差异
- **活动影响**: 营销活动对注册量的影响
- **异常检测**: 识别异常注册峰值

## 📚 学习要点

### 技术技能

1. **Pandas时间序列处理**
   - `pd.to_datetime()`: 时间格式转换
   - `resample()`: 时间重采样
   - `to_period()`: 周期转换

2. **数据可视化**
   - Matplotlib中文配置
   - 多线图对比展示
   - 图表美化和标注

3. **数据库操作**
   - PyMySQL连接MySQL
   - SQL查询和数据提取
   - 数据库连接管理

### 业务理解

1. **用户增长分析**: 了解用户获取和增长趋势

2. **时间序列分析**: 识别时间维度的规律和趋势

3. **运营数据支持**: 为运营决策提供数据依据

   

   ---

**最后更新**: 2026-05-01  
**项目状态**: 持续更新中  
**欢迎Star和Fork** ⭐