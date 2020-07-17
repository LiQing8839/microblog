#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 17:03
# @Author  : Qing
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask

app = Flask(__name__)

from app import routes