import requests


class WordRandomizer:
    def __init__(self):
        self.number = '0'
        self.apikey = 'n1f8tj8bcwxlf16n14zz5yc4btgdcsdabfun85zqac8g7vgsj'
        self.difficulty()
        self.apiURL = 'https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength='+self.number+'&api_key=' + self.apikey

    def get_word(self):
        response = requests.get(self.apiURL).json()
        word = response.get('word')
        return word

    def difficulty(self):
        answer = input("Choose Difficulty (easy, medium ,expert): ")
        if answer.lower() == "easy":
            self.number = '5'
        elif answer.lower() == "medium":
            self.number = '6'
        elif answer.lower() == "expert":
            self.number = '8'

