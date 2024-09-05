
import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        # Generate a number between 1 and the difficulty level
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        # Prompt the user to guess a number between 1 and difficulty
        while True:
            try:
                user_guess = int(input(f"Guess a number between 1 and {self.difficulty}: "))
                if 1 <= user_guess <= self.difficulty:
                    return user_guess
                else:
                    print(f"Please enter a number between 1 and {self.difficulty}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def compare_results(self, user_guess):
        # Compare the secret number with the user's guess
        return user_guess == self.secret_number

    def play(self):
        # Play the Guess Game
        self.generate_number()
        print("A secret number has been generated!")
        user_guess = self.get_guess_from_user()
        if self.compare_results(user_guess):
            print(f"Congratulations! You've guessed the correct number: {self.secret_number}")
            return True
        else:
            print(f"Sorry, the correct number was: {self.secret_number}")
            return False
