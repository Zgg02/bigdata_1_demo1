import pandas as pd
import numpy as np

# df = pd.DataFrame(np.random.randn(10,3))
# col = df[1]
# # 求绝对值
# a = np.abs(col)
# print(col[np.abs(col)>1])

# 置换与随机抽样
# df = pd.DataFrame(np.arange(20).reshape(5,4))
# s = np.random.permutation(5)
# # print(df.take(s))
# print(df.sample(n=3,axis=1))

data = {
    "key":['a','b','c'],
    "num":range(3)
}
df = pd.DataFrame(data)
print(df)
print(pd.get_dummies(df['key']))

print("==================")
data = {
        "key":['b','b','a','c','a','b'],
        "num":range(6)
}
df = pd.DataFrame(data)
print(pd.get_dummies(df['key']))