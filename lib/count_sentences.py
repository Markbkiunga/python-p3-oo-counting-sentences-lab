#!/usr/bin/env python3
class MyString:
    pass

    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self.value.endswith("."):
            return True
        else:
            return False

    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False

    def count_sentences(self):
        for punctuation in ["!", "?"]:
            self.value = self.value.replace(punctuation, ". ")
        sentences = [sentence for sentence in self.value.split(". ") if sentence]
        print(sentences)
        return len(sentences)


simple_string = MyString("one. two! three?")
simple_string.count_sentences()
