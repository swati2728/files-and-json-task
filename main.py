import json

user_sign=input("enter longin or signup:-")
if user_sign=="signup":
	print("you have signup your account plz go forward!!")
	name=input("enter your username:-")
	password=input("enter your password:-")
	repassword=input("enter your repassword:-")
	if "@"in password or "#"in repassword:
		if password==repassword:
			my_files=open("userdetails.json",'r')
			print(my_files)
			if name not in my_files:
				print("countion")
			else:
				print("already exit!!")

			# print("both password and repassword are same,successful")
		else:
			print("both password and repassword are not same,sorry!!try again....")	
	else:
		print("atlest password should contain on special character and one number")
if user_sign=="longin":
	name=input("enter your name")
	password=input("enter your password:-")
	repassword=input("enter your repassword:-")
	my_files=open("userdetails.json",'r')
	print(my_files)
	if name not in my_files:
		print(name,"you are logged successful!!")
	else:
		print("invalid name and password!!sorry")
	description=input("write small description about you:-")
	birth_day=input("enter your birth_day")
	hobbies=input("enter what is your hobbies")
	gender=input("enter your gender(male/female)")
	with open("userdetails.json","w+") as files:
		files.write(str({description:""},{birth_day:""},{hobbies:""}))
