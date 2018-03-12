#问题是求解Emily这个名字随着年份的变化，其使用次数的变化情况
#读取数据
import pandas as pd
data = pd.read_csv('/Users/xuyadan/Data_Analysis/projects/us-baby-names/NationalNames.csv')


#提取需要的部分成为一个字典结构
specific_part = data[(data.Name=='Emily') & (data.Gender=='F')]

Emily_count = []
specific_name = dict()
for index,row in specific_part.iterrows():
    specific_name[row['Year']] = row['Count']
    Emily_count.append(row['Count'])
print(specific_name)
print(Emily_count)

#画图
import matplotlib.pyplot as plt
years = range(1880,2015)
f,ax = plt.subplots(figsize=(18,8))
plt.plot(years,Emily_count,'g-')
plt.title('Emily name variation over time')
plt.ylabel('Counts')
plt.xlabel('Years')
plt.xticks(years,rotation='vertical')
plt.xlim([1980,2015])
plt.show()










# years = range(1880,2015)
# for each_year in years:
#     each_year_data = data[data['year'] == each_year]
# Emily_count = []
# Emily_dict = dict()
# for year in years:
#     for index,row in data.iterrows():
#         if row['Name'] == 'Emily':
#             Emily_dict[year] = row['Count']
#             Emily_count.append(Emily_dict[year])
#         else:
#             pass
# print(Emily_dict)
