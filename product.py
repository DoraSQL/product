
product =[]
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':  #quit
        break
    price = input('請輸入商品價格: ')
    # p=[]
    # p.append(name)
    # p.append(price)
    # product.append(p)
    product.append([name,price])
print(product)


for p in product:
    print(p[0], '的價格是', p[1])


with open('products.csv', 'w') as f:
    for p  in product:
    	f.write(p[0] + ',' + p[1] + '\n')