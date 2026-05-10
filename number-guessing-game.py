import random
guessN= random.randint(1,10)

print("Welcome to Number guessing game")

while True:
    try:
         n= int(input("Guess any number between 1 and 10:"))
    except ValueError:
         print ("invalid characer")
         continue
    if n==guessN:
         print("Yay! you guessed it right")
         break
    elif 1<=n<=10:
         if n>guessN:
             print("try guessing a lil lower")
  
         elif  n<guessN:
             print("try guessing a lil higher")

    else:
         print("invalid character")


