# "Guess the number" mini-project


import simpleguitk as simplegui
import math, random

GAME = None

print 'Welcome to the "Guess the number" game!'
print # Blank line

# initializing the start of new_game() with a range of 100
num_range = 100

# helper function to start and restart the game
def new_game():
    """initialize global variables used in your code here.
    depending on the rage selected, random number is created
    and stored in secret_number. Depending the range selected, 
    total guesses is initialized"""
    
    global secret_number, num_range, total_guesses 

    secret_number = random.randrange(num_range)
    if num_range is 100:
        total_guesses = 7
        print "What is your guess?"
    else:
        total_guesses = 10
        print "What is your guess?"
           
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game"""  
    global num_range, GAME
    print
    print "New game. Chose a number between 0 and 100. You have 7 guesses"
    GAME = "Select a number between 0 and 100. You have 7 guesses"
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range, GAME
    print
    print "New game. Chose a number between 0 and 1000. You have 10 guesses"
    GAME = "Select a number between 0 and 1000. You have 10 guesses"
    num_range = 1000
    new_game()
    
def input_guess(guess):
    """ This handler takes the guess paramenter from the text_input call and
    converts it into an int(). Program will deduct 1 from the running total of 
    total_guesses. Compares users guess with secret_number and gives hints."""
     
    global total_guesses
    guess = int(guess)
    print # Blank line in-between guesses
    print "Your guess was %d. You have %d guesses remaining " \
        % (guess, (total_guesses - 1))


    # main game logic goes here
        
    if total_guesses == 1:
        print "You're out of guesses. Correct number was %d. You lose!" \
            % secret_number
        print #Blank line
        print "New game" 
        new_game()
        return False
        
    if guess < secret_number:
        print "Higher!"
    elif guess > secret_number:
        print "Lower!"
    elif guess == secret_number:
        print
        print "You win! Let's play again."
        new_game()
    else:
        False
    total_guesses = total_guesses - 1

def draw_handler(canvas):
    canvas.draw_text(GAME, (11, 25), 12, "red")
    
# create frame and buttons
frame = simplegui.create_frame("Guessing Game", 350, 350)
label1 = frame.add_label("Select your game range")
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
blankline = frame.add_label("")
frame.add_input("What is your guess", input_guess, 210)
frame.set_draw_handler(draw_handler)
# register event handlers for control elements and start frame
frame.start()

# start game
new_game()
