import sqlite3



from os import sys

sys.path.insert(1,'../')
from main import signup


class login():
	def login(self):
			
			match_user = 1
			actual_password = ""
			
			user_id = input("ENTER ID: ")
			enter_password = input("ENTER PASSWORD: ")

			


			# connecting to the database 
			connection = sqlite3.connect("data_base.db") 
			# cursor 
			crsr = connection.cursor() 
			crsr.execute("SELECT * FROM user")  
			# store all the fetched data in the ans variable 
			ans= crsr.fetchall()  
			  
			# loop to print all the data 
			for i in ans: 
			    if (i[1]) == user_id:
			    	actual_password =i[-1]
			    	cancel=0
			    	break

			    	
			# close the connection 
			connection.close() 

			while (enter_password != actual_password or cancel):
				print("Please check deatails again!")
				sign_flag  = int(input("New user ? signup | ENTER 1 | login - ENTER 2 : "))
				if sign_flag ==1:
					signup.signup().signup()
				else:
					user_id = input("ENTER ID: ")
					enter_password = input("ENTER PASSWORD: ")
					
					
					for i in ans: 
					    if (i[1]) == user_id:
					    	actual_password =i[-1]
					    	cancel=0
					    	break

			system("clear")
			print(user_id)
			print("welcome to read stories enter 1 else 2")
			#profile.profile().show_profile(user_id)


			 

	def logout(self):
		snap_main()