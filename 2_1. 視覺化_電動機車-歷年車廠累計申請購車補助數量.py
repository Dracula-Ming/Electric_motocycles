# 長條圖 (X、Y軸需要 1對1)
# bar(left, height[選擇性參數1 = 值1, 選擇性參數2 = 值2,....])
import pandas as pd
import matplotlib.pyplot as plt # 圖表模組套件

# 設定資料
data = pd.read_csv("Python Topic\data\電動機車-歷年車廠累計申請購車補助數量.csv")
quantity = data["電動機車數量"]
brand = data["車廠品牌"]

# 顯示中文
plt.rcParams["font.family"]='Microsoft YaHei'
plt.rcParams["font.size"]= 14

# 設定畫布大小
plt.figure(figsize = (11, 6))

# 設定 圖表類型 及 相關設定 width= 設長條圖的寬度, tick_label = 設定x軸的刻度名
bars = plt.bar(brand, quantity, width= 0.5, tick_label = brand,color="#6495ED")
plt.xlabel("車廠品牌",size=16)
plt.ylabel("電動機車補助數量", size=16)
plt.title("電動機車-歷年車廠累計申請購車補助數量\n",size=20)
plt.text(3.1,450000,"數據截止至2023/6/9\n資料來源: 電動機車產業網", color='b')
plt.grid(axis="y")

# 在長條圖上顯示文字
for bar in bars:
    height = bar.get_height()
    ave = (height / sum(quantity)) * 100
    plt.text(bar.get_x() + bar.get_width() / 2, height, f"{height:,.0f}", ha='center', va='bottom',fontsize=12, color='r')
    plt.text(bar.get_x() + bar.get_width() / 2, height/1.7, f"{ave:.1f}%", ha='center', va='top')

# 顯示圖表
plt.show()

# 關閉圖表
plt.close()