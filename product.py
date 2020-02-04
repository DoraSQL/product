
import os #operating ysytem

#讀取檔案
def read_file(filename): 
    product =[]
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            product.append([name,price])    
    return product

#讓user輸入
def user_input(product):
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
    return product 

#印出所有購買紀錄
def print_products(product):
    for p in product:
        print(p[0], '的價格是', p[1])


#寫入檔案
def write_file(filename, product):
    with open(filename, 'w' , encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p  in product:
            f.write(p[0] + ',' + str(p[1]) + '\n')



def main():
    #確認檔案是否存在
    filename = 'products.csv'
    if os.path.isfile(filename): #檢查檔案在不在
        print('yeah! 找到檔案了!')
        product = read_file(filename) #若檔案存在才執行read_file()
    else:
        print('找不到檔案... 哭哭 >w<')

    product = user_input(product)
    print_products(product)
    write_file('products.csv', product )

main()

