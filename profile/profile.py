from os import sys
sys.path.insert(1,'../')

#from main import snap_main

from main import login


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
		sql_connections_table ="""CREATE TABLE if not exists {}(connection_user_id char, sent_request_user_id char,received_request_user_id char)""".format(user_id) 
		crsr_friends.execute(sql_connections_table)
		crsr_friends.execute("SELECT * FROM {}".format(user_id))  
		user_detail = crsr_friends.fetchall()


		sql_num_connections =""" SELECT COUNT(connection_user_id ) FROM {};""".format(user_id)
		crsr_friends.execute(sql_num_connections)
		num_c = crsr_friends.fetchall()



		
		for i in user:
			
			if i[0] ==user_id:

				fname = i[1]
				lname = i[2]
				gender =i[3]
				email = i[4]
				phone = i[5]

				print("user_id : ",user_id)
				print("Name : ",fname,lname)
				print("Gender : ",gender)
				print("Email Id: ",email)
				print("Phone Number: ",phone)
				print("Total Connections : ",num_c[0][0])

		print("")
		print("Enter 1:> Post Stories  | Enter 2:> See Connections | Enter 3:> logout | Enter 4:> Find_connection")
		user_will = int(input())
		if user_will ==1:
			pass
		elif user_will ==2:
			pass
		elif user_will ==3:
			login.login().logout()
		elif user_will ==4:
			pass


		#add_connection
		#see_connection_requ









