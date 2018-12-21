# -*- coding: UTF-8 -*-

# Filename : class_save_read_army.py
# author by : （学员ID)

# 目的:
#

import os
import sys
import io

import numpy as np
import matplotlib.pylab as plt

import random
import datetime

import json

from class_soldier import Soldier
from class_army import Army

class SaveReadArmy:

    def __init__(self, army):

        # 确定要写入的文件路径
        # for ATOM
        # csv_path = os.getcwd() + '\\' + 'config\\all_atoms.csv'
        self.fpath_army = os.getcwd() + '\\armies\\' + army.army_name + '-' + str(army.army_code) + '.json'
        self.fpath_soldier = os.getcwd() + '\\armies\\' + army.army_name + '-' + str(army.army_code) + '-' + '士兵们.json'
        # for cmd Python
        # csv_path = os.getcwd() + '\\' + '..\\config\\all_atoms.csv'
        # self.fpath_army = os.getcwd() + '\\' + '..\\armies\\' + army.army_name + '-' + str(army.army_code) + '.json'
        # self.fpath_soldier = os.getcwd() + '\\' + '..\\armies\\' + army.army_name + '-' + str(army.army_code) + '-' + '士兵们.json'
        # for PyCharm
        # self.fpath_army = '..\\armies\\' + army.army_name + '_' + str(army.army_code) + '.json'
        # self.fpath_soldier = '..\\armies\\' + army.army_name + '_' + str(army.army_code) + '_' + '士兵们.json'

        return

    # 保存一只军队的所有信息至2个文件
    def save_army(self, army):

        # print(self.fpath_army)
        f = open(self.fpath_army, 'w')  # write 方式写 - indent=4 表示分行

        json_str = json.dumps(army, indent=4, default=self._army2json, ensure_ascii=False)
        f.write(json_str)
        f.close()

        f = open(self.fpath_soldier, 'w')  # write 方式写 - indent=4 表示分行
        json_str = json.dumps(army.soldiers, indent=4, default=self._soliders2json, ensure_ascii=False)
        f.write(json_str)

        f.close()

        return

    # 从2个文件读取一只军队的概要信息
    def load_army(self, name, code):

        # 确定要读出的文件路径
        # for ATOM
        self.fpath_army = os.getcwd() + '\\armies\\' + name + '-' + str(code) + '.json'
        self.fpath_soldier = os.getcwd() + '\\armies\\' + name + '-' + str(code) + '-' + '士兵们.json'
        # for cmd Python
        # self.fpath_army = os.getcwd() + '\\..\\armies\\' + name + '-' + str(code) + '.json'
        # self.fpath_soldier = os.getcwd() + '\\..\\armies\\' + name + '-' + str(code) + '-' + '士兵们.json'
        # for PyCharm
        # self.fp_army = '..\\armies\\' + name + '_' + str(code) + '.json'
        # self.fp_soldier = '..\\armies\\' + name + '_' + str(code) + '_' + '士兵们.json'

        # 读取概要信息
        f = open(self.fpath_army, 'r')  # read 方式读

        # line = f.readline()
        # d = json.loads(line)    # 将读入的 json 字串转化为一个 dict
        d = json.load(f)

        # 将读取的概要信息赋予一个 Army 类对象
        rtn_army = Army()
        rtn_army.army_name = name
        rtn_army.army_code = code

        time_str = d['成立日期']
        rtn_army.created = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        time_str = d['解散日期']
        rtn_army.dismissed = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')

        rtn_army.alives = d['当前人数']

        f.close()

        # 读取士兵们的信息
        f = open(self.fpath_soldier, 'r')  # read 方式读

        # line = f.readline()
        # ds = json.loads(line)   # 将读入的 json 字串转化为一个 dict 列表
        ds = json.load(f)   # 将整个 json 文件读入

        for d in ds:
            rtn_solider = Soldier()
            rtn_solider.fullname = d['士兵姓名']
            time_str = d['入伍日期']
            rtn_solider.attended_time = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            rtn_solider.age = d['士兵年龄']
            rtn_solider.strength = d['士兵力气']
            rtn_solider.power = d['士兵体力']
            rtn_solider.skill = d['战斗技巧']
            rtn_solider.experience = d['战斗经验']
            rtn_solider.equipment = d['战斗装备']
            rtn_solider.is_alive = d['是否活着']

            rtn_army.soldiers.append(rtn_solider)

        f.close()

        return rtn_army

    # 将 solider 对象序列化成 json
    def _soliders2json(self, soliders_obj):
        data = {
            '士兵姓名': soliders_obj.fullname,
            '入伍日期': soliders_obj.attended_time.strftime('%Y-%m-%d %H:%M:%S'),
            '士兵年龄': soliders_obj.age,
            '士兵力气': soliders_obj.strength,
            '士兵体力': soliders_obj.power,
            '战斗技巧': soliders_obj.skill,
            '战斗经验': soliders_obj.experience,
            '战斗装备': soliders_obj.equipment,
            '是否活着': soliders_obj.is_alive
        }
        return data

    # 将 army 对象序列化成 json (仅概要信息部分）
    def _army2json(self, army_obj):
        data = {
            '军团番号': army_obj.army_code,
            '军团名称': army_obj.army_name,
            '成立日期': army_obj.created.strftime('%Y-%m-%d %H:%M:%S'),
            '解散日期': army_obj.dismissed.strftime('%Y-%m-%d %H:%M:%S'),
            '当前人数': army_obj.alives,
            '当前战力': army_obj.cal_fighting_capacity(),
        }
        return data

    """
    # 将 json 字串反序列化成 solider 对象
    def _json2solider(self, d):
        return

    # 将 json 字串反序列化成 army 对象
    def _json2army(self, d):
        return Army(d['军团番号'], d['军团名称'], d['成立日期'], d['解散日期'], d['当前人数'], d['当前战力'])

    """
