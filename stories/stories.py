import sqlite3
from os import sys
sys.path.insert(1,"../")


class stories():

	def add_story(self,user_id):
		header = input("What's your story about? ")
		text = input("Enter your story : ")



		connection_friends = sqlite3.connect("../profile/connections.db")
		crsr_friends = connection_friends.cursor()
		sql_connections_table ="""CREATE TABLE if not exists {}(user_id char, fname char,lname char,stories text)""".format(user_id) 
		crsr_friends.execute(sql_connections_table)
		crsr_friends.execute("INSERT INTO {}(stories) VALUES(?)".format(user_id),text)  
		user_detail = connection_friends.commit()

	def show_stories(self,user_id):
		
		connection_friends = sqlite3.connect("../profile/connections.db")
		crsr_friends = connection_friends.cursor()
		sql_connections_table ="""CREATE TABLE if not exists {}(user_id char, fname char,lname char,stories text)""".format(user_id) 
		crsr_friends.execute(sql_connections_table)
		crsr_friends.execute("SELECT stories FROM {}".format(user_id))  
		user_stoires = crsr_friends.fetchall()
		for i in user_stoires:
			print(i[0])

	def delete_stories(self,user_id) :
		pass





		

stories().show_stories("sameer")