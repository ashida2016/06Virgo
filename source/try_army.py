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

# 练习一： 招募一只 n 人的军队， 并命名
print("---练习一---")

soldiers_of_army = 50

my_first_army = Army()
my_first_army.recruit(soldiers_of_army)

name = input("请输入军团名称：")
my_first_army.army_name = name

print("招募了一只军团如下：")
my_first_army.simple_view()

# 练习二：检阅军队
print("---练习二---")
my_first_army.simple_view()
my_first_army.overview()

# 练习三：解散军队
print("---练习三---")
#my_first_army.dismiss()
#my_first_army.simple_view()
#my_first_army.overview()

# 联系四： 训练军队
print("---练习四---")

# 训练一次
print("开始训练 1 次......")

before = my_first_army.cal_fighting_capacity()
my_first_army.training()
after = my_first_army.cal_fighting_capacity()

print("本次训练前战力为： %.2f,  本次训练后战力为： %.2f， 提升了 %.2f 的战力，提升比例为 %.1f%%" % \
      (before, after, after-before, (after-before)/before*100 ))

# 训练 n 次，查看效果
times = 40
print("开始训练 %d 次......" %(times))

before = my_first_army.cal_fighting_capacity()
for i in range(1, times):
      my_first_army.training()
after = my_first_army.cal_fighting_capacity()

print("本次训练前战力为： %.2f,  本次训练后战力为： %.2f， 提升了 %.2f 的战力，提升比例为 %.1f%%" % \
      (before, after, after-before, (after-before)/before*100 ))
my_first_army.overview()



