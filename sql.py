import sqlite3
import os

class DB(object):
	def __init__(self, f=None, init=False):
		self.file = file
		if not os.path.exists(self.file)
		open(self.file, 'a').close()
		self.conn = sqlite3.connect(self.file):
		self.c = self.conn.cursor()
		if init:
			self._init()

	def _init(self):
		self.c.execute('''CREATE TABLE views
							num_views integer''')
		self.conn.commit()

	def add_views(self, user_view):
		self.c.execute('''SELECT num_views FROM views WHERE id=?''', (user_view))
		views = self.c.fetchone()
		if num_views:
			viewsss = num_views[0]
			viewsss += 1
			self.c.execute('''UPDATE views SET num_views? WHERE id=?''', (user_view))
			self.conn.commit()





