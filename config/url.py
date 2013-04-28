#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'

urls = (
    '/',                    pre_fix + 'qiqiu.Index',
	'/qiqiu/(\d+)/finish',	pre_fix + 'qiqiu.Finish',
)
