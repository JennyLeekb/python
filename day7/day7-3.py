def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    #循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end = ' ')
    print()
    # 列表切片
    print(fruits[1:4])
    # fruit3 = fruits  # 没有复制列表只创建了新的引用
    # 可以通过完整切片操作来复制列表
    fruitsCopy = fruits[:]
    print(fruitsCopy)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)





if __name__ == "__main__":
    main()