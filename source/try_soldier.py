# -*- coding: UTF-8 -*-

# Filename : try_draw4.py
# author by : （学员ID)

# 目的： 进一步了解制作数列的 np.arange
#

import os
import sys
import io

from class_soldier import Soldier
from class_naming_machine import NamingMachine

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
nm = NamingMachine()
soldier.fullname = nm.pick_full_name()

print("这个士兵叫(%s)，年龄为 (%d), 力气值(%d), 战斗技巧(%d), 装备(%d), 战斗力(%d)" %  \
        (soldier.fullname, soldier.age, soldier.strength, soldier.skill, soldier.equipment, soldier.fighting_capacity))

# 练习二：产生 100个士兵，选出战斗力最高的士兵打印出其信息
numbers = 100
soldiers = []
max_fcap = -1
max_index = -1
for i in range(numbers):
    s = Soldier()
    s.fullname = nm.pick_full_name()
    soldiers.append(s)
    if s.fighting_capacity > max_fcap:
        max_fcap = s.fighting_capacity
        max_index = i

print("战斗力最强的士兵叫(%s), 年龄为 (%d), 力气值(%d), 战斗技巧(%d), 装备(%d), 战斗力(%d)" % \
        (soldiers[max_index].fullname, soldiers[max_index].age, soldiers[max_index].strength,  \
         soldiers[max_index].skill, soldiers[max_index].equipment, soldiers[max_index].fighting_capacity))

# 练习三：计算两个士兵的交战

# 练习四：计算士兵随着年龄增长的战斗力变化（制图）
