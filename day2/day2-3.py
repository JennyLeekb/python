"""
输入年份 如果是闰年输出True 否则输出False


author: lkb
"""

year = int(input('请输入年份： '))
is_leep = (year%4==0 and year%100!=0 or year%400==0)
print(is_leep)

