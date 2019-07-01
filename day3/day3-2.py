"""
掷骰子决定做什么事情

Author: lkb
"""

from random import randint

face = randint(1,6)
if face == 1:
    print('111')
elif face == 2:
    print('222')
elif face == 3:
    print('333')
elif face == 4:
    print('444')
elif face == 5:
    print('555')
else:
    print('666')
