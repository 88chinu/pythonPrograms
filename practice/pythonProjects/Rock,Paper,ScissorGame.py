import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃'}
choices = (ROCK, PAPER, SCISSORS)

wins = 0
losses = 0
ties = 0

def get_user_choice():
    while True:
        choice = input("\nChoose Rock, Paper or Scissors (r/p/s): ").lower()
        if choice in choices:
            return choice
        print("❌ Invalid choice! Please enter r, p, or s.")

def display_choices(user_choice, computer_choice):
    print(f"\nYou chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    global wins, losses, ties

    if user_choice == computer_choice:
        print("🤝 It's a tie!")
        ties += 1

    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("🎉 You win this round! Great choice!")
        wins += 1
    else:
        print("😢 You lost this round. Try again!")
        losses += 1

def show_scorecard():
    print("\n📊 FINAL SCORE CARD")
    print("-" * 25)
    print(f"🏆 Wins   : {wins}")
    print(f"💀 Losses : {losses}")
    print(f"🤝 Ties   : {ties}")

    if wins > losses:
        print("\n🎊 CONGRATULATIONS! You won the game overall!")
    elif wins < losses:
        print("\n💪 Good effort! Computer won this time.")
    else:
        print("\n⚖️ It's an overall tie! Well played.")

def play_game():
    print("🎮 Welcome to Rock, Paper & Scissors!")
    print("🔥 Beat the computer if you can!")
    print("-" * 35)

    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        again = input("\nDo you want to play another round? (y/n): ").lower()
        if again == 'n':
            break

    show_scorecard()
    print("\n🙏 Thanks for playing! See you again 👋")

play_game()
