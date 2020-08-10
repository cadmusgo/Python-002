import pandas as pd
import numpy as np

# 產生測試資料集
group = ['x', 'y', 'z']
data_size = 50
df = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), data_size)],
    'id': np.random.randint(100, 2000, data_size),
    "age": np.random.randint(15, 50, data_size)
})

# 1. SELECT * FROM data;
print(df)

# 2. SELECT * FROM data LIMIT 10;
print(df.head(10))

# 3. SELECT id FROM data;  //id 是 data # 表的特定一列
print(df['id'])

# 4. SELECT COUNT(id) FROM data;
print(df['id'].count())

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(df[(df['id'] < 1000) & (df['age'] > 30)])
print(df.query(' id < 1000 & age > 30'))

# 6. SELECT id,COUNT(DISTINCT order_id) FROM # table1 GROUP BY id;
df = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 5)],
    'id': ['a', 'a', 'b', 'c', 'a'],
    "order_id": ['1001', '1002', '1003', '1001', '1001']
})
result = df.groupby('id').order_id.nunique()
print(result)

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 # ON t1.id = t2.id;
df1 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 2)],
    'id': ['a1', 'a2'],
    "age": np.random.randint(15, 50, 2)
})
df2 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 2)],
    'id': ['a1', 'a2'],
    "age": np.random.randint(15, 50, 2)
})
res = pd.merge(df1, df2, on='id')
print(res)

# 8. SELECT * FROM table1 UNION SELECT * FROM # table2;
print(pd.concat([df1, df2]))

# 9. DELETE FROM table1 WHERE id=10;
print(df[df['id'] != 10])

# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(df.drop(['id'], axis=1))
