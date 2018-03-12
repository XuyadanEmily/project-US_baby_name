import pandas as pd
data = pd.read_csv('/Users/xuyadan/Data_Analysis/projects/us-baby-names/NationalNames.csv')
names_dict = dict()
for index,row in data.iterrows():
    if row['Name'] not in names_dict:
        names_dict[row['Name']] = row['Count']
    else:
        names_dict[row['Name']] += row['Count']

# name = 'Emily'
# print('%s -> %i'%(name,names_dict.get(name)))

from collections import Counter
top_10 = Counter(names_dict).most_common(10)
print('全美流行的婴儿名字top10:')
for pair in top_10:
    print('姓名：%s -> 数量：%i' %(pair[0],pair[1]))

print('全美最不流行婴儿名字：')
for pair in Counter(names_dict).most_common()[-10:-1]:
    print('姓名：%s -> 数量：%i'%(pair[0],pair[1]))

def average_length_data_transform():
    years = []

    female_average_length = []
    female_average_name_length = dict()

    male_average_length = []
    male_average_name_length = dict()

    for index,row in data.iterrows():
        if row['Gender'] == 'F':
            curr_year = row['Year']
            curr_name_length = len(row['Name'])
            if curr_year not in female_average_name_length:
                female_average_name_length[curr_year] = [curr_name_length,1]
            else:
                female_average_name_length[curr_year][0] += curr_name_length
                female_average_name_length[curr_year][1] += 1
        else:
            curr_year = row['Year']
            curr_name_length = len(row['Name'])
            if curr_year not in male_average_name_length:
                male_average_name_length[curr_year] = [curr_name_length,1]
            else:
                male_average_name_length[curr_year][0] += curr_name_length
                male_average_name_length[curr_year][1] += 1


    for key,value in female_average_name_length.items():
        years.append(key)
        female_average_length.append(float(value[0])/value[1])
    for key,value in male_average_name_length.items():
        years.append(key)
        male_average_length.append(float(value[0])/value[1])
    return (female_average_length,female_average_name_length,male_average_length,male_average_name_length)
female_average_length, female_average_name_length, male_average_length, male_average_name_length = average_length_data_transform()
for year in range(1880,1891):
    print('年份：%i，总长：%i，个数：%i'%(year,female_average_name_length.get(year)[0],female_average_name_length.get(year)[1]))
print(female_average_length[:10])

#数据可视化
import matplotlib.pyplot as plt
years = range(1880,2015)
f,ax = plt.subplots(figsize = (10,6))
ax.set_xlim([1880,2014])

plt.plot(years,female_average_length,label='Average length of female',color='r')
plt.plot(years,male_average_length,label='Average length of male',color='b')

ax.set_ylabel('Length of name')
ax.set_xlabel('Year')

ax.set_title('Average length of names')

legend = plt.legend(loc='best',frameon=True,borderpad=1,borderaxespad=1)
plt.show()

