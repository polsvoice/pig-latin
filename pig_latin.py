#! /usr/bin/python

pyg = "ay"

original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  first_two = word[0:2]
  first_three = word[0:3]
  print(first, first_two, first_three)
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print(new_word)
else:
  print("empty")