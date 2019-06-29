"""
将华氏度转化为摄氏度
F = 1.8C + 32

author: lkb
"""

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f 华氏度 = %.1f 摄氏度' % (f,c))