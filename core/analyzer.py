from collections import Counter

def count_frequency(df):
    nums = []
    for _, row in df.iterrows():
        nums.extend([row[i] for i in ["号1","号2","号3","号4","号5","号6"]])
    return dict(Counter(nums))

