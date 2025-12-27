import pandas as pd

def load_history(path):
    df = pd.read_csv(path, encoding="utf-8")
    cols = ["年份", "期号", "号1", "号2", "号3", "号4", "号5", "号6"]
    df = df[cols]
    # 新增：构造 date 字段，并转为字典列表
    records = []
    for _, row in df.iterrows():
        record = {
            "date": f"{int(row['年份'])},{int(row['期号'])}",
            "号1": int(row["号1"]),
            "号2": int(row["号2"]),
            "号3": int(row["号3"]),
            "号4": int(row["号4"]),
            "号5": int(row["号5"]),
            "号6": int(row["号6"]),
        }
        records.append(record)
    return records
