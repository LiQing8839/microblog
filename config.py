#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/20 10:34
# @Author  : Qing
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False