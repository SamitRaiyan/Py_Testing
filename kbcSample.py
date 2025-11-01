# kbc sample
# questionList
questions = [
    "What is 2 + 3?",
    "What comes after 7?",
    "How many sides does a triangle have?",
    "What is the opposite of 'big'?",
    "Which animal says 'meow'?",
    "What color is the sky on a clear day?",
    "How many legs does a dog have?",
    "What is 5 - 2?",
    "Which fruit is yellow and shaped like a crescent?",
    "What sound does a cow make?"
]
# optionList
options = [
    ["1. 3", "2. 4", "3. 5", "4. 6"],
    ["1. 6", "2. 9", "3. 8", "4. 10"],
    ["1. 2", "2. 3", "3. 4", "4. 5"],
    ["1. Small", "2. Tall", "3. Large", "4. Huge"],
    ["1. Dog", "2. Cow", "3. Cat", "4. Horse"],
    ["1. Green", "2. Yellow", "3. Blue", "4. Red"],
    ["1. 2", "2. 3", "3. 4", "4. 5"],
    ["1. 1", "2. 2", "3. 3", "4. 4"],
    ["1. Apple", "2. Mango", "3. Banana", "4. Orange"],
    ["1. Meow", "2. Moo", "3. Bark", "4. Neigh"]
]
# answerList
answers = [
    3,  # c -> 5
    3,  # c -> 8
    2,  # b -> 3
    1,  # a -> Small
    3,  # c -> Cat
    3,  # c -> Blue
    3,  # c -> 4
    3,  # c -> 3
    3,  # c -> Banana
    2   # b -> Moo
]
# replyList
reply = []

#                                             --------------representing the questions------------------
#1st question
print("Question 1:") 
print(questions[0])
print(options[0])
ans1Input = input("Input your answer of the question-1 : ")
print(ans1Input)
reply.insert(0,ans1Input)
if ans1Input == 3 :
    print("Correct Answer\nReward : 1\nTotal : 1")
else:
    print("Wrong Answer\nReward : 0\nTotal : 0")

"""
#2nd question
print("Question 2:") 
print(questions[1])
print(options[1])
ans2Input = input("Input your answer of the question-2 : ")
print(ans2Input)
reply.insert(0,ans2Input)
if ans1Input == 3 :
    print("Correct Answer\nReward : 2\nTotal : 3")
else:
    print("Wrong Answer\nReward : 0\nTotal : 1")

#3rd question
print("Question 1:") 
print(questions[2])
print(options[2])
ans1Input = input("Input your answer of the question-3 : ")
print(ans1Input)
reply.insert(0,ans1Input)
if ans1Input == 3 :
    print("Correct Answer\nReward : 1\nTotal : 1")
else:
    print("Wrong Answer\nReward : 0\nTotal : 0")



"""