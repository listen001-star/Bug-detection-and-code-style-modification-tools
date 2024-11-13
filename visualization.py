'''import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
csv_file = 'pylint_report.csv'
df = pd.read_csv(csv_file)

# 提取 Error Type 首字母并统计四类错误
df['Error Category'] = df['Error Type'].str[0]  # 取每个错误类型的首字母
error_counts = df['Error Category'].value_counts()

# 绘制饼状图
plt.figure(figsize=(8, 8))
plt.pie(error_counts, labels=error_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("C, W, E, R Error Type Distribution in Pylint Report")
plt.show()'''

import pandas as pd
import matplotlib.pyplot as plt

# 读取历史 CSV 文件
history_csv = 'history.csv'
df = pd.read_csv(history_csv, parse_dates=['Date'])

# 设置日期为索引，方便按时间顺序绘图
df.set_index('Date', inplace=True)

# 绘制四类错误的折线图
plt.figure(figsize=(10, 6))
for category in ['C', 'W', 'E', 'R']:
    plt.plot(df.index, df[category], marker='o', label=f'{category} Errors')

plt.xlabel("Date")
plt.ylabel("Error Count")
plt.title("Trend of C, W, E, R Error Counts Over Time")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# 读取 CSV 文件
csv_file = 'pylint_report.csv'
df = pd.read_csv(csv_file)

# 提取 Error Type 首字母并统计四类错误
df['Error Category'] = df['Error Type'].str[0]  # 取每个错误类型的首字母
error_counts = df['Error Category'].value_counts()

# 绘制饼状图
plt.figure(figsize=(8, 8))
plt.pie(error_counts, labels=error_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("C, W, E, R Error Type Distribution in Pylint Report")
plt.show()