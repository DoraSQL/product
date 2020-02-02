
import os #operating ysytem

product =[]
if os.path.isfile('products.csv'): #檢查檔案在不在
    print('yeah! 找到檔案了!')
    #讀取檔案
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            product.append([name,price])
    print(product)
else:
    print('找不到檔案... 哭哭 >w<')

#讓user輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':  #quit
        break
    price = input('請輸入商品價格: ')
    # p=[]
    # p.append(name)
    # p.append(price)
    # product.append(p)
    price = int(price) 
    product.append([name,price])
print(product)

#印出所有購買紀錄
for p in product:
    print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w' , encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p  in product:
    	f.write(p[0] + ',' + str(p[1]) + '\n')