score=0
question ="what is the capital of france?"
print (question)
user_answer = input(" your answer")

if user_answer.lower() == "paris":
    print("correct!")
    score +=1
else: 
    print("Oops! the correct answer is paris.")

question ="what is the capital of UK?"
print (question)
user_answer = input(" your answer")

if user_answer.lower() == "london":
    print("correct!")
    score +=1
else: 
    print("Oops! the correct answer is london.")


question ="what is the capital of  netherlands?"
print (question)
user_answer = input(" your answer")

if user_answer.lower() == "amsterdam":
    print("correct!")
    score +=1
else: 
    print("Oops! the correct answer is amsterdam.")


question ="what is the capital of sweden?"
print (question)
user_answer = input(" your answer")

if user_answer.lower() == "stockholm":
    print("correct!") 
    score +=1
else: 
    print("Oops! the correct answer is stockholm.")

question ="what is the capital of spain?"
print (question)
user_answer = input(" your answer")

if user_answer.lower() == "madrid":
    print("correct!") 
    score +=1
else: 
    print("Oops! the correct answer is madrid.")

print(f"your score is: {score}")