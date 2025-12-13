import numpy as np

def predict_next(df):

    recent = df.tail(300)

    nums = []
    for i in range(1, 7):
        nums.extend(list(recent[f"号{i}"]))

    nums = np.array(nums)
    unique, counts = np.unique(nums, return_counts=True)

    # 出现次数排序
    sorted_idx = np.argsort(-counts)
    top6 = unique[sorted_idx][:6].tolist()

    # 概率
    prob = np.mean(counts[sorted_idx][:6] / np.sum(counts)) * 100

    return top6, prob

