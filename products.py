# 建立空清單
products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q': # quit
        break
    price = input('請輸入商品價格: ')

    # 傳統流程寫法
    # p = [] # 問完商品和價格就先建立一個清單，因為在迴圈中，所以每建立一次就循環回來變空值，輸入後再加到大清單後。
    # p.append(name)
    # p.append(price)

    # 簡易寫法
    # p = [name, price] 
    # products.append(p) # 把小清單 p 加入到大清單 products 中

    # 一行寫法
    products.append([name, price])

print(products) # 印出整個清單

for product in products:
    # print(product) # 印出單筆清單
    print(product[0], '的價格是', product[1]) # 個別印出單筆清單中的第 0 筆資料和第 1 筆資料