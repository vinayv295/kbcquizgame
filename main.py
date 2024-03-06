
# in this game player can use lifelines only 2 times
# This function show correct answer for corrent question to the player
def lifeline(a):
    print('Right Answer is :',a)

# github id :- harminvp00
# Master_Level function save players achivement if level > Master_level
# by this function of code player not lost all game 
def Master_Level(lev):
    Master_lev=0
    if lev >= 4:
      Master_lev=1
    if lev >= 9:
      Master_lev=2
    if lev >= 12:
      Master_lev=3
    if lev >= 14:
      Master_lev=4
    return Master_lev
    
    
# main coding 
# List is used here to store questions
questions = [
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
  "12.On which of the following days is world computer literacy  day observed?"
]

# all_option  = [ a.first_option    b.second_option ]
#               [ c.third_option    d.fourth_option ]

# Option A for All Questions
first_option = [
  "a.Anandiben Patel", "a.Rishi Sunak ", "a.Mumbai", "a.Dirghaayu",
  "a.Plassey", "a.Tola", "a.Imran khan", "a.Murli vijay", "a.turkey", "a.UK",
  "a.December 22", "a.March 28"
]

# Option B for All Questions
second_option = [
  "b.Droupadi Murmu", "b.Liz Truss", "b.Delhi", "b.Chiranjeevi", "b.Buxar",
  "b.Carat", "b.Shehbaz Sharif", "b.Ishant Sharma", "b.Islamabad", "b.USA",
  "b.July 18", "b.May 31"
]

# Option C for All Questions
third_option = [
"c.Prathibha DeviSingh Patil", "c.Boris Johnson", "c.Himachal Pradesh",
"c.Suhagan", "c.Assaye", "c.Maund", "c.Nawaz Sarif", "c.Mickal Clarke",
"c.Dhaka", "c.India", "c.June 22", "c.December 2"
]

# Option D for All Questions
fourth_option = [
  "d.Sumitra Sathe", "d.George Washington", "d.Kanpur", "d.Sushil",
  "d.Panipat", "d.Troy", "d.Narendra Modi", "d.Virat Kohli", "d.Delhi",
  "d.Pakistan", "d.March 14", "d.September 27"
]

# Right Answer for All Question
answers = ["c", "a", "b", "c", "a", "b", "b", "b", "c", "b", "a", "c"]

# Rewards which you get for each right answer
reward = [
  1000, 2000, 3000, 5000, 10000, 200000, 40000, 80000, 160000, 320000, 640000,
  1250000, 2500000, 5000000, 7500000, 10000000, 75000000
]

# Variable declaration according to need in diffrent task     
      
i=0                     # it's value is used to display Question or options    
count=2                 # it's indicates the avialable lifeline for player
ll='no'                 # ll = lifeline , if player input 'yes' it can be show right answer of the question
level=-1                # it is a simply level of the player
Master_level=0          # if the player achive master level and lost the game 
                        # then player not lost its all earned rewards but it was achive only his last master_level reward not all


# This loop will be not terminate untill player enter wrong answer of the question     
for i in range(i,len(questions)):
    print('Master Level = Level',Master_level)
    print('Available LineLines :',count,'\n')
    print(questions[i])

    print(f'{first_option[i]}           {second_option[i]}')
    print(f'{third_option[i]}           {fourth_option[i]}')

    # if player enter yes for two time then this condition never run for third time 
    if count>0: 
        ll=input("Want to use lifeline?? (yes or no) :-")
        if  ll == 'yes':
            count-=1
            lifeline(answers[i])

    # User Reply        
    reply= input('\nEnter answer here:')
    
    # if reply is right answer then player level is increment also reward is showed
    if reply == answers[i]:
        level+=1
        Master_level=Master_Level(level)
        print(f'correct you have won {reward[i]}\n') 

    # if answer is not right then code will be terminates
    else:
        print('OOPS, The Wrong Answer!')
        break
