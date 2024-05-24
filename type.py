import time
def calculate speed (start_time, end_time, characters):
#calculate elapsed time in seconds
elapsed_time = start_time - end_time
#Remove trailing new line character
characters =  characters.strip()
word_count = len (characters.split())
