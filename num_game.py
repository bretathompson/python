# This is a guess the number game.
import random

print('hello. what is your name?')
name = input()
print('Well, ' + name +', Iam thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
      print('Take a guess.')
      guess = int(input())

      if guess < secretNumber:
          print('Your guess is to low')
      elif guess > secretNumber:
          print('Your guess is to high.')
      else:
        break

if guess == secretNumber:
    print('good job, ' + name + '! you guessed myt number in ' + str(guessesTaken) + ' guesses ')
else:
    print('nope. the number i was thinking of was ' +str(guessesTaken))

