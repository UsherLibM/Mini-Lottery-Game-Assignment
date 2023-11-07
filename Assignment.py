import time
import random
# Assignment    : 1
# Began         : 10/26/2023
# Time          : 4.5 Hrs
# End           : 10/26/2023
# Author        : Usher Lib

#Menu Function Definition
def main_menu():
    print(' _______________________________________________\n|\t' 
          '      Welcome To Game Night\t\t|\n|\t   -------   V1.1  ------- \t\t|\n' 
          '  ------ What game would you like to play?------')
    print('6 for Lottery', '5 for Fantasy', '4 for Pick', '3 for Pick', '0 to Quit', sep='\n')
    choice = input('Enter a number: ')
    limiter = 1
    
    while limiter == 1:
        if choice == '0':
            print('......... Thanks for playing ..........')
            for num in (5, 4, 3, 2, 1):
                print('!!\tSELF-DESTRUCT IN', num, '\t!!')
                time.sleep(0.8)
                limiter = 0
        elif choice == '6' or choice =='5' or choice == '4' or choice == '3':
            choice = int(choice)
            generate_lottery_number(choice)
            if choice == 6 or choice == 5:
                print('\n  ------ What game would you like to play?------')
                print('6 for Lottery', '5 for Fantasy', '4 for Pick', '3 for Pick', '0 to Quit', sep='\n')
                choice = input('Enter a number: ')
            else:
                print('  ------ What game would you like to play?------')
                print('6 for Lottery', '5 for Fantasy', '4 for Pick', '3 for Pick', '0 to Quit', sep='\n')
                choice = input('Enter a number: ')
        else:
            print('Wrong selection')
            choice = input('Enter a number: ')
        
def generate_lottery_number(theSelectedGame):
    limiter, total = 1, 0
    while limiter == 1: 
        total += limiter
        if theSelectedGame == 5:limiter = 1  if total != 5 and theSelectedGame == 5 else 0; print(number := random.randrange(1,37), end=' ')
        elif theSelectedGame == 6: limiter = 1  if total != 6 and theSelectedGame == 6 else 0; print(number := random.randrange(1,54), end=' ')
        elif theSelectedGame == 3 or 4: limiter = 1 if total != theSelectedGame else 0; print(number := random.randrange(1,10), end=' ')
        if total == theSelectedGame and theSelectedGame == 4: print(' FB:', fireball := random.randrange(1,10), sep='')
        elif total == theSelectedGame and theSelectedGame == 3: print(' FB:', fireball := random.randrange(1,10), sep='')
        
                
                
    
    
    
main_menu()
