# -*- coding: UTF-8 -*-

# Filename : class_soldier.py
# author by : （学员ID)

# 目的：
#      巩固类的开发方法， 制作一个士兵类
#

import random
import datetime

from class_global_const import GlobalConst
from class_naming_machine import NamingMachine

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

        # 启动一个起名机，为士兵取名
        nm = NamingMachine()
        self.fullname = nm.pick_full_name()

        # 士兵入伍日期
        self.attended_time = datetime.datetime.now()

        # 士兵年纪，初始值随机，
        # 组建军队时会被按正态分布重置
        # 补充兵员时会随机生成
        self.age = random.randint(cst.min_age, cst.max_age)

        # 士兵初始力气
        self.strength = random.uniform(cst.min_strength, cst.max_strength * 0.9)

        # 士兵的当前体力
        self.power = cst.max_power

        # 士兵初始战斗技巧
        self.skill = random.uniform(cst.min_skill, cst.max_skill * 0.5)

        # 士兵初始战斗经验
        self.experience = random.uniform(cst.min_experice, cst.max_experice * 0.5)

        # 士兵初始战斗装备一律为无
        self.equipment = 0

        # 该士兵是否还活着
        self.is_alive = 1

        # 士兵死亡时间
        # self.death_time = cst.forever

        # 士兵个人战斗力，均为实时计算，不存储
        # self.fighting_capacity = self.cal_fighting_capacity()

        return

    # 计算士兵的实时战力
    def cal_fighting_capacity(self):

        fcap = 0
        if self.is_alive > 0:
            # 0 体力时战斗力为 0%， 100体力时战斗力为 100%
            fcap = ((self.skill ** 3 + self.strength ** 2 + self.experience ** 2 + self.equipment) / self.age ** 0.5) * self.power / 100

        return fcap
    
    # 士兵自我汇报信息
    def report_me(self):

        s_live_die = ''
        if self.is_alive > 0:
            s_live_die = '(√ 活着)'
        else:
            s_live_die = '(★ 阵亡)'


        print("我叫 %s%s， 年龄 %d， 入伍日期 %s， 力气值 %.2f, 战斗技巧 %.2f，战斗经验 %.2f， 战斗装备 %d， 当前体力 %d， 当前战力 %.2f" % \
              (self.fullname, s_live_die, self.age, self.attended_time.strftime('%Y-%m-%d %H:%M:%S'), \
               self.strength, self.skill, self.experience, self.equipment, \
               self.power, self.cal_fighting_capacity()
               ))
        
        return 

