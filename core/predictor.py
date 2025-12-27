from collections import Counter

def simple_predict(data_list):
    """
    data_list: list of dict, e.g. [{'号1': 10, '号2': 20, ..., 'date': '2025,361'}, ...]
    """
    nums = []
    for row in data_list:
        for key in ["号1", "号2", "号3", "号4", "号5", "号6"]:
            if key in row:
                try:
                    num = int(row[key])
                    nums.append(num)
                except (ValueError, TypeError):
                    continue
    cnt = Counter(nums)
    top6 = [num for num, _ in cnt.most_common(6)]
    # 如果不足6个，用1~49补全（可选）
    if len(top6) < 6:
        all_nums = set(range(1, 50))
        top6 = top6 + sorted(all_nums - set(top6))[:6 - len(top6)]
    return sorted(top6)
