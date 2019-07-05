"""
实现判断一个数是不是素数的函数。
"""

def is_prime(num):
    for x in range (2,num):
        if num % x == 0:
            return False
    return True



# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':  
    x = int(input('请输入一个正整数：'))
    if is_prime(x):
        print('%d是素数')
    else:
        print('%d不是素数')