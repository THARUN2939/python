#comp vs me

import random

options={'R':'Rock','r':'Rock','P':'Paper','p':'Paper','S':'Scissors','s':'Scissors'}
comp=random.choice(list(options.keys()))

you=input('Your choice: Rock(type R or r), Paper(type P or p) or Scissors(type S or s)? ')

if you not in list(options.keys()):
    print('\nINVALID OPTION CHOSEN BY YOU. GAME ABORTED!')
else:
    print(f'\nYou chose: {options[you]}')
    print(f'Comp chose: {options[comp]}')
    print()
    
    if you==comp:
        print('GAME TIED.')
    else:
        if you in ['R','r']:
            if comp in ['P','p']:
                print('YOU LOSE.')
            else:
                print('YOU WIN!!!')
        elif you in ['P','p']:
            if comp in ['R','r']:
                print('YOU WIN!!!')
            else:
                print('YOU LOSE.')
        else:
            if comp==['R','r']:
                print('YOU LOSE.')
            else:
                print('YOU WIN!!!')
print()