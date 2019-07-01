"""
英制单位英寸和公制单位厘米互换

Author: lkb
"""

value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%.3f 英寸 = %.3f 厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.3f 厘米 = %.3f 英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')