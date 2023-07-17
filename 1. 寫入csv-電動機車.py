import csv
""" 
fn = '電動機車-補助購車數.csv'

with open(fn, 'w', newline='', encoding='utf-8-sig') as csvFile:

    csvWiter = csv.writer(csvFile)
    csvWiter.writerow(['年份','補助購車輛'])
    csvWiter.writerow(['102年','6625'])
    csvWiter.writerow(['103年','4442'])
    csvWiter.writerow(['104年','9765'])
    csvWiter.writerow(['105年','18942'])
    csvWiter.writerow(['106年','39025'])
    csvWiter.writerow(['107年','78676'])
    csvWiter.writerow(['108年','173033'])
    csvWiter.writerow(['109年','93244'])
    csvWiter.writerow(['110年','88311'])
    csvWiter.writerow(['111年','79138'])
    csvWiter.writerow(['112年','25907'])
    print("寫入成功")
 """
#%%
""" 
fn = '電動機車-歷年法人購車用途.csv'

with open(fn, 'w', newline='', encoding='utf-8-sig') as csvFile:

    csvWiter = csv.writer(csvFile)
    csvWiter.writerow(['電動機車數量','購車用途'])
    csvWiter.writerow(['14668','租賃使用'])
    csvWiter.writerow(['13909','共享租賃'])
    csvWiter.writerow(['5384','業務使用'])
    csvWiter.writerow(['3735','展示推廣'])
    csvWiter.writerow(['1679','郵務使用'])
    csvWiter.writerow(['5701','其他'])
    print("寫入成功")
 """
#%%
""" 
fn = '電動機車-法人購車品牌傾向.csv'

with open(fn, 'w', newline='', encoding='utf-8-sig') as csvFile:

    csvWiter = csv.writer(csvFile)
    csvWiter.writerow(['電動機車數量','購車品牌'])
    csvWiter.writerow(['6014','威摩科技'])
    csvWiter.writerow(['5509','睿能數位'])
    csvWiter.writerow(['4400','和雲行動'])
    csvWiter.writerow(['3241','中華郵政'])
    csvWiter.writerow(['1680','艾上綠能'])
    csvWiter.writerow(['24232','其他'])
    print("寫入成功")
 """
#%%

fn = '電動機車-歷年車廠申請購車補助數量.csv'

with open(fn, 'w', newline='', encoding='utf-8-sig') as csvFile:

    csvWiter = csv.writer(csvFile)
    csvWiter.writerow(['電動機車數量','車廠品牌'])
    csvWiter.writerow(['486891','睿能'])
    csvWiter.writerow(['55383','中華'])
    csvWiter.writerow(['30625','光陽'])
    csvWiter.writerow(['29182','宏佳騰'])
    csvWiter.writerow(['33195','其他'])
    print("寫入成功")