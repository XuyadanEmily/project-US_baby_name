#该问题是要解决在每一年中top25的名字总量所占百分比随着年份的变化情况
#读取数据
import pandas as pd
data = pd.read_csv('/Users/xuyadan/Data_Analysis/projects/us-baby-names/NationalNames.csv')

#将数据转变成字典格式
all_of_each_year = dict()
years = range(1880,2015)
for each_year in years:
    each_year_data = data[data['Year']==each_year]
    all_of_each_year[each_year] = dict()
    for index,row in each_year_data.iterrows():
        all_of_each_year[each_year][row['Name']] = row['Count']

#要算出总量以及top25的量的情况
from collections import Counter
all_sum = []
top_25_sum = []
for year,names_in_year in all_of_each_year.items():
    all_sum.append(sum(Counter(names_in_year).values()))
    top_25 = Counter(names_in_year).most_common(25)
    sum_temp = 0
    for pair in top_25:
        sum_temp += pair[1]
    top_25_sum.append(sum_temp)

#计算top25所占的比例多少
import numpy as np
percent_unique_names = np.array(top_25_sum).astype(float)/np.array(all_sum)*100

#画图
import matplotlib.pyplot as plt
f,ax = plt.subplots(figsize=(10,6))
ax.set_xlim([1880,2014])

plt.plot(years,percent_unique_names,label='Percent of Unique Names',color = 'purple')

ax.set_ylabel('Percent')
ax.set_xlabel('Year')
ax.set_title('Percent of unique names')
legend = plt.legend(loc='best', frameon=True, borderpad=1, borderaxespad=1)
plt.show()




