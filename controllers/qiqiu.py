#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
from datetime import datetime

render = settings.render
db = settings.db

class Index:

    def GET(self):
        solution = db.select('solution, contest_user', 
				what='solution.solution_id, solution.finished, contest_user.name1, solution.problem_id, contest_user.sitNo', 
				where='solution.contest_id=1162 and solution.result=1 and solution.user_id = contest_user.id', 
				group='problem_id, name1', 
				order='finished asc, solution_id desc')
        return render.index(solution)

class Finish:
	def GET(self, id):
		i = web.input()
		status = i.get('status', 'yes')
		if status == 'yes':
			finished = 1
		elif status == 'no':
			finished = 0
		db.update('solution', finished=finished, where='solution_id=$id', vars=locals())
		raise web.seeother('/')
