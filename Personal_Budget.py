import json
from datetime import datetime

#this method, it adds a new transaction to the JSON file 
#by reading the current file 
#then adding the new transactions
#it doesn't take any parameters
def add_trans():
	# ask the user to enter the description of the new transaction
	print("Enter description")
	desc = input()
	# ask the user to enter the amount of the new transaction
	print("Enter amount")
	amount = valid_numbers()
	# ask the user to enter the date of the new transaction
	print("Enter date")
	date = valid_date()
	#transform date type from String to Date object
	#datetime_object = datetime.strptime(date, '%Y-%m-%d')
	#creating a new transacction as dictionary with its attributes 
	new_trans = {"descreption" : desc, "amount" : amount, "date": date}
	#it opens json file for reading and writing
	with open("data.json", "r+") as message_json:
        #it saves the previous transactions in a varaible
		message = json.load(message_json)
		#it adds the new transaction to the old ones
		message.append(new_trans)
		#it change the current file position to 0
		message_json.seek(0)
		#converting the message to JSON
		json.dump(message, message_json)
	print("Transaction has been added")
	print("Would you like to insert another Transaction? yes/no")

#this method collects the current budget
#by reading the current file
#then adding every amount in the transcations
#it takes one parameter which is the number of expected transactions
def current_budget(num_trans):
	#it opens json file for reading and writing
	with open("data.json", "r+") as message_json:
		#it saves the previous transactions in a varaible
		message = json.load(message_json)
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

#this method returns selected transactions based on the requried date
def budeget_date(m,y):
	#it opens json file for reading and writing
	with open("data.json", "r+") as message_json:
		#it saves the previous transactions in a varaible
		message = json.load(message_json)
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

def valid_numbers():
	while True:
		try:
			n = int(input())
		except ValueError:
			print("please, choose the prefered number")
			continue
		else:
			break
	return n

def valid_answer():
	while True:
		answer = input()
		if answer.lower() != "yes" and answer.lower() != "no":
			print("please, Choose yes or no")
			continue
		else:
			break
	return answer


def valid_date():
	while True:
		try:
			answer = input()
			date = datetime.strptime(answer, '%Y-%m-%d')
		except ValueError:
			print("Please, Enter the date with this format YYYY-M-D")
			continue
		if date.year	> datetime.today().year:
			print("Please, Enter the right year")
			continue
		else:
			break
	return answer

#########################################################################################################


print("""please choose, 
	1 for adding a Transaction, 
	2 for collecting the budget, 
	3 for Exit
	""")
while True:
	try:
		n = int(input())
	except ValueError:
		print("please, choose the prefered number")
		continue
	if n != 1 and n != 2 and n != 3:
		print("please, choose the prefered number")
		continue
	else:
		break
###############
#writing 
if(int(n) == 1):
	add_trans()
	answer = valid_answer()
	while(True):
		if(answer == "yes"):			
			add_trans()
			answer = valid_answer()
		else:
			print("GoodBye")
			break

###################################
if (int(n) == 2 ):
	print("How many transactions Would you like to see?")
	while True:
		try:
			t = int(input())
		except ValueError:
			print("please, Enter the prefered number")
			continue
		if t < 0:
			print("Please, Enter postive number")
		else:
			break
	current_budget(t)
	print("would you like to select certain date? yes/no")
	answer2 = valid_answer()
	if ( answer2 == "yes"):
		print("month")
		m = input()
		print("year")
		y = input()
		budeget_date(int(m),int(y))
	else:
		print("GoodBye")


if(int(n) == 3):
	print("GoodBye")























