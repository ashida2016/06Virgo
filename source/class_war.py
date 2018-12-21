# -*- coding: UTF-8 -*-

# Filename : class_war.py
# author by : （学员ID)

# 目的：
#      巩固类的开发方法， 制作一个士兵类
#
import random

from class_global_const import GlobalConst

class War:

    def __init__(self):
        self.cst = GlobalConst()    # 在本类内部保持这些常数
        return

    # 两个士兵间的决斗
    def fight_of_2_soldiers(self, soldiers):

        if len(soldiers) == 2:  # 仅当只有2个士兵才能对决
            s1 = soldiers[0]
            s2 = soldiers[1]

            s1fc = s1.cal_fighting_capacity()
            s2fc = s2.cal_fighting_capacity()

            if s1fc > s2fc:
                s2.is_alive = 0                     # 失败者死亡
                s1.skill += random.random()         # 每次战斗提升 0-1 技巧
                s1.experience += random.random()    # 每次战斗提升 0-1 经验
                s1.power *= (s1fc-s2fc)/s1fc               # 每次战斗后体力值下降
                if s1.power < self.cst.min_power:
                    s1.power = self.cst.min_power
            elif s1fc < s2fc:
                s1.is_alive = 0                     # 失败者死亡
                s2.skill += random.random()         # 每次战斗提升 0-1 技巧
                s2.experience += random.random()    # 每次战斗提升 0-1 经验
                s2.power *= (s2fc-s1fc)/s2fc               # 每次战斗后体力值下降
                if s2.power < self.cst.min_power:
                    s2.power = self.cst.min_power

        return

    # 两只军队间的战斗
    def fight_of_2_armies(self, armies):

        if len(armies) == 2:    # 仅当只有2只军队时才可交战

            attacker = armies[0]    # 默认进攻方为第一只军队
            defender = armies[1]    # 默认防守方为第二只军队

            # 士兵捉对厮杀次数默认为人数少的一方 * n
            fight_times = 0
            if attacker.alives > defender.alives:
                fight_times = int(defender.alives * 1.5)
            else:
                fight_times = int(attacker.alives * 1.5)

            for i in range(fight_times):
                s1 = self.pick_a_soldier(attacker)
                if not s1.is_alive:
                    break  # 挑不出活人了，战斗结束
                s2 = self.pick_a_soldier(defender)
                if not s2.is_alive:
                    break  # 挑不出活人了，战斗结束

                #print("\n第(%d)次战斗开始....选人..." % (i))
                #s1.report_me()
                #s2.report_me()
                opponent = [s1, s2]

                #print("开始战斗....")
                self.fight_of_2_soldiers(opponent)
                #s1.report_me()
                #s2.report_me()

            # 战斗完成后更新部队幸存者人数
            count = 0
            for s in attacker.soldiers:
                if s.is_alive:
                    count += 1
            attacker.alives = count

            count = 0
            for s in defender.soldiers:
                if s.is_alive:
                    count += 1
            defender.alives = count

        return

    # 从军队中挑出一个体力值最高的活人
    def pick_a_soldier(self, army):

        max_p = self.cst.min_power
        rtn_s = army.soldiers[0]

        for s in army.soldiers:
            if s.is_alive:
                if s.power > max_p:
                    max_p = s.power
                    rtn_s = s

        return rtn_s
