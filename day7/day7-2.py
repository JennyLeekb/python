def main():
    list1 = [1,3,5,7,100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    #计算列表长度
    print(len(list1))
    #下标（索引）计算
    print(list1[1])
    print(list1[4])
    print(list1[-3])
    print(list1[-1])
    list1[2] = 300
    print(list1)
    #添加元素
    list1.append(200)
    list1.insert(1,400)
    list1 += [1000,2000]
    print(list1)
    print(len(list1))
    #删除元素
    list1.remove(3)
    if 100 in list1:
        list1.remove(100)
    del list1[-1]
    print(list1)
    # 清空列表元素
    list1.clear()
    print(list1)


if __name__ == "__main__":
    main()