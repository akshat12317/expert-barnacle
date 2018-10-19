import random as r
name=input('Enter your name-')
while True:
    print('Enter your choice')
    user=input('Rock, Paper,Scissors or do you want to end the game(end) :-')
    choice=['Rock','Paper','Scissors']
    computer=r.choice(choice)
    try:
        if user==computer or user.upper()==computer:
            print(f'{user} vs {computer}')
            print('''it's a draw!!!!''')
        elif user=='Rock' and computer=='Scissors':
            print(f'{user} vs {computer}')      
            print(f'{name} wins!!!')
        elif user=='Rock' and computer=='Paper':
            print(f'{user} vs {computer}')
            print(f'{name} lost!!!')
        elif user=='end' or user.lower()=='end':
            print('thankyou for playing, have a nice day ahead')
            break
        elif user=='Paper' and computer=='Rock':
            print(f'{user} vs {computer}')
            print(f'{name} wins!!!')
        elif user=='Paper' and computer=='Scissors':
            print(f'{user} vs {computer}')
            print(f'{name} lost!!!')
        elif user=='Scissors' and computer=='Rock':
            print(f'{user} vs {computer}')
            print(f'{name} lost!!!')
        elif user=='Scissors' and computer=='Paper':
            print(f'{user} vs {computer}')
            print(f'{name} wins!!!')
        else:
            print('wrong choice, please try again')
    except Exception as e:
        print(e)
