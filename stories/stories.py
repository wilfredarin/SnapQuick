import sqlite3
from os import sys

import snap_time 
sys.path.insert(1,"../")


class stories():

	def add_story(self,user_id):
		
		header = input("Enter a Suitable Title: ")
		body = input("Enter your story : ")


		stories = sqlite3.connect("stories.db")
		crsr_stories = stories.cursor()
		sql_stories = """ CREATE TABLE if not exists stories(user_id char,heading char,body text,created_time datetime,updated_time datetime,stamp_time datetime)"""
		crsr_stories.execute(sql_stories)

		crsr_stories.execute("INSERT INTO stories(user_id,heading,body,created_time ) VALUES(?????)",user_id,header,body,snap_time.snap_time().record_time(),snap_time.snap_time().stamp_time())  
		stories.commit()

		system("clear")
		print("story posted successfuly!")



	def show_stories(self,user_id):

		stories = sqlit3.connect("stories.db")
		crsr_stories = stories.cursor()
		sql_find_stories = """SELECT * FROM stories"""
		crsr_stories.execute(sql_find_stories)
		stories_data = crsr_stories.fetchall()

		for i in stories_data: 
			if i[0]==user_id:
				print(i[1])
				print(i[2])
				print(i[3])


	def update_stories(self,user_id,heading):
		pass
		


		

