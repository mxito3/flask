# -*- coding: utf-8 -*-
# @Author: YP
# @Date:   2018-07-16 18:11:19
# @Last Modified by:   YP
# @Last Modified time: 2018-07-16 19:24:29
from flask import Flask,Blueprint
mod = Blueprint('user',__name__)
@mod.route('/api/user')
def user():
	return "i am user"
	