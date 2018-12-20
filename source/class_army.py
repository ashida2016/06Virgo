# -*- coding: UTF-8 -*-

# Filename : class_army.py
# author by : （学员ID)

# 目的：
#

import os
import sys
import io

import numpy as np
import matplotlib.pylab as plt

import random
import datetime

from class_soldier import Soldier
from class_naming_machine import NamingMachine

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


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

class Army:

    def __init__(self):

        self.cst = GlobalConst()    # 在本类内部保持这些常数
        self.army_code = 'Unkown'   # 军团番号
        self.army_name = 'Unkown'   # 军团名称

        self.created = datetime.datetime.now()    # 成立日期（当前计算机时间）
        self.dismissed = self.cst.forever         # 解散日期 大于当前日期视为还没解散

        self.soldiers = []          # 士兵个体
        self.alives = 0             # 军团存活人数
        self.fighting_capacity = 0  # 总战斗力

        return

    # 招募军队
    def recruit(self, numbers):

        # 为新军团设定番号，默认命名及设定人数
        self.army_code = random.randint(10000, 99999)
        self.army_name = '新的军团-' + str(self.army_code)
        self.alives = numbers

        # 先自动生成 N 个士兵对象
        for i in range(numbers):
            self.soldiers.append(Soldier())

        # 对士兵年龄按 正态分布 方式重置
        mu = self.cst.middle_age
        sigma = int(self.cst.middle_age / 4 - 1)
        new_ages = np.random.normal(mu, sigma, numbers)

        # 重新赋予年龄
        i = 0
        for s in self.soldiers:
            # 将正态分布的年龄赋予士兵
            s.age = int(new_ages[i])
            # 应对极端情况的保护
            if s.age > self.cst.max_age:
                s.age = self.cst.max_age
            elif s.age < self.cst.min_age:
                s.age = self.cst.min_age
            # 下标 + 1
            i += 1

        # 最后更新军团总战力，战力均为实时计算，不保存
        # self.fighting_capacity = self.cal_fighting_capacity()

        return

    # 解散军队
    def dismiss(self):

        for s in self.soldiers:
            s.is_alive = 0

        self.alives = 0
        self.dismissed = datetime.datetime.now()    # 成立日期（当前计算机时间）

        return

    # 计算军队战斗力
    def cal_fighting_capacity(self):

        fcap = 0

        if self.alives > 0:      # 仅当军团还有活人时计算
            for s in self.soldiers:
                if s.is_alive:  # 仅当士兵本人还活着时计算
                    fcap += s.cal_fighting_capacity()   # 永远取士兵的最新战斗力值

        return fcap

    # 复杂模式查看军队 - 绘制军队全景图
    def overview(self):

        if self.alives > 0:

            # 汇总显示
            fig = plt.figure(1)

            textstr = '军团番号 - (%d) \n军团名称 - (%s)\n\n成立时间 - (%s)\n解散时间 - (%s)\n\n目前人数 - (%d)\n目前总战力 - (%.2f)K' % \
                      (self.army_code, self.army_name, \
                       self.created.strftime('%Y-%m-%d %H:%M:%S'), self.dismissed.strftime('%Y-%m-%d %H:%M:%S'), \
                      self.alives, self.cal_fighting_capacity()/1000)

            # these are matplotlib.patch.Patch properties
            props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

            # place a text box in upper left in axes coords
            plt.text(0.05, 0.5, textstr, fontsize=20,  horizontalalignment='left', verticalalignment='center', bbox=props)

            # 准备3个图 （ 一行三列 ）
            fig, axs = plt.subplots(1, 3)

            # 图一： 年龄分布图 （ bar 图）
            # 生成 x 坐标 - 年龄
            x = []
            for i in range(self.cst.min_age, self.cst.max_age + 1):
                x.append(str(i))

            # 生成 y 坐标 - 人数
            y = [0] * (self.cst.max_age - self.cst.min_age + 1)  # 数组初始化，注意个数
            for s in self.soldiers:
                if s.is_alive:
                    y[s.age - self.cst.min_age] += 1

            # print(x)
            # print(y)
            axs[0].bar(x, y)
            axs[0].set_xlabel('年龄 %d-%d 岁' % (self.cst.min_age, self.cst.max_age))
            axs[0].set_ylabel('该年龄的人数')
            axs[0].set_title('1)年龄分布图')

            # 图二： 力气值分布图（ 横 bar 图 ）
            y = ['极大', '较大', '普通', '较小', '极小']
            y_pos = np.arange(len(y))

            count = [0] * 5 # 划分 5 档显示
            for s in self.soldiers:
                if s.is_alive:
                    if s.strength <= 20:
                        count[4] += 1
                    elif s.strength <= 40:
                        count[3] += 1
                    elif s.strength <= 60:
                        count[2] += 1
                    elif s.strength <= 80:
                        count[1] += 1
                    else:
                        count[0] += 1

            # print(count)
            axs[1].barh(y_pos, count, color='green')
            axs[1].set_yticks(y_pos)
            axs[1].set_yticklabels(y)
            axs[1].invert_yaxis()

            axs[1].set_xlabel('每档人数 ' )
            axs[1].set_ylabel('五档分类， 力气值范围 %d-%d ' % (self.cst.min_strength, self.cst.max_strength))
            axs[1].set_title('2)士兵力气分布图')

            # 图三： 战斗技巧分布图（散点图）
            x = []
            y = []
            colors = []
            i = 0
            for s in self.soldiers:
                if s.is_alive:
                    x.append(str(i))
                    y.append(s.skill)
                    if s.skill < (self.cst.max_skill - self.cst.min_skill)/3 + self.cst.min_skill :
                        colors.append('green')
                    elif s.skill > (self.cst.max_skill - self.cst.min_skill)/3*2 + self.cst.min_skill:
                        colors.append('red')
                    else:
                        colors.append('yellow')
                    i += 1

            area = 3       # 原点面积固定
            axs[2].scatter(x, y, s=area, c=colors)
            axs[2].set_xlabel('按每个士兵分布' )
            axs[2].set_ylabel('三档分类，战斗技巧值范围 %d-%d ' % (self.cst.min_skill, self.cst.max_skill))
            axs[2].set_title('2)战斗技巧分布图')

            plt.show()

        else:

            fig = plt.figure(3)
            textstr = '军团番号 - (%d) \n军团名称 - (%s)\n\n成立时间 - (%s)\n解散时间 - (%s)\n\n目前人数 - (%d)\n目前总战力 - (%.2f)K' % \
                      (self.army_code, self.army_name, \
                       self.created.strftime('%Y-%m-%d %H:%M:%S'), self.dismissed.strftime('%Y-%m-%d %H:%M:%S'), \
                      self.alives, self.cal_fighting_capacity()/1000)
            textstr = '此军队已经全部阵亡！\n' + textstr

            # these are matplotlib.patch.Patch properties
            props = dict(boxstyle='round', facecolor='red', alpha=0.5)

            # place a text box in upper left in axes coords
            plt.text(0.05, 0.5, textstr, fontsize=20,  horizontalalignment='left', verticalalignment='center', bbox=props)
            plt.show()

        return

    # 简易模式查看军队 - 命令行输出
    def simple_view(self):

        textstr = '******\r军团番号 - (%d) \t军团名称 - (%s)\n成立时间 - (%s)\t解散时间 - (%s)\n当前人数 - (%d)\t当前战力 - (%.2f)K' % \
                  (self.army_code, self.army_name, \
                   self.created.strftime('%Y-%m-%d %H:%M:%S'),
                   self.dismissed.strftime('%Y-%m-%d %H:%M:%S'), \
                   self.alives, self.cal_fighting_capacity() )
        print(textstr)

        return

        # 训练军队
    def training(self):

        if self.alives > 0:
            for s in self.soldiers:
                if s.is_alive:
                    if s.strength < self.cst.max_strength:
                        s.strength += random.random() / 10
                    if s.skill < self.cst.max_skill:
                        s.skill += random.random() / 10
                    if s.experience < self.cst.max_experice:
                        s.experience += random.random() / 10

        return

    # 军队的自然老化
    def aged(self, years):

        for s in self.soldiers:
            # 仅当士兵存活时才会生长
            if s.is_alive:
                # 年龄大于60岁将退出军队
                s.age += years
                if s.age > self.cst.max_age:
                    s.is_alive = 0
                else:
                    # 力气随着岁数增长而变化
                    # 30岁前每年 + 1, 31 - 45 不变，46 - 60 每年 - 2
                    # min,max为限
                    if s.age <= 30:
                        s.strength += 1
                        if s.strength > self.cst.max_strength:
                            s.strength = self.cst.max_strength
                    elif s.age >= 40:
                        s.strength -= 2
                        if s.strength < self.cst.min_strength:
                            s.strength = self.cst.min_strength

                    # 经验随着年龄的增长而增长
                    s.experience += 0.2
                    if s.experience > self.cst.max_experice:
                        s.experience = self.cst.max_experice

        # 重新更新军队人数
        self.alives = 0
        for s in self.soldiers:
            if s.is_alive:
                self.alives += 1

        return

    # 补充军队
    def replacement(self, numbers):
        replaced = 0
        for s in self.soldiers:
            if not s.is_alive:
                new_man = Soldier()       # 新招一个士兵
                # 将新兵的属性赋予这个空人
                s.fullname = new_man.fullname
                s.attended_time = new_man.attended_time
                s.age = new_man.age
                s.strength = new_man.strength
                s.skill = new_man.skill
                s.experience = new_man.experience
                s.equipment = new_man.equipment
                s.is_alive = new_man.is_alive

                replaced += 1       # 用掉了一个补充名额
                self.alives += 1    # 军队总存活人数 +1

            if replaced >= numbers: # 当用完招聘名额时结束
                break

        return replaced   # 返回剩余的补充名额
