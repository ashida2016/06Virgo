# -*- coding: UTF-8 -*-

# Filename : class_soldier.py
# author by : （学员ID)

# 目的：
#      巩固类的开发方法， 制作一个士兵类
#

import random
import datetime

from class_global_const import GlobalConst
"""
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
"""

class Soldier:

    def __init__(self):

        cst = GlobalConst()

        # 士兵姓名，初始值为无名氏
        self.fullname = ''

        # 士兵入伍时间
        self.attended_time = datetime.datetime.now()

        # 士兵年纪，初始值随机，组建军队时必须按正态分布重置
        self.age = random.randint(cst.min_age, cst.max_age)

        # 士兵初始力气
        self.strength = random.uniform(cst.min_strength, cst.max_strength * 0.9)

        # 士兵初始战斗技巧
        self.skill = random.uniform(cst.min_skill, cst.max_skill * 0.5)

        # 士兵初始战斗经验
        self.experience  = random.uniform(cst.min_experice, cst.max_experice * 0.5)

        # 士兵初始战斗装备一律为无
        self.equipment = 0

        # 该士兵是否还活着
        self.is_alive = 1

        # 士兵死亡时间
        # self.death_time = cst.forever

        # 士兵个人战斗力
        self.fighting_capacity = self.cal_fighting_capacity()

        return

    # 计算士兵的实时战力
    def cal_fighting_capacity(self):

        fcap = 0
        if self.is_alive > 0:
            fcap = (self.skill ** 3 + self.strength ** 2 + self.experience ** 2 + self.equipment) / self.age ** 0.5

        return fcap
