#! /usr/bin/python

pyg = "ay"

original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  for letter in word:
    if letter not in ("a", "e", "i", "o", "u"):
      first = first + letter
    else:
      break
  new_word = word + first + pyg
  new_word = new_word[len(first)-1:len(new_word)]
  print(new_word)
else:
  print("empty")