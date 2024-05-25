# The frequency of the letters of the alphabet in English
# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
# Letter frequency
# https://en.wikipedia.org/wiki/Letter_frequency

from english_dictionary.scripts.read_pickle import get_dict
english_dict = get_dict()
# english_dict["xylophone"]  # english_dict is a Python dictionary of English
import random

letters = ""
centerLetter = ""
score = 0

# define alphabet
consonantsMoreFrequent = ["r", "n", "t", "l", "c", "d", "g", "p", "m", "h", "b"]
consonantsLessFrequent = ["y", "g", "v", "k", "w", "z", "x", "j", "q"]
vowels = ["a", "e", "i", "o", "u"]

# set letters 
def setLetters():
  selectedConsonantsMF = random.sample(consonantsMoreFrequent, 4)
  selectedConsonantsLF = random.sample(consonantsLessFrequent, 1)
  selectedVowels = random.sample(vowels, 2)
  letters = selectedConsonantsMF + selectedConsonantsLF + selectedVowels
  print("letters: ", letters)
  centerLetter = random.sample(letters, 1)
  print("center letter: ", centerLetter)
  
# letters = ["g", "i", "n", "z", "l", "d", "a"]
# centerLetter = "a"

# create guess list
guessList = []

def showLetters():  
  theLetters = ', '.join(letters)
  print("letters: ", theLetters)
  print("centerLetter: ", centerLetter)

def usesAllLetters(guess):
  global score
  counter = 0
  for letter in letters:
    if letter in guess:
      counter += 1
  if counter == 7:
    score += 15
    return "pangram!"
  else:
    score += len(guess)
    return len(guess)

# get and check input
def makeGuess():
  global score
  guess = input("Enter word guess here: ")
  if len(guess) < 4:
    print("Too short!")
    makeGuess()
  elif centerLetter not in guess:
    print("Missing center letter!")
    makeGuess()
  elif guess in guessList:
    print("Already found!")
    makeGuess()
  else:
    if lookupWord(guess) == True:
      guessList.append(guess)
      print(guessList)
      print(usesAllLetters(guess))
      print("points!")
      print(f"Score: {score}")
    else:
      print("word not found. no points!")
    makeGuess()

# look up guess in dictionary
def lookupWord(word):
  try:
    meaning = english_dict[word]
    print(meaning)
    if meaning:
      return True
    else:
      return False
  except Exception as e:
    # print(f"Error: {e}")
    return False


# run functions
setLetters()
# showLetters()
makeGuess()


# try this instead of PyDictionary

# install first: pip install nltk

# import nltk
# from nltk.corpus import words

# nltk.download('words')

# def word_exists(word):
#     word = word.lower()
#     return word in words.words()

# word_to_check = "hello"
# if word_exists(word_to_check):
#     print(f"'{word_to_check}' exists in the English language.")
# else:
#     print(f"'{word_to_check}' does not exist in the English language.")
