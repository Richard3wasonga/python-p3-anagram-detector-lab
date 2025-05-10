# your code goes here!
class Anagram:

    def __init__(self,word):
        self.word = word.lower()

    def match(self,word_list):
        sorted_word = sorted(self.word)

        matches = []
        for words in word_list:
            if sorted(words.lower()) == sorted_word and words.lower() != self.word:
                matches.append(words)

        return matches