import json

user_sign=input("enter longin or signup:-")
if user_sign=="signup":
	print("you have signup your account plz go forward!!")
	name=input("enter your username:-")
	password=input("enter your password:-")
	repassword=input("enter your repassword:-")
	if "@"  in password or "#" in repassword:
		if password==repassword:
			print("both password and repassword are same,successful")
		else:
			print("both password and repassword are not same,sorry!!try again....")	
	else:
		print("atlest password should contain on special character and one number")
	# with open("userdetails.json") as file:
	# 	data = json.load(f)
	# 	data['userdetails']
	# if name not in new_file:
	# 		print("contioun")
	# 	else:
	# 		print("username alredy exits")	



	with open("userdetails.json","w+") as file:
			file.write(str({"user":[{name:password},{name:repassword}]}))
			# file.close()
	# 		new_file=open("userdetails.json",'r')
	# 		print(new_file.read())
	# if name not in new_file:
	# 		print("contioun")
	# 	else:
	# 		print("username alredy exits")	










