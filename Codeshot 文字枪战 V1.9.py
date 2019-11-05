# 文字枪战 V1.9

import random
AIammo = 0
AIHP = 2
playerAmmo = 0
playerHP = 2
dead = 0
yes = 'Y'
dicition = yes
sessions = 0
giftAmmo = random.randint(5,15)
giftHP = random.randint(1,5)

print("<===============>")
print("文字枪战 V1.9.0")
print("<===============>")
print("")

#大循环

while dicition == yes:

    sessions = 0
    
    while dead == 0:
        
        sessions += 1
        
        #AI部分：
        
        RandomMax = random.randint(0,20)
        dicitionNumber = int(RandomMax)
        

        if dicitionNumber <= 10:            
            AIdicition = ("保护我")

        if dicitionNumber > 10 and dicitionNumber <= 13:
            AIdicition = ("上子弹")
            AIammo = AIammo + 1
            
            if sessions == 1:
                AIammo = 0

        if AIammo > 0 and dicitionNumber > 13 <= 20:
            AIdicition = ("开枪")

        if AIammo == 0 and dicitionNumber > 13:
            if AIammo > 0:
                AIdicition = ("开枪")
            else:
                AIammo = AIammo + 1
                AIdicition = ("上子弹")

                if sessions == 1:
                    AIammo = 0

        #AI高级判定:
                    
        RandomMax2 = random.randint(1,2)
        dicitionNumber2 = int(RandomMax)

        if playerAmmo == 0 and sessions != 1:

            if dicitionNumber2 == 1:
                
                AIdicition = ("上子弹")
                AIammo = AIammo + 1

            if dicitionNumber2 == 2 and AIammo > 0:

                AIdicition = ("开枪")

            if dicitionNumber2 == 2 and AIammo < 0:

                AIammo = AIammo + 1
                AIdicition = ("上子弹")

                if sessions == 1:
                    AIammo = 0

            if sessions == 1:
                AIammo = 0

        if sessions == 1:
            AIdicition = ("上子弹")
            AIammo += 1
                
        if sessions == 20:
            print (">>>AI变异体出现!!!<<<")
            print ("")
            AIammo += 6
            AIHP += 3
            print ("目前AI状态;血量={0},子弹数量={1}".format(AIHP,AIammo))
            print ("")

        print ("")        
        print ("===>AI已准备好")
        print ("")

        #玩家部分：
        
        if sessions == 17:
            print ("")
            print ("空投已布置")
            print ("")
            playerdicition = input("你的决定(保护我，上子弹，开枪，捡空投):")

            while playerdicition not in {'保护我','上子弹','开枪','捡空投'}:
                
                payerdicition = input("不合法的格式，请重新输入:")

                
        else:
            playerdicition = input("你的决定(保护我，上子弹，开枪):")
            
            while playerdicition not in {'保护我','上子弹','开枪'}:

                print ("")
                
                playerdicition = input("不合法的格式，请重新输入:")
            
        
        #攻击判定:


        if AIdicition == ("保护我") and playerdicition == ("保护我"):
            print ("")
            print (">>>双开护盾，无伤回合")
            print ("")
            print ("++++++++++++++++++++++++++++++++++++++++++++++++")
            
        if AIdicition == ("保护我") and playerdicition == ("上子弹"):
            playerAmmo = playerAmmo + 1
            print ("")
            print (">>>无伤回合，玩家子弹加一，玩家剩余子弹：{0}".format(playerAmmo))
            print ("")
            print ("++++++++++++++++++++++++++++++++++++++++++++++++")
            
        if AIdicition == ("保护我") and playerdicition == ("开枪"):
            print ("")
            print (">>>AI开启护盾")
            
            if playerAmmo == 0:
                print ("")
                print (">>>弹药不足，攻击无效")
                print ("")
                print ("++++++++++++++++++++++++++++++++++++++++++++++++")
            else:
                playerAmmo = playerAmmo - 1
                print ("")
                print (">>>玩家射在了AI的护盾上,玩家剩余弹药：{0}".format(playerAmmo))
                print ("")
                print ("++++++++++++++++++++++++++++++++++++++++++++++++")

        if AIdicition == ("上子弹") and playerdicition == ("保护我"):
            print ("")
            print (">>>无伤局，AI上子弹，AI子弹加一，AI子弹剩余:{0}".format(AIammo))
            print ("")
            print ("++++++++++++++++++++++++++++++++++++++++++++++++")

        if AIdicition == ("上子弹") and playerdicition == ("上子弹"):
            playerAmmo = playerAmmo + 1
            print ("")
            print (">>>无伤局，双方子弹数都加一，AI子弹剩余:{0};玩家子弹剩余:{1}".format(AIammo,playerAmmo))
            print ("")
            print ("++++++++++++++++++++++++++++++++++++++++++++++++")
            
        if AIdicition == ("上子弹") and playerdicition == ("开枪"):
            
            if playerAmmo == 0:
                print ("")
                print (">>>子弹数量不足，攻击无效;AI子弹加一")
                print ("")
                print ("++++++++++++++++++++++++++++++++++++++++++++++++")
            else:
                playerAmmo -= 1
                AIammo -= 1
                print ("")
                print (">>>玩家在AI上子弹的过程中射中了AI")
                print ("")
                print (">>>玩家子弹剩余{0}".format(playerAmmo))
                AIHP -= 1
                print ("")
                print (">>>AI还剩{0}条命".format(AIHP))
                print ("")
                
                if AIHP == 0:
                    dead += 1
                    print ("")
                    print (">>>玩家干掉了AI")
                    print ("")

        if AIdicition == ("开枪") and playerdicition == ("保护我"):
            AIammo = AIammo - 1
            print ("")
            print (">>>AI开枪，但射在了玩家的护盾上，AI剩余子弹：{0}".format(AIammo))
            print ("")
            print ("++++++++++++++++++++++++++++++++++++++++++++++++")

        if AIdicition == ("开枪") and playerdicition == ("上子弹"):
            AIammo -= 1
            print ("")
            print (">>>AI打中了了玩家")
            print ("")
            print (">>>AI子弹剩余{0}".format(AIammo))
            playerHP -= 1
            print ("")
            print (">>>玩家还剩{0}条命".format(playerHP))
            print ("")
            
            if playerHP == 0:
                dead += 1
                print ("")
                print (">>>AI干掉了玩家")
                print ("")
                
        if AIdicition == ("开枪") and playerdicition == ("开枪"):
            AIammo = AIammo - 1
            if playerAmmo > 0:
                playerAmmo = playerAmmo - 1
                print ("")
                print (">>>双方开枪，平局，玩家子弹剩余{0};AI子弹剩余{1}".format(playerAmmo,AIammo))
                print ("")
                print ("++++++++++++++++++++++++++++++++++++++++++++++++")
            else:
                print ("")
                print (">>>双方开枪，但玩家子弹不足，被AI爆头")
                print ("")
                dead = dead + 1



        if playerdicition == ("捡空投") and sessions == 17:
            print ("")
            print ("!!!恭喜你从空投中捡到了{giftAmmo}颗子弹和{giftHP}条命!!!".format(giftAmmo = giftAmmo,giftHP = giftHP))
            print ("")
            playerAmmo = playerAmmo + giftAmmo
            playerHP = playerHP + giftHP
            print ("++++++++++++++++++++++++++++++++++++++++++++++++")
            
    dicition = input("是否重新开始？(Y/n):")
    while dicition not in {'Y','y','n','N'}:
        
        dicition = input("不合法的格式，请重新输入(Y/n)")

    #二次初始化：
    
    if dead == 1:
        dead = 0

    print ("你用了{0}个回合".format(sessions))
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::")
    AIammo = 0
    AIHP = 2
    playerAmmo = 0
    playerHP = 2

print("游戏结束")
        

        

