import random as rd
from itertools import permutations

def secret_code():    
    """
    Returns a randomly created 4-digit code
    """
    num = rd.choice(list(permutations("0123456789", 4)))
    num = ''.join(num)
    return num

def guess():
    """
    Returns the user's guess.
    """
    try:
        repeat = True
        while repeat:
            user_str = str(input("Enter your guess: "))
            for i in user_str:
                if user_str.count(i) > 1:
                    print("Error: The number has repeating digits. Try a new code.")
                    repeat = True
                    break
                else:
                    repeat = False
    except ValueError:
        print("Error: Invalid input. Only numbers allowed!")
    return user_str

def game(code):
    """
    Function to count picas and fijas.
    @Args:
        code    = Randomly created 4-digit code (type List).
    """
    code = list(code)
    user_guess = guess()
    user_guess = list(user_guess)

    # Picas and fijas count
    picas_fijas = [0, 0]
    for i, j in zip(code, user_guess):
        if j in code:
            if j == i:
                picas_fijas[0] += 1
            else:
                picas_fijas[1] += 1
    
    return picas_fijas

def end_game():
    """
    Asks the user wether to continue the game or not.
    Returns True or False.
    """
    answer = str(input("Do you want to play again? [Y/n]: "))
    if answer == "Y" or answer == "y":
        return True
    elif answer == "N" or answer == "n":
        print("Thanks for playing!")
        return False
    else:
        print("Thanks for playing!")
        return False

def run():
    """
    Executes the game.
    """
    # Intro
    print("\n\n**** WELCOME TO PICAS AND FIJAS!****\n")
    user_name = str(input("Please, enter your name: "))
    print("\nHello " + user_name + "!\nLet's play a game!")
    print(
        """
        **** INSTRUCTIONS:
        The game consists of you trying to guess a secret 4-digit code.
        If some of the digits you entered match the right position within the code, they would be known as 'FIJAS'.
        However, if the matching digits are in different positions, they are known as 'PICAS'.
            For example:
            Secret code:  4271
            Your guess:   1234
            Answer: You have 2 PICAS | 1 FIJAS
            <<The picas are the numbers 4 and 1, the fija is the number 2!>>
            \n**Warning: You only have 10 attempts to guess the code!!
            \nXD HAVE FUN!!!\n
        """
    )

    # Results
    repeat = True
    while repeat:
        code = secret_code()
        
        # Condition for Max. 10 attempts
        attempt = 1
        while attempt <= 10:
            picas_fijas = game(code)
            print("You have {} PICAS | {} FIJAS".format(picas_fijas[1], picas_fijas[0]))
            if picas_fijas[0] == 4:
                print(f"CONGRATULATIONS {user_name.upper()}! YOU HAVE GUESSED THE NUMBER!!!")
                print("You did it in {} attempts.".format(attempt))
                repeat = end_game()
                attempt = 11
            else:
                attempt += 1
                if attempt == 11:
                    print("SORRY, YOU LOST! :(")
                    print("The secret number was {}: ".format(code))
                    repeat = end_game()

if __name__ == '__main__':
    run()