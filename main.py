
questions = [
    "Which language was used to create Facebook?",
    "Where is Goverment Polytechnic Gandhinagar?"
]

option = [
    ['python','english','javascript','php', 3],
    ['Ahmedabad', 'Gandhinagar', 'Baroda', 'Rajkot', 2]
]

reward = [10000,20000,50000,100000,250000,500000,1000000]
i=0
for i in range(i,len(questions)):
    print(questions[i])

    print(f'a.{option[i][0]}        b.{option[i][1]}')
    print(f'c.{option[i][2]}        d.{option[i][3]}')

    reply= int(input('\nEnter answer here:'))
    
    if( reply == option[i][-1]):
        print(f'correct you have won {reward[i]}\n\n')
    else:
        print('OOPS, The Wrong Answer!')
        print('|| Game Over || ("=")\n\n')
        break

        
        
 

