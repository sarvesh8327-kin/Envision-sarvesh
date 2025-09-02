import random
import os

class NumberGuessingGame:
    """A number guessing game where the player tries to guess a random number between 1 and 100."""
    
    def __init__(self):   # ✅ fixed constructor
        self.min_number = 1
        self.max_number = 100
        self.target_number = 0
        self.attempts = 0
        self.best_score = float('inf')
        self.games_played = 0
        
    def generate_random_number(self):
        """Generate a random number between min_number and max_number."""
        return random.randint(self.min_number, self.max_number)
    
    def display_welcome(self):
        """Display welcome message and game instructions."""
        print("=" * 50)
        print("         WELCOME TO NUMBER GUESSING GAME")
        print("=" * 50)
        print(f"I'm thinking of a number between {self.min_number} and {self.max_number}.")
        print("Can you guess what it is?")
        print("-" * 50)
    
    def display_stats(self):
        """Display game statistics."""
        print("\n" + "-" * 50)
        print("GAME STATISTICS:")
        print(f"Games Played: {self.games_played}")
        if self.best_score != float('inf'):
            print(f"Best Score: {self.best_score} attempts")
        else:
            print("Best Score: Not set yet")
        print("-" * 50)
    
    def get_user_guess(self):
        """Get and validate user input."""
        while True:
            try:
                guess = int(input(f"\nEnter your guess (between {self.min_number}-{self.max_number}): "))
                if self.min_number <= guess <= self.max_number:
                    return guess
                else:
                    print(f"Please enter a number between {self.min_number} and {self.max_number}.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    def play_round(self):
        """Play one round of the guessing game."""
        self.target_number = self.generate_random_number()
        self.attempts = 0
        guessed_correctly = False
        
        print("\nNew game started! Good luck!")
        print(f"Hint: The number is between {self.min_number} and {self.max_number}")
        
        while not guessed_correctly:
            self.attempts += 1
            guess = self.get_user_guess()
            
            if guess == self.target_number:
                guessed_correctly = True
                print(f"\n🎉 Congratulations! You guessed the number in {self.attempts} attempts!")
                
                # Update best score
                if self.attempts < self.best_score:
                    self.best_score = self.attempts
                    print("🏆 New best score!")
                
            elif guess < self.target_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
        
        self.games_played += 1
    
    def show_menu(self):
        """Display the main menu and handle user choice."""
        while True:
            print("\n" + "=" * 50)
            print("            NUMBER GUESSING GAME MENU")
            print("=" * 50)
            print("1. Play Game")
            print("2. View Statistics")
            print("3. Reset Statistics")
            print("4. Exit")
            print("-" * 50)
            
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == "1":
                self.play_round()
            elif choice == "2":
                self.display_stats()
            elif choice == "3":
                self.best_score = float('inf')
                self.games_played = 0
                print("\nStatistics reset successfully!")
            elif choice == "4":
                print("\nThanks for playing! Goodbye! 👋")
                return False  # Signal to exit
            else:
                print("\nInvalid choice! Please enter a number between 1-4.")
            
            input("\nPress Enter to continue...")
            return True  # Signal to continue

def clear_screen():
    """Clear the terminal screen."""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def main():
    """Main function to run the game."""
    game = NumberGuessingGame()
    
    while True:
        clear_screen()
        game.display_welcome()
        
        # Show menu and check if user wants to exit
        if not game.show_menu():
            break
        
        # Ask if user wants to play another session
        play_again = input("\nWould you like to play another session? (y/n): ").lower().strip()
        if play_again not in ['y', 'yes']:
            print("Thanks for playing! Goodbye! 👋")
            break

# ✅ Correct entry point
if __name__ == "__main__":
    main()
