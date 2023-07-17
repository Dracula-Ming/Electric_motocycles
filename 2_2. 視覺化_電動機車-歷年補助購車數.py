# 用pandas 讀取csv 檔，
# 並將 "銷售數量" 轉為 整數型態
# 連接 MySQL 創建資料表 e_moto_2022
# 並將csv檔的資料寫入資料表

# import MySQLdb
# import pandas as pd

# data = pd.read_csv(r"Python Topic\data\電動機車-近十年補助購車數.csv", header=0, nrows=13, encoding="utf-8-sig")

# data["補助購車輛"] = data["補助購車輛"].astype("int")
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
#     sql1 = """CREATE TABLE IF NOT EXISTS e_moto_tenYears (year VARCHAR(20),
#                                                           quantity int(10))"""

#     # 使用 execute() 來"執行" SQL 語法
#     cursor.execute(sql1)
#     print("資料表建立完成")

#     # SQL 語法: 創建 資料表 及 欄位
#     for i in range(len(data)):
#         sql2 = """INSERT INTO e_moto_tenYears  (year, quantity)
#                                                 VALUES(%s,%b)"""
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
# 連接 SQL
# 使用 panda 讀取 sql(語法 , 連線設定)
# 將資料 繪成 長條圖

import pandas as pd
import matplotlib.pyplot as plt # 圖表模組套件
import MySQLdb
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
    sql  = "SELECT * FROM `e_moto_tenYears`;"
    # 資料讀取
    data = pd.read_sql_query(sql,conn)

    # 設定資料
    year = data["year"]
    quantity = data["quantity"]

    # 顯示中文
    plt.rcParams["font.family"]='Microsoft YaHei'
    plt.rcParams["font.size"]= 14

    # 設定畫布大小
    plt.figure(figsize = (11, 6))

    # 設定 圖表類型 及 相關設定 width= 設長條圖的寬度, tick_label = 設定x軸的刻度名
    plt.bar(year, quantity, width= 0.5, tick_label = year,color="#1F7A8C")
    plt.xlabel("年份",size=16)# 圖表 X軸文字標籤
    plt.ylabel("電動機車數量", size=16)# 圖表 Y軸文字標籤
    plt.title("電動機車-近十年補助購車數\n",size=20) # 圖表 上方文字標籤
    plt.text(7.6,165000,"數據截止至2023/6/9\n資料來源: 電動機車產業網", color='#795663')
    plt.grid(axis="y")

    # 在長條圖上顯示數值
    # 利用繪圖套件的Text() 搭配 For 迴圈
    # 取得每筆資料的座標
    # 再一一輸出至長條圖上方
    # 再使用參數調整置中 及 對齊長條圖上方底部
    # 若要讓數值在長條圖中間，只需要 y軸 除2 即可
    for x, y in zip(year,quantity):
         plt.text(x,y,f"{y:,.0f}", ha='center', va='bottom',fontsize=12, color='r')

    # 顯示圖表
    plt.show()

    # 關閉圖表
    plt.close()

except Exception as e:
    print("資料庫連接失敗: ", e)

finally:
    conn.close()
    print("資料連線結束")