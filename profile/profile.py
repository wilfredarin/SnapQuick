from os import sys
sys.path.insert(1,'../')

#from main import snap_main




import sqlite3

class profile():
	
	def show_profile(self,user_id):

		connection = sqlite3.connect("../main/data_base.db") 
		crsr = connection.cursor() 
		crsr.execute("SELECT * FROM user")
		user= crsr.fetchall()  
		connection.close() 

		connection_friends = sqlite3.connect("connections.db")
		crsr_friends = connection_friends.cursor()
		sql_connections_table ="""CREATE TABLE if not exists {}(user_id char, fname char,lname char,stories text)""".format(user_id) 
		crsr_friends.execute(sql_connections_table)
		crsr_friends.execute("SELECT stories FROM {}".format(user_id))  
		user_stoires = crsr_friends.fetchall()
		for i in user_stoires:
			print(i)



		



		
		for i in user:
			
			if i[0] ==user_id:

				fname = i[1]
				lname = i[2]
				gender = i[3]

		print("user_id : ",user_id)
		print("Name : ",fname,lname)
		print("Gender : ",gender)
		print("Total Connections : ",num_c[0][0])

		#add_connection
		#see_connection_request





profile().show_profile("sameer")





