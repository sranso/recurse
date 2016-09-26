# mob pairing 9/26
n_guesses = 6
guesses = set()
word = "never graduate"
game_over = False

def print_game_state():
    global game_over

    correct = [c for c in guesses if c in word]
    incorrect = [c for c in guesses if c not in word]
    unguessed = [c for c in word if c not in guesses]
    unguessed = [c for c in unguessed if c.strip()]

    if len(unguessed) == 0:
        print("Good job! You saved a life.")
        game_over = True

    if len(incorrect) >= 6:
        print("Uh oh. You got hanged...")
        game_over = True

    print("Phrased so far")
    display = word

    for c in unguessed:
        display = display.replace(c, "*")
    print(display)

    print("Correct Guesses:", correct)
    print("Incorrect Guesses:", incorrect)

while not game_over:
    print("What is your guess?")
    guess = raw_input()
    guess = guess.strip()
    if len(guess) != 1:
        print("please only guess 1 letter")
        continue
    else:
        guesses.add(guess)
    print_game_state()
