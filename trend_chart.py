import pandas as pd
import matplotlib.pyplot as plt

def generate_trend_chart(csv_path):
    df = pd.read_csv(csv_path, encoding="utf-8")
    df["留言月份"] = pd.to_datetime(df["dateline_txt"]).dt.to_period("M").astype(str)
    df_grouped = df.groupby(["留言月份", "情绪类型"]).size().unstack(fill_value=0)
    df_grouped = df_grouped.reindex(columns=["正面", "负面"], fill_value=0)

    df_grouped.plot(kind="line", figsize=(10, 5))
    plt.title("反馈趋势图")
    plt.ylabel("留言数量")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/trend.png")
    plt.close()