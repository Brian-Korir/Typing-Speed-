import time
import random
from pyuca import Collator
def get_random_sentence():
  sentences=[
    
       "The quick brown fox jumps over the lazy dog.",
      "A programmer is a person who can fix a problem without knowing what it is.",
      "Python is a powerful and versatile programming language.",
      "There are 10 types of people in the world: those who understand binary, and those who don't.",
      "Always code as if the person who ends up maintaining your code will be a violent psychopath who knows where you live.",
  ]
  return random.choice(sentences)
def typing_test():
  
#Intro message
print("Welcome to the typing  test!")
print("Type your own words and press enter to check your results")
print("We will check your speling too!")
#gets random sentence 
random_sentence = get_random_sentence()
print(random-sentence)

#start time 
start_time = time.time()

#end time 
end-time = time.time()

#calculate elapased time 
elapsed_time = end_time -start_time

#calculate typing speed (wpm)
words = len(random.split())
wpm = int(words / elapsed_time) * 60

# Spell checking
checker=  SpellChecker("en_US") #Change "en_US" for different dictionaries
misspelled = []
for word in typed_text.split():
  if not checker.check(word):
    misspeled.append(word)

#retype for checking
print("\nNow, retype the semtence to check for errors:")
retped_text = input("> ")
correct_chars = 0
total_chars = len(random_sentence.replace(" ", ""))
for i in range (len(random_sentence)):
  if random_sentence[i] == retyped_text[i] aand random_sentence[i] !=" ":
     correct_chars +=1


accuracy = int(correct_chars / total_chars) * 100)
#print results
print("\nResults:")
print(f"WPM: {wpm}")
print(f"Accuracy: {accuracy}% (excluding misspelled word)")

#print misspelled word (if any)
if misspelled:
  print("\n Misspeled words in the first attempt:")
     for word in  misspelled:
       print(word)
typing_test()
