#program will display types of questions to choose from

#user will pick a type of question

#random question from a list of questions will be given

#for actual algorithm questions, we'll do runtime

#rerun the program and select problem answer or problem hints
	#and give it the problem number with what you want


def quizzer():
	opener()
	choice = make_choice()

	if choice == 1:
		#
	elif: choice == 2:
		#
	else:
		#

def make_choice():
	choices = [1,2,3]
	choice = input("> ")
	while True:
		if int(choice) not in choices:
			choice = input("Erm... Select 1, 2, or 3. Please! > ")
		else:
			break
	return int(choice)

def opener():
	msg = "______<^^^^>__\n"
	msg += "☆ ∩∩ （ • •）☆\n"
	msg += "┏━∪∪━━━━━━━━┓\n"
	msg += "*		    *\n"			
	msg += '* Hey Buddy * \n'
	msg += "┗━━━━━━━━━━━┛"
	print(msg)

	instruction = "Press 1 if you're in search for a question; "
	instruction += "\nPress 2 if you're in search for a hint; "
	instruction += "\nPress 3 if you're in search for an answer: "
	print(instruction)

quizzer()