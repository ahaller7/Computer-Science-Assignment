######################
# Andrew Haller
# November 21st, 2019
# CMPT 120: D300
# Assignment 2A
######################


######################
# 1.1
# A function that counts the number of letters in any given string using a while loop
def traverse_string_with_while(string): #defines the function
  numletters=0  #numletters is initialized to zero
  while numletters < len(string):
    numletters = numletters + 1
  return numletters #returns the number of letters in the string

print("The string 'Hello' has: ", traverse_string_with_while("Hello"), "characters")
print("The string 'Computer Science!!!' has: ", traverse_string_with_while("Computer Science!!!"), "characters")
print("\n")

#Test #1 Testing a standard string
if traverse_string_with_while("Hello") == 5:
  print("Good!")
else:
  print("Failed")

#Test #2 Testing a string with spaces and other characters
if traverse_string_with_while("Computer Science!!!") == 19:
  print("Good!")
else:
  print("Failed")
print("\n")
  


print("****************")
######################
# 1.2
# A function that counts the number of words in a file using a for loop
def count_words(filename):
  file = open(filename, "r") #opens the file
  text = file.read() #reads the file
  file.close() #closes the file
  brokentext = text.split() #splits the file into a list with all the words
  num_words = len(brokentext) #counts the number of words in the file
  return num_words #returns the number of words
  
  
print("The file 'count_words.txt' has", count_words("count_words.txt"), "words")
print("The file 'opinions.txt' has", count_words("opinions.txt"), "words" )
print("\n")

#Test #1 Counting the number of words in the count_words.txt file
if count_words("count_words.txt") == 551:
  print("Good!")
else:
  print("Failed")
  
#Test #2 Counting the number of words in the opinions.txt file
if count_words("opinions.txt") == 88:
  print("Good!")
else:
  print("Failed")
print("\n")


print("****************")
######################
# 1.3
# A function that counts the number of sentences in a file
def count_sentences(filename):
  file = open(filename,"r") #opens the file
  text = file.read() #reads the file
  file.close() #closes the file
  new_sentence1 = text.count(".") #counts the number of periods
  new_sentence2 = text.count("!") #counte the number of exclamation marks
  new_sentence3 = text.count("?") #counts the number of question marks
  not_sentence1 = text.count("Mr.") #counts the number of occurences of 'Mr.'
  not_sentence2 = text.count("Mrs.") #counts the number of occurences of 'Mrs.'
  num_sentences = new_sentence1 + new_sentence2 + new_sentence3 - not_sentence1 - not_sentence2
  return num_sentences #return the number of sentences in the file
  
print("#SENTENCES in count_sentences.txt:",count_sentences("count_sentences.txt"))
print("#SENTENCES in opinions.txt:",count_sentences("opinions.txt"))
print("\n")

#Test #1 Counts the number of sentences in count_sentence.txt
if count_sentences("count_sentences.txt") == 19:
  print("Good!")

#Test #2 Counts the number of sentences in opinions.txt
if count_sentences("opinions.txt") == 14:
  print("Good!")
print("\n")


print("****************")
######################
# 1.4 
# A function that writes and if necessary creates a text file. What is written to the textfile is what is inputed by the user.
def create_text_file(): #defines the function
  filename = input("Enter a file name (including extension):")
  import os #imports os
  file_exists = os.path.exists(filename) #checks if the filename already exists
 
  if file_exists == True: #If the filename already exists new data will be appended to the file
    file = open(filename,"a")
    x1 = input("Enter text data:")
    while x1 != "": #Until the user types return without entering any text the user will keep being prompted to neter new data
      file.write(x1)
      file.write("\n") #Every time the user types return the new data will be on a new line
      x1 = input("Enter text data:")
    file.close() #closes the file
    return 1
    
  else: #If the filename does not already exist, a new file will be created.
    file = open(filename,"w+")
    x1 = input("Enter text data:")
    while x1 != "": #Same as line 11
      file.write(x1)
      file.write("\n")
      x1 = input("Enter text data:")
    file.close()
    return 0
    
create_text_file() #calls the function

### It is difficult to write code to test this file but there are two important tests that can be done manually.
# TEST #1: Enter a filename that does not already exist, then input several lines of text. A new file should be created with the text that was entered on different lines for every time return was pressed.
# TEST #2. Enter a filename that already exists, then input several lines of text. The file with the same name should be added to with the inputed lines below the text that was already there.
print("\n")


print("****************")
######################
# 1.5  
# A function that finds a game character's new x,y position given its initial x,y position and the amount it moves in both the x and y directions
def move_game_character(name,initialx,initialy,movementx,movementy):
  newx = initialx + movementx
  newy = initialy + movementy
  return newx,newy

print("Andrew has moved to location:", move_game_character("Andrew",4,15,2,8))
print("Brandon has moved to location:", move_game_character("Brandon",2,45,-2,-5))
print("\n")


#Test #1: Character moving by positive values
if move_game_character("Andrew",4,15,2,8) == (6, 23):
  print("Good!")
else:
  print("Failed")
  
#Test #1: Character moving by negative values
if move_game_character("Brandon",2,45,-2,-5) == (0, 40):
  print("Good!")
else:
  print("Failed")
print("\n")

  
print("****************")
######################
# 1.6
def similar_movie(movie): #defines a function similar_movie
  file = open("film_reviews.txt","r") #opens filmreviews.txt
  filmreviews = file.readlines() #reads each line of the file into a list called filmreviews
  file.close() #closes the file
  dictionary = {} #creates an empty dictionary which will stores the movies and their keywords
  valuesdictionary = {}  #creates an empty dictionary which will store how many matching keywords are associated with each movie
  
  for i in range(len(filmreviews)): #a for loop that iterates through every element of the list filmreviews
      filmreviews3 = filmreviews[i].split(",") #splits the line at the commas
      dictionary[filmreviews3[0]] = filmreviews3[1:]  #The first term becomes the key and the remaining terms become the value that is entered into dictionary
      
  moviekeywords = dictionary[movie] #moviekeywords becomes a list of the argument movie's keywords
  del dictionary[movie] #deletes the movie which is the argument movie from the dictionary
  
  for movie in dictionary:   #a for loop which iterates through all the movies in the dictionary and creates a valuesdictionary which holds the number of matching keywords for each movie
    movienum = 0   #movienum is the number of keywords in each movie which match the argument's keywords
    for keyword in moviekeywords:   #a for loop which iterates through all the argument movie's keywords
      if keyword in  dictionary[movie]:   #if the argument movie's keyword is a keyword in the movie that is being searched movienum goes up by 1
        movienum = movienum + 1
    valuesdictionary[movie] = movienum    #The movie that is being search becomes the key and movienum becomes the value in the valuesdictionary
 
  x = 0    #x is the highest number of keywords in the movie which has the greatest number of keywords
  mostsimilar = -1 #mostsimilar will be the variable that holds the movie with greatest number of matching keywords
  
  for movie2 in valuesdictionary: #a for loop which iterates through all the movies in valuesdictionary
    if valuesdictionary[movie2] > x: #if the total number of keywords for the movie is greater than the current high, that movie becomes the mostsimilar movie and its number of keywords becomes the new x
      mostsimilar = movie2
      x = valuesdictionary[movie2]
    elif valuesdictionary[movie2] == x: #if the total number of keywords for the movie is equal to the current high, the movie gets added to a string with the movie that it is tied with
      mostsimilar = str(mostsimilar) + ", and " + str(movie2)
  return mostsimilar #returns the movie with the most similar number of keywords
  

print("The movie that is the most similar to Black Panther is", similar_movie("Black Panther"))
print("The movie that is the most similar to 12 Strong is", similar_movie("12 Strong"))
print("The movie that is the most similar to A Wrinkle in Time is", similar_movie("A Wrinkle in Time"))
print("\n")

#Test 1: A test where 2 movies are tied for the greatest number of keywords matching
if similar_movie("Black Panther") == "12 Strong, and Armed":
  print("Good!")
  
#Test 2: A test where 1 movie has the greatest number of keywords matching
if similar_movie("12 Strong") == "Armed":
  print("Good!")
print("\n")



print("****************")
######################
#1.7  A function that checks if a variable is of type String
def check_type_is_string(x):
  if type(x) == str: #checks if the type of the variable is string
    return True #if the variable is a string it returns true
  else:
    return False #if the variable is not a string it returns false
  
print("24 is of type string?",check_type_is_string(24))
print("'24' is of type string?", check_type_is_string('24'))
print("'Hello' is of type string?", check_type_is_string('Hello'))
print("\n")

#Test #1. Checks if an integer is of type string.
if check_type_is_string(24) == False:
  print("Good!")
else:
  print("Failed")
  
#Test #2. Checks if a string of numbers is of type string.
if check_type_is_string("24") == True:
  print("Good!")
else:
  print("Failed")
  
#Test #3. Checks if a string of letters is of type string.
if check_type_is_string("Hello") == True:
  print("Good!")
else:
  print("Failed")
print("\n")



print("****************")
######################
#1.8
#Checks what items a player can buy in a video game.
def shop_items_player_can_buy(money,items_prices): #defines the function
  available = []  #creates an emptt list which will hold the items the player can buy
  for key, value in items_prices.items():
    if value <= money:
      available = available + [key]
  return available #returns a list of what items the player can buy
  

print(shop_items_player_can_buy(50,{"book":5,"map":10,"house":100}))
print(shop_items_player_can_buy(50,{"vehicle":50,"football":5,"uniform":10,"truck":70}))
print("\n")

#Test #1. Determines what items a player can buy.
if shop_items_player_can_buy(50,{"book":5,"map":10,"house":100}) == ['book', 'map']:
  print("Good!")
else:
  print("Failed")
  
  
#Test #2. Determines what items a player can buy.
if shop_items_player_can_buy(50,{"vehicle":50,"football":5,"uniform":10,"truck":70}) == ['vehicle', 'football', 'uniform']:
  print("Good!")
else:
  print("Failed")
print("\n")



print("****************")
######################
# 1.9
# Determines whether a sentence has a positive or negative opinion of a topic
file = open("opinions.txt") #opens the file
text = file.readlines() #reads the file by line and stores it as a list
file.close() #closes the file

def sentence_opnion(sentence):
  positive_words = ["great","poetic","bad in a good way","good","favourite","exciting","clever","thoughtful"]
  negative_words = ["horrible", "scarry", "bad","meh","wasted", "phone", "sucked",]
  if "sucked" in sentence:
    return -1
  for word in positive_words:
    if word in sentence:
     return 1
  for word in negative_words:
     if word in negative_words:
      return -1
  
for i in range(1,14): #prints what the sentence opinion is for every line of the file
  print("The opinion of line", str(i) + ":", sentence_opnion(text[i]))
print("\n")
  
#Test #1: The result should be 1
if sentence_opnion(text[1]) == 1:
  print("Good!")
else:
  print("Failed")
  
#Test #2: The result should be -1
if sentence_opnion(text[2]) == -1:
  print("Good!")
else:
  print("Failed")
print("\n")

  

print("****************")
######################
# 1.10 Astronomy
# Determines the value of hottest, coldest, brightest, and darkest star from a file called stars.txt

def parse_stars_file(filename): #defines the function that parses the stars.txt file into a list of the temperatures and a list of the magnitudes
  file = open(filename,"r") #opens the file stars.txt
  astronomy = file.readlines() #reads the file by line
  file.close() #closes the file
  temperatures = []
  magnitudes = []
  
  for line in astronomy: 
    temperatures.append(line.split()[0])
    magnitudes.append(line.split()[1])
  return temperatures, magnitudes #returns a list of the temperatures and a list of the magnitudes
    

def find_hottest_star(filename): #A function to find the hottest star
  temperatures, magnitudes = parse_stars_file(filename) #calls the pars_stars_file function
  max_value = temperatures[0]
  for value in temperatures:
    if float(value) > float(max_value):
      max_value = value
  return max_value
      
def find_coldest_star(filename): #A function to find the coldest star
  temperatures, magnitudes = parse_stars_file(filename) #calls the pars_stars_file function
  min_value = temperatures[0]
  for value in temperatures:
    if float(value) < float(min_value):
      min_value = value
  return min_value
  
def find_brightest_star(filename): #A function to find the brighest star
  temperatures, magnitudes = parse_stars_file(filename) #calls the pars_stars_file function
  max_value = magnitudes[0]
  for value in magnitudes:
    if float(value) > float(max_value):
      max_value = value
  return max_value
  
def find_darkest_star(filename): #A function to find the darkest star
  temperatures, magnitudes = parse_stars_file(filename) #calls the pars_stars_file function
  min_value = magnitudes[0]
  for value in magnitudes:
    if float(value) < float(min_value):
      min_value = value
  return min_value

print("How hot the hottest star is:", find_hottest_star("stars.txt"))
print("How cold the coldest star is:", find_coldest_star("stars.txt"))
print("How bright the brightest star is:",find_brightest_star("stars.txt"))
print("How dark the darkest star is:",find_darkest_star("stars.txt"))
print("\n")



#Test #1: Test the hottest star
if (find_hottest_star("stars.txt")) == "14786.0720701":
  print("Good!")
else:
  print("Failed")
  
#Test #2: Test the coldest star
if find_coldest_star("stars.txt") == "683.14508541":
  print("Good!")
else:
  print("Failed")
  
#Test #3: Test the brightest star
if find_brightest_star("stars.txt") == "18.08":
  print("Good!")
else:
  print("Failed")

#Test #4: Test the darkest star
if find_darkest_star("stars.txt") == "-2.77":
  print("Good!")
else:
  print("Failed")
print("\n")
  

print("****************")
######################
# 1.11
# A function that transforms a string and displays the encoded string
def transform_string(string):
  newstring = "" #A blank string is created
  for letter in string:
    if letter == "a":
      newstring = newstring + "m"
    if letter == "b":
      newstring = newstring + "b"
    if letter == "c":
      newstring = newstring + "z"
    if letter == "d":
      newstring = newstring + "q"
    if letter == "e":
      newstring = newstring + "k"
    if letter == "f":
      newstring = newstring + "t"
    if letter == "g":
      newstring = newstring + "o"
    if letter == "h":
      newstring = newstring + "v"
    if letter == "i":
      newstring = newstring + "c"
    if letter == "j":
      newstring = newstring + "r"
    if letter == "k":
      newstring = newstring + "y"
    if letter == "l":
      newstring = newstring + "g"
    if letter == "m":
      newstring = newstring + "e"
    if letter == "n":
      newstring = newstring + "f"
    if letter == "o":
      newstring = newstring + "w"
    if letter == "p":
      newstring = newstring + "x"
    if letter == "q":
      newstring = newstring + "s"
    if letter == "r":
      newstring = newstring + "u"
    if letter == "s":
      newstring = newstring + "i"
    if letter == "t":
      newstring = newstring + "d"
    if letter == "u":
      newstring = newstring + "a"
    if letter == "v":
      newstring = newstring + "l"
    if letter == "w":
      newstring = newstring + "n"
    if letter == "x":
      newstring = newstring + "h"
    if letter == "y":
      newstring = newstring + "j"
    if letter == "z":
      newstring = newstring + "p"
    if letter == "A":
      newstring = newstring + "M"
    if letter == "B":
      newstring = newstring + "B"
    if letter == "C":
      newstring = newstring + "Z"
    if letter == "D":
      newstring = newstring + "Q"
    if letter == "E":
      newstring = newstring + "K"
    if letter == "F":
      newstring = newstring + "T"
    if letter == "G":
      newstring = newstring + "O"
    if letter == "H":
      newstring = newstring + "V"
    if letter == "I":
      newstring = newstring + "C"
    if letter == "J":
      newstring = newstring + "R"
    if letter == "K":
      newstring = newstring + "Y"
    if letter == "L":
      newstring = newstring + "G"
    if letter == "M":
      newstring = newstring + "E"
    if letter == "N":
      newstring = newstring + "F"
    if letter == "O":
      newstring = newstring + "W"
    if letter == "P":
      newstring = newstring + "X"
    if letter == "Q":
      newstring = newstring + "S"
    if letter == "R":
      newstring = newstring + "U"
    if letter == "S":
      newstring = newstring + "I"
    if letter == "T":
      newstring = newstring + "D"
    if letter == "U":
      newstring = newstring + "A"
    if letter == "V":
      newstring = newstring + "L"
    if letter == "W":
      newstring = newstring + "N"
    if letter == "X":
      newstring = newstring + "H"
    if letter == "Y":
      newstring = newstring + "J"
    if letter == "Z":
      newstring = newstring + "P"
  return newstring
  
  
print("'abcde' transforms to:", transform_string("abcde"))
print("'DIFJ' transforms to:", transform_string("DIFJ"))
print("'JH%KlmP&o' transforms to:",transform_string("JH%KlmP&o"))
print("'How are You' transfomrs to:",transform_string("How are You"))
print("\n")

#Test#1: Generic test
if transform_string("abcde") == "mbzqk":
  print("Good!")
else:
  print("False")
  
#Test#2: Test with capitals
if transform_string("DIFJ") == "QCTR":
  print("Good!")
else:
  print("False")

#Test#3: Test with special characters. (special characters get removed)
if transform_string("JHKlmPo") == "RVYgeXw":
  print("Good!")
else:
  print("False")
  
#Test #4 Test with spaces. (Spaces get removed)
if transform_string("HowareYou") == "VwnmukJwa":
  print("Good!")
else:
  print("False")
print("\n")


print("****************")
######################
# 1.12
# A function that breaks bioinformatics down into a readable format

def read_bio_data(filename):
  file = open(filename,"r") #opens the file
  orchid = file.read() #reads the file
  file.close() #closes the file
  
  code = orchid.split(">") #splits the file wherever there is the character '>'
  code.pop(0) #removes the first element from the list as it is blank
  return code

sequence_records = read_bio_data("ls_orchid.fasta")
num_of_sequence_records = len(sequence_records) #Calculates the number of sequence records
print("num_of_sequence_records: " + str(num_of_sequence_records))

print("\n")


def print_bio_data(sequence_record): #Defines a function that prints one sequence record
    newcode = sequence_record.split("\n")
    newcode2 = newcode[0].split("|")
    
    print("DESCRIPTION:")
    for i in newcode2:
      print("\t" + i)
    print("\n")
    
    print("SEQUENCE")
    for i in newcode[1:]:
      print("\t" + i)
    print("\n\n")
  
  
for i in range(len(sequence_records)): #Prints all the sequence records
  print("\nSEQUENCE #"+str(i+1))
  print(print_bio_data(sequence_records[i]))


###Creating a test is too complicated but it would look something like this:
# if print_bio_data(sequence_records[1])) == "The easier to read text of sequence record #1"
#   print("Good")
# else:
#   print("Failed")

#This is far too complicated to make unit tests for 