import pandas as pd
import matplotlib.pyplot as plt

#%%
# 讀取SQL資料庫的資料表
# 經過排序後
# 輸出折線圖表
import MySQLdb
try:
    # 開啟資料庫連接
    conn = MySQLdb.connect (host="127.0.0.1",     # 主機名稱
                            user="root",          # 帳號
                            password="Ray009KCT", # 密碼
                            database= "ming",  # 選擇資料庫
                            port=3306,            # port     
                            charset="utf8")       # 資料庫編碼
    
     # 使用cursor()方法操作資料庫
    cursor = conn.cursor()

    # SQL語法: 查詢資料表的所有資料
    sql = ("SELECT * FROM `e_moto`;")
    # 執行語法
    df = pd.read_sql_query(sql,conn)

    df['year'] = df['year'].astype(str)

    # 篩選出2019~2023的數據
    selected_years = ['2019','2020','2021', '2022', '2023']
    df_selected_years = df[df['year'].isin(selected_years)]

    # 進行分組並計算每個年份和月份的銷售總量
    grouped = df_selected_years.groupby(['year', 'month'])['sell'].sum().reset_index()

    # 顯示中文
    plt.rcParams["font.family"]='Microsoft YaHei'
    plt.rcParams["font.size"]= 16

    # 建立畫布和子圖
    fig, ax = plt.subplots()
   
    # 遍歷每個年份，繪製折線圖
    for year in selected_years:
        year_data = grouped[grouped['year'] == year]
        x = year_data['month']
        y = year_data['sell']
        # 對 x 和 y 數據進行排序
        x_sorted = sorted(x, key=lambda month: int(month))
        y_sorted = [y for _, y in sorted(zip(x, y), key=lambda month: int(month[0]))]
        ax.plot(x_sorted, y_sorted, label=year)

    # 添加圖例
    ax.legend()

    # 設定圖表標題和軸標籤
    plt.title('2019-2023年每個月份的總銷售量',size="20")
    plt.xlabel('月份')
    plt.ylabel('總銷售量')
    plt.text(4,52000,"2023年的數據截止到4月\n資料來源: 各大機車資訊網", color='b',size=14)
    plt.grid(axis="y")

    # 顯示圖表
    plt.show()

    # 關閉圖表
    plt.close()

except Exception as e:
    print("資料庫連接失敗: ", e)

finally:
    conn.close()
    print("資料連線結束")
