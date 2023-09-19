#!/usr/bin/env python3

class MyString:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        if self._value.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        if self._value.endswith('?'):
            return True
        else:
            return False

    def is_exclamation(self):
        if self._value.endswith('!'):
            return True
        else:
            return False

    def count_sentences(self):
        sentences = str.split(r'[.!?]', self._value)
        
        sentences = [s.strip() for s in sentences if s.strip()]
        
        
        return len(sentences)

string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_sentence()) 
print(string.is_question())  
print(string.is_exclamation())  
print(string.count_sentences()) 
