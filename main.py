from word import WordRandomizer
from hangman import HangMan
from pics import HANGMAN_PICS
from pyfiglet import Figlet


object1 = WordRandomizer()
HANGMAN_TITLE = Figlet(font='pebbles')


def play(self):
    print(HANGMAN_TITLE.renderText("HANGMAN by Sam"))
    print(f"this word has {self.length} letters!")
    print(HANGMAN_PICS[self.index])
    while self.win:
        self.get_spaces(self.word)
        guess = self.get_guess()

        if guess in self.usedLetters:
            print("you already used that letter!")
            self.attempts -= 1
            print(f"you have {self.attempts} attempts left")
            print(HANGMAN_PICS[self.index])
            self.index += 1
            self.is_win(self.points, guess)
        else:
            if guess == self.word:
                self.update_spaces(guess)
                self.is_win(self.points, guess)

            elif self.is_correct(guess):
                print(HANGMAN_PICS[self.index])
                print("you are correct! - next letter!")
                self.update_spaces(guess)
                self.points += 1
                self.is_win(self.points, guess)

            elif not self.is_correct(guess):
                self.attempts -= 1
                self.index += 1
                self.usedLetters.append(guess)
                self.is_win(self.points, guess)
                print(HANGMAN_PICS[self.index])
                print(f"Wrong! -- Try again!, you have {self.attempts} left!")


game = HangMan(object1.get_word())
play(game)
