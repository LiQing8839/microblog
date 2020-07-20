#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 17:03
# @Author  : Qing
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes , models