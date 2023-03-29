## even = /2
## odd != /2
print('Wlecome In The Even Odd Game')
print('Please Enter A Number... And I Will Tell you if it Even Or Odd')
print('If you Wanna Close The Game Enter X')
while True:
    number = input(' Enter A number : ')

    if number == 'x':
        print('Closing the Game')
        print('Thanks....')
        break
    # even number % 2 = 0

    try :
        number = int(number)
        if number % 2 == 0:
            print('Even Number')
        else:
            print('Odd Number')
    except ValueError:
        print('Please Enter A Valid Number')
    print('--------------')
    
