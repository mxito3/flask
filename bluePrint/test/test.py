# -*- coding: utf-8 -*-
# @Author: YP
# @Date:   2018-07-16 18:11:54
# @Last Modified by:   YP
# @Last Modified time: 2018-07-16 19:08:08
from flask import Flask,Blueprint
mod=Blueprint('test',__name__)

@mod.route('/api/test')
def test():
	return "this is test"

@mod.route('/test')
def test1():
	return "this is test1"