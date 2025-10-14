import random

WORD_LIST = [
     
     "keyboard", "project", 
    "python", "simple", "computer"
]

STAGES = [
    """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       ===
    """,
    """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       ===
    """,
    """
   +---+
   |   |
   O   |
  /|\\  |
       |
       ===
    """,
    """
   +---+
   |   |
   O   |
  /|   |
       |
       ===
    """,
    """
   +---+
   |   |
   O   |
   |   |
       |
       ===
    """,
    """
   +---+
   |   |
   O   |
       |
       |
       ===
    """,
    """
   +---+
   |   |
       |
       |
       |
       ===
    """
]


while True:
    
    print("WELCOME TO HANGMAN!")
    
    chosen_word = random.choice(WORD_LIST)
    word_length = len(chosen_word)
    
    lives = 6
    game_over = False
    
   
    display = ["_"] * word_length
    guessed_letters = []

    
    incorrect_guesses_count = 6 - lives
    print(STAGES[incorrect_guesses_count]) 
    print("\n" + " ".join(display))
    print(f"Lives: {lives}")
    print("-" * 30)

   
    while not game_over:
       
        while True:
            guess = input("Guess a letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter only.")
            elif guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try a new letter.")
            else:
                guessed_letters.append(guess)
                break
        
        
        is_correct_guess = False
        
       
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                is_correct_guess = True

        
        if not is_correct_guess:
            lives -= 1
            print(f"❌ '{guess}' is NOT in the word. You lose a life.")

        
        incorrect_guesses_count = 6 - lives
        print(STAGES[incorrect_guesses_count]) 
        print("\nWord:", " ".join(display))
        print("Missed letters:", " ".join(guessed_letters))
        print(f"Lives remaining: {lives}")
        print("-" * 30)

        
        
       
        if "_" not in display:
            game_over = True
            print(f"\n🎉 CONGRATULATIONS! You guessed the word: {chosen_word.upper()}")
            
       
        if lives == 0:
            game_over = True
            print(f"\n💀 GAME OVER! The word was: {chosen_word.upper()}")

    
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again not in ('y', 'yes'):
        print("Thanks for playing! Goodbye.")
        break