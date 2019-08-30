import sqlite3
from os import system


class signup():
	def signup(self):
		system("clear")
		print("@@@ SnapQuick Registration page! ")
		

		connection = sqlite3.connect("../main/data_base.db")  
		crsr = connection.cursor() 
		crsr.execute("SELECT * FROM user")  
		ans= crsr.fetchall()

		check = 0
		t = 0
		while not check:
			user_id = input("choose a user Id: ")
			for j in ans:
				if j[0] == user_id:
					print("Already Taken")
					t=1
					break
			if t:
					t=0
			else:
				check = 1
				print("Available!")

		set_password = input("Enter Password: ")	
		fname = input("First Name: ")	
		lname = input("Last Name: ")
		gender = input("Gender: ")


		sql_command = """INSERT INTO user VALUES (?,?,?,?,?);"""
		crsr.execute(sql_command,(user_id,fname,lname,gender,set_password)) 
		connection.commit()
		print("account succesfully Created !")
		#profile.profile().show_profile(entered_id)
