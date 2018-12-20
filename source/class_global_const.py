# -*- coding: UTF-8 -*-

# Filename : class_global_const.py
# author by : （学员ID)

# 目的：
#       掌握在不同文件间共享变量的方法

import datetime

class GlobalConst:

    def __init__(self):

        # 设定年龄上限和下限
        self.max_age = 60
        self.min_age = 16
        self.middle_age = (self.max_age + self.min_age) / 2

        # 设定力气值上下限
        self.max_strength = 100
        self.min_strength = 1

        # 设定体力上下限
        self.max_power = 100
        self.min_power = 0

        # 设定战斗技巧上下限
        self.max_skill = 100
        self.min_skill = 1

        # 设定战斗经验的上下限
        self.max_experice = 100
        self.min_experice = 1

        # 解散日期
        date_str = "2100-1-1 0:00:00"
        self.forever = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

        return
