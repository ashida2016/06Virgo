# -*- coding: UTF-8 -*-

# Filename : class_soldier.py
# author by : （学员ID)

# 目的：
#      巩固类的开发方法， 制作一个士兵类
#

import os
import sys
import io

# import pandas as pd
import random

import numpy as np
import matplotlib.pylab as plt

# 解决输出显示汉字乱码的问题
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码
#plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

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


class Soldier:

    def __init__(self):
        # 士兵年纪
        self.age = random.randint(min_age, max_age)

        # 士兵初始力气
        self.strength = random.randint(min_strength, max_strength)

        # 士兵初始战斗技巧
        self.skill = random.randint(min_skill, max_skill)

        # 士兵初始战斗装备一律为无
        self.equipment = 0

        # 该士兵是否还活着
        self.is_alive = 1

        # 士兵个人战斗力
        self.fighting_capacity = self.cal_fighting_capacity()

        return

    def cal_fighting_capacity(self):
        fcap = (self.skill ** 3 + self.strength ** 2 + self.equipment) / self.age ** 0.5
        return fcap
