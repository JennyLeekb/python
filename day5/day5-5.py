"""
玩家摇两颗色子, 如果第一次摇出7点或11点, 玩家胜;如果摇出2点 3点 12点, 庄家胜 
其他情况游戏继续,玩家再次摇色子， 如果摇出7点， 庄家胜；如果摇出第一次摇的点数，玩家胜；否则游戏继续
玩家继续摇色子，玩家进入游戏时有1000元的赌注，全部输光游戏结束。
"""

from random import randint

money = 1000
while money > 0:
    while True:
        debt = int(input('请下注：'))
        if debt>0 and debt<=money :
            break
    a = randint(1,6)
    b = randint(1,6)
    first = a + b
    print('第一次摇出%d'%first)
    need_go_on = False
    if first == 7 or first == 11:
        money += debt
        print('玩家胜！摇出色子数为%d, 钱剩余%d'%(first,money))   
    elif first == 2 or first == 3 or first == 12:
        money -= debt
        print('庄家胜！摇出色子数为%d, 钱剩余%d'%(first,money)) 
    else:
        need_go_on = True
    

    while(need_go_on):
        a = randint(1,6)
        b = randint(1,6)
        num = a + b
        if num == 7:
            money -= debt
            print('庄家胜！摇出色子数为%d, 钱剩余%d'%(num,money)) 
            break
        elif num == first:
            money += debt
            print('玩家胜！摇出色子数为%d, 钱剩余%d'%(num,money)) 
            break
        else:
            need_go_on = True

print('游戏结束')