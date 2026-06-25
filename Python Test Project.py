secret = 25
lives = 5
for i in range(5):
   guess = int(input("\tEnter a number between 1 and 50:"))
   if guess == secret:
    print("You won!")
    break
   elif guess < secret - 20 or guess > secret + 20:
      print("Ice Cold!")
   elif guess < secret - 15 or guess > secret + 15:
      print("Cold")
   elif guess < secret - 10 or guess > secret + 10:
      print("Warm!")
   elif guess < secret   or guess > secret :
      print("Hot!")
   lives = lives - 1
   print("Number of lives left is:", lives) 
if lives == 0:
   print("You are out of lives! The secret number was:", secret)

