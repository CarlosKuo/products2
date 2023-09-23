# 讀取檔案
products = [] # 建立空清單
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        # 詳細寫法
        # strip() 去除換行和空格符號，split() 用逗點切割
        # s = line.strip().split(',')
        # name = s[0]
        # price = s[1]
        if '商品,價格' in line: # 跳過第一列的名稱敘述
            continue
        # 簡易寫法
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q': # quit
        break
    price = input('請輸入商品價格: ')
    price = int(price)

    # 詳細流程寫法
    # p = [] # 問完商品和價格就先建立一個清單，因為在迴圈中，所以每建立一次就循環回來變空值，輸入後再加到大清單後。
    # p.append(name)
    # p.append(price)

    # 簡易寫法
    # p = [name, price] 
    # products.append(p) # 把小清單 p 加入到大清單 products 中

    # 一行寫法
    products.append([name, price])
print(products) # 印出整個清單

# 印出所有購買紀錄
for product in products:
    # print(product) # 印出單筆清單
    print(product[0], '的價格是', product[1]) # 個別印出單筆清單中的第 0 筆資料和第 1 筆資料


# 寫入檔案
# 加入編碼參數(encoding)解決中文字問題
with open('products.csv', 'w', encoding='utf-8') as file:
    # 第一行寫名稱
    file.write('商品,價格\n')
    # 從 products 一個一個取東西出來放到變數 product 去做存取動作
    for product in products:
        # 檔案寫入 - write() 函式如要字串串起來要用 + 號，如果用逗點會認為參數，而 write() 這函式沒有額外參數，所以會報錯
        file.write(product[0] + ',' + str(product[1]) + '\n')
