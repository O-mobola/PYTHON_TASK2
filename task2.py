#this program accept users until no user left, 
#check password
#store every user and print masterlist at the end

import random
import string 

users_list =[ ]
users={}
while True:
	
	first_name = input("What's your first name: ")
	last_name = input("What's your last name: ")
	your_email = input("What's your email: ")
	suggest = ""
	new_password= ""
	choosen = ""
	corrected_password = ""
	user = [ ]

#generate random password with character length of 9
	def get_password():
		possible_letters= 'abcdefghijklmnopqrstuvwxyzQ%@#L123456789' 
		for chars in possible_letters:
			outcome1 = random.sample(possible_letters, 5)
			outcome2 = ''.join(outcome1)
		
#get the first two letters First name and the last two letters of the last name.	
		first = first_name[ :2 ]
		last = last_name[ -2: ]
		first_last_letters = first + last
		password = first_last_letters + outcome2
		
		return password
	
	
	get_password()

#check for password error
	print("Will you like to use this password:")
	suggest = get_password()
	print(suggest)
	choosen = input ("enter yes to accept and no not to accept: ").upper()
	if choosen == 'YES':
		print("Your password: ", suggest)
		print("registration successful")
	else: 
		new_password = input("Enter your password: ")
		if len(new_password) < 7:
			print("password must be minimum of 7 characters.")
			corrected_password = input("enter password again:")
		else:
			print(f"Your choice of password is: {new_password}")
				
#defines data function that stores user information in array user.	
	def data():
		user=[ ]		
		for users in range(1):
			user.append(f"first_name: {first_name}")
			user.append(f"last_name: {last_name}")
			user.append(f"email: {your_email}")
			user.append(f"random_password: {suggest}")
			user.append(f"new_password: {new_password}")
			user.append(f"corrected_password: {corrected_password}")

#stores each user in array users_list	
			users_list.append(user) 
			return user


	print(data())

#condition for program termination	
	prompt= input("should the program terminate? yes or no: ")
	if prompt.lower() == 'yes':
		print("Registration completed")
		users = {'registered': users_list}
		print(users )
		break		
	if prompt.lower() == 'no':
		continue
	
	


	  
	  

