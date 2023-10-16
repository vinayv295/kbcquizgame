questions = [
    ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "PHP", 4],
    ["In which of these sports would you find two teams pulling on a rope?", "Hockey", "Discus", "Bowling", "Tug of War", 4],
    ["Which of these animals usually lives in burrows?", "Monkey", "Lion", "Tiger", "Rabbit", 4],
    ["In India, which of these is not a common fuel used to run cars?", "CNG", "Petrol", "Diesel", "Coal", 4],
    ["At what temperature measured in Celsius does water boil at sea level?", "90", "85", "50", "100", 4]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0

for i in range(len(questions)):
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(f"a. {questions[i][1]}   b. {questions[i][2]}")
    print(f"c. {questions[i][3]}   d. {questions[i][4]}")
    
    reply = input("Enter your answer (a, b, c, d) or q to quit: ").lower()
    
    if reply == 'q':
        break
    
    if reply == 'd':
        print(f"Correct answer! You have won Rs {levels[i]}")
        money = levels[i]
    else:
        print("Wrong answer. Game over.")
        break

print(f"Your take-home money is Rs {money}")
