# -*- coding: UTF-8 -*-

# Filename : try_draw4.py
# author by : （学员ID)

# 目的： 进一步了解制作数列的 np.arange
#

import os
import sys
import io

#from class_soldier import Soldier
from class_army import Army


# 解决输出显示汉字乱码的问题
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 练习一： 生成一只 n 人的军队， 并命名
print("---练习一---")

soldiers_of_army = 10000

my_first_army = Army()
my_first_army.recruit(soldiers_of_army)
my_first_army.army_name = '我的一号军团'


# 练习二：检阅军队
print("---练习二---")
#my_first_army.alive = 0
my_first_army.overview()

# 练习三：查看军队的战斗力


