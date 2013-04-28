#!/usr/bin/env python
# coding: utf-8
import web

db = web.database(dbn='mysql', db='oj', user='root', pw='rootpass')

render = web.template.render('templates/', cache=False)

web.config.debug = True

config = web.storage(
    email='zrq495@gmail.com',
    site_name = '气球',
    site_desc = '',
    static = '/static',
	color = {1000:'红', 1010:'橙', 1011:'黄', 1012:'绿', 1013:'青', 1014:'蓝', 1015:'紫', 1016:'白', 1017:'黑'}
)


web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
