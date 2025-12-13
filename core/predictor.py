import numpy as np

def simple_predict(df):
    nums = []
    for _, row in df.iterrows():
        nums.extend([row[i] for i in ["号1","号2","号3","号4","号5","号6"]])
    from collections import Counter
    cnt = Counter(nums)
    # top6 highest frequency
    top6 = [num for num,_ in cnt.most_common(6)]
    return sorted(top6)
