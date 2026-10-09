import random

LEVELS = {"easy": (1, 50, 10), "medium": (1, 100, 7), "hard": (1, 200, 5)}

def play_round(level="medium"):
    low, high, max_attempts = LEVELS[level]
    secret = random.randint(low, high)
    attempts = 0
    print(f"
🎯 Guess a number between {low} and {high} ({max_attempts} attempts)
")
    while attempts < max_attempts:
        try:
            guess = int(input(f"  Attempt {attempts+1}/{max_attempts}: "))
        except ValueError:
            print("  Please enter a valid number.")
            continue
        attempts += 1
        if guess == secret:
            score = max(100 - (attempts - 1) * 10, 10)
            print(f"
  🎉 Correct! You got it in {attempts} attempt(s). Score: {score}")
            return score
        elif guess < secret:
            print(f"  📈 Too low! {'Almost!' if secret - guess <= 5 else ''}")
        else:
            print(f"  📉 Too high! {'Almost!' if guess - secret <= 5 else ''}")
    print(f"
  ❌ Out of attempts! The number was {secret}.")
    return 0

def main():
    print("=== Number Guessing Game ===")
    total_score = 0
    rounds = 0
    while True:
        level = input("
Choose level (easy/medium/hard) or 'quit': ").strip().lower()
        if level == "quit":
            break
        if level not in LEVELS:
            print("Invalid level. Choose easy, medium, or hard.")
            continue
        score = play_round(level)
        total_score += score
        rounds += 1
    if rounds > 0:
        print(f"
🏆 Game Over! Rounds: {rounds} | Total Score: {total_score} | Avg: {total_score//rounds}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
