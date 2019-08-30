import sqlite3
from os import sys

sys.path.insert(1,"../")
from main import login
from main import signup


def snap_main():
	print("@@@@Welcome to SnapQuick@@@@")
	print("")

	log = int(input("Enter '1': Login | Enter '2': signup: "))
	print("")


	connection  = sqlite3.connect("data_base.db")
	crsr = connection.cursor()
	sql_command = """ CREATE TABLE user(user char,fname char,lname char,gender char,password char)"""
	#crsr.execute(sql_command)

	#check log or sign
	if log==1:

		login.login().login()

	else:
		signup.signup().signup()








snap_main()




