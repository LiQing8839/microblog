#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 17:03
# @Author  : Qing
# @Site    : 
# @File    : routes.py
# @Software: PyCharm

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"