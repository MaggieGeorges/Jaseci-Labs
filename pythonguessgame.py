""" A number guessing game. """

import random

class Game:
    def __init__(self, attempts):
        self.attempts=attempts
        
    def play(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    
    
class GuessTheNumberGame(Game):
    def __init__(self, attempts=5):
        super().__init__(attempts)
        self.correct_number = random.randint(1, 10)
        
    def play(self):
        while self.attempts > 0:
            guess = input("Guess a number between 1 and 10: ")
            if guess.isdigit():
               if self.process_guess(int(guess)):
                   print("Congratulations! You've guessed the correct number.")
                   return  # End the game if guessed correctly
            else:
                print("That's not a valid number! Please try again.")
                
            self.attempts -= 1
            if self.attempts > 0:
                print(f"You have {self.attempts} attempts left.")
                
        print(f"Sorry, you didn't guess the number, Better luck next time!")
        
    def process_guess(self, guess):
        if guess < self.correct_number:
            print("Too low!")
        elif guess > self.correct_number:
            print("Too high!")
        else:
            return True
        return False
    
game = GuessTheNumberGame()
game.play()