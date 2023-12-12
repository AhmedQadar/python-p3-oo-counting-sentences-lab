#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self._value = value

  def get_value(self):
    return self._value

  def set_value(self, string_value):
    if type(string_value) == str:
      self._value = string_value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)  

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")

 
  def count_sentences(self):
      sentence_count = 0
      prev_char = None

      for char in self._value:
          if char in ".?!":
              if prev_char not in ".?!":
                  sentence_count += 1
          prev_char = char

      return sentence_count