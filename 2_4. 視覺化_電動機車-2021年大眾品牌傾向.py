# 用pandas 讀取csv 檔，
# 並將 "銷售數量" 轉為 整數型態
# 連接 MySQL 創建資料表 e_moto_2022
# 並將csv檔的資料寫入資料表

# import MySQLdb
# import pandas as pd

# data = pd.read_csv(r"Python Topic\data\2021年-各車廠總銷售量.csv", header=0, nrows=9, encoding="utf-8-sig")

# data["銷售數量"] = data["銷售數量"].astype("int")
# try:
#     # 開啟資料庫連接
#     conn = MySQLdb.connect (host="127.0.0.1",     # 主機名稱
#                             user="root",          # 帳號
#                             password="Ray009KCT", # 密碼
#                             database= "ming",     # 選擇資料庫
#                             port=3306,            # port
#                             autocommit=True)      # 自動提交模式
    
#     # 使用 cursor() 函式 操作資料庫
#     cursor = conn.cursor()

#     # SQL 語法: 創建 資料表 及 欄位
#     sql1 = """CREATE TABLE IF NOT EXISTS e_moto_2021   (brand VARCHAR(20),
#                                                         sell int(10))"""

#     # 使用 execute() 來"執行" SQL 語法
#     cursor.execute(sql1)
#     print("資料表建立完成")

#     # SQL 語法: 創建 資料表 及 欄位
#     for i in range(len(data)):
#         sql2 = """INSERT INTO e_moto_2021  (brand, sell)
#                                             VALUES(%s,%b)"""
#         var = (data.iloc[i,0],data.iloc[i,1])
#         cursor.execute(sql2,var)
    
#     print("資料寫入完成")
# except Exception as e:
#     print("資料庫連接失敗")

# finally:
#     cursor.close()
#     conn.close()
#     print("資料庫連線結束")


#%%
# 連接 MySQL
# 使用 panda 讀取 sql(語法 , 連線設定)
# 將資料 繪成 圓餅圖
import MySQLdb
import pandas as pd
import matplotlib.pyplot as plt
try:
    conn = MySQLdb.connect(host = "127.0.0.1",     # 主機名稱
                           user = "root",          # 帳號
                           password = "Ray009KCT", # 密碼
                           port = 3306,            # Port
                           database = "ming",      # 選擇資料庫
                           charset = "utf8",       # 設定編碼
                           autocommit=True)        # 自動提交模式
    # 使用cursor()方法操作資料庫
    cursor = conn.cursor()
    sql  = "SELECT * FROM `e_moto_2021`;"
    # 資料讀取
    data = pd.read_sql_query(sql,conn)


    # 設定資料
    brand = data["brand"]
    quantity = data["sell"]
    colors = ["#DAB2D3","#EAC9C0","#9EDAE3","#65C4D8","#6494E8","#84C0E9","#7CC5B8"]
    space = [0.1,0.02,0,0,0,0,0]

    # 顯示中文
    plt.rcParams["font.family"]='Microsoft YaHei'
    plt.rcParams["font.size"]= 16

    # 設定畫布大小
    plt.figure(figsize = (11, 7))

    # 設定圓餅圖 及 相關資料 (數值, 各項標籤, 顏色, 陰影, 間距, 離圓心距, 百分比)
    plt.pie(quantity,             # 數值
            labels = brand,       # 各項標籤
            colors = colors,      # 顏色
            shadow = True,        # 陰影
            explode = space,      # 間距
            pctdistance = 0.8,    # 數字距離圓心的距離
            autopct = "%1.1f%%")  # 百分比設定於小數點第一位

    # 設定為正圓
    plt.axis('equal')

    # 設定圖例 及 位置
    plt.legend(loc = "upper right")

    # 設定標題
    plt.title("2021年-電動機車大眾品牌傾向", size = 20)

    # 顯示圖表
    plt.show()

    # 關閉圖表
    plt.close()

except Exception as e:
    print("資料庫連接失敗: ", e)

finally:
    conn.close()
    print("資料連線結束")