import sqlite3
from os import sys,system

sys.path.insert(1,"../profile")
from profile import profile

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
		email_id = input("Email Id: ")
		phone_number = int(input("Phone Number: "))


		sql_command = """INSERT INTO user VALUES (?,?,?,?,?,?,?);"""
		crsr.execute(sql_command,(user_id,fname,lname,gender,email_id,phone_number,set_password,)) 
		connection.commit()
		print("account succesfully Created !")
		profile().show_profile(entered_id)
