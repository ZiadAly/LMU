import json
from datetime import datetime

#this method collects the current budget
#by reading the current file
#then adding every amount in the transcations
#it takes one parameter which is the number of expected transactions
def Current_Budget(num_trans):
	#it opens json file for reading and writing
	with open("data.json", "r+") as Transactions_json:
		#it saves the previous transactions in a varaible
		message = json.load(Transactions_json)
		#Declating budget varaible
		budget = 0
		#Declaring count for the loop
		i = 0
		#a loop for collecting the current budget
		while (i < len(message)):
			#adding the current amounts 
			budget = budget + int(message[i]["amount"])
			i +=1
		#returning the current budget
		print("Your Current budget is " + str(budget))
        #returning the selected transactions 
		print(message[-int(num_trans):])

#this method, it adds a new transaction to the JSON file 
#by reading the current file 
#then adding the new transactions
#it doesn't take any parameters
def Add_Trans():
	# ask the user to enter the description of the new transaction
	print("Enter description")
	desc = input()
	# ask the user to enter the amount of the new transaction
	print("Enter amount")
	amount = Valid_Numbers()
	# ask the user to enter the date of the new transaction
	print("Enter date")
	date = Valid_Date()
	#transform date type from String to Date object
	#datetime_object = datetime.strptime(date, '%Y-%m-%d')
	#creating a new transacction as dictionary with its attributes 
	new_trans = {"descreption" : desc, "amount" : amount, "date": date}
	#it opens json file for reading and writing
	with open("data.json", "r+") as Transactions_json:
        #it saves the previous transactions in a varaible
		message = json.load(Transactions_json)
		#it adds the new transaction to the old ones
		message.append(new_trans)
		#it change the current file position to 0
		Transactions_json.seek(0)
		#converting the message to JSON
		json.dump(message, Transactions_json)
		budget = 0
		#Declaring count for the loop
		i = 0
		#a loop for collecting the current budget
		while (i < len(message)):
			#adding the current amounts 
			budget = budget + int(message[i]["amount"])
			i +=1
		#returning the current budget
	print("Transaction has been added")
	print("Your Current budget is " + str(budget) + "$")
	print("Would you like to insert another Transaction? yes/no")



#this method returns selected transactions based on the requried date
def Budeget_Date(m,y):
	#it opens json file for reading and writing
	with open("data.json", "r+") as Transactions_json:
		#it saves the previous transactions in a varaible
		message = json.load(Transactions_json)
		#Declaring count for the loop
		i = 0
		#Declaring a list to add the required transactions
		out = []
		#a loop for adding the required transactions 
		while(i < len(message)):
			#Transforimg the date from String to date object
			datetime_object = datetime.strptime(message[i]['date'], '%Y-%m-%d')	
			#getting the year from the date object
			year = datetime_object.year	
			#getting the month from the date object
			month = datetime_object.month
			#comparing the month and the year from the transactions with the required date
			if(y == int(year) and m == int(month)):
				#adding the requried transactions to the output list
				out.append(message[i])
			i = i + 1
	#print the required transactions
	if len(out) == 0:
		print("the required date doesn't exist")
	else:
		print(out)

#this method returns valid integer numbers
#it takes no paramters
def Valid_Numbers():
	#loop stays true till the user enter a valid input
	while True:
		#try and except statments
		try:
			#Asking the user to enter an integer number
			n = int(input())
		#if the user enter a different value, it handles the erorr
		except ValueError:
			print("please, choose the prefered number")
			#to go to the next iteration
			continue
		else:
			#to break the loop if there is no errors
			break
	#returning the valid number
	return n
#this method returns valid answer yes or no
#it takes no parameters
def Valid_Answer():
	#loop stays true till the user enter a valid input
	while True:
		#asking the user to enter a yes or no
		answer = input()
		#checking the user input
		if answer.lower() != "yes" and answer.lower() != "no":
			print("please, Choose yes or no")
		    #to go to the next iteration
			continue
		else:
			#to break the loop if there is no errors
			break
	#returning the valid answer
	return answer

#this method return valid date with a certain format
#it takes no parameters
def Valid_Date():
	#loop stays true till the user enter a valid input
	while True:
		try:
			#asking the user to enter a yes or no
			answer = input()
			#Transforming the user answer to date type
			date = datetime.strptime(answer, '%Y-%m-%d')
		#if the user enter a different format, 
		#it handles the erorr and print the follwoing statment
		except ValueError:
			print("Please, Enter the date with this format YYYY-M-D")
			#to go to the next iteration
			continue
		#the next line checks if the user input has a right year
		if date.year > datetime.today().year:

			print("Please, Enter the right year")
			#to go to the next iteration
			continue
		else:
		    #to break the loop if there is no errors
			break
	#returning the right date
	return answer


#this method returns valid positive answer
def Valid_Pos_Number():
	#loop stays true till the user enter a valid input
	while True:
		try:
		    #asking the user to enter a yes or no
			t = int(input())
		#it handles the erorr and print the follwoing statment
		except ValueError:
			print("please, Enter the prefered number")
			continue
		#checking it the input above 0
		if t < 0:
			print("Please, Enter postive number")
			#to go to the next iteration
			continue
		else:
		    #to break the loop if there is no errors
			break
	#returning a valid positive number
	return t

#########################################################################################################


print("""please choose, 
	1 for adding a Transaction, 
	2 for collecting the budget, 
	3 for Exit
	""")
#loop stays true till the user enter a valid input
while True:
	try:
	    #asking the user to enter a valid number
		n = int(input())
	#it handles the erorr and print the follwoing statment
	except ValueError:
		print("please, choose one of the options (1 or 2 or 3)")
		#to go to the next iteration
		continue
	# checking the user input 
	if n != 1 and n != 2 and n != 3:
		print("please, choose one of the options (1 or 2 or 3)")
		#to go to the next iteration
		continue
	else:
		#to break the loop if there is no errors
		break

#if the user input is option one
if(int(n) == 1):
	#Activing the Add_trans() method
	Add_Trans()
	#Activating the Valid_Answer() method, to get a yes or no input
	answer = Valid_Answer()
#loop stays true till the user enter a valid input
	while(True):
		#checking if the user input is yes, it activates the Add_Trans() again
		if(answer == "yes"):			
			Add_Trans()
	        #Activating the Valid_Answer() method, to get a yes or no input
			answer = Valid_Answer()
		else:
			#if the user input is no, it ends the program
			print("GoodBye")
			break

###################################
#if the user input is option two
if (int(n) == 2 ):
	print("Would you like to specify the number of viewed Transactions ? yes/no")
	#Activating the Valid_Answer() method, to get a yes or no input
	answer2 = Valid_Answer()
	#checking if the user input is yes, it activates the current_budget() method
	if(answer2 == "yes"):
		print("How many transactions Would you like to see?")
	    #Activating the Valid_pos_number() method, to get a positive integer number
		t = Valid_Pos_Number()
		#activating the current_budget() method, 
		#passing the number of the required transactions as a parameter
		Current_Budget(t)
	else:
		#activating the current_budget() method, 
        #expecting 10 returning transactions
		Current_Budget(10)
	print("would you like to select certain date? yes/no")
	#Activating the Valid_Answer() method, to get a yes or no input
	answer3 = Valid_Answer()
	#checking if the user input is yes, it activates the budget_date() method
	if ( answer3 == "yes"):
		print("month")
	    #Activating the Valid_numbers() method, to get an integer number
		m = Valid_Numbers()
		print("year")
		#Activating the Valid_numbers() method, to get an integer number
		y = Valid_Numbers()
		#activating the budget_date() method, 
		#passing the required month and  year as parameters
		Budeget_Date(m,y)
	else:
		#end the program
		print("GoodBye")

#if the user input is option three
if (n == 3):
	#end the program
	print("GoodBye")



































