# -*- coding: UTF-8 -*-

# Filename : try_draw4.py
# author by : （学员ID)

# 目的： 进一步了解制作数列的 np.arange
#

import os
import sys
import io

from class_soldier import Soldier

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# --- 以下为通用部分， 凡使用士兵类的都要复制过去 -----
# 设定年龄上限和下限
max_age = 60
min_age = 16
middle_age = (max_age + min_age) / 2

# 设定力气值上下限
max_strength = 90
min_strength = 30

# 设定战斗技巧上下限
max_skill = 50
min_skill = 1
# --- 以上为通用部分， 凡使用士兵类的都要复制过去 -----


# 练习一：产生一个士兵
print("---练习一---")

soldier = Soldier()
print("这个士兵年龄为 (%d), 力气值(%d), 战斗技巧(%d), 装备(%d)" % (soldier.age, soldier.strength, soldier.skill, soldier.equipment))
