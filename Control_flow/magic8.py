#Program for a Magic8 ball using Control flow
import random
name = "Preetham Ravula"
question = "Is this going to happen?"
answer = ""
random_number = random.randint(1,12)
#print(random_number)
if random_number == 1:
  answer = "Yes-definetly."

elif random_number == 2:
  answer = "It is decidedly so."

elif random_number == 3:
  answer = "Without a doubt."

elif random_number == 4:
  answer = "Reply hazy, try again."

elif random_number == 5:
  answer = "Ask again later."

elif random_number == 6:
  answer = "Better not tell you now."

elif random_number == 7:
  answer = "My sources say no."

elif random_number == 8:
  answer = "Outlook not so good."

elif random_number == 9:
  answer = "Very doubtful."

elif random_number == 10:
  answer = "For sure."

elif random_number == 11:
  answer = "You betcha."

elif random_number == 12:
  answer = "Everything will be better than expected."

else:
  answer = "Error"
if len(name) > 0 and len(question) > 0:
  print(name + " asks: " + question )
  print("Magic 8-Ball's answer: ", answer )

elif len(name) > 0 and len(question) == 0:
  print(name + " ask a question first ")

elif len(name) == 0 and len(question) > 0:
  print(question)
  print("Magic 8-Ball's answer: ", answer )

elif len(name) == 0 and len(question) == 0:
  print("Need a user and a question")
