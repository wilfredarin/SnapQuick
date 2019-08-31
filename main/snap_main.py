import sqlite3
from os import sys, system

sys.path.insert(1,"../")

import login
import signup


def snap_main():
	print("@@@@Welcome to SnapQuick@@@@")
	print("")

	log = int(input("Enter '1': Login | Enter '2': signup: "))
	print("")


	connection  = sqlite3.connect("data_base.db")
	crsr = connection.cursor()
	sql_command = """ CREATE TABLE if not exists user(user_id char,fname char,lname char,gender char,email_id char,phone_number int,password char)"""
	crsr.execute(sql_command)

	#check log or sign
	if log==1:

		login.login().login(user_id)

	else:
		signup.signup().signup()



snap_main()




