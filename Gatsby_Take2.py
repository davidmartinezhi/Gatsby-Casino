import random

def call(options):
    '''Checks if the call made is a valid option, cleans it, and returns it'''
    call = ''
    count = 0
    
    #Checks if the call is a valid option on that class available options
    while (call not in options) or (count == 0):

        call = input('\nCall: ')
        call = call.lower()
        call = call.strip()
        count += 1
    #If the user has made an attempt more than once, the available options will be displayed
        if count > 1:
            print('Please select a letter from the available options')
            print('Options:', options)
        
        print('\n---------------------\n')
    return call

def keep_playing(money, active):
    '''Checks if the player wants to keep playing, and returns a boolean variable to "active"'''

    options = ['y', 'n']
    print('CURRENT MONEY: $' + str(money))
    print('''
    Enter [Y] to keep playing
    Enter [N] to Quit
    ''')

    play = call(options)

    #Checks for money and end game variable, to know if the game must be stopped
    if (play == 'n') or (money <= 0):
        
        print('Thank you for playing!')
        print('\nYou started with a $100')
        print('\nYou left with $' + str(money))
        print('\n---------------------\n')
        active = False
        return active

    return active
    
def instructions(money):
    '''Prints the game rules and dedications'''
    prompt = '''
       ('-------Welcome to Gatsby\'s Games of Chance-------')

       By: Gerardo Martínez
       Dedicated to: Concepción Villar
       
    
    As you beggin the game you'll have $100 Dollars to play with.
    
    You will be able to play Games of chances and bet on the result.

    Remember: The bigger the risk, the bigger your reward.

    Instructions:
    1) Make as much money as you can.
    2) Don't run out of money or you'll lose
    3) Bet wisely
    4)If at any point of the game you want to quit, enter [N]
    '''
    print(prompt)
    
    return money
    
def games_menu(money):
    '''Deploys the game menu and asks for the game to be played'''

    prompt = '''

    0) RULES
    * Enter [0] to see the game rules and tips
    * RECOMMENDED TO SEE THE RULES BEFORE STARTING TO PLAY

    1) COIN FLIP 
    * Enter [1] to play

        - Head or Tails?, bet wisely 
        - Win the amount of money you bet          


    2) CHO-HAN 
    * Enter [2] to play

        -Two dices will be thrown
        -Is the sum of both dices an Even or an Odd number? 
        * Win the amount of money you bet


    3) CARDS GAME 
    * Enter [3] to play

        -Play against your computer
        -The higher card wins 
        * Win your bet * 2


    4) Roulette
    * Enter [4] to choose your type of bet

        1) By picking a even/odd number (Win your bet * 2)
        2) By picking a exact number (Win your bet * 35)
        3) By picking a color, red/black (Win your bet * 2)
        
    N) End Game
    * Enter [N] to leave the game

 ------------------------------------------'''
    #Deploys game menu and informs about the money available
    print('\n     ----------------Games Menu----------------\n')
    print('CURRENT MONEY: ' + str(money))
    print(prompt)

    #Available options list that is passed to the call function for the user to choose correctly
    options = ['0','1','2', '3', '4', 'n']
    game = call(options)

    return game

def submit_bet(money):
    '''Asks for the amount to be betted and checks for the money available, so the bet can be inputed, returns a float'''  
    #Notifies the user on how much money he has and initiates variables
    print('You currently have $', money)
    bet = 0
    count = 0  
    #Checks if there is money and that the bet is in the range
    while ((money < bet) or (bet <= 0)) or (count == 0):
        bet = int(input('Make your bet: '))
        count += 1
        if count > 1:
            print('Please make a bet that is on your money range.')
      
    print('\nYou have succesfully made a bet of $' + str(bet) + '.')
    print('\n---------------------\n')

    return bet
   
def coin_flip(money):
    '''Simulates flipping a coin, if the user predicts the face he wins, returns money updated'''

    print('Coin Flip Game')
    options = ['h', 't']

    possible = ['Heads', 'Tails']
  
    prompt = '''
    Enter [H] to call Heads

    Enter [T] to call Tails'''
    print(prompt)

    choice = call(options)
    bet = submit_bet(money)

    #Give some thrill to the experience
    print('Call: ' + choice.upper())
    print('Bet: ' + str(bet))
    print('''
    Coin is being flipped...

    Coin is up in the air...

    The coin just landed...

    The result is... ''')

    #Find out the result at the last second, just as the user
    result = random.choice(possible)
    print('\n\t' + result + '!') 

    #Checks if the user won or lost
    if choice == result[0].lower():
        print('\nCongratulations, you just WON $' + str(bet) + '.')
        money += bet 
    else:
        print('\nBetter Luck next time, -$' + str(bet)+ '.')
        money -= bet 
    
    print('\n---------------------\n')
    return money

def cho_han(money):
    '''Simulate rolling two dice and adding the results together. The player predicts if the sum of dice is odd or even.'''
    '''Returns the money updated'''
    #Print the game title
    print('CHO-HAN GAME')
    #add available options to call
    options = ['e', 'o']
    prompt = '''
    Enter the letter [E] to place bet for a Even sum of dice
    Enter the letter [O] to place bet for a Odd sum of dice'''
    print(prompt)
    #User makes a call and bets on it
    choice = call(options)
    bet = submit_bet(money)

    #Thrill
    #First dice thrown
    dice1 = random.randint(1,6)
    print('Throwing first dice...')
    print('\nFirst dice is a', dice1)
  #Second dice thrown
    dice2 = random.randint(1,6)
    print('\n\nThrowing second dice...')
    print('\nSecond dice is a', dice2)
  
    #Print Sum
    sum_dices = dice1 + dice2
    print('\nThe Sum is:', sum_dices)
  
    #Calculate if player won or lost
    if (sum_dices % 2) == 0:
        if (choice == 'e'):
            print('\n\tCongratulations, you just WON $' + str(bet) + '.')
            money += bet
        else:
            print('\n\tBetter Luck next time, -$' + str(bet)+ '.')
            money -= bet
      
    elif (sum_dices % 2) != 0:
    
        if (choice == 'o'):
            print('\nCongratulations, you just WON $' + str(bet) + '.')
            money += bet
        else:
            print('\nBetter Luck next time, -$' + str(bet)+ '.')
            money -= bet
    print('\n---------------------\n')
    return money

def cards_game(money):
    '''Simulates two players picking a card randomly from a deck of cards. The higher number wins.'''
    '''Returns money updated'''

    #Prints game title and asks for a bet
    print('Cards Game')
    bet = submit_bet(money)
 
    #Made a big string with the the cards on it, then splited the cards individualy. The string is setted up from lower value to max.
    deck = 4 * ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cards = str(deck)
    
    #Draw a card for each player, and since it is on the player hand we pop it from the cards list
    player_card = deck[random.randint(0, len(deck))]

    npc_card = deck[random.randint(0, len(deck))]
    
    print('\nNPC card: ' + npc_card)
    print('Player card: ' + player_card)
    
    #Check wich card has a higjer value
    if cards.find(npc_card) < cards.find(player_card):
        print('\n\tCongratulations, you just WON $' + str(bet) + '.')
        money += bet*2
    else:
        print('\n\tBetter Luck next time, -$' + str(bet)+ '.')
        money -= bet

    print('\n---------------------\n')
    return money 

def roulette_odd_even_bet(money, ball, roulette):
    '''Bet on the probability of the ball landing on a even or odd number, updates money'''
    #Print game description and options
    print('Bet if the ball will land on an even or odd number')
    prompt = '''\n
    -Enter the letter [O] to place bet on ODD numbers.

    -Enter the letter [E] to place bet on EVEN numbers.'''
    print(prompt)

    #Declare available call options, let the user make a call and bet on it
    options = ['o', 'e']
    choice = call(options)
    bet = submit_bet(money)

    print('\nThe ball is spinning!')
    print('It\'s stopping')
    print('The ball landed on ...')
    print('\n\t' + ball)

    #Check for even or odd value with strings
    if choice == 'e':

        if ball in roulette[3:-1:2]:
            print('Congratulations')
            money += bet*2
        else:
            print('Better luck next time -$' + str(bet))
            money -= bet

    #Check for odd value in strings
    elif choice == 'o':

        if ball in roulette[2:-1:2]:
            print('Congratulations, you did it, you won $' + str(bet * 2))
            money += bet*2
        else:
            print('Better luck next time -$' + str(bet))
            money -= bet

    print('\n---------------------\n')
    return money

def roulette_especific_location_bet(money, ball, roulette):
    '''Simulates the random location a ball can land on, with the prediction, returns money updated'''
    print('Bet on the specific location the ball will land on')
    #The user selects a prediction from the roulette list and bets on it
    print('Select your prediction (00, 0, 1... 36): ')
    choice = call(roulette)
    bet = submit_bet(money)

    #Some thrill for the experience, as we show the result
    print('\nRoulette is spinning...')
    print('It\'s stopping now...')
    print('The ball just landed on ' + ball + '!')

    #Control flow according to the user prediction and the final ball location
    if ball == choice:
        print('Congratulations, you did it, you won $' + str(bet * 35))
        money += bet*35

    else:
        print('Better luck next time -$' + str(bet))
        money -= bet

    print('\n---------------------\n')
    return money

def roulette_black_red_bet(money, ball, roulette):
    '''Bet on the probability of the ball landing on a even or odd number, updates money'''
    print('Bet on color')
    #Defined black and red cases
    red = roulette[2:14:2] + roulette[16:29:2] + roulette[31:39:2] 
    black = []
    for n in roulette:
        if n in red:
            continue
        elif n == '00' or n == '0':
            continue
        else:
            black.append(n)

    #The user makes the call availables for this game and submits a bet
    print('Select the color (Press "B" for Black or "R" for Red): ')
    options = ['b', 'r']
    choice = call(options)
    bet = submit_bet(money)

    print('\n' + ball + '!')
    #Results according to the ball collor 'b' for black and 'r' for red
    if choice == 'b':
        if ball in black:
            print('Congratulations, you did it, you won $' + str(bet * 2))
            money += bet * 2
        else:
            print('Better luck next time -$' + str(bet))
            money -= bet
        
    elif choice == 'r':
        if ball in red:
            print('Congratulations, you did it, you won $' + str(bet * 2))
            money += bet * 2
        else:
            print('Better luck next time -$' + str(bet))
            money -= bet

    print('\n---------------------\n')
    return money

def roulette(money):
    '''Simulate the roulette with 3 type of bets, and return the money updated'''
    
    #Show the three kind of bets the user can bet on
    prompt = '''\n
                 (Roulette Bet Options)

    1) Enter [1] to bet on  the result being an "Odd or Even" number
        (Remember, if 0 or 00 comes up, you lose)
    
    2) Enter [2] to bet on a "specific number".
    
    3) Enter [3] to bet on  the result being a "Black or Red" color
        (Remember, if 0 or 00 comes up, you lose)'''
    print(prompt)

    #Define the available calls the user can make
    options = ['1', '2', '3']
    choice = call(options)

    #Create the roulette numbers
    roulette = '00+0+1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26+27+28+29+30+31+32+33+34+35+36'
    roulette = roulette.split('+')
    
    #Create the random end location of the ball
    ball = random.choice(roulette[::-1])

    #Flow control according to the game choice the user select
    if choice == '1':
        money = roulette_odd_even_bet(money, ball, roulette)

    elif choice == '2':
        money = roulette_especific_location_bet(money, ball, roulette)

    elif choice == '3':
        money = roulette_black_red_bet(money, ball, roulette)
    
    return money

def main():
    '''Basic structure of the program, active while active variable is true'''
    money = 100
    active = True

    while active:

        game = games_menu(money)

        if game == '0':
            money = instructions(money)
            active = keep_playing(money, active)

        if game == '1':
            money = coin_flip(money)
            active = keep_playing(money, active)

        if game == '2':
            money = cho_han(money)
            active = keep_playing(money, active)

        if game == '3':
            money = cards_game(money)
            active = keep_playing(money, active)
        
        if game == '4':
            money = roulette(money)
            active = keep_playing(money, active)

        if game == 'n':
            active = keep_playing(money, active)


main()











#
    
