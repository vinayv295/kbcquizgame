print(
    'Welcome to KAUN BANEGA CROREPATI quiz by vinay vaishnav\n\t"Enter the correct option name in lowercase"'
)
question_list = [
    "1.Indian felmale politician and lawyer who served as the 12th president of India ",
    "2.Which Indian became  Prime Minister of Uk on 25 October 2022?",
    "3.Where is qutub minar?",
    "4. Which of these terms can only be used for women?",
    "5.Which battle in 1757 marked the beginning of British occupation in India??",
    "6.The weight of diamonds is usually measured in what?",
    "7.Who is the prime minister of pakistan?",
    "8.Who is the bowler of cricket?",
    "9.What is the capital of bangladesh?",
    "10.Where is new york?",
    "11.National Mathematics Day is observed annually on ",
    "12.On which of the following days is world computer literacy  day observed?",
]
first_option = [
    "a.Anandiben Patel",
    "a.Rishi Sunak ",
    "a.Mumbai",
    "a.Dirghaayu",
    "a.Plassey",
    "a.Tola",
    "a.Imran khan",
    "a.Murli vijay",
    "a.turkey",
    "a.UK",
    "a.December 22",
    "a.March 28",
]
second_option = [
    "b.Droupadi Murmu",
    "b.Liz Truss",
    "b.Delhi",
    "b.Chiranjeevi",
    "b.Buxar",
    "b.Carat",
    "b.Shehbaz Sharif",
    "b.Ishant Sharma",
    "b.Islamabad",
    "b.USA",
    "b.July 18",
    "b.May 31",
]
third_option = [
    "c.Prathibha DeviSingh Patil",
    "c.Boris Johnson",
    "c.Himachal Pradesh",
    "c.Suhagan",
    "c.Assaye",
    "c.Maund",
    "c.Nawaz Sarif",
    "c.Mickal Clarke",
]
"c.Dhaka", "c.India", "c.June 22", "c.December 2"

fourth_option = [
    "d.Sumitra Sathe",
    "d.George Washington",
    "d.Kanpur",
    "d.Sushil",
    "d.Panipat",
    "d.Troy",
    "d.Narendra Modi",
    "d.Virat Kohli",
    "d.Delhi",
    "d.Pakistan",
    "d.March 14",
    "d.September 27",
]
# all_option  = [first_option,second_option,third_option,fourth_option]
ans_key = ["c", "a", "b", "c", "a", "b", "b", "b", "c", "b", "a", "c"]
ans_list = []
correct_answers = 0

price = [
    1000,
    2000,
    3000,
    5000,
    10000,
    200000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1280000,
]
# money of all answers.
a = 0
while a < len(question_list):
    print(question_list[a])
    print(first_option[a])
    print(second_option[a])
    print(third_option[a])
    print(fourth_option[a])
    user = input("enter the option name of your answer-")
    if user == ans_key[a]:
        print("Congrats! your answer is correct:", "\t you won", price[a])
        print("")
        correct_answers = 1
    else:
        print("Sorry your answer is wrong")
        print("")
        break
    a = a + 1
    ans_list.append(user)

print(
    f"Congrats! You Have  Completed Your Game with \nthe Price is {price[a-1]}",
    " \nThanks For playing created by vinay vaishnav",
)
