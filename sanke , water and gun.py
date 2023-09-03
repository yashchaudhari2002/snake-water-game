import random
print('#'*20)
print("""Let's Play a Game...!
Enter Here you can enter Snake,water,gun""")
print('#'*20)
l1=[]
l2=[]
chance=5
while chance>0:
    n = input('Enter your choice: ')
    lstn1 = ["SNAKE", "WATER", "GUN"]
    choice = random.choice(lstn1)
    print(f'Your Choice is {n.capitalize()} and computer chose {choice.capitalize()}')
    if n.upper()=='SNAKE':
        if choice.upper()=='WATER':
            print('Congratulations..! You Won..')
            l1.append(n)
        elif choice.upper()=='SNAKE':
            print('Its a Tie..!')
        else:
            print('Sorry you loose')
            l2.append(n)
    elif n.upper()=='GUN':
        if choice.upper()=='SNAKE':
            print('Congratulations..! You Won..')
            l1.append(n)
        elif choice.upper() == 'GUN':
            print('Its a Tie..!')
        else:
            print('Sorry you loose')
            l2.append(n)
    elif n.upper()=='WATER':
        if choice.upper()=='GUN':
            print('Congratulations..! You Won..')
            l1.append(n)
        elif choice.upper() == 'WATER':
            print('Its a Tie..!')
        else:
            print('Sorry you loose')
            l2.append(n)
    else:
        print('Please provide valid choice')
    chance=chance-1
print('#'*30)
print('Thank you for playing this Game, Your score is as follows')
print(f'Won : {len(l1)} Times')
print(f'Loose : {len(l2)} Times')
print('#'*30)
if len(l1)>len(l2):
    print('Congratulations you Won the Game..!')
elif len(l1)==len(l2):
    print('Game is Tied')
else:
    print('Sorry you lost')
print('#'*30)

