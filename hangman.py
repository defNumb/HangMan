class HangMan:

    def __init__(self, word):
        self.word = word
        self.letters = list(word)
        self.attempts = 7
        self.length = len(word)
        self.spaces = list("_" * self.length)
        self.win = True
        self.usedLetters = []
        self.points = 0
        self.index = 0

    def get_guess(self):

        guess = input(f"please guess a letter or guess the word!: ")

        if guess not in 'abcdefghijklmnopqrstuvwxyz' and guess != self.word:
            print("Please Enter a valid character")

        else:
            return str(guess)

    def is_correct(self, letter):
        if letter in self.letters:
            self.usedLetters.append(letter)
            return True
        else:
            return False

    def play_again(self):
        answer = input("want to play again? Y/N: ")
        if answer.upper() == "Y":
            self.spaces = list("_" * self.length)
            self.win = True
            self.usedLetters = []
            self.points = 0
            self.attempts = 7
            self.index = 0
            game = HangMan(object1.get_word())
            play(game)
        else:
            self.win = False

    def get_spaces(self, word):
        print(self.spaces)

    def update_spaces(self, guess):
        for i, j in enumerate(self.letters):
            if guess in self.letters[i]:
                self.spaces[i] = guess
            elif guess == self.word:
                self.spaces = list(guess)

    def is_win(self, points, guess):

        if points == len(self.word):
            print(f"you guessed the word {self.word}!")
            print(f"{self.spaces}")
            self.play_again()

        elif self.attempts == 0:
            print("you Lost!")
            print(f"the word was: {self.word}")
            self.play_again()

        elif guess == self.word:

            print(f"you guessed the word {self.word}!")
            print(f"{self.spaces}")
            self.play_again()

