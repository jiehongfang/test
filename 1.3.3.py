import pandas as pd

# 提供的数据，这里我们直接使用了字符串来表示，但在实际应用中，你可能需要从文件或其他来源读取这些数据
data = {
'Team': ['Riders1', 'Riders2', 'Devils2', 'Devils3', 'Kings3', 'kings4', 'Kings1', 'Kings1', 'Riders2', 'Royals4', 'FRoyals1', 'Riders2'],
'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]
}

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 注意：队伍名称中存在大小写不一致的情况（比如 'Kings3' 和 'kings4'），我们需要将它们统一
# 这里我们选择将所有队伍名称转换为小写
df['Team'] = df['Team'].str.lower()

# 计算每个队伍的平均分（保留两位小数）
average_scores = df.groupby('Team')['Points'].mean().round(2)

# 打印结果看hhh
print(average_scores)
