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

answers = [
    3,  # 5
    3,  # 8
    2,  # 3
    1,  # Small
    3,  # Cat
    3,  # Blue
    3,  # 4
    3,  # 3
    3,  # Banana
    2   # Moo
]

reply = []
total_reward = 0

for i in range(10):
    print(f"Question {i+1}:")
    print(questions[i])
    print(" ".join(options[i]))
    ans_input = int(input(f"Input your answer for question-{i+1}: "))
    reply.append(ans_input)
    
    if ans_input == answers[i]:
        total_reward += i + 1
        print(f"Correct Answer\nReward: {i+1}\nTotal: {total_reward}\n")
    else:
        print(f"Wrong Answer\nReward: 0\nTotal: {total_reward}")
        print("----Game Over----\n")
        break

print("Quiz Over! Your final score is:", total_reward)
# print("\nall the previous answers: ")
# print(reply)
