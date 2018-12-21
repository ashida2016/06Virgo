# -*- coding: UTF-8 -*-

# Filename : try_war.py
# author by : （学员ID)

# 目的： 进一步了解制作数列的 np.arange
#

import os
import sys
import io


from class_soldier import Soldier
from class_army import Army
from class_war import War


# 解决输出显示汉字乱码的问题
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

war = War()
# 练习一： 随机生成2个士兵， 并让其决斗
print("\n---练习一---")
print("战斗前.....")
sd1 = Soldier()
sd1.report_me()

sd2 = Soldier()
sd2.report_me()

opponent = [sd1, sd2]
war.fight_of_2_soldiers(opponent)
print("战斗后.....")
sd1.report_me()
sd2.report_me()


# 练习二： 随机生成2只军队，让其进行战斗
print("\n---练习二---")

soldiers_of_army = 500000
my_first_army = Army()
my_first_army.recruit(soldiers_of_army)
my_first_army.army_name = '岳家军'
# 仅对第一只军队进行训练
for i in range(1, 30):
      my_first_army.training()
      my_first_army.recuperate()  # 训练一次后必须马上恢复体力才能得出正确的战力值
print("招募并训练了(1)军团如下：")
my_first_army.simple_view()


soldiers_of_army = 650000
my_second_army = Army()
my_second_army.recruit(soldiers_of_army)
my_second_army.army_name = '陌刀队'
print("招募了(2)军团如下：")
my_second_army.simple_view()

opponent = [my_first_army, my_second_army]
war.fight_of_2_armies(opponent)

print("\n。。。战斗后情况。。。")
my_first_army.simple_view()
my_second_army.simple_view()
